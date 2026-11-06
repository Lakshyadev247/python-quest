import React, { useState } from 'react';
import { X, Lock, Mail, User, ArrowRight, AlertCircle, Server } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { getBaseApiUrl, setBaseApiUrl, resetBaseApiUrl, testServerConnection } from '../api/client';

export default function AuthModal({ isOpen, onClose, initialMode = 'login' }) {
  const [mode, setMode] = useState(initialMode);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  // Server settings drawer state
  const [showServerConfig, setShowServerConfig] = useState(false);
  const [serverUrl, setServerUrl] = useState(getBaseApiUrl());
  const [testingConnection, setTestingConnection] = useState(false);
  const [connectionStatus, setConnectionStatus] = useState(null);

  const { login, register, continueAsGuest } = useAuth();

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      if (mode === 'login') {
        await login(username, password);
      } else {
        await register(username, email, password);
      }
      onClose();
    } catch (err) {
      setError(err.message || 'Authentication failed');
      // If network failure, automatically expand server config so user can adjust IP
      if (err.message && (err.message.includes('backend') || err.message.includes('fetch') || err.message.includes('connect'))) {
        setShowServerConfig(true);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleTestConnection = async () => {
    setTestingConnection(true);
    setConnectionStatus(null);
    const result = await testServerConnection(serverUrl);
    setTestingConnection(false);
    if (result.ok) {
      setBaseApiUrl(serverUrl);
      setConnectionStatus({ ok: true, message: 'Connected to backend server!' });
    } else {
      setConnectionStatus({ ok: false, message: `Could not reach server: ${result.error}` });
    }
  };

  const handleSaveServerUrl = () => {
    setBaseApiUrl(serverUrl);
    setConnectionStatus({ ok: true, message: 'Server URL saved!' });
    setTimeout(() => setConnectionStatus(null), 3000);
  };

  const handleGuestEnter = () => {
    continueAsGuest();
    onClose();
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content" style={{ maxWidth: '440px', maxHeight: '90vh', overflowY: 'auto' }}>
        <div className="modal-header">
          <h3 style={{ fontSize: '1.2rem', fontWeight: 700 }}>
            {mode === 'login' ? 'Sign In to Python Quest' : 'Create Free Account'}
          </h3>
          <button onClick={onClose} className="btn-icon">
            <X size={18} />
          </button>
        </div>

        <form onSubmit={handleSubmit} style={{ padding: '24px' }}>
          {error && (
            <div style={{
              display: 'flex',
              alignItems: 'flex-start',
              gap: '8px',
              padding: '10px 14px',
              borderRadius: 'var(--radius-sm)',
              background: 'var(--accent-red-bg)',
              color: 'var(--accent-red)',
              fontSize: '0.85rem',
              marginBottom: '16px',
              lineHeight: 1.4
            }}>
              <AlertCircle size={16} style={{ flexShrink: 0, marginTop: '2px' }} />
              <div>
                <span>{error}</span>
              </div>
            </div>
          )}

          <div className="form-group">
            <label className="form-label">Username</label>
            <div style={{ position: 'relative' }}>
              <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter username"
                className="form-input"
                style={{ paddingLeft: '36px' }}
              />
              <User size={16} style={{ position: 'absolute', left: '12px', top: '12px', color: 'var(--text-muted)' }} />
            </div>
          </div>

          {mode === 'register' && (
            <div className="form-group">
              <label className="form-label">Email</label>
              <div style={{ position: 'relative' }}>
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Enter email address"
                  className="form-input"
                  style={{ paddingLeft: '36px' }}
                />
                <Mail size={16} style={{ position: 'absolute', left: '12px', top: '12px', color: 'var(--text-muted)' }} />
              </div>
            </div>
          )}

          <div className="form-group">
            <label className="form-label">Password</label>
            <div style={{ position: 'relative' }}>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter password (min 6 chars)"
                className="form-input"
                style={{ paddingLeft: '36px' }}
              />
              <Lock size={16} style={{ position: 'absolute', left: '12px', top: '12px', color: 'var(--text-muted)' }} />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="btn btn-primary"
            style={{ width: '100%', padding: '12px', marginTop: '8px', fontSize: '0.95rem' }}
          >
            {loading ? 'Connecting...' : mode === 'login' ? 'Sign In' : 'Create Account'}
            <ArrowRight size={16} />
          </button>

          {/* Guest / Offline Mode Option */}
          <button
            type="button"
            onClick={handleGuestEnter}
            className="btn btn-secondary"
            style={{ width: '100%', padding: '10px', marginTop: '10px', fontSize: '0.85rem' }}
          >
            👀 Browse as Guest (progress is not saved)
          </button>

          <div style={{ textAlign: 'center', marginTop: '14px', fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            {mode === 'login' ? (
              <span>
                New learner?{' '}
                <button
                  type="button"
                  onClick={() => { setMode('register'); setError(''); }}
                  style={{ background: 'none', border: 'none', color: 'var(--accent-blue)', cursor: 'pointer', fontWeight: 600 }}
                >
                  Create an account
                </button>
              </span>
            ) : (
              <span>
                Already have an account?{' '}
                <button
                  type="button"
                  onClick={() => { setMode('login'); setError(''); }}
                  style={{ background: 'none', border: 'none', color: 'var(--accent-blue)', cursor: 'pointer', fontWeight: 600 }}
                >
                  Sign In
                </button>
              </span>
            )}
          </div>

          {/* Server Connection Drawer */}
          <div style={{ marginTop: '20px', paddingTop: '16px', borderTop: '1px solid var(--border-color)' }}>
            <button
              type="button"
              onClick={() => setShowServerConfig(!showServerConfig)}
              style={{
                background: 'none',
                border: 'none',
                color: 'var(--text-muted)',
                cursor: 'pointer',
                fontSize: '0.8rem',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                margin: '0 auto'
              }}
            >
              <Server size={14} />
              {showServerConfig ? 'Hide Server Connection Settings' : '⚙️ Configure PC Server IP / Connection'}
            </button>

            {showServerConfig && (
              <div style={{
                marginTop: '12px',
                padding: '12px',
                background: 'var(--bg-secondary)',
                borderRadius: 'var(--radius-sm)',
                fontSize: '0.8rem'
              }}>
                <label style={{ display: 'block', fontWeight: 600, marginBottom: '6px', color: 'var(--text-primary)' }}>
                  Backend Server URL:
                </label>
                <div style={{ display: 'flex', gap: '6px', marginBottom: '8px' }}>
                  <input
                    type="text"
                    value={serverUrl}
                    onChange={(e) => setServerUrl(e.target.value)}
                    placeholder="http://192.168.1.100:5000/api"
                    className="form-input"
                    style={{ flex: 1, padding: '6px 10px', fontSize: '0.8rem' }}
                  />
                  <button
                    type="button"
                    onClick={handleTestConnection}
                    disabled={testingConnection}
                    className="btn btn-secondary"
                    style={{ padding: '6px 12px', fontSize: '0.8rem', flexShrink: 0 }}
                  >
                    {testingConnection ? 'Testing...' : 'Test'}
                  </button>
                </div>

                <div style={{ display: 'flex', gap: '8px' }}>
                  <button
                    type="button"
                    onClick={handleSaveServerUrl}
                    className="btn btn-primary"
                    style={{ padding: '6px 12px', fontSize: '0.78rem', flex: 1 }}
                  >
                    Save Server URL
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      resetBaseApiUrl();
                      const next = getBaseApiUrl();
                      setServerUrl(next);
                      setConnectionStatus({ ok: true, message: `Reset to default: ${next}` });
                    }}
                    className="btn btn-secondary"
                    style={{ padding: '6px 10px', fontSize: '0.78rem' }}
                  >
                    Reset to default
                  </button>
                </div>

                {connectionStatus && (
                  <div style={{
                    marginTop: '8px',
                    padding: '6px 10px',
                    borderRadius: '4px',
                    background: connectionStatus.ok ? 'var(--accent-green-bg)' : 'var(--accent-red-bg)',
                    color: connectionStatus.ok ? 'var(--accent-green)' : 'var(--accent-red)',
                    fontSize: '0.75rem',
                    lineHeight: 1.3
                  }}>
                    {connectionStatus.ok ? '✓ ' : '✕ '}{connectionStatus.message}
                  </div>
                )}
              </div>
            )}
          </div>
        </form>
      </div>
    </div>
  );
}
