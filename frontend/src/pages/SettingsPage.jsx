import React, { useState } from 'react';
import {
  Sun, Moon, Server, Database, Check, RefreshCw, RotateCcw, Smartphone,
  Lock, Unlock
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { usePet } from '../context/PetContext';
import {
  getBaseApiUrl,
  setBaseApiUrl,
  resetBaseApiUrl,
  testServerConnection,
  isCapacitorApp
} from '../api/client';

export default function SettingsPage() {
  const { theme, setTheme, uiTheme, setUiTheme, progressionMode, setProgressionMode, isGuest, deleteGuestAccount } = useAuth();
  const { petEnabled, setPetEnabled } = usePet();

  const currentBase = getBaseApiUrl();
  const isStandalone = currentBase === 'offline' || isCapacitorApp();
  const [apiUrl, setApiUrlState] = useState(currentBase === 'offline' ? '' : currentBase);
  const [savedSuccess, setSavedSuccess] = useState(false);
  const [testResult, setTestResult] = useState(null);
  const [testing, setTesting] = useState(false);
  const [guestDataCleared, setGuestDataCleared] = useState(false);

  const handleSaveApiUrl = (e) => {
    e.preventDefault();
    if (!apiUrl.trim() || apiUrl.trim().toLowerCase() === 'offline') {
      handleSwitchToStandalone();
      return;
    }
    setBaseApiUrl(apiUrl);
    setApiUrlState(getBaseApiUrl());
    setSavedSuccess(true);
    setTimeout(() => setSavedSuccess(false), 3000);
  };

  const handleSwitchToStandalone = () => {
    setBaseApiUrl('offline');
    setApiUrlState('');
    setTestResult({ ok: true, data: { status: 'offline', message: 'Running 100% Standalone' } });
    setSavedSuccess(true);
    setTimeout(() => setSavedSuccess(false), 3000);
  };

  const handleTestConnection = async () => {
    setTesting(true);
    setTestResult(null);
    const target = apiUrl.trim() || 'offline';
    const result = await testServerConnection(target);
    setTesting(false);
    setTestResult(result);
    if (result.ok && target !== 'offline') {
      setBaseApiUrl(target);
      setApiUrlState(getBaseApiUrl());
      setSavedSuccess(true);
      setTimeout(() => setSavedSuccess(false), 3000);
    }
  };

  const handleReset = () => {
    resetBaseApiUrl();
    const newBase = getBaseApiUrl();
    setApiUrlState(newBase === 'offline' ? '' : newBase);
    setTestResult(null);
    setSavedSuccess(true);
    setTimeout(() => setSavedSuccess(false), 3000);
  };

  const handleClearCache = () => {
    const keys = Object.keys(localStorage);
    keys.forEach(k => {
      if (k.startsWith('cache_')) localStorage.removeItem(k);
    });
    alert('Offline cache cleared successfully.');
  };

  return (
    <div className="page-container" style={{ display: 'flex', flexDirection: 'column', gap: '24px', maxWidth: '700px' }}>
      <div>
        <h2 style={{ fontSize: '1.4rem', fontWeight: 800, marginBottom: '6px' }}>Settings & Configuration</h2>
        <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
          Manage your application preferences, companion mascot, and offline storage.
        </p>
      </div>

      {/* Standalone Status Card */}
      <div className="card" style={{
        background: 'linear-gradient(135deg, rgba(46, 160, 67, 0.12), rgba(56, 139, 253, 0.12))',
        border: '1.5px solid var(--accent-green)',
        display: 'flex',
        alignItems: 'center',
        gap: '14px',
        padding: '18px 20px'
      }}>
        <div style={{
          width: '42px',
          height: '42px',
          borderRadius: '50%',
          background: 'rgba(46, 160, 67, 0.2)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: 'var(--accent-green)',
          flexShrink: 0
        }}>
          <Check size={24} />
        </div>
        <div style={{ flex: 1 }}>
          <div style={{ fontWeight: 800, fontSize: '1rem', color: 'var(--accent-green)' }}>
            100% Offline Standalone Mode: Active
          </div>
          <div style={{ fontSize: '0.84rem', color: 'var(--text-secondary)', marginTop: '4px', lineHeight: 1.5 }}>
            All 12 Worlds, 126 Levels, Quizzes, and the Python code execution engine work directly on this device without requiring external internet or servers.
          </div>
        </div>
      </div>

      {/* Theme Settings */}
      <div className="card">
        <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: '12px' }}>Display Theme</h3>
        <p style={{ fontSize: '0.84rem', color: 'var(--text-secondary)', marginBottom: '10px' }}>Choose the color mode you prefer.</p>
        <div style={{ display: 'flex', gap: '12px' }}>
          <button
            onClick={() => setTheme('dark')}
            className={`btn ${theme === 'dark' ? 'btn-blue' : 'btn-secondary'}`}
            style={{ padding: '10px 20px', flex: 1 }}
          >
            <Moon size={18} />
            Dark Theme
          </button>
          <button
            onClick={() => setTheme('light')}
            className={`btn ${theme === 'light' ? 'btn-blue' : 'btn-secondary'}`}
            style={{ padding: '10px 20px', flex: 1 }}
          >
            <Sun size={18} />
            Light Theme
          </button>
        </div>

        <div style={{ borderTop: '1px solid var(--border-color)', margin: '18px 0 14px' }} />
        <h4 style={{ fontSize: '0.95rem', fontWeight: 700, marginBottom: '4px' }}>Interface Style</h4>
        <p style={{ fontSize: '0.84rem', color: 'var(--text-secondary)', marginBottom: '12px', lineHeight: 1.5 }}>
          Choose how panels, cards, and menus look. Classic keeps the current Python Quest design.
        </p>
        <div className="ui-theme-options">
          <button
            type="button"
            onClick={() => setUiTheme('classic')}
            className={`ui-theme-option ${uiTheme === 'classic' ? 'selected' : ''}`}
            aria-pressed={uiTheme === 'classic'}
          >
            <span className="ui-theme-option-glyph">🎮</span>
            <span className="ui-theme-option-copy">
              <strong>Classic</strong>
              <span>Default Python Quest interface.</span>
            </span>
            {uiTheme === 'classic' && <Check size={18} className="ui-theme-option-check" />}
          </button>
          <button
            type="button"
            onClick={() => setUiTheme('modern')}
            className={`ui-theme-option ${uiTheme === 'modern' ? 'selected' : ''}`}
            aria-pressed={uiTheme === 'modern'}
          >
            <span className="ui-theme-option-glyph">⚡</span>
            <span className="ui-theme-option-copy">
              <strong>Modern Minimal</strong>
              <span>Clean cards and rounded edges.</span>
            </span>
            {uiTheme === 'modern' && <Check size={18} className="ui-theme-option-check" />}
          </button>
        </div>

        <div style={{ borderTop: '1px solid var(--border-color)', margin: '18px 0 14px' }} />
        <h4 style={{ fontSize: '0.95rem', fontWeight: 700, marginBottom: '4px' }}>Curriculum Progression Mode</h4>
        <p style={{ fontSize: '0.84rem', color: 'var(--text-secondary)', marginBottom: '12px', lineHeight: 1.5 }}>
          Control how levels unlock as you learn.
        </p>
        <div className="ui-theme-options">
          <button
            type="button"
            onClick={() => setProgressionMode('sequential')}
            className={`ui-theme-option ${progressionMode === 'sequential' ? 'selected' : ''}`}
            aria-pressed={progressionMode === 'sequential'}
          >
            <span className="ui-theme-option-glyph"><Lock size={18} /></span>
            <span className="ui-theme-option-copy">
              <strong>Sequential Unlock</strong>
              <span>Finish each level to unlock the next one.</span>
            </span>
            {progressionMode === 'sequential' && <Check size={18} className="ui-theme-option-check" />}
          </button>
          <button
            type="button"
            onClick={() => setProgressionMode('all')}
            className={`ui-theme-option ${progressionMode === 'all' ? 'selected' : ''}`}
            aria-pressed={progressionMode === 'all'}
          >
            <span className="ui-theme-option-glyph"><Unlock size={18} /></span>
            <span className="ui-theme-option-copy">
              <strong>Unlock All</strong>
              <span>Open any world or level right away.</span>
            </span>
            {progressionMode === 'all' && <Check size={18} className="ui-theme-option-check" />}
          </button>
        </div>
      </div>

      {/* Companion Pet Mascot Settings */}
      <div className="card" style={{
        border: '1.5px solid rgba(168, 85, 247, 0.4)',
        background: 'linear-gradient(180deg, rgba(168, 85, 247, 0.05) 0%, var(--bg-secondary) 100%)',
        boxShadow: '0 4px 20px rgba(168, 85, 247, 0.08)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '12px', marginBottom: '16px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{
              width: '40px',
              height: '40px',
              borderRadius: '10px',
              background: 'linear-gradient(135deg, #7c3aed, #4c1d95)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#fff',
              fontSize: '1.3rem',
              boxShadow: '0 0 12px rgba(147, 51, 234, 0.4)'
            }}>
              👻
            </div>
            <div>
              <h3 style={{ fontSize: '1.05rem', fontWeight: 800, margin: 0, color: 'var(--text-primary)' }}>
                Mini Reaper Mascot
              </h3>
              <p style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', margin: '2px 0 0' }}>
                Your animated floating companion who reacts to your code and celebrates victories!
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <span style={{
              fontSize: '0.78rem',
              fontWeight: 700,
              padding: '3px 9px',
              borderRadius: '12px',
              background: petEnabled ? 'rgba(46, 160, 67, 0.18)' : 'rgba(100, 116, 139, 0.18)',
              color: petEnabled ? 'var(--accent-green)' : 'var(--text-muted)',
              border: `1px solid ${petEnabled ? 'rgba(46, 160, 67, 0.35)' : 'rgba(100, 116, 139, 0.3)'}`
            }}>
              {petEnabled ? 'Mascot Active' : 'Mascot Hidden'}
            </span>
            <button
              onClick={() => setPetEnabled(!petEnabled)}
              className={`btn ${petEnabled ? 'btn-primary' : 'btn-secondary'}`}
              style={{
                padding: '7px 16px',
                fontSize: '0.85rem',
                fontWeight: 700,
                background: petEnabled ? 'linear-gradient(135deg, #9333ea, #7c3aed)' : undefined,
                borderColor: petEnabled ? '#a855f7' : undefined
              }}
            >
              {petEnabled ? 'Turn Pet OFF' : 'Turn Pet ON'}
            </button>
          </div>
        </div>

        <div style={{
          background: 'var(--bg-tertiary)',
          borderRadius: '8px',
          padding: '12px 14px',
          fontSize: '0.82rem',
          color: 'var(--text-secondary)',
          lineHeight: 1.6
        }}>
          <div>✨ <strong>Floating Companion:</strong> Floats in the bottom-right corner while you code.</div>
          <div>🎉 <strong>Live Reactions:</strong> Celebrates test passes and cheers for every completed challenge!</div>
          <div>💤 <strong>Smart Rest:</strong> Falls asleep when you take breaks and wakes up when you return!</div>
          <div>💬 <strong>Mascot Cheers:</strong> Click Mini Reaper anytime for motivational tips and cheers.</div>
        </div>
      </div>

      {/* Backend API Configuration (Optional PC Server Linking) */}
      <div className="card">
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
          <Server size={18} color="var(--accent-blue)" />
          <h3 style={{ fontSize: '1rem', fontWeight: 700 }}>PC Server Sync (Optional)</h3>
        </div>
        <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '14px', lineHeight: 1.5 }}>
          No PC is required to use the app. However, if you are running Python Quest on a PC on your local Wi-Fi and wish to sync progress with it, you can enter the PC's IP address below.
        </p>

        <form onSubmit={handleSaveApiUrl} style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <div style={{ display: 'flex', gap: '10px', alignItems: 'center', flexWrap: 'wrap' }}>
            <input
              type="text"
              value={apiUrl}
              onChange={(e) => setApiUrlState(e.target.value)}
              className="form-input"
              style={{ flex: 1, minWidth: '220px' }}
              placeholder="e.g. http://192.168.1.100:5000/api"
              inputMode="url"
              autoCapitalize="none"
              autoCorrect="off"
            />
            <button type="button" onClick={handleTestConnection} disabled={testing} className="btn btn-secondary" style={{ padding: '10px 16px' }}>
              {testing ? 'Testing...' : 'Test Connection'}
            </button>
            <button type="submit" className="btn btn-primary" style={{ padding: '10px 20px' }}>
              {savedSuccess ? <Check size={18} /> : 'Save URL'}
            </button>
          </div>
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
            <button
              type="button"
              onClick={handleSwitchToStandalone}
              className="btn btn-secondary"
              style={{ fontSize: '0.8rem', padding: '6px 12px', borderColor: 'var(--accent-green)', color: 'var(--accent-green)' }}
            >
              <Smartphone size={14} />
              Use Standalone Mode (No PC)
            </button>
            <button
              type="button"
              onClick={handleReset}
              className="btn btn-secondary"
              style={{ fontSize: '0.8rem', padding: '6px 12px' }}
            >
              <RotateCcw size={14} />
              Reset
            </button>
            <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', wordBreak: 'break-all' }}>
              Current Mode: <strong>{isStandalone ? 'Offline Standalone' : currentBase}</strong>
            </span>
          </div>
        </form>
        {savedSuccess && (
          <p style={{ fontSize: '0.8rem', color: 'var(--accent-green)', marginTop: '8px' }}>
            ✓ Settings updated successfully.
          </p>
        )}
        {testResult && (
          <p style={{ fontSize: '0.8rem', color: testResult.ok ? 'var(--accent-green)' : 'var(--accent-red)', marginTop: '8px' }}>
            {testResult.ok ? '✓ Connected successfully!' : `✕ Connection failed: ${testResult.error}`}
          </p>
        )}
      </div>

      {/* Offline Storage & Cache */}
      {isGuest && (
        <div className="card" style={{ borderColor: 'var(--accent-red)' }}>
          <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: '8px', color: 'var(--accent-red)' }}>Guest Account Data</h3>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '14px', lineHeight: 1.5 }}>
            Delete this Guest Explorer profile and its saved level progress from this browser. This cannot be undone.
          </p>
          <button
            onClick={() => {
              if (!window.confirm('Delete the Guest Explorer profile and all saved guest progress from this browser? This cannot be undone.')) return;
              setGuestDataCleared(deleteGuestAccount());
            }}
            className="btn btn-secondary"
            style={{ padding: '8px 16px', fontSize: '0.85rem', borderColor: 'var(--accent-red)', color: 'var(--accent-red)' }}
          >
            Delete Guest Account and Progress
          </button>
          {guestDataCleared && <p style={{ fontSize: '0.82rem', color: 'var(--accent-green)', marginTop: '10px' }}>Guest account and saved progress deleted from this browser.</p>}
        </div>
      )}

      <div className="card">
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
          <Database size={18} color="var(--accent-purple)" />
          <h3 style={{ fontSize: '1rem', fontWeight: 700 }}>Offline Storage & Content Cache</h3>
        </div>
        <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '14px' }}>
          Curriculum data and user progress are stored locally on your device for instant offline access.
        </p>
        <button onClick={handleClearCache} className="btn btn-secondary" style={{ padding: '8px 16px', fontSize: '0.85rem' }}>
          <RefreshCw size={15} />
          Clear Cached Content
        </button>
      </div>
    </div>
  );
}
