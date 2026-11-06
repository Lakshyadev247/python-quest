import React, { useState, useEffect } from 'react';
import {
  Zap, Award, CheckCircle, Play, ArrowRight,
  BookOpen, Clock, Sparkles, AlertTriangle, Settings
} from 'lucide-react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';

export default function DashboardPage({ setActivePage, onOpenLevel, onOpenAuth }) {
  const { user, isGuest } = useAuth();
  const [progressData, setProgressData] = useState(null);
  const [loadError, setLoadError] = useState(null);

  useEffect(() => {
    async function loadProgress() {
      if (!user || user.is_guest) {
        return;
      }
      setLoadError(null);
      try {
        const data = await api.get('/progress');
        setProgressData(data);
      } catch (err) {
        console.error('Failed to load progress data:', err);
        setLoadError(err.message || 'Could not load your progress.');
      }
    }
    loadProgress();
  }, [user]);

  if (!user) {
    return (
      <div className="page-container" style={{ textAlign: 'center', padding: '60px 20px' }}>
        <div style={{
          width: '72px',
          height: '72px',
          margin: '0 auto 24px',
          borderRadius: '20px',
          background: 'linear-gradient(135deg, #388bfd, #2ea043)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: 'white',
          boxShadow: 'var(--shadow-md)'
        }}>
          <Sparkles size={36} />
        </div>
        <h1 style={{ fontSize: '2.4rem', fontWeight: 800, marginBottom: '12px' }}>
          Welcome to Python Quest
        </h1>
        <p style={{ fontSize: '1.1rem', color: 'var(--text-secondary)', maxWidth: '600px', margin: '0 auto 32px', lineHeight: 1.6 }}>
          Transform your Python learning into a structured, level-based adventure.
          Designed specifically for learners with zero prior coding experience.
        </p>
        <div style={{ display: 'flex', gap: '12px', justifyContent: 'center' }}>
          <button onClick={onOpenAuth} className="btn btn-primary" style={{ padding: '12px 28px', fontSize: '1rem' }}>
            <Play size={18} fill="white" />
            Start Learning Free
          </button>
          <button onClick={() => setActivePage('learn')} className="btn btn-secondary" style={{ padding: '12px 24px', fontSize: '1rem' }}>
            Explore Curriculum
          </button>
        </div>
      </div>
    );
  }

  const completedCount = progressData?.completed_levels_count || 0;
  const totalLevels = progressData?.total_levels || 126;
  const completionPct = progressData?.completion_percentage || 0;
  const currentWorld = progressData?.current_world;
  const currentLevel = progressData?.current_level;
  const recentActivities = progressData?.recent_activities || [];

  return (
    <div className="page-container" style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {isGuest && (
        <div className="card" style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '12px',
          borderColor: 'rgba(210, 153, 34, 0.45)',
          background: 'var(--accent-gold-bg)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <AlertTriangle size={20} color="var(--accent-gold)" />
            <div>
              <div style={{ fontWeight: 700, fontSize: '0.95rem' }}>You are browsing as a guest</div>
              <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)' }}>
                Lessons are readable, but progress, XP, quizzes and code execution require a free account.
              </div>
            </div>
          </div>
          <button onClick={onOpenAuth} className="btn btn-primary" style={{ padding: '8px 18px' }}>
            Create account / Sign in
          </button>
        </div>
      )}

      {loadError && !isGuest && (
        <div className="card" style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '12px',
          borderColor: 'rgba(248, 81, 73, 0.4)',
          background: 'var(--accent-red-bg)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <AlertTriangle size={20} color="var(--accent-red)" />
            <div>
              <div style={{ fontWeight: 700, fontSize: '0.95rem' }}>Could not load your progress</div>
              <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)' }}>{loadError}</div>
            </div>
          </div>
          <button onClick={() => setActivePage('settings')} className="btn btn-secondary" style={{ padding: '8px 16px' }}>
            <Settings size={15} />
            Server settings
          </button>
        </div>
      )}

      {/* Welcome Banner Card */}
      <div className="card" style={{
        background: 'linear-gradient(135deg, rgba(56, 139, 253, 0.15), rgba(46, 160, 67, 0.15))',
        borderColor: 'rgba(56, 139, 253, 0.3)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '20px'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <div className="avatar-circle" style={{ width: '56px', height: '56px', fontSize: '1.4rem' }}>
            {user.username.charAt(0).toUpperCase()}
          </div>
          <div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Welcome back,</div>
            <h2 style={{ fontSize: '1.4rem', fontWeight: 800 }}>{user.username}</h2>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginTop: '4px' }}>
              <span style={{ fontSize: '0.8rem', padding: '2px 8px', borderRadius: '12px', background: 'var(--accent-purple-bg)', color: 'var(--accent-purple)', fontWeight: 600 }}>
                {user.current_rank}
              </span>
              <span style={{ fontSize: '0.8rem', color: 'var(--accent-gold)', fontWeight: 600 }}>
                Level {user.current_level_id}
              </span>
            </div>
          </div>
        </div>

        <button
          onClick={() => {
            if (currentLevel?.id) {
              onOpenLevel(currentLevel.id);
            } else {
              setActivePage('learn');
            }
          }}
          className="btn btn-primary"
          style={{ padding: '12px 24px', fontSize: '0.95rem' }}
        >
          <Play size={18} fill="white" />
          Continue Learning
        </button>
      </div>

      {/* Stats Grid */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
        gap: '16px'
      }}>
        <div className="card">
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--accent-gold)', marginBottom: '8px' }}>
            <Zap size={22} fill="currentColor" />
            <span style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-secondary)' }}>Total XP</span>
          </div>
          <div style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--text-primary)' }}>
            {user.total_xp}
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>
            Rank: {user.current_rank || 'Beginner'}
          </div>
        </div>

        <div className="card">
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--accent-green)', marginBottom: '8px' }}>
            <CheckCircle size={22} />
            <span style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-secondary)' }}>Completed Levels</span>
          </div>
          <div style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--text-primary)' }}>
            {completedCount} <span style={{ fontSize: '1rem', color: 'var(--text-muted)', fontWeight: 500 }}>/ {totalLevels}</span>
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>
            {completionPct}% of curriculum
          </div>
        </div>

        <div className="card">
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--accent-purple)', marginBottom: '8px' }}>
            <Award size={22} />
            <span style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-secondary)' }}>Current World</span>
          </div>
          <div style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text-primary)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
            {currentWorld?.title || 'World 1'}
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>
            World {currentWorld?.number || 1} of 12
          </div>
        </div>
      </div>

      {/* Course Overall Progress Bar */}
      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
          <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>Overall Curriculum Progression</span>
          <span style={{ fontWeight: 700, color: 'var(--accent-blue)', fontSize: '0.9rem' }}>{completionPct}% Complete</span>
        </div>
        <div style={{ width: '100%', height: '10px', background: 'var(--bg-tertiary)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
          <div style={{
            width: `${completionPct}%`,
            height: '100%',
            background: 'linear-gradient(90deg, var(--accent-blue), var(--accent-green))',
            borderRadius: 'var(--radius-full)',
            transition: 'width 0.4s ease'
          }} />
        </div>
      </div>

      {/* Two Column Layout: Current Mission & Recent Activities */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '20px' }}>
        {/* Current Level Card */}
        <div className="card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--accent-blue)', fontSize: '0.8rem', fontWeight: 700, marginBottom: '8px' }}>
              <BookOpen size={16} />
              UP NEXT FOR YOU
            </div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 700, marginBottom: '6px' }}>
              Level {currentLevel?.number || user.current_level_id}: {currentLevel?.title || 'What Is Programming?'}
            </h3>
            <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', lineHeight: 1.6, marginBottom: '16px' }}>
              {currentLevel?.description || 'Study this lesson, pass the coding exercises, and clear the examination to unlock Level 2.'}
            </p>
          </div>

          <button
            onClick={() => onOpenLevel(currentLevel?.id || 1)}
            className="btn btn-blue"
            style={{ width: '100%', padding: '10px' }}
          >
            Start Level {currentLevel?.number || user.current_level_id}
            <ArrowRight size={16} />
          </button>
        </div>

        {/* Recent Activity Card */}
        <div className="card">
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '0.8rem', fontWeight: 700, color: 'var(--text-secondary)', marginBottom: '16px' }}>
            <Clock size={16} />
            RECENT LEARNING ACTIVITY
          </div>

          {recentActivities.length === 0 ? (
            <p style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>
              No activities yet. Complete your first lesson to earn XP and unlock achievements!
            </p>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              {recentActivities.map((tx) => (
                <div key={tx.id} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-tertiary)', fontSize: '0.85rem' }}>
                  <span style={{ color: 'var(--text-primary)' }}>{tx.description || tx.source}</span>
                  <span style={{ color: 'var(--accent-gold)', fontWeight: 700 }}>+{tx.amount} XP</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
