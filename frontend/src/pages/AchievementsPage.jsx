import React, { useState, useEffect } from 'react';
import {
  Trophy, CheckCircle, Lock, Award, Star, Zap,
  Terminal, Code, Repeat, Layers, GraduationCap, Wrench, RefreshCw
} from 'lucide-react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';

const ICON_MAP = {
  Terminal,
  CheckCircle,
  Award,
  Zap,
  Star,
  Wrench,
  Repeat,
  Code,
  Layers,
  GraduationCap
};

export default function AchievementsPage({ onOpenAuth }) {
  const { user } = useAuth();
  const [achievements, setAchievements] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadAchievements() {
      if (!user) {
        setLoading(false);
        return;
      }
      try {
        const res = await api.get('/achievements');
        setAchievements(res.achievements || []);
      } catch (err) {
        console.error('Failed to load achievements:', err);
      } finally {
        setLoading(false);
      }
    }
    loadAchievements() ;
  }, [user]);

  if (!user) {
    return (
      <div className="page-container" style={{ textAlign: 'center', padding: '60px 20px' }}>
        <Trophy size={48} style={{ margin: '0 auto 16px', color: 'var(--accent-gold)' }} />
        <h2 style={{ fontSize: '1.5rem', fontWeight: 700, marginBottom: '8px' }}>Achievements & Trophy Cabinet</h2>
        <p style={{ color: 'var(--text-secondary)', marginBottom: '20px' }}>Sign in to view and unlock programming trophies.</p>
        <button onClick={onOpenAuth} className="btn btn-primary">Sign In</button>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="page-container" style={{ textAlign: 'center', padding: '60px' }}>
        <RefreshCw className="spin" size={28} style={{ margin: '0 auto 12px', color: 'var(--accent-blue)' }} />
        <p>Opening Trophy Cabinet...</p>
      </div>
    );
  }

  const unlockedCount = achievements.filter(a => a.unlocked).length;

  return (
    <div className="page-container" style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '12px' }}>
        <div>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 800, marginBottom: '6px' }}>
            Trophy Cabinet & Badges
          </h2>
          <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
            Earn achievements by writing code, conquering boss challenges, and clearing examinations.
          </p>
        </div>

        <div className="stat-pill xp" style={{ padding: '8px 16px', fontSize: '0.95rem' }}>
          <Trophy size={18} />
          <span>{unlockedCount} / {achievements.length} Unlocked</span>
        </div>
      </div>

      {/* Achievements Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '16px' }}>
        {achievements.map((ach) => {
          const IconComponent = ICON_MAP[ach.icon] || Trophy;
          const isUnlocked = ach.unlocked;

          return (
            <div
              key={ach.id}
              className="card"
              style={{
                display: 'flex',
                gap: '16px',
                alignItems: 'flex-start',
                border: isUnlocked ? '1px solid rgba(210, 153, 34, 0.4)' : '1px solid var(--border-color)',
                background: isUnlocked ? 'linear-gradient(135deg, var(--bg-card), rgba(210, 153, 34, 0.05))' : 'var(--bg-secondary)',
                opacity: isUnlocked ? 1 : 0.6,
                transition: 'all 0.15s ease'
              }}
            >
              <div style={{
                width: '48px',
                height: '48px',
                borderRadius: '12px',
                background: isUnlocked ? 'var(--accent-gold-bg)' : 'var(--bg-tertiary)',
                color: isUnlocked ? 'var(--accent-gold)' : 'var(--text-muted)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                flexShrink: 0
              }}>
                {isUnlocked ? <IconComponent size={24} /> : <Lock size={20} />}
              </div>

              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '4px' }}>
                  <h4 style={{ fontSize: '0.95rem', fontWeight: 700, color: 'var(--text-primary)' }}>
                    {ach.title}
                  </h4>
                  <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--accent-gold)' }}>
                    +{ach.xp_bonus} XP
                  </span>
                </div>

                <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', lineHeight: 1.4, marginBottom: '6px' }}>
                  {ach.description}
                </p>

                <div style={{ fontSize: '0.75rem', color: isUnlocked ? 'var(--accent-green)' : 'var(--text-muted)', fontWeight: 600 }}>
                  {isUnlocked ? '✓ Unlocked' : 'Locked'}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
