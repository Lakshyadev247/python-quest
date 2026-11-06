import React from 'react';
import { Sun, Moon, Zap, Award, WifiOff, LogIn, Settings } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function Navbar({ onOpenAuth, activePage, setActivePage }) {
  const { user, theme, setTheme, isOnline } = useAuth();

  const toggleTheme = () => {
    setTheme(theme === 'dark' ? 'light' : 'dark');
  };

  const pageTitles = {
    dashboard: 'Dashboard',
    learn: 'Python Quest Curriculum',
    practice: 'Interactive Coding Playground',
    revision: 'Revision & Exam Preparation',
    achievements: 'Trophy Cabinet & Badges',
    profile: 'Player Profile',
    settings: 'Settings',
  };

  return (
    <header className="navbar">
      <div className="navbar-left">
        <h2 style={{ fontSize: '1.15rem', fontWeight: 700, margin: 0 }}>
          {pageTitles[activePage] || 'Python Quest'}
        </h2>
        {!isOnline && (
          <span style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: '0.75rem', padding: '2px 8px', borderRadius: '12px', background: 'var(--accent-red-bg)', color: 'var(--accent-red)', fontWeight: 600 }}>
            <WifiOff size={14} /> Offline Mode
          </span>
        )}
      </div>

      <div className="navbar-right">
        {user ? (
          <>
            {/* Total XP Pill */}
            <div className="stat-pill xp" title="Total Experience Points">
              <Zap size={16} fill="currentColor" />
              <span>{user.total_xp} XP</span>
            </div>

            {/* Current Rank Pill */}
            <div className="stat-pill rank" title="Current Player Rank">
              <Award size={16} />
              <span>{user.current_rank}</span>
            </div>
          </>
        ) : (
          <button onClick={onOpenAuth} className="btn btn-primary" style={{ padding: '6px 14px', fontSize: '0.85rem' }}>
            <LogIn size={15} />
            Sign In
          </button>
        )}

        {/* Theme Toggle Button */}
        <button
          onClick={toggleTheme}
          className="btn-icon"
          title={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
        >
          {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
        </button>

        {/* Settings shortcut for phones (the sidebar is hidden there) */}
        {setActivePage && (
          <button
            onClick={() => setActivePage('settings')}
            className="btn-icon navbar-settings-mobile"
            title="Server & app settings"
          >
            <Settings size={18} />
          </button>
        )}
      </div>
    </header>
  );
}
