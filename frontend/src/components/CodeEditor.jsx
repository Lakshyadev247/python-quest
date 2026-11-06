import React, { useState, useRef, useEffect } from 'react';
import Editor, { loader } from '@monaco-editor/react';
import * as monaco from 'monaco-editor';
import editorWorker from 'monaco-editor/editor/editor.worker.js?worker';
import { Play, RotateCcw, CheckCircle2, XCircle, HelpCircle, Send, Terminal, Lightbulb, Copy } from 'lucide-react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';

// Bundle Monaco locally instead of loading it from a CDN.  The APK is often
// used without internet access, and the CDN loader used to leave the editor
// blank when offline.
if (typeof window !== 'undefined') {
  self.MonacoEnvironment = {
    getWorker: () => new editorWorker(),
  };
  loader.config({ monaco });
}

export default function CodeEditor({
  challenge,
  initialCode: initialCodeProp,
  onPassed,
  readOnly = false,
  height = '340px'
}) {
  const { user, isGuest, theme, refreshUser } = useAuth();
  // Do not prefill a solution in curriculum challenges (which have a challenge.id).
  // In the playground/practice mode (or when initialCodeProp/initial_code is provided), load the starter code.
  const computeInitialCode = () => {
    if (initialCodeProp !== undefined) return initialCodeProp;
    if (!challenge?.id && challenge?.initial_code) return challenge.initial_code;
    return '';
  };
  const initialCode = computeInitialCode();
  const [code, setCode] = useState(initialCode);
  const codeRef = useRef(initialCode);
  const editorRef = useRef(null);
  const typingTimerRef = useRef(null);

  // Synchronize when template starter code changes in Practice Playground
  useEffect(() => {
    const nextCode = initialCodeProp !== undefined
      ? initialCodeProp
      : (!challenge?.id && challenge?.initial_code ? challenge.initial_code : null);

    if (nextCode !== null && nextCode !== undefined && !challenge?.id) {
      codeRef.current = nextCode;
      setCode(nextCode);
      if (editorRef.current && editorRef.current.getValue() !== nextCode) {
        editorRef.current.setValue(nextCode);
      }
    }
  }, [initialCodeProp, challenge?.initial_code, challenge?.id]);

  // Synchronize live code and challenge with AI companion
  useEffect(() => {
    const curCode = codeRef.current || code || '';
    window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
      detail: {
        code: curCode,
        challengeTitle: challenge?.title || '',
        challengeInstructions: challenge?.instructions || '',
        hints: challenge?.hints || []
      }
    }));
  }, [challenge?.id, challenge?.title, challenge?.instructions]);

  const [output, setOutput] = useState(null);
  const [isRunning, setIsRunning] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [testResults, setTestResults] = useState(null);
  const [showHints, setShowHints] = useState(false);
  const [revealedHintsCount, setRevealedHintsCount] = useState(1);
  const [showSolution, setShowSolution] = useState(false);
  const [pastedFeedback, setPastedFeedback] = useState(false);

  // Input-based challenges in Worlds 4–12 run with their first visible test
  // input so learners can try pasted code without hitting an empty-input error.
  const challengeLevelNumber = Number(challenge?.level_id ?? challenge?.level_number);
  const isWorld4Challenge = challengeLevelNumber >= 31 && challengeLevelNumber <= 39;
  const isWorld5Challenge = challengeLevelNumber >= 40 && challengeLevelNumber <= 48;
  const isWorld6Challenge = challengeLevelNumber >= 49 && challengeLevelNumber <= 63;
  const isWorld7To12Challenge = challengeLevelNumber >= 64 && challengeLevelNumber <= 126;
  const usesSampleInput = isWorld4Challenge || isWorld5Challenge || isWorld6Challenge || isWorld7To12Challenge;
  const sampleInput = usesSampleInput
    ? (challenge?.test_cases?.find((testCase) => !testCase.is_hidden)?.input_data ?? '')
    : '';

  const handleToggleHints = () => {
    if (!showHints && revealedHintsCount === 0) {
      setRevealedHintsCount(1);
    }
    setShowHints(!showHints);
  };

  const handlePasteSolution = () => {
    if (!challenge?.solution_code) return;
    const sol = challenge.solution_code;
    codeRef.current = sol;
    setCode(sol);
    if (editorRef.current) {
      editorRef.current.setValue(sol);
    }
    setPastedFeedback(true);
    setTimeout(() => setPastedFeedback(false), 4000);

    // Companion pet event
    window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
      detail: { code: sol }
    }));
    window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
      detail: { action: 'explaining', message: "Let's analyze this solution together!", duration: 3500 }
    }));
  };

  const handleCodeChange = (newVal) => {
    const val = newVal || '';
    codeRef.current = val;
    setCode(val);

    // As soon as the user starts editing their code, clear stale wrong/error output!
    if (output !== null) setOutput(null);
    if (testResults !== null) setTestResults(null);

    // Keep AI Tutor live context synchronized
    window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
      detail: { code: val }
    }));

    // Debounced pet typing reaction
    if (typingTimerRef.current) clearTimeout(typingTimerRef.current);
    typingTimerRef.current = setTimeout(() => {
      window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
        detail: { action: 'typing', message: 'Working on some Python magic...', duration: 2200 }
      }));
    }, 600);
  };

  const handleReset = () => {
    const resetTarget = computeInitialCode();
    codeRef.current = resetTarget;
    setCode(resetTarget);
    if (editorRef.current) {
      editorRef.current.setValue(resetTarget);
    }
    setOutput(null);
    setTestResults(null);
    window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
      detail: { code: resetTarget, lastStdout: '', lastError: '', testResults: null }
    }));
  };

  const handleRun = async () => {
    const codeToRun = editorRef.current ? editorRef.current.getValue() : codeRef.current;
    setIsRunning(true);
    setOutput(null);
    setTestResults(null);

    // Companion pet thinking reaction
    window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
      detail: { action: 'thinking', message: 'Analyzing your solution...', duration: 0 }
    }));

    try {
      const res = await api.post('/code/execute', {
        code: codeToRun,
        ...(usesSampleInput ? { input: sampleInput } : {}),
      });
      setOutput(res);

      window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
        detail: {
          code: codeToRun,
          lastStdout: res.stdout || '',
          lastError: res.stderr || ''
        }
      }));

      if (!res.success || res.stderr) {
        window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
          detail: { action: 'wrong', message: 'Oops! Check the output console.', duration: 3500 }
        }));
      } else {
        window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
          detail: { action: 'reading', message: 'Code executed cleanly!', duration: 3000 }
        }));
      }
    } catch (err) {
      setOutput({
        success: false,
        stdout: '',
        stderr: err.message || 'Execution failed'
      });
      window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
        detail: {
          code: codeToRun,
          lastStdout: '',
          lastError: err.message || 'Execution failed'
        }
      }));
      window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
        detail: { action: 'wrong', message: 'Oops! Check the output console.', duration: 3500 }
      }));
    } finally {
      setIsRunning(false);
    }
  };

  const handleSubmit = async () => {
    if (!challenge?.id) return;
    const codeToSubmit = editorRef.current ? editorRef.current.getValue() : codeRef.current;
    setIsSubmitting(true);
    setOutput(null);
    setTestResults(null);

    // Companion pet loading reaction
    window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
      detail: { action: 'loading', message: 'Evaluating your test cases...', duration: 0 }
    }));

    try {
      const res = await api.post('/code/submit', {
        challenge_id: challenge.id,
        code: codeToSubmit
      });
      setTestResults(res);
      setOutput({
        success: res.passed,
        stdout: res.stdout,
        stderr: res.stderr
      });

      window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
        detail: {
          code: codeToSubmit,
          lastStdout: res.stdout || '',
          lastError: res.stderr || '',
          testResults: res
        }
      }));

      if (res.passed) {
        window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
          detail: { action: 'celebrating', message: 'Brilliant! All tests passed! 🎉', duration: 4200 }
        }));
        refreshUser();
        if (onPassed) onPassed(res);
      } else {
        window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
          detail: { action: 'wrong', message: 'Oops! Check the output console.', duration: 3500 }
        }));
      }
    } catch (err) {
      setOutput({
        success: false,
        stdout: '',
        stderr: err.message || 'Submission failed'
      });
      window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
        detail: { action: 'error', message: 'Submission failed. Check your network or syntax.', duration: 3500 }
      }));
    } finally {
      setIsSubmitting(false);
    }
  };

  const hints = Array.isArray(challenge?.hints) ? challenge.hints : [];

  const getBeginnerFriendlyAdvice = () => {
    const errText = output?.stderr || '';
    if (errText) {
      const s = errText.toLowerCase();
      if (s.includes("nameerror: name 'print' is not defined") || (s.includes("print") && s.includes("did you mean: 'print'"))) {
        return {
          title: "⚠️ Case Sensitivity Error (Print vs print)",
          message: "Python is strictly case-sensitive! You wrote 'Print' with a capital 'P'. Change it to lowercase 'print(...)'."
        };
      }
      if (s.includes("nameerror: name") && s.includes("is not defined")) {
        const match = errText.match(/name '([^']+)' is not defined/i);
        const word = match ? match[1] : "your text";
        return {
          title: "⚠️ Missing Quotation Marks",
          message: `Did you forget quotes around '${word}'? In Python, all plain words and text must be enclosed in quotes like '${word}'. Without quotes, Python thinks '${word}' is a variable or command name!`
        };
      }
      if (s.includes("unterminated string literal") || s.includes("eol while scanning string literal")) {
        return {
          title: "⚠️ Unclosed Quotation Mark",
          message: "You opened a quotation mark ' but forgot to close it with another quote ' before the end of the line! Make sure your statement looks like: print('your text here')"
        };
      }
      if (s.includes("was never closed") || s.includes("unexpected eof while parsing")) {
        return {
          title: "⚠️ Missing Closing Parenthesis",
          message: "You opened a parenthesis '(' after print, but forgot to close it with ')' at the end of the line! Make sure your statement ends with ')'."
        };
      }
      if (s.includes("syntaxerror: invalid syntax")) {
        return {
          title: "⚠️ Syntax Formatting Mistake",
          message: "Check your punctuation and brackets. In Python, the print command looks like: print('Your exact text here') with lowercase print, parentheses (), and quotation marks ''."
        };
      }
    }

    if (testResults && !testResults.passed) {
      return {
        title: "⚠️ Output Did Not Match Requirements",
        message: "Your code ran without syntax errors, but the printed text doesn't match the required output. Look closely at the expected output vs your output below. Double check capitalization, spelling, and spaces!"
      };
    }

    return null;
  };

  const advice = getBeginnerFriendlyAdvice();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      {/* Editor Controls Bar */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '8px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }}>Python 3</span>
          {challenge?.xp_reward && (
            <span style={{ fontSize: '0.8rem', padding: '2px 8px', borderRadius: '12px', background: 'var(--accent-gold-bg)', color: 'var(--accent-gold)', fontWeight: 600 }}>
              +{challenge.xp_reward} XP
            </span>
          )}
        </div>

        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end', flexWrap: 'wrap', gap: '8px', flex: '1 1 360px' }}>
          {(hints.length > 0 || challenge?.solution_code) && (
            <button
              onClick={handleToggleHints}
              className="btn btn-secondary"
              style={{
                padding: '6px 12px',
                fontSize: '0.85rem',
                color: showHints ? 'var(--accent-blue)' : 'inherit',
                borderColor: showHints ? 'var(--accent-blue)' : 'var(--border-color)'
              }}
            >
              <HelpCircle size={16} />
              Hints &amp; Solution ({hints.length + (challenge?.solution_code ? 1 : 0)})
            </button>
          )}

          <button
            onClick={handleReset}
            className="btn btn-secondary"
            title="Reset code"
            style={{ padding: '6px 10px' }}
          >
            <RotateCcw size={16} />
          </button>

          <button
            onClick={handleRun}
            disabled={isRunning || isSubmitting}
            className="btn btn-blue"
            style={{ padding: '6px 14px' }}
          >
            <Play size={16} fill="white" />
            {isRunning ? 'Running...' : usesSampleInput ? 'Run Example' : 'Run Code'}
          </button>

          {challenge?.id && (
            <button
              onClick={handleSubmit}
              disabled={isSubmitting || isRunning}
              className="btn btn-primary"
              style={{ padding: '6px 16px', whiteSpace: 'nowrap', flex: '0 0 auto' }}
            >
              <Send size={16} />
              {isSubmitting ? 'Evaluating...' : 'Submit Code'}
            </button>
          )}
        </div>
      </div>

      {/* Progressive Step-by-Step Hints & Auto-Paste Solution */}
      {showHints && (hints.length > 0 || challenge?.solution_code) && (
        <div style={{
          background: 'var(--bg-tertiary)',
          border: '1.5px solid var(--accent-blue)',
          borderRadius: 'var(--radius-md)',
          padding: '16px',
          display: 'flex',
          flexDirection: 'column',
          gap: '12px',
          boxShadow: '0 4px 12px rgba(0,0,0,0.15)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid var(--border-color)', paddingBottom: '8px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 800, fontSize: '0.92rem', color: 'var(--accent-blue)' }}>
              <Lightbulb size={18} />
              <span>Step-by-Step Guidance (Progressive Hints)</span>
            </div>
            <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
              Revealed {Math.min(revealedHintsCount, hints.length)} of {hints.length} concept hints
            </span>
          </div>

          {/* List of Revealed Hints */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {hints.slice(0, revealedHintsCount).map((hintText, idx) => (
              <div key={idx} style={{
                background: 'var(--bg-primary)',
                border: '1px solid var(--border-color)',
                borderRadius: '8px',
                padding: '10px 14px',
                fontSize: '0.88rem'
              }}>
                <div style={{ fontWeight: 700, color: '#58a6ff', marginBottom: '4px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span>💡 Hint {idx + 1}:</span>
                </div>
                <div style={{ color: 'var(--text-primary)', lineHeight: 1.5, fontFamily: hintText.includes('\n') || hintText.includes('(') ? 'var(--font-mono)' : 'inherit' }}>
                  {hintText}
                </div>
              </div>
            ))}
          </div>

          {/* Action Row: Reveal Next Hint / Instant Auto-Paste / View Solution */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap', paddingTop: '4px' }}>
            {revealedHintsCount < hints.length && (
              <button
                onClick={() => setRevealedHintsCount(prev => Math.min(prev + 1, hints.length))}
                className="btn btn-secondary"
                style={{ fontSize: '0.82rem', padding: '6px 14px', fontWeight: 600 }}
              >
                Reveal Next Hint ({revealedHintsCount + 1}/{hints.length}) →
              </button>
            )}

            {challenge?.solution_code && (
              <button
                onClick={() => {
                  setShowSolution(true);
                  handlePasteSolution();
                }}
                className="btn btn-primary"
                style={{
                  fontSize: '0.82rem',
                  padding: '6px 14px',
                  fontWeight: 700,
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  background: '#238636',
                  color: '#ffffff',
                  border: 'none',
                  cursor: 'pointer'
                }}
              >
                <Copy size={14} />
                Auto-Paste Solution into Editor
              </button>
            )}

          </div>

          {/* Full Solution Block with Auto-Paste Button */}
          {showSolution && challenge?.solution_code && (
            <div style={{
              background: 'rgba(56, 139, 253, 0.08)',
              border: '1.5px solid rgba(56, 139, 253, 0.4)',
              borderRadius: '8px',
              padding: '14px',
              display: 'flex',
              flexDirection: 'column',
              gap: '10px'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '8px' }}>
                <span style={{ fontWeight: 800, color: 'var(--accent-blue)', fontSize: '0.88rem' }}>
                  ✅ Complete Reference Solution:
                </span>
                <button
                  onClick={handlePasteSolution}
                  className="btn btn-primary"
                  style={{
                    padding: '6px 14px',
                    fontSize: '0.82rem',
                    fontWeight: 700,
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px',
                    background: '#238636'
                  }}
                >
                  <Copy size={14} />
                  Auto-Paste Solution into Editor
                </button>
              </div>

              <pre style={{
                background: '#0d1117',
                border: '1px solid #30363d',
                borderRadius: '6px',
                padding: '12px',
                fontFamily: 'var(--font-mono)',
                fontSize: '0.88rem',
                color: '#58a6ff',
                margin: 0,
                overflowX: 'auto',
                whiteSpace: 'pre'
              }}>
                {challenge.solution_code}
              </pre>

              {pastedFeedback && (
                <div style={{
                  fontSize: '0.84rem',
                  color: 'var(--accent-green)',
                  fontWeight: 700,
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px'
                }}>
                  <CheckCircle2 size={16} />
                  Solution pasted into editor! Click &ldquo;{usesSampleInput ? 'Run Example' : 'Run Code'}&rdquo; or &ldquo;Submit Code&rdquo; to test it.
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Monaco Editor Container */}
      <div style={{
        border: '1px solid var(--border-color)',
        borderRadius: 'var(--radius-md)',
        overflow: 'hidden',
        boxShadow: 'inset 0 1px 3px rgba(0,0,0,0.2)'
      }}>
        <Editor
          height={height}
          defaultLanguage="python"
          value={code}
          onMount={(editor) => {
            editorRef.current = editor;
            window._lastMonacoEditor = editor;
            if (initialCode && (!challenge?.id || !editor.getValue())) {
              editor.setValue(initialCode);
            }
            editor.onDidChangeModelContent(() => {
              handleCodeChange(editor.getValue());
            });
          }}
          onChange={handleCodeChange}
          theme={theme === 'light' ? 'light' : 'vs-dark'}
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            fontFamily: 'var(--font-mono)',
            scrollBeyondLastLine: false,
            readOnly: readOnly,
            tabSize: 4,
            insertSpaces: true,
            lineNumbers: 'on',
            automaticLayout: true,
          }}
        />
      </div>

      {/* Output Console / Test Results */}
      {(output || testResults) && (
        <div style={{
          background: 'var(--bg-secondary)',
          border: '1px solid var(--border-color)',
          borderRadius: 'var(--radius-md)',
          padding: '14px',
          display: 'flex',
          flexDirection: 'column',
          gap: '10px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid var(--border-color)', paddingBottom: '8px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-secondary)' }}>
              <Terminal size={16} />
              Console Output & Test Results
            </div>
            {testResults && (
              <span style={{
                fontSize: '0.8rem',
                fontWeight: 600,
                padding: '2px 8px',
                borderRadius: '10px',
                background: testResults.passed ? 'var(--accent-green-bg)' : 'var(--accent-red-bg)',
                color: testResults.passed ? 'var(--accent-green)' : 'var(--accent-red)'
              }}>
                {testResults.passed ? 'All Test Cases Passed! ✓' : `${testResults.tests_passed}/${testResults.total_tests} Tests Passed`}
              </span>
            )}
          </div>

          {/* Beginner Friendly Advice Banner */}
          {advice && (
            <div style={{
              padding: '12px 14px',
              borderRadius: 'var(--radius-sm)',
              background: 'rgba(210, 153, 34, 0.12)',
              border: '1px solid rgba(210, 153, 34, 0.4)',
              display: 'flex',
              flexDirection: 'column',
              gap: '6px'
            }}>
              <div style={{ fontWeight: 700, fontSize: '0.9rem', color: '#e3b341', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Lightbulb size={16} color="#e3b341" />
                <span>Beginner Helper: {advice.title}</span>
              </div>
              <div style={{ fontSize: '0.85rem', color: 'var(--text-primary)', lineHeight: 1.5 }}>
                {advice.message}
              </div>
            </div>
          )}

          {/* Test Case Details Table */}
          {testResults?.test_results && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
              {testResults.test_results.map((tr, idx) => (
                <div
                  key={idx}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '6px',
                    padding: '8px 10px',
                    borderRadius: 'var(--radius-sm)',
                    background: tr.passed ? 'var(--accent-green-bg)' : 'var(--accent-red-bg)',
                    fontSize: '0.85rem'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '8px', flexWrap: 'wrap' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      {tr.passed ? <CheckCircle2 size={16} color="var(--accent-green)" /> : <XCircle size={16} color="var(--accent-red)" />}
                      <span style={{ fontWeight: 600 }}>Test Case #{tr.test_index}</span>
                    </div>
                    <span style={{ color: tr.passed ? 'var(--accent-green)' : 'var(--accent-red)', fontWeight: 600 }}>
                      {tr.passed ? 'Passed' : 'Failed'}
                    </span>
                  </div>

                  {!tr.passed && (
                    <div style={{
                      display: 'grid',
                      gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
                      gap: '6px'
                    }}>
                      <div>
                        <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)', marginBottom: '2px' }}>INPUT</div>
                        <pre className="code-output">{tr.input || '(none)'}</pre>
                      </div>
                      <div>
                        <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)', marginBottom: '2px' }}>EXPECTED</div>
                        <pre className="code-output">{tr.expected_output || '(empty)'}</pre>
                      </div>
                      <div>
                        <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)', marginBottom: '2px' }}>YOUR OUTPUT</div>
                        <pre className="code-output">{tr.actual_output || '(empty)'}</pre>
                      </div>
                    </div>
                  )}

                  {tr.stderr && (
                    <pre className="code-output" style={{ color: 'var(--accent-red)' }}>{tr.stderr}</pre>
                  )}
                </div>
              ))}
            </div>
          )}

          {/* Standard Output */}
          {output?.stdout && (
            <div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: '4px' }}>STANDARD OUTPUT:</div>
              <pre style={{
                margin: 0,
                padding: '8px 12px',
                borderRadius: 'var(--radius-sm)',
                background: 'var(--bg-tertiary)',
                color: 'var(--text-primary)',
                fontFamily: 'var(--font-mono)',
                fontSize: '0.85rem',
                whiteSpace: 'pre-wrap',
                maxHeight: '180px',
                overflowY: 'auto'
              }}>
                {output.stdout}
              </pre>
            </div>
          )}

          {/* Empty output indicator */}
          {output && !output.stdout && !output.stderr && !testResults && (
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', fontStyle: 'italic', padding: '6px 4px' }}>
              ℹ️ Program executed successfully with no console output (Exit Code {output.exit_code ?? 0}).
            </div>
          )}

          {/* Standard Error / Security Error */}
          {output?.stderr && (
            <div>
              <div style={{ fontSize: '0.75rem', color: 'var(--accent-red)', marginBottom: '4px' }}>ERROR / TRACEBACK:</div>
              <pre style={{
                margin: 0,
                padding: '8px 12px',
                borderRadius: 'var(--radius-sm)',
                background: 'rgba(248, 81, 73, 0.1)',
                border: '1px solid rgba(248, 81, 73, 0.3)',
                color: 'var(--accent-red)',
                fontFamily: 'var(--font-mono)',
                fontSize: '0.85rem',
                whiteSpace: 'pre-wrap',
                maxHeight: '180px',
                overflowY: 'auto'
              }}>
                {output.stderr}
              </pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
