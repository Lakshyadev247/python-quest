import React, { useState, useEffect } from 'react';
import { User, Award, Zap, Flame, CheckCircle, Clock, RefreshCw, LogOut } from 'lucide-react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';

const RANKS_INFO = [
  { name: 'Beginner', minXp: 0, desc: 'Starting your programming journey (World 1)' },
  { name: 'Python Apprentice', minXp: 3000, desc: 'Grasping variables, logic, and data types (World 2+)' },
  { name: 'Code Explorer', minXp: 9000, desc: 'Mastering operators, conditions, and branching (World 4+)' },
  { name: 'Logic Builder', minXp: 18000, desc: 'Structuring loops, collections, and algorithms (World 6+)' },
  { name: 'Python Developer', minXp: 28000, desc: 'Building modular functions and error handling (World 8+)' },
  { name: 'Advanced Developer', minXp: 38000, desc: 'Creating OOP architectures and pipelines (World 10+)' },
  { name: 'Python Master', minXp: 46000, desc: 'Full capstone programming authority & databases (World 12)' },
];

export default function ProfilePage({ onOpenAuth }) {
  const { user, logout, updateProfile } = useAuth();
  const [profileData, setProfileData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadProfile() {
      if (!user) {
        setLoading(false);
        return;
      }
      try {
        const res = await api.get('/profile');
        setProfileData(res);
      } catch (err) {
        console.error('Failed to load profile:', err);
      } finally {
        setLoading(false);
      }
    }
    loadProfile();
  }, [user]);

  if (!user) {
    return (
      <div className="page-container" style={{ textAlign: 'center', padding: '60px 20px' }}>
        <h2 style={{ fontSize: '1.5rem', fontWeight: 700, marginBottom: '8px' }}>User Profile</h2>
        <p style={{ color: 'var(--text-secondary)', marginBottom: '20px' }}>Sign in to view your learning records and ranks.</p>
        <button onClick={onOpenAuth} className="btn btn-primary">Sign In</button>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="page-container" style={{ textAlign: 'center', padding: '60px' }}>
        <RefreshCw className="spin" size={28} style={{ margin: '0 auto 12px', color: 'var(--accent-blue)' }} />
        <p>Loading profile records...</p>
      </div>
    );
  }

  const stats = profileData?.stats || {};
  const recentXp = profileData?.recent_xp || [];

  return (
    <div className="page-container" style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {/* Profile Header Card */}
      <div className="card" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <div className="avatar-circle" style={{ width: '64px', height: '64px', fontSize: '1.6rem' }}>
            {user.username.charAt(0).toUpperCase()}
          </div>
          <div>
            <h2 style={{ fontSize: '1.4rem', fontWeight: 800 }}>{user.username}</h2>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>{user.email}</div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginTop: '6px' }}>
              <span style={{ fontSize: '0.8rem', padding: '2px 8px', borderRadius: '12px', background: 'var(--accent-purple-bg)', color: 'var(--accent-purple)', fontWeight: 600 }}>
                {user.current_rank}
              </span>
              <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                Joined {user.created_at ? new Date(user.created_at).toLocaleDateString() : 'recently'}
              </span>
            </div>
          </div>
        </div>

        <button onClick={logout} className="btn btn-secondary" style={{ padding: '8px 16px' }}>
          <LogOut size={16} />
          Sign Out
        </button>
      </div>

      {/* Stats Overview */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '16px' }}>
        <div className="card">
          <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '4px' }}>Total XP Earned</div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--accent-gold)' }}>{user.total_xp}</div>
        </div>
        <div className="card">
          <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '4px' }}>Completed Levels</div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--accent-green)' }}>{stats.completed_levels || 0}</div>
        </div>
        <div className="card">
          <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '4px' }}>Coding Submissions</div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--accent-blue)' }}>{stats.passed_submissions || 0} / {stats.total_submissions || 0}</div>
        </div>
        <div className="card">
          <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '4px' }}>Trophies Unlocked</div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--accent-purple)' }}>{stats.unlocked_achievements || 0}</div>
        </div>
      </div>

      {/* Ranks Ladder */}
      <div className="card">
        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '14px' }}>
          Player Rank Progression Ladder
        </h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {RANKS_INFO.map((r, idx) => {
            const isUnlocked = user.total_xp >= r.minXp;
            const isCurrent = user.current_rank === r.name;
            return (
              <div
                key={r.name}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '12px 16px',
                  borderRadius: 'var(--radius-md)',
                  background: isCurrent ? 'var(--accent-purple-bg)' : 'var(--bg-tertiary)',
                  border: isCurrent ? '1px solid var(--accent-purple)' : '1px solid var(--border-color)',
                  opacity: isUnlocked ? 1 : 0.5
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                  <span style={{
                    width: '28px',
                    height: '28px',
                    borderRadius: '50%',
                    background: isUnlocked ? 'var(--accent-purple)' : 'var(--border-color)',
                    color: '#fff',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontWeight: 700,
                    fontSize: '0.85rem'
                  }}>
                    {idx + 1}
                  </span>
                  <div>
                    <div style={{ fontWeight: 700, fontSize: '0.95rem', color: 'var(--text-primary)' }}>
                      {r.name} {isCurrent && <span style={{ fontSize: '0.75rem', color: 'var(--accent-purple)', marginLeft: '6px' }}>(Current)</span>}
                    </div>
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>{r.desc}</div>
                  </div>
                </div>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', color: 'var(--accent-gold)' }}>
                  {r.minXp}+ XP
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
