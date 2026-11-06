import React, { useState, useEffect } from 'react';
import {
  X, BookOpen, Code2, HelpCircle, Trophy, CheckCircle,
  ArrowRight, RefreshCw, Lock, Lightbulb, Terminal, Cpu, AlertTriangle, CheckCircle2
} from 'lucide-react';
import { api } from '../api/client';
import CodeEditor from './CodeEditor';
import { useAuth } from '../context/AuthContext';
import curriculumData from '../data/curriculum.json';

const JSON_LESSON_FIELDS = [
  'learning_objectives', 'terminology', 'practical_examples', 'line_by_line',
  'common_mistakes', 'practice_questions'
];

const getChallengeInputGuidance = (challenge) => {
  const sampleInput = challenge?.test_cases?.[0]?.input_data;
  if (typeof sampleInput === 'string' && sampleInput.trim()) {
    return 'The sample input shown here is sent to your program automatically when you click Run Example. Read it with input(); do not type these sample values into your code. Submit Code also checks other input values.';
  }
  return 'This example does not send any input. Do not add input() unless the task asks your program to read a value.';
};

function normalizeLesson(lesson) {
  if (!lesson) return lesson;
  const normalized = { ...lesson };
  for (const field of JSON_LESSON_FIELDS) {
    const value = normalized[field];
    if (typeof value === 'string') {
      try {
        normalized[field] = JSON.parse(value);
      } catch {
        // Keep ordinary prose intact when the field is not JSON-encoded.
      }
    }
  }
  return normalized;
}

