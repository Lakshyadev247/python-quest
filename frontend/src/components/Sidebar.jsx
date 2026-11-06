import React from 'react';
import {
  LayoutDashboard,
  Map,
  Code2,
  RotateCcw,
  Trophy,
  User,
  Settings,
  Flame,
  Zap,
  Terminal
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function Sidebar({ activePage, setActivePage, onOpenAuth }) {
  const { user } = useAuth();

  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'learn', label: 'Learn', icon: Map },
    { id: 'practice', label: 'Coding Practice', icon: Code2 },
    { id: 'revision', label: 'Revision', icon: RotateCcw },
    { id: 'achievements', label: 'Achievements', icon: Trophy },
    { id: 'profile', label: 'Profile', icon: User },
    { id: 'settings', label: 'Settings', icon: Settings },
  ];

  return (
    <aside className="sidebar">
      {/* Brand Header */}
      <div className="sidebar-header">
        <div className="logo-icon">
          <Terminal size={22} />
        </div>
        <div>
          <h1 className="logo-text">Python Quest</h1>
          <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)', fontWeight: 600 }}>GAMIFIED PYTHON</span>
        </div>
      </div>

      {/* Navigation Links */}
      <nav className="sidebar-nav">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activePage === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActivePage(item.id)}
              className={`nav-item ${isActive ? 'active' : ''}`}
            >
              <Icon size={18} />
              <span>{item.label}</span>
            </button>
          );
        })}
      </nav>

      {/* Footer User Badge or Sign In Prompt */}
      <div className="sidebar-footer">
        {user ? (
          <div
            onClick={() => setActivePage('profile')}
            className="user-badge"
            style={{ cursor: 'pointer' }}
          >
            <div className="avatar-circle">
              {user.username.charAt(0).toUpperCase()}
            </div>
            <div className="user-info">
              <div className="user-name">{user.username}</div>
              <div className="user-rank">{user.current_rank}</div>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '3px', color: 'var(--accent-gold)', fontSize: '0.8rem', fontWeight: 700 }}>
              <Zap size={14} fill="currentColor" />
              {user.total_xp}
            </div>
          </div>
        ) : (
          <button
            onClick={onOpenAuth}
            className="btn btn-primary"
            style={{ width: '100%' }}
          >
            Sign In / Register
          </button>
        )}
      </div>
    </aside>
  );
}