// Helper to tokenize and render inline code, bold text, quotes, and keywords
function renderTokenizedInline(text) {
  if (!text) return null;
  const normalized = String(text)
    .replace(/&rarr;/g, '→')
    .replace(/&larr;/g, '←')
    .replace(/&gt;/g, '>')
    .replace(/&lt;/g, '<')
    .replace(/&amp;/g, '&');
  const parts = normalized.split(/(`[^`]+`|\*\*[^*]+\*\*)/g);

  return parts.map((part, i) => {
    if (!part) return null;

    // Backtick code: `...`
    if (part.startsWith('`') && part.endsWith('`')) {
      const code = part.slice(1, -1);
      return (
        <span
          key={i}
          style={{
            fontFamily: 'var(--font-mono)',
            fontSize: '0.88rem',
            fontWeight: 700,
            padding: '2px 7px',
            borderRadius: '5px',
            background: 'rgba(56, 139, 253, 0.18)',
            color: '#58a6ff',
            border: '1px solid rgba(56, 139, 253, 0.35)',
            margin: '0 3px',
            display: 'inline-block'
          }}
        >
          {code}
        </span>
      );
    }

    // Bold text: **...**
    if (part.startsWith('**') && part.endsWith('**') && part.length > 4) {
      const boldText = part.slice(2, -2);
      return (
        <strong key={i} style={{ color: 'var(--text-primary)', fontWeight: 800 }}>
          {boldText}
        </strong>
      );
    }

    return <span key={i}>{part}</span>;
  });
}

// Color-highlights code, keywords, quotes, and wraps special callout blocks into cards
function HighlightedLessonText({ text }) {
  if (!text) return null;
  const paragraphs = text.split('\n\n');

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
      {paragraphs.map((para, pIdx) => {
        const trimmed = para.trim().replace(/^#{1,6}\s*/gm, '');
        if (!trimmed) return null;

        const isWhy = trimmed.startsWith('🎯') || trimmed.toLowerCase().includes('why do we use') || trimmed.toLowerCase().includes('why do we need') || trimmed.toLowerCase().includes('why use');
        const isWhat = trimmed.startsWith('🤖') || trimmed.toLowerCase().includes('what python does') || trimmed.toLowerCase().includes('step-by-step');
        const isRule = trimmed.startsWith('⚠️') || trimmed.toLowerCase().includes('crucial rule') || trimmed.toLowerCase().includes('golden rule') || trimmed.toLowerCase().includes('case-sensitive') || trimmed.toLowerCase().includes('case sensitivity');

        let cardBg = 'transparent';
        let cardBorder = 'none';
        let cardPadding = '0';
        let cardRadius = '0';

        if (isWhy) {
          cardBg = 'rgba(210, 153, 34, 0.09)';
          cardBorder = '1px solid rgba(210, 153, 34, 0.35)';
          cardPadding = '14px 18px';
          cardRadius = 'var(--radius-md)';
        } else if (isWhat) {
          cardBg = 'rgba(56, 139, 253, 0.09)';
          cardBorder = '1px solid rgba(56, 139, 253, 0.35)';
          cardPadding = '14px 18px';
          cardRadius = 'var(--radius-md)';
        } else if (isRule) {
          cardBg = 'rgba(248, 81, 73, 0.09)';
          cardBorder = '1px solid rgba(248, 81, 73, 0.35)';
          cardPadding = '14px 18px';
          cardRadius = 'var(--radius-md)';
        }

        // Split paragraph into lines to detect lists (e.g., 1. .strip()..., 2. .lower()...)
        // Auto-split inline numbered items like "Key Methods: 1. ... 2. ..." into individual lines
        const normalizedPara = trimmed.replace(/([^\n])\s+(?=[0-9]+[.)]\s)/g, '$1\n');
        const rawLines = normalizedPara.split('\n');
        const lines = rawLines.map(l => l.trim()).filter(Boolean);
        const hasListItems = lines.some(l => /^[0-9]+[.)]/.test(l) || l.startsWith('- ') || l.startsWith('• '));

        if (hasListItems) {
          return (
            <div
              key={pIdx}
              style={{
                background: cardBg,
                border: cardBorder,
                padding: cardPadding,
                borderRadius: cardRadius,
                display: 'flex',
                flexDirection: 'column',
                gap: '10px'
              }}
            >
              {lines.map((line, lIdx) => {
                const isItem = /^[0-9]+[.)]/.test(line);
                const isBullet = line.startsWith('- ') || line.startsWith('• ');

                if (isItem) {
                  return (
                    <div
                      key={lIdx}
                      style={{
                        padding: '12px 16px',
                        background: 'rgba(56, 139, 253, 0.05)',
                        border: '1px solid rgba(56, 139, 253, 0.2)',
                        borderRadius: 'var(--radius-sm)',
                        lineHeight: 1.7,
                        fontSize: '0.93rem',
                        color: 'var(--text-primary)',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '4px'
                      }}
                    >
                      <div>{renderTokenizedInline(line)}</div>
                    </div>
                  );
                }

                if (isBullet) {
                  return (
                    <div
                      key={lIdx}
                      style={{
                        padding: '8px 14px',
                        background: 'rgba(255, 255, 255, 0.02)',
                        borderLeft: '3px solid var(--accent-blue)',
                        lineHeight: 1.6,
                        fontSize: '0.9rem',
                        color: 'var(--text-primary)'
                      }}
                    >
                      {renderTokenizedInline(line)}
                    </div>
                  );
                }

                return (
                  <div key={lIdx} style={{ lineHeight: 1.7, fontSize: '0.95rem', color: 'var(--text-primary)', marginBottom: '4px' }}>
                    {renderTokenizedInline(line)}
                  </div>
                );
              })}
            </div>
          );
        }

        return (
          <div
            key={pIdx}
            style={{
              background: cardBg,
              border: cardBorder,
              padding: cardPadding,
              borderRadius: cardRadius,
              lineHeight: 1.8,
              fontSize: '0.95rem',
              color: 'var(--text-primary)',
              whiteSpace: 'pre-line'
            }}
          >
            {renderTokenizedInline(trimmed)}
          </div>
        );
      })}
    </div>
  );
}

export default function LevelModal({ levelId, onClose, onLevelUpdate, onOpenAuth, onNavigateLevel }) {
  const { user, isGuest, progressionMode, refreshUser } = useAuth();
  const isGuestUser = Boolean(isGuest || !user || user?.is_guest);
  const [levelData, setLevelData] = useState(() => curriculumData.levels[String(levelId)] || curriculumData.levels[levelId] || curriculumData.levels[1] || null);
  const [lessonData, setLessonData] = useState(() => normalizeLesson(curriculumData.lessons[String(levelId)] || curriculumData.lessons[levelId] || curriculumData.lessons[1] || null));
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('learn'); // 'learn', 'challenges', 'quiz', 'boss'
  
  // MCQ state
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizResult, setQuizResult] = useState(null);
  const [isSubmittingQuiz, setIsSubmittingQuiz] = useState(false);

  // Lesson completion state
  const [isCompletingLesson, setIsCompletingLesson] = useState(false);

  // Active Challenge index
  const [activeChallengeIdx, setActiveChallengeIdx] = useState(0);

  const getGuestProg = () => {
    try {
      const stored = localStorage.getItem(`pyquest_guest_prog_${levelId}`);
      return stored ? JSON.parse(stored) : {};
    } catch (e) {
      return {};
    }
  };

  const updateGuestProg = (updates) => {
    const current = getGuestProg();
    const updated = { ...current, ...updates };
    
    // Check if level is completed
    const challenges = (levelData?.challenges || []).filter(c => !c.is_boss);
    const hasBoss = (levelData?.challenges || []).some(c => c.is_boss);
    const hasQuiz = (levelData?.quiz_questions || []).length > 0;
    
    const lessonOk = updated.lesson_completed === true;
    const chalOk = challenges.length === 0 || (updated.challenges_passed >= 1);
    const quizOk = !hasQuiz || (updated.mcq_passed && updated.mcq_score >= 80);
    const bossOk = !hasBoss || (updated.boss_completed === true);
    
    if (lessonOk && chalOk && quizOk && bossOk) {
      updated.is_level_completed = true;
      localStorage.setItem(`pyquest_guest_unlocked_${Number(levelId) + 1}`, 'true');
    } else {
      updated.is_level_completed = false;
    }
    
    localStorage.setItem(`pyquest_guest_prog_${levelId}`, JSON.stringify(updated));
    setLevelData(prev => prev ? {
      ...prev,
      user_progress: {
        ...(prev.user_progress || {}),
        ...updated
      }
    } : prev);
    refreshUser();
    if (onLevelUpdate) onLevelUpdate();
    return updated;
  };

  useEffect(() => {
    async function loadData() {
      setLoading(true);
      try {
        const lvlRes = await api.get(`/levels/${levelId}`);
        if (isGuestUser) {
          const gProg = getGuestProg();
          lvlRes.level.user_progress = { ...(lvlRes.level.user_progress || {}), ...gProg };
        }
        setLevelData(lvlRes.level);

        const lsnRes = await api.get(`/lessons/${levelId}`);
        setLessonData(normalizeLesson(lsnRes.lesson));
      } catch (err) {
        console.error('Failed to load level data, using bundled curriculum:', err);
        const fallbackLvl = curriculumData.levels[String(levelId)] || curriculumData.levels[levelId] || curriculumData.levels[1];
        if (fallbackLvl) {
          const gProg = getGuestProg();
          setLevelData({
            ...fallbackLvl,
            user_progress: { ...(fallbackLvl.user_progress || {}), ...gProg }
          });
        }
        const fallbackLsn = curriculumData.lessons[String(levelId)] || curriculumData.lessons[levelId] || curriculumData.lessons[1];
        if (fallbackLsn) {
          setLessonData(normalizeLesson(fallbackLsn));
        }
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, [levelId, isGuestUser]);

  // Synchronize Live AI Context when level, tab, or challenge changes
  useEffect(() => {
    const curLevel = levelData || curriculumData.levels[String(levelId)] || curriculumData.levels[levelId] || curriculumData.levels[1];
    const curLesson = lessonData || normalizeLesson(curriculumData.lessons[String(levelId)] || curriculumData.lessons[levelId] || curriculumData.lessons[1]);
    if (!curLevel) return;

    const isBossTab = activeTab === 'boss';
    const standardChallenges = (curLevel.challenges || []).filter(c => !c.is_boss);
    const activeChal = isBossTab
      ? ((curLevel.challenges || []).find(c => c.is_boss) || null)
      : (standardChallenges[activeChallengeIdx] || standardChallenges[0] || null);

    const chalTitle = activeChal?.title || (
      activeTab === 'learn' ? 'Lesson Overview' : (
        activeTab === 'quiz' ? 'Concept Quiz' : (
          activeTab === 'boss' ? 'Boss Challenge' : 'Coding Challenge'
        )
      )
    );

    const chalInstructions = activeChal?.requirements || activeChal?.description || activeChal?.instructions || (
      activeTab === 'learn' ? (curLesson?.summary || curLesson?.introduction || '') : (
        curLesson?.summary || ''
      )
    );

    window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
      detail: {
        worldTitle: curLevel.world_name || `World ${curLevel.world_id || 1}`,
        levelNumber: curLevel.level_number || curLevel.number || levelId,
        levelTitle: curLevel.title || `Level ${levelId}`,
        tab: activeTab,
        challengeTitle: chalTitle,
        challengeInstructions: chalInstructions,
        challengeDescription: activeChal?.description || '',
        challengeRequirements: activeChal?.requirements || '',
        solutionCode: activeChal?.solution_code || '',
        hints: activeChal?.hints || [],
        lessonSummary: curLesson?.summary || '',
        lessonObjectives: curLesson?.learning_objectives || [],
        lessonSyntax: curLesson?.syntax_breakdown || '',
        lessonExamples: curLesson?.practical_examples || [],
        lessonTerminology: curLesson?.terminology || [],
        lessonCommonMistakes: curLesson?.common_mistakes || [],
        isModalOpen: true
      }
    }));

    return () => {
      window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
        detail: {
          isModalOpen: false,
          worldTitle: 'Free Exploration',
          levelNumber: null,
          levelTitle: '',
          tab: 'general',
          challengeTitle: '',
          challengeInstructions: '',
          challengeDescription: '',
          challengeRequirements: '',
          solutionCode: '',
          hints: [],
          lessonSummary: '',
          lessonObjectives: [],
          lessonSyntax: '',
          lessonExamples: [],
          lessonTerminology: [],
          lessonCommonMistakes: [],
          code: '',
          lastError: '',
          lastStdout: '',
          isModalOpen: false,
        }
      }));
    };
  }, [levelId, levelData, lessonData, activeTab, activeChallengeIdx]);


  const handleCompleteLesson = async (forceValue = null) => {
    const isCurrentlyComplete = Boolean(levelData?.user_progress?.lesson_completed);
    const nextState = forceValue !== null ? forceValue : !isCurrentlyComplete;

    if (nextState) {
      window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
        detail: { action: 'celebrating', message: 'Lesson completed! Ready for the coding challenge? 🚀', duration: 3500 }
      }));
    }

    if (isGuestUser) {
      updateGuestProg({ lesson_completed: nextState });
      return;
    }
    setIsCompletingLesson(true);
    try {
      await api.post('/progress/lesson', { level_id: levelId, completed: nextState });
      refreshUser();
      // Refresh level data
      const lvlRes = await api.get(`/levels/${levelId}`);
      setLevelData(lvlRes.level);
      if (onLevelUpdate) onLevelUpdate();
    } catch (err) {
      alert(err.message || 'Failed to update lesson status');
    } finally {
      setIsCompletingLesson(false);
    }
  };

  const handleQuizOptionSelect = (qId, optId) => {
    if (quizResult) return; // Prevent changing after submit
    setQuizAnswers(prev => ({ ...prev, [qId]: optId }));
  };

  const handleSubmitQuiz = async () => {
    setIsSubmittingQuiz(true);
    try {
      const res = await api.post(`/quizzes/${levelId}/submit`, { answers: quizAnswers });
      setQuizResult(res);
      if (res.passed) {
        window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
          detail: { action: 'celebrating', message: 'Quiz passed with flying colors! 🌟', duration: 4000 }
        }));
      } else {
        window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
          detail: { action: 'reading', message: 'Review the lesson notes and try again!', duration: 3500 }
        }));
      }
      if (isGuestUser) {
        updateGuestProg({ mcq_score: res.score_percent, mcq_passed: res.passed });
      } else {
        refreshUser();
        const lvlRes = await api.get(`/levels/${levelId}`);
        setLevelData(lvlRes.level);
        if (onLevelUpdate) onLevelUpdate();
      }
    } catch (err) {
      alert(err.message || 'Quiz submission failed');
    } finally {
      setIsSubmittingQuiz(false);
    }
  };

  const handleRetryQuiz = () => {
    setQuizResult(null);
    setQuizAnswers({});
  };

  const handleChallengePassed = async (isBoss = false) => {
    if (isBoss) {
      window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
        detail: { action: 'levelUp', message: 'LEVEL UP! Incredible job! 👑', duration: 5000 }
      }));
    } else {
      window.dispatchEvent(new CustomEvent('pyquest:pet-reaction', {
        detail: { action: 'celebrating', message: 'Challenge Cleared! Awesome job! 🎉', duration: 4200 }
      }));
    }

    if (isGuestUser) {
      if (isBoss) {
        updateGuestProg({ boss_completed: true });
      } else {
        updateGuestProg({ challenges_passed: 1 });
      }
      return;
    }
    refreshUser();
    try {
      const lvlRes = await api.get(`/levels/${levelId}`);
      if (lvlRes?.level) {
        setLevelData(lvlRes.level);
      }
    } catch (err) {
      console.warn('Failed to refresh level data after challenge passed:', err);
    }
    if (onLevelUpdate) onLevelUpdate();
  };

  if (loading) {
    return (
      <div className="modal-overlay">
        <div className="modal-content" style={{ padding: '40px', textAlign: 'center' }}>
          <RefreshCw className="spin" size={32} style={{ margin: '0 auto 16px', color: 'var(--accent-blue)' }} />
          <p>Loading Level Content...</p>
        </div>
      </div>
    );
  }

  const baseLevelData = levelData || curriculumData.levels[String(levelId)] || curriculumData.levels[levelId] || curriculumData.levels[1];
  const guestPreviousProgress = (() => {
    if (!isGuestUser) return {};
    try {
      return JSON.parse(localStorage.getItem(`pyquest_guest_prog_${Number(baseLevelData?.number) - 1}`) || '{}');
    } catch {
      return {};
    }
  })();
  const canAccessLevel = progressionMode === 'all'
    || Boolean(baseLevelData?.is_unlocked)
    || Number(baseLevelData?.number) === 1
    || (isGuestUser && guestPreviousProgress.is_level_completed === true);
  const effectiveLevelData = baseLevelData ? { ...baseLevelData, is_unlocked: canAccessLevel } : baseLevelData;
  const effectiveLessonData = lessonData || normalizeLesson(curriculumData.lessons[String(levelId)] || curriculumData.lessons[levelId] || curriculumData.lessons[1]);
  if (!effectiveLevelData) return null;

  const isLineWalkthroughLesson = Number(effectiveLevelData.number) >= 1 && Number(effectiveLevelData.number) <= 126;
  const isWorldSixLesson = Number(effectiveLevelData.number) >= 49 && Number(effectiveLevelData.number) <= 63;
  const isWorldSevenToTwelveLesson = Number(effectiveLevelData.number) >= 64 && Number(effectiveLevelData.number) <= 126;
  const walkthroughOutput = Number(effectiveLevelData.number) <= 48
    ? effectiveLessonData?.practical_examples?.[0]?.output
    : effectiveLessonData?.expected_output;

  const prog = effectiveLevelData.user_progress || {};
  const challenges = (effectiveLevelData.challenges || []).filter(c => !c.is_boss);
  const bossChallenge = (effectiveLevelData.challenges || []).find(c => c.is_boss);
  const questions = effectiveLevelData.quiz_questions || [];

  const isLessonComplete = Boolean(prog.lesson_completed);
  const isChalComplete = challenges.length === 0 || (prog.challenges_passed >= 1);
  const isMcqComplete = questions.length === 0 || (prog.mcq_passed && Number(prog.mcq_score || 0) >= 80);
  const isBossComplete = !bossChallenge || Boolean(prog.boss_completed);

  // Exact section percentages:
  const lessonPercent = isLessonComplete ? 100 : 0;
  const chalPercent = challenges.length === 0 ? 100 : Math.min(100, Math.round(((prog.challenges_passed || 0) / challenges.length) * 100));
  const mcqPercent = questions.length === 0 ? 100 : (prog.mcq_score ? Math.round(prog.mcq_score) : 0);
  const bossPercent = isBossComplete ? 100 : 0;

  // Criteria count and overall level percentage:
  let criteriaCount = 0;
  let passedCount = 0;
  criteriaCount++; if (isLessonComplete) passedCount++;
  if (challenges.length > 0) { criteriaCount++; if (isChalComplete) passedCount++; }
  if (questions.length > 0) { criteriaCount++; if (isMcqComplete) passedCount++; }
  if (bossChallenge) { criteriaCount++; if (isBossComplete) passedCount++; }

  const overallPercent = criteriaCount > 0 ? Math.round((passedCount / criteriaCount) * 100) : 100;
  const isLevelFullyComplete = overallPercent === 100 || Boolean(prog.is_level_completed);

  if (progressionMode !== 'all' && !canAccessLevel) {
    return (
      <div className="modal-overlay">
        <div className="modal-content" style={{ padding: '32px', textAlign: 'center', maxWidth: '520px' }}>
          <Lock size={34} color="var(--accent-gold)" style={{ margin: '0 auto 14px' }} />
          <h2 style={{ fontSize: '1.2rem', marginBottom: '8px' }}>Level {effectiveLevelData.number} is locked</h2>
          <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6, marginBottom: '20px' }}>
            Complete the level before this one to unlock it. Finish every level in the current world to open the next world.
          </p>
          <button onClick={onClose} className="btn btn-primary">Back to Worlds and Levels</button>
        </div>
      </div>
    );
  }

  return (
    <div className="modal-overlay">
      <div className="modal-content large">
        {/* Modal Header */}
        <div className="modal-header">
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '0.8rem', fontWeight: 700, padding: '2px 8px', borderRadius: '12px', background: 'var(--accent-blue-bg)', color: 'var(--accent-blue)' }}>
                LEVEL {effectiveLevelData.number}
              </span>
              <h2 style={{ fontSize: '1.25rem', fontWeight: 700, margin: 0 }}>{effectiveLevelData.title}</h2>

              {/* Overall Progress Indicator Badge */}
              <div
                title="Overall Level Completion Percentage"
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '6px',
                  background: overallPercent === 100 ? 'rgba(46, 160, 67, 0.15)' : 'rgba(56, 139, 253, 0.15)',
                  border: `1px solid ${overallPercent === 100 ? 'var(--accent-green)' : 'var(--accent-blue)'}`,
                  padding: '3px 10px',
                  borderRadius: '14px'
                }}
              >
                <div style={{
                  width: '36px',
                  height: '6px',
                  background: 'rgba(255,255,255,0.15)',
                  borderRadius: '3px',
                  overflow: 'hidden'
                }}>
                  <div style={{
                    width: `${overallPercent}%`,
                    height: '100%',
                    background: overallPercent === 100 ? 'var(--accent-green)' : 'var(--accent-blue)',
                    transition: 'width 0.3s ease'
                  }} />
                </div>
                <span style={{
                  fontSize: '0.8rem',
                  fontWeight: 800,
                  color: overallPercent === 100 ? 'var(--accent-green)' : 'var(--accent-blue)'
                }}>
                  {overallPercent}% Completed
                </span>
              </div>

              {isLevelFullyComplete && (
                <span style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: '0.8rem', fontWeight: 600, color: 'var(--accent-green)', background: 'var(--accent-green-bg)', padding: '2px 8px', borderRadius: '12px' }}>
                  <CheckCircle size={14} /> Completed
                </span>
              )}
            </div>
            <p className="modal-header-desc" style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', margin: '4px 0 0 0' }}>
              {effectiveLevelData.description}
            </p>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0 }}>
            {isLevelFullyComplete && onNavigateLevel && (
              <button
                onClick={() => onNavigateLevel(effectiveLevelData.number + 1)}
                className="btn btn-primary"
                style={{ padding: '6px 14px', fontSize: '0.85rem', fontWeight: 700 }}
              >
                Level {effectiveLevelData.number + 1} →
              </button>
            )}
            <button onClick={onClose} className="btn-icon">
              <X size={20} />
            </button>
          </div>
        </div>

        {/* Single Unified Level Navigation Tabs */}
        <div className="level-tabs" style={{
          borderBottom: '1px solid var(--border-color)',
          background: 'var(--bg-secondary)',
          padding: '0 16px',
          display: 'flex',
          gap: '8px',
          overflowX: 'auto',
          alignItems: 'center'
        }}>
          <button
            onClick={() => setActiveTab('learn')}
            className="level-tab"
            style={{
              padding: '12px 14px',
              border: 'none',
              background: 'none',
              borderBottom: activeTab === 'learn' ? '2px solid var(--accent-blue)' : '2px solid transparent',
              color: activeTab === 'learn' ? 'var(--accent-blue)' : 'var(--text-secondary)',
              fontWeight: 600,
              fontSize: '0.88rem',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              whiteSpace: 'nowrap',
              transition: 'all 0.2s ease'
            }}
          >
            <BookOpen size={17} />
            <span>1. Learn</span>
            <span style={{
              fontSize: '0.72rem',
              fontWeight: 700,
              padding: '1px 6px',
              borderRadius: '8px',
              background: isLessonComplete ? 'rgba(46, 160, 67, 0.2)' : activeTab === 'learn' ? 'rgba(56, 139, 253, 0.15)' : 'var(--bg-tertiary)',
              color: isLessonComplete ? 'var(--accent-green)' : activeTab === 'learn' ? 'var(--accent-blue)' : 'var(--text-muted)'
            }}>
              {lessonPercent}% {isLessonComplete ? '✓' : ''}
            </span>
          </button>

          <button
            onClick={() => setActiveTab('challenges')}
            className="level-tab"
            style={{
              padding: '12px 14px',
              border: 'none',
              background: 'none',
              borderBottom: activeTab === 'challenges' ? '2px solid var(--accent-blue)' : '2px solid transparent',
              color: activeTab === 'challenges' ? 'var(--accent-blue)' : 'var(--text-secondary)',
              fontWeight: 600,
              fontSize: '0.88rem',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              whiteSpace: 'nowrap',
              transition: 'all 0.2s ease'
            }}
          >
            <Code2 size={17} />
            <span>2. Challenges</span>
            <span style={{
              fontSize: '0.72rem',
              fontWeight: 700,
              padding: '1px 6px',
              borderRadius: '8px',
              background: isChalComplete ? 'rgba(46, 160, 67, 0.2)' : activeTab === 'challenges' ? 'rgba(56, 139, 253, 0.15)' : 'var(--bg-tertiary)',
              color: isChalComplete ? 'var(--accent-green)' : activeTab === 'challenges' ? 'var(--accent-blue)' : 'var(--text-muted)'
            }}>
              {chalPercent}% {isChalComplete ? '✓' : ''}
            </span>
          </button>

          <button
            onClick={() => setActiveTab('quiz')}
            className="level-tab"
            style={{
              padding: '12px 14px',
              border: 'none',
              background: 'none',
              borderBottom: activeTab === 'quiz' ? '2px solid var(--accent-blue)' : '2px solid transparent',
              color: activeTab === 'quiz' ? 'var(--accent-blue)' : 'var(--text-secondary)',
              fontWeight: 600,
              fontSize: '0.88rem',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              whiteSpace: 'nowrap',
              transition: 'all 0.2s ease'
            }}
          >
            <HelpCircle size={17} />
            <span>3. Examination</span>
            <span style={{
              fontSize: '0.72rem',
              fontWeight: 700,
              padding: '1px 6px',
              borderRadius: '8px',
              background: isMcqComplete ? 'rgba(46, 160, 67, 0.2)' : activeTab === 'quiz' ? 'rgba(56, 139, 253, 0.15)' : 'var(--bg-tertiary)',
              color: isMcqComplete ? 'var(--accent-green)' : activeTab === 'quiz' ? 'var(--accent-blue)' : 'var(--text-muted)'
            }}>
              {mcqPercent}% {isMcqComplete ? '✓' : ''}
            </span>
          </button>

          <button
            onClick={() => setActiveTab('boss')}
            className="level-tab"
            style={{
              padding: '12px 14px',
              border: 'none',
              background: 'none',
              borderBottom: activeTab === 'boss' ? '2px solid var(--accent-purple)' : '2px solid transparent',
              color: activeTab === 'boss' ? 'var(--accent-purple)' : 'var(--text-secondary)',
              fontWeight: 600,
              fontSize: '0.88rem',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              whiteSpace: 'nowrap',
              transition: 'all 0.2s ease'
            }}
          >
            <Trophy size={17} color="var(--accent-purple)" />
            <span>4. Boss Challenge</span>
            <span style={{
              fontSize: '0.72rem',
              fontWeight: 700,
              padding: '1px 6px',
              borderRadius: '8px',
              background: isBossComplete ? 'rgba(46, 160, 67, 0.2)' : activeTab === 'boss' ? 'rgba(163, 113, 247, 0.2)' : 'var(--bg-tertiary)',
              color: isBossComplete ? 'var(--accent-green)' : activeTab === 'boss' ? 'var(--accent-purple)' : 'var(--text-muted)'
            }}>
              {bossPercent}% {isBossComplete ? '✓' : ''}
            </span>
          </button>
        </div>

        {/* Modal Body: Active Tab Content */}
        <div className="modal-body" style={{ flex: 1, padding: '24px' }}>
          {/* Level Complete Advance Banner */}
          {isLevelFullyComplete && (
            <div style={{
              background: 'linear-gradient(135deg, rgba(46, 160, 67, 0.15), rgba(56, 139, 253, 0.15))',
              border: '2px solid var(--accent-green)',
              borderRadius: 'var(--radius-md)',
              padding: '14px 20px',
              marginBottom: '16px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '12px'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <span style={{ fontSize: '1.8rem' }}>🎉</span>
                <div>
                  <h4 style={{ fontSize: '1rem', fontWeight: 800, color: 'var(--accent-green)', margin: 0 }}>
                    LEVEL {effectiveLevelData.number} COMPLETED!
                  </h4>
                  <p style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', margin: '2px 0 0 0' }}>
                    All requirements passed. Level {effectiveLevelData.number + 1} is now unlocked!
                  </p>
                </div>
              </div>
              {onNavigateLevel && (
                <button
                  onClick={() => onNavigateLevel(effectiveLevelData.number + 1)}
                  className="btn btn-primary"
                  style={{ padding: '8px 20px', fontSize: '0.9rem', fontWeight: 700 }}
                >
                  Continue to Level {effectiveLevelData.number + 1} →
                </button>
              )}
            </div>
          )}

          {/* Preview Mode Banner for locked levels */}
          {!effectiveLevelData.is_unlocked && !isLevelFullyComplete && (
            <div style={{
              background: 'rgba(210, 153, 34, 0.12)',
              border: '1px solid var(--accent-gold)',
              borderRadius: 'var(--radius-md)',
              padding: '12px 18px',
              marginBottom: '16px',
              display: 'flex',
              alignItems: 'center',
              gap: '12px'
            }}>
              <Lock size={20} color="var(--accent-gold)" style={{ flexShrink: 0 }} />
              <div style={{ fontSize: '0.85rem', color: 'var(--text-primary)' }}>
                <strong>Preview Mode:</strong> You are exploring <strong>Level {effectiveLevelData.number}: {effectiveLevelData.title}</strong>. You can read the complete lesson, inspect all challenges, and review the code quizzes! Complete previous levels sequentially to record verified progress and earn XP.
              </div>
            </div>
          )}

          {/* Guest notice */}
          {isGuestUser && (
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '8px',
              padding: '10px 16px',
              background: 'var(--accent-gold-bg)',
              border: '1px solid rgba(210, 153, 34, 0.3)',
              borderRadius: 'var(--radius-md)',
              marginBottom: '16px',
              fontSize: '0.82rem',
              color: 'var(--text-primary)'
            }}>
              <span>
                👋 Playing in Guest Mode. Your progress will be saved in your browser storage.
              </span>
              <button onClick={onOpenAuth} className="btn btn-primary" style={{ padding: '5px 14px', fontSize: '0.8rem' }}>
                Create Account to Sync
              </button>
            </div>
          )}
          {/* TAB 1: LEARN (13 Sections) */}
          {activeTab === 'learn' && lessonData && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '20px', maxWidth: '850px', margin: '0 auto' }}>
              {/* Top Lesson Completion Action Banner */}
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                flexWrap: 'wrap',
                gap: '12px',
                background: isLessonComplete ? 'rgba(46, 160, 67, 0.12)' : 'var(--bg-secondary)',
                border: `1.5px solid ${isLessonComplete ? 'var(--accent-green)' : 'var(--border-color)'}`,
                padding: '14px 20px',
                borderRadius: 'var(--radius-md)'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <CheckCircle size={22} color={isLessonComplete ? 'var(--accent-green)' : 'var(--border-color)'} />
                  <div>
                    <div style={{ fontWeight: 700, fontSize: '0.95rem', color: isLessonComplete ? 'var(--accent-green)' : 'var(--text-primary)' }}>
                      {isLessonComplete ? '✓ Lesson Completed (100%)' : 'Lesson In Progress (0%)'}
                    </div>
                    <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)' }}>
                      {isLessonComplete ? '+50 XP claimed! You can review concepts anytime.' : 'Study the lesson below and click to mark it completed.'}
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => handleCompleteLesson()}
                  disabled={isCompletingLesson}
                  className={isLessonComplete ? 'btn btn-secondary' : 'btn btn-primary'}
                  style={{
                    padding: '8px 20px',
                    fontSize: '0.88rem',
                    fontWeight: 700,
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px'
                  }}
                >
                  <CheckCircle size={16} />
                  {isCompletingLesson
                    ? 'Saving...'
                    : isLessonComplete
                      ? 'Completed ✓ (Toggle)'
                      : 'Mark Lesson Completed (+50 XP)'}
                </button>
              </div>

              {/* A. Learning Objectives */}
              <div className="card" style={{ borderLeft: '4px solid var(--accent-blue)' }}>
                <h3 style={{ fontSize: '1rem', fontWeight: 700, color: 'var(--accent-blue)', marginBottom: '8px' }}>
                  🎯 Learning Objectives
                </h3>
                <ul style={{ paddingLeft: '20px', display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  {(Array.isArray(lessonData.learning_objectives) ? lessonData.learning_objectives : [lessonData.learning_objectives]).map((obj, i) => (
                    <li key={i} style={{ fontSize: '0.9rem', color: 'var(--text-primary)' }}>{obj}</li>
                  ))}
                </ul>
              </div>

              {/* B. Prerequisites */}
              {lessonData.prerequisites && (
                <div style={{ background: 'var(--bg-tertiary)', padding: '12px 16px', borderRadius: 'var(--radius-md)', fontSize: '0.85rem' }}>
                  <span style={{ fontWeight: 600, color: 'var(--text-secondary)' }}>Prerequisites: </span>
                  <span style={{ color: 'var(--text-primary)' }}>{lessonData.prerequisites}</span>
                </div>
              )}

              {/* C. Introduction */}
              <div>
                <h3 style={{ fontSize: '1.1rem', fontWeight: 800, marginBottom: '10px', color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span>📘</span> Introduction
                </h3>
                <HighlightedLessonText text={lessonData.introduction} />
              </div>

              {/* D. Detailed Explanation */}
              <div>
                <h3 style={{ fontSize: '1.1rem', fontWeight: 800, marginBottom: '10px', color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span>🔍</span> Detailed Explanation
                </h3>
                <HighlightedLessonText text={lessonData.detailed_explanation} />
              </div>

              {/* E. Technical Terminology */}
              {Array.isArray(lessonData.terminology) && lessonData.terminology.length > 0 && (
                <div style={{ marginBottom: '8px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px', flexWrap: 'wrap', gap: '8px' }}>
                    <h3 style={{ fontSize: '1.1rem', fontWeight: 800, margin: 0, color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span>💡</span> Key Vocabulary & Words (Plain English)
                    </h3>
                    <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                      Everyday analogies so you never get confused by programming terms
                    </span>
                  </div>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '12px' }}>
                    {lessonData.terminology.map((t, idx) => (
                      <div key={idx} style={{
                        padding: '16px',
                        borderRadius: 'var(--radius-md)',
                        background: 'var(--bg-tertiary)',
                        border: '1.5px solid rgba(163, 113, 247, 0.25)',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '8px',
                        transition: 'transform 0.15s ease'
                      }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{
                            fontWeight: 800,
                            color: '#a371f7',
                            background: 'rgba(163, 113, 247, 0.15)',
                            border: '1px solid rgba(163, 113, 247, 0.35)',
                            padding: '4px 10px',
                            borderRadius: '6px',
                            fontSize: '0.88rem',
                            fontFamily: 'var(--font-mono)'
                          }}>
                            {t.term}
                          </span>
                        </div>
                        <div style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', lineHeight: 1.6 }}>
                          {t.definition}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* F. Syntax Breakdown */}
              {lessonData.syntax_breakdown && (
                <div>
                  <h3 style={{ fontSize: '1.1rem', fontWeight: 800, marginBottom: '10px', color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span>📐</span> Visual Syntax Blueprint
                  </h3>
                  
                  {Number(effectiveLevelData.id) === 1 ? (
                    <div>
                      {/* Mobile View: Dedicated color-coded component that fits narrow phone screens cleanly */}
                      <div className="mobile-only">
                        <div style={{
                          padding: '16px',
                          borderRadius: 'var(--radius-md)',
                          background: 'var(--bg-primary)',
                          border: '1.5px solid var(--border-color)',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '14px'
                        }}>
                          <div style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', fontWeight: 600 }}>
                            Every print command has 3 essential parts:
                          </div>

                          {/* Code Display */}
                          <div style={{
                            background: '#0d1117',
                            border: '1px solid #30363d',
                            borderRadius: '8px',
                            padding: '14px',
                            fontFamily: 'var(--font-mono)',
                            fontSize: '1.05rem',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            gap: '4px',
                            flexWrap: 'wrap'
                          }}>
                            <span style={{ color: '#58a6ff', fontWeight: 800 }}>print</span>
                            <span style={{ color: '#bc8cff', fontWeight: 800 }}>(</span>
                            <span style={{ color: '#bc8cff', fontWeight: 800 }}>'</span>
                            <span style={{ color: '#e3b341', fontWeight: 800 }}>Your message here</span>
                            <span style={{ color: '#bc8cff', fontWeight: 800 }}>'</span>
                            <span style={{ color: '#bc8cff', fontWeight: 800 }}>)</span>
                          </div>

                          {/* Explanation Cards for each part */}
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                            <div style={{
                              display: 'flex',
                              alignItems: 'flex-start',
                              gap: '10px',
                              background: 'rgba(88, 166, 255, 0.1)',
                              border: '1px solid rgba(88, 166, 255, 0.3)',
                              borderRadius: '8px',
                              padding: '10px 12px'
                            }}>
                              <span style={{
                                background: '#58a6ff',
                                color: '#0d1117',
                                fontWeight: 800,
                                fontSize: '0.75rem',
                                padding: '3px 8px',
                                borderRadius: '4px',
                                fontFamily: 'var(--font-mono)',
                                flexShrink: 0
                              }}>COMMAND</span>
                              <div style={{ fontSize: '0.84rem', color: 'var(--text-primary)', lineHeight: 1.5 }}>
                                <strong>print</strong> &mdash; Built-in Python function name (MUST be strictly lowercase!)
                              </div>
                            </div>

                            <div style={{
                              display: 'flex',
                              alignItems: 'flex-start',
                              gap: '10px',
                              background: 'rgba(188, 140, 255, 0.1)',
                              border: '1px solid rgba(188, 140, 255, 0.3)',
                              borderRadius: '8px',
                              padding: '10px 12px'
                            }}>
                              <span style={{
                                background: '#bc8cff',
                                color: '#0d1117',
                                fontWeight: 800,
                                fontSize: '0.75rem',
                                padding: '3px 8px',
                                borderRadius: '4px',
                                fontFamily: 'var(--font-mono)',
                                flexShrink: 0
                              }}>CONTAINER</span>
                              <div style={{ fontSize: '0.84rem', color: 'var(--text-primary)', lineHeight: 1.5 }}>
                                <strong>( '</strong> and <strong>' )</strong> &mdash; Opening and closing brackets & quotation marks. Brackets tell Python what to run; quotes hold text!
                              </div>
                            </div>

                            <div style={{
                              display: 'flex',
                              alignItems: 'flex-start',
                              gap: '10px',
                              background: 'rgba(227, 179, 65, 0.1)',
                              border: '1px solid rgba(227, 179, 65, 0.3)',
                              borderRadius: '8px',
                              padding: '10px 12px'
                            }}>
                              <span style={{
                                background: '#e3b341',
                                color: '#0d1117',
                                fontWeight: 800,
                                fontSize: '0.75rem',
                                padding: '3px 8px',
                                borderRadius: '4px',
                                fontFamily: 'var(--font-mono)',
                                flexShrink: 0
                              }}>STRING TEXT</span>
                              <div style={{ fontSize: '0.84rem', color: 'var(--text-primary)', lineHeight: 1.5 }}>
                                <strong>'Your message here'</strong> &mdash; Your exact words inside quotes that Python displays on screen.
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>

                      {/* Desktop View: Exact same ASCII blueprint for wide screens */}
                      <div className="desktop-only">
                        <div style={{
                          padding: '16px',
                          borderRadius: 'var(--radius-md)',
                          background: 'var(--bg-primary)',
                          border: '1.5px solid var(--border-color)',
                          fontFamily: 'var(--font-mono)',
                          fontSize: '0.92rem',
                          color: '#79c0ff',
                          whiteSpace: 'pre',
                          overflowX: 'auto',
                          lineHeight: 1.6
                        }}>
                          {lessonData.syntax_breakdown}
                        </div>
                      </div>
                    </div>
                  ) : (
                    <div style={{
                      padding: '16px',
                      borderRadius: 'var(--radius-md)',
                      background: 'var(--bg-primary)',
                      border: '1.5px solid var(--border-color)',
                      fontFamily: 'var(--font-mono)',
                      fontSize: '0.92rem',
                      color: '#79c0ff',
                      whiteSpace: 'pre-wrap',
                      overflowX: 'auto',
                      lineHeight: 1.6
                    }}>
                      {lessonData.syntax_breakdown}
                    </div>
                  )}
                </div>
              )}

              {/* G. Practical Examples & H. Line-by-Line */}
              {Array.isArray(lessonData.practical_examples) && lessonData.practical_examples.length > 0 && (
                <div>
                  <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '12px' }}>💻 Practical Examples</h3>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                    {lessonData.practical_examples.map((ex, idx) => (
                      <div key={idx} className="card" style={{ padding: '16px' }}>
                        <div style={{ fontWeight: 600, marginBottom: '8px', color: 'var(--text-primary)' }}>{ex.title}</div>
                        <pre style={{
                          padding: '12px',
                          borderRadius: 'var(--radius-sm)',
                          background: 'var(--bg-primary)',
                          fontFamily: 'var(--font-mono)',
                          fontSize: '0.9rem',
                          color: '#56d364',
                          whiteSpace: 'pre-wrap',
                          marginBottom: '8px'
                        }}>
                          {ex.code}
                        </pre>
                        <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '8px', whiteSpace: isWorldSevenToTwelveLesson ? 'pre-wrap' : undefined }}>{ex.explanation}</p>
                        {ex.output && (
                          <div style={{ fontSize: '0.8rem', background: 'var(--bg-tertiary)', padding: '6px 10px', borderRadius: 'var(--radius-sm)', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)', whiteSpace: isLineWalkthroughLesson ? 'pre-wrap' : undefined }}>
                            Expected Output: {ex.output}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {isLineWalkthroughLesson && Array.isArray(lessonData.line_by_line) && lessonData.line_by_line.length > 0 && (
                <div>
                  <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '12px' }}>Line-by-Line Walkthrough</h3>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                    {lessonData.line_by_line.map((step, idx) => (
                      <div key={idx} className="card" style={{ padding: '12px 16px' }}>
                        <div style={{ fontWeight: 700, color: 'var(--accent-blue)', marginBottom: '6px' }}>
                          Line {step.line || idx + 1}
                        </div>
                        {step.code && (
                          <pre style={{ margin: '0 0 8px', padding: '10px 12px', borderRadius: '6px', background: 'var(--bg-primary)', fontFamily: 'var(--font-mono)', fontSize: '0.88rem', whiteSpace: 'pre-wrap' }}>
                            {step.code}
                          </pre>
                        )}
                        {step.explanation && <p style={{ margin: 0, lineHeight: 1.6, color: 'var(--text-secondary)' }}>{step.explanation}</p>}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {isLineWalkthroughLesson && walkthroughOutput && (
                <div className="card">
                  <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: '8px' }}>Output from the Walkthrough</h3>
                  <pre style={{ margin: 0, padding: '12px', borderRadius: '6px', background: 'var(--bg-primary)', fontFamily: 'var(--font-mono)', whiteSpace: 'pre-wrap' }}>
                    {walkthroughOutput}
                  </pre>
                </div>
              )}

              {(isWorldSixLesson || isWorldSevenToTwelveLesson) && Array.isArray(lessonData.practice_questions) && lessonData.practice_questions.length > 0 && (
                <div className="card">
                  <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: '8px' }}>Practice and Self-Check</h3>
                  <ol style={{ margin: 0, paddingLeft: '22px', display: 'flex', flexDirection: 'column', gap: '8px', lineHeight: 1.6 }}>
                    {lessonData.practice_questions.map((question, idx) => (
                      <li key={idx}>
                        {typeof question === 'string' ? question : (
                          <>
                            <div>{question.question}</div>
                            {question.answer && (
                              <details style={{ marginTop: '4px', color: 'var(--text-secondary)' }}>
                                <summary style={{ cursor: 'pointer', color: 'var(--accent-blue)' }}>Show answer</summary>
                                <div style={{ marginTop: '4px' }}>{question.answer}</div>
                              </details>
                            )}
                          </>
                        )}
                      </li>
                    ))}
                  </ol>
                </div>
              )}

              {/* J. Common Mistakes */}
              {Array.isArray(lessonData.common_mistakes) && lessonData.common_mistakes.length > 0 && (
                <div>
                  <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: 'var(--accent-red)', marginBottom: '12px' }}>
                    ⚠️ Common Mistakes to Avoid
                  </h3>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    {lessonData.common_mistakes.map((m, idx) => (
                      <div key={idx} style={{ padding: '14px', borderRadius: 'var(--radius-md)', background: 'var(--accent-red-bg)', border: '1px solid rgba(248, 81, 73, 0.3)' }}>
                        <div style={{ fontFamily: 'var(--font-mono)', color: 'var(--accent-red)', fontWeight: 600, fontSize: '0.9rem', marginBottom: '4px' }}>
                          ❌ Mistake: {m.mistake}
                        </div>
                        <div style={{ fontSize: '0.85rem', color: 'var(--text-primary)', marginBottom: '6px' }}>
                          <strong>Why it fails:</strong> {m.why}
                        </div>
                        <div style={{ fontFamily: 'var(--font-mono)', color: 'var(--accent-green)', fontSize: '0.85rem' }}>
                          ✓ Correct Fix: {m.fix}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* K. Real-World Applications */}
              {lessonData.real_world_apps && (
                <div className="card">
                  <h3 style={{ fontSize: '1rem', fontWeight: 700, color: 'var(--accent-gold)', marginBottom: '6px' }}>
                    🌍 Real-World Applications
                  </h3>
                  <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', margin: 0 }}>
                    {lessonData.real_world_apps}
                  </p>
                </div>
              )}

              {/* L. Lesson Summary */}
              {lessonData.summary && (
                <div style={{ background: 'var(--bg-tertiary)', padding: '16px', borderRadius: 'var(--radius-md)', borderLeft: '4px solid var(--accent-green)' }}>
                  <h3 style={{ fontSize: '0.95rem', fontWeight: 700, color: 'var(--accent-green)', marginBottom: '4px' }}>
                    📝 Lesson Summary
                  </h3>
                  <p style={{ fontSize: '0.9rem', color: 'var(--text-primary)', margin: 0 }}>
                    {lessonData.summary}
                  </p>
                </div>
              )}

              {/* Lesson Completion Action Button (Bottom) */}
              <div style={{ display: 'flex', justifyContent: 'center', marginTop: '16px' }}>
                <button
                  onClick={() => handleCompleteLesson()}
                  disabled={isCompletingLesson}
                  className={isLessonComplete ? 'btn btn-secondary' : 'btn btn-primary'}
                  style={{ padding: '12px 32px', fontSize: '1rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '8px' }}
                >
                  <CheckCircle size={20} />
                  {isCompletingLesson
                    ? 'Saving...'
                    : isLessonComplete
                      ? 'Lesson Completed (100% ✓ - Toggle)'
                      : 'Mark Lesson as Completed (+50 XP)'}
                </button>
              </div>
            </div>
          )}

          {/* TAB 2: CODING CHALLENGES */}
          {activeTab === 'challenges' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {challenges.length === 0 ? (
                <p style={{ textAlign: 'center', color: 'var(--text-muted)' }}>No challenges for this level.</p>
              ) : (
                <div>
                  {/* Challenge Selection Tabs if multiple */}
                  {challenges.length > 1 && (
                    <div style={{ display: 'flex', gap: '8px', marginBottom: '16px' }}>
                      {challenges.map((c, i) => (
                        <button
                          key={c.id}
                          onClick={() => setActiveChallengeIdx(i)}
                          className={`btn ${activeChallengeIdx === i ? 'btn-blue' : 'btn-secondary'}`}
                          style={{ padding: '6px 14px', fontSize: '0.85rem' }}
                        >
                          Challenge {i + 1}
                        </button>
                      ))}
                    </div>
                  )}

                  {/* Challenge Description Card */}
                  <div className="card" style={{ marginBottom: '16px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                      <h3 style={{ fontSize: '1.1rem', fontWeight: 700 }}>
                        {challenges[activeChallengeIdx]?.title}
                      </h3>
                      <span style={{ fontSize: '0.8rem', padding: '2px 8px', borderRadius: '10px', background: 'var(--accent-gold-bg)', color: 'var(--accent-gold)', fontWeight: 600 }}>
                        {challenges[activeChallengeIdx]?.difficulty?.toUpperCase()}
                      </span>
                    </div>

                    <p style={{ fontSize: '0.95rem', color: 'var(--text-primary)', whiteSpace: 'pre-line', marginBottom: '8px' }}>
                      {challenges[activeChallengeIdx]?.description}
                    </p>

                    <p style={{ fontSize: '0.84rem', color: 'var(--text-secondary)', lineHeight: 1.55, margin: '0 0 10px' }}>
                      Work through the checklist below in order. Then compare your program's output with the example, including its spelling, spaces, and line breaks.
                    </p>

                    {challenges[activeChallengeIdx]?.requirements && (
                      <div style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', background: 'var(--bg-tertiary)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', lineHeight: 1.55 }}>
                        <strong>What your code must do:</strong> {challenges[activeChallengeIdx].requirements}
                      </div>
                    )}

                    {/* Example Test Case Preview */}
                    {challenges[activeChallengeIdx]?.test_cases && challenges[activeChallengeIdx].test_cases.length > 0 && (
                      <div style={{
                        marginTop: '12px',
                        background: '#0d1117',
                        border: '1px solid #30363d',
                        borderRadius: 'var(--radius-sm)',
                        padding: '10px 14px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '6px'
                      }}>
                        <div style={{ fontSize: '0.78rem', fontWeight: 700, color: 'var(--accent-green)', letterSpacing: '0.5px' }}>
                          📝 Example run
                        </div>
                        <p style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', lineHeight: 1.5, margin: 0 }}>
                          {getChallengeInputGuidance(challenges[activeChallengeIdx])}
                        </p>
                        <div style={{ display: 'grid', gridTemplateColumns: challenges[activeChallengeIdx].test_cases[0].input_data ? '1fr 1fr' : '1fr', gap: '10px' }}>
                          {challenges[activeChallengeIdx].test_cases[0].input_data ? (
                            <div>
                              <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginBottom: '3px' }}>Input sent to your program:</div>
                              <pre style={{ margin: 0, fontFamily: 'var(--font-mono)', fontSize: '0.82rem', color: '#e3b341', background: 'rgba(255,255,255,0.03)', padding: '6px 8px', borderRadius: '4px' }}>
                                {challenges[activeChallengeIdx].test_cases[0].input_data}
                              </pre>
                            </div>
                          ) : null}
                          <div>
                            <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginBottom: '3px' }}>Expected Output:</div>
                            <pre style={{ margin: 0, fontFamily: 'var(--font-mono)', fontSize: '0.82rem', color: '#58a6ff', background: 'rgba(255,255,255,0.03)', padding: '6px 8px', borderRadius: '4px' }}>
                              {challenges[activeChallengeIdx].test_cases[0].expected_output}
                            </pre>
                          </div>
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Monaco Code Editor */}
                  <CodeEditor
                    key={challenges[activeChallengeIdx]?.id}
                    challenge={challenges[activeChallengeIdx]}
                    onPassed={() => handleChallengePassed(false)}
                    height="360px"
                  />
                </div>
              )}
            </div>
          )}

          {/* TAB 3: MCQ EXAMINATION */}
          {activeTab === 'quiz' && (
            <div style={{ maxWidth: '800px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid var(--border-color)', paddingBottom: '12px' }}>
                <div>
                  <h3 style={{ fontSize: '1.1rem', fontWeight: 700 }}>Level {effectiveLevelData.number} MCQ Examination</h3>
                  <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Score at least 80% to satisfy examination progression requirements.</p>
                </div>
                {quizResult && (
                  <div style={{ textAlign: 'right' }}>
                    <div style={{ fontSize: '1.4rem', fontWeight: 800, color: quizResult.passed ? 'var(--accent-green)' : 'var(--accent-red)' }}>
                      {quizResult.score_percent}%
                    </div>
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                      {quizResult.correct_count} / {quizResult.total_questions} Correct
                    </div>
                  </div>
                )}
              </div>

              {/* Questions List */}
              {questions.map((q, qIdx) => {
                const feedback = quizResult?.feedback?.find(f => f.question_id === q.id);
                return (
                  <div key={q.id} className="card" style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    <div style={{ fontWeight: 600, fontSize: '0.95rem', color: 'var(--text-primary)', whiteSpace: 'pre-line', lineHeight: 1.6 }}>
                      {qIdx + 1}. {q.question}
                    </div>

                    {q.code_snippet && (
                      <pre style={{
                        padding: '10px 14px',
                        borderRadius: 'var(--radius-sm)',
                        background: 'var(--bg-primary)',
                        fontFamily: 'var(--font-mono)',
                        fontSize: '0.85rem',
                        color: '#79c0ff'
                      }}>
                        {q.code_snippet}
                      </pre>
                    )}

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                      {q.options.map((opt) => {
                        const isSelected = quizAnswers[q.id] === opt.id;
                        let optStyle = {
                          padding: '10px 14px',
                          borderRadius: 'var(--radius-md)',
                          border: '1px solid var(--border-color)',
                          background: 'var(--bg-secondary)',
                          color: 'var(--text-primary)',
                          cursor: quizResult ? 'default' : 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '10px',
                          fontSize: '0.9rem',
                          textAlign: 'left'
                        };

                        if (isSelected && !quizResult) {
                          optStyle.borderColor = 'var(--accent-blue)';
                          optStyle.background = 'var(--accent-blue-bg)';
                        }

                        if (quizResult && feedback) {
                          if (opt.id === feedback.correct_option_id) {
                            optStyle.borderColor = 'var(--accent-green)';
                            optStyle.background = 'var(--accent-green-bg)';
                          } else if (isSelected && !feedback.is_correct) {
                            optStyle.borderColor = 'var(--accent-red)';
                            optStyle.background = 'var(--accent-red-bg)';
                          }
                        }

                        return (
                          <button
                            key={opt.id}
                            onClick={() => handleQuizOptionSelect(q.id, opt.id)}
                            style={optStyle}
                          >
                            <span style={{
                              width: '20px',
                              height: '20px',
                              borderRadius: '50%',
                              border: '2px solid var(--border-color)',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              fontSize: '0.75rem',
                              fontWeight: 700,
                              flexShrink: 0,
                              borderColor: isSelected ? 'var(--accent-blue)' : 'var(--border-color)'
                            }}>
                              {isSelected ? '●' : ''}
                            </span>
                            {opt.option_text && opt.option_text.includes('\n') ? (
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', textAlign: 'left', width: '100%' }}>
                                {opt.option_text.split('\n').map((line, lIdx) => (
                                  <div key={lIdx} style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <span style={{
                                      fontSize: '0.7rem',
                                      color: 'var(--accent-blue)',
                                      background: 'rgba(56, 139, 253, 0.1)',
                                      border: '1px solid rgba(56, 139, 253, 0.25)',
                                      padding: '1px 6px',
                                      borderRadius: '4px',
                                      fontWeight: 700,
                                      fontFamily: 'var(--font-sans)',
                                      flexShrink: 0
                                    }}>
                                      Line {lIdx + 1}
                                    </span>
                                    <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.88rem' }}>{line}</span>
                                  </div>
                                ))}
                              </div>
                            ) : (
                              <span style={{
                                whiteSpace: 'pre-wrap',
                                fontFamily: 'var(--font-mono)',
                                fontSize: '0.88rem',
                                lineHeight: 1.5,
                                textAlign: 'left'
                              }}>
                                {opt.option_text}
                              </span>
                            )}
                          </button>
                        );
                      })}
                    </div>

                    {/* Feedback Explanation after submit */}
                    {feedback && (
                      <div style={{
                        marginTop: '8px',
                        padding: '10px 14px',
                        borderRadius: 'var(--radius-sm)',
                        background: feedback.is_correct ? 'var(--accent-green-bg)' : 'var(--accent-red-bg)',
                        fontSize: '0.85rem'
                      }}>
                        <div style={{ fontWeight: 600, color: feedback.is_correct ? 'var(--accent-green)' : 'var(--accent-red)', marginBottom: '2px' }}>
                          {feedback.is_correct ? '✓ Correct Answer' : '✗ Incorrect'}
                        </div>
                        <div style={{ color: 'var(--text-primary)' }}>
                          {feedback.explanation}
                        </div>
                      </div>
                    )}
                  </div>
                );
              })}

              {/* Action Buttons */}
              <div style={{ display: 'flex', justifyContent: 'center', gap: '12px', marginTop: '12px' }}>
                {!quizResult ? (
                  <button
                    onClick={handleSubmitQuiz}
                    disabled={isSubmittingQuiz || Object.keys(quizAnswers).length < questions.length}
                    className="btn btn-primary"
                    style={{ padding: '10px 28px', fontSize: '1rem' }}
                  >
                    {isSubmittingQuiz ? 'Grading...' : 'Submit Examination'}
                  </button>
                ) : (
                  <button
                    onClick={handleRetryQuiz}
                    className="btn btn-secondary"
                    style={{ padding: '10px 24px', fontSize: '0.95rem' }}
                  >
                    <RefreshCw size={16} />
                    Try Again
                  </button>
                )}
              </div>
            </div>
          )}

          {/* TAB 4: FINAL BOSS CHALLENGE */}
          {activeTab === 'boss' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {!bossChallenge ? (
                <p style={{ textAlign: 'center', color: 'var(--text-muted)' }}>No boss challenge configured for this level.</p>
              ) : (
                <div>
                  <div className="card" style={{ borderLeft: '4px solid var(--accent-purple)', marginBottom: '16px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <Trophy size={20} color="var(--accent-purple)" />
                        <h3 style={{ fontSize: '1.15rem', fontWeight: 800, color: 'var(--accent-purple)' }}>
                          {bossChallenge.title}
                        </h3>
                      </div>
                      <span style={{ fontSize: '0.8rem', padding: '3px 10px', borderRadius: '12px', background: 'var(--accent-purple-bg)', color: 'var(--accent-purple)', fontWeight: 700 }}>
                        +150 XP BOSS REWARD
                      </span>
                    </div>

                    <p style={{ fontSize: '0.95rem', color: 'var(--text-primary)', whiteSpace: 'pre-line', marginBottom: '8px' }}>
                      {bossChallenge.description}
                    </p>

                    <p style={{ fontSize: '0.84rem', color: 'var(--text-secondary)', lineHeight: 1.55, margin: '0 0 10px' }}>
                      Work through the checklist below in order. Then compare your program's output with the example, including its spelling, spaces, and line breaks.
                    </p>

                    {bossChallenge.requirements && (
                      <div style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', background: 'var(--bg-tertiary)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', lineHeight: 1.55 }}>
                        <strong>What your code must do:</strong> {bossChallenge.requirements}
                      </div>
                    )}

                    {/* Example Test Case Preview for Boss Challenge */}
                    {bossChallenge?.test_cases && bossChallenge.test_cases.length > 0 && (
                      <div style={{
                        marginTop: '12px',
                        background: '#0d1117',
                        border: '1px solid #30363d',
                        borderRadius: 'var(--radius-sm)',
                        padding: '10px 14px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '6px'
                      }}>
                        <div style={{ fontSize: '0.78rem', fontWeight: 700, color: 'var(--accent-purple)', letterSpacing: '0.5px' }}>
                          📝 Example run
                        </div>
                        <p style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', lineHeight: 1.5, margin: 0 }}>
                          {getChallengeInputGuidance(bossChallenge)}
                        </p>
                        <div style={{ display: 'grid', gridTemplateColumns: bossChallenge.test_cases[0].input_data ? '1fr 1fr' : '1fr', gap: '10px' }}>
                          {bossChallenge.test_cases[0].input_data ? (
                            <div>
                              <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginBottom: '3px' }}>Input sent to your program:</div>
                              <pre style={{ margin: 0, fontFamily: 'var(--font-mono)', fontSize: '0.82rem', color: '#e3b341', background: 'rgba(255,255,255,0.03)', padding: '6px 8px', borderRadius: '4px' }}>
                                {bossChallenge.test_cases[0].input_data}
                              </pre>
                            </div>
                          ) : null}
                          <div>
                            <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginBottom: '3px' }}>Expected Output:</div>
                            <pre style={{ margin: 0, fontFamily: 'var(--font-mono)', fontSize: '0.82rem', color: '#58a6ff', background: 'rgba(255,255,255,0.03)', padding: '6px 8px', borderRadius: '4px' }}>
                              {bossChallenge.test_cases[0].expected_output}
                            </pre>
                          </div>
                        </div>
                      </div>
                    )}
                  </div>

                  <CodeEditor
                    key={bossChallenge.id}
                    challenge={bossChallenge}
                    onPassed={() => handleChallengePassed(true)}
                    height="380px"
                  />
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
