import React, { useState, useEffect } from 'react';
import { RotateCcw, AlertTriangle, CheckCircle, BookOpen, ArrowRight, RefreshCw } from 'lucide-react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';

export default function RevisionPage({ onOpenLevel, onOpenAuth }) {
  const { user } = useAuth();
  const [revisionData, setRevisionData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadRevision() {
      if (!user) {
        setLoading(false);
        return;
      }
      try {
        const res = await api.get('/revision');
        setRevisionData(res);
      } catch (err) {
        console.error('Failed to load revision data:', err);
      } finally {
        setLoading(false);
      }
    }
    loadRevision();
  }, [user]);

  if (!user) {
    return (
      <div className="page-container" style={{ textAlign: 'center', padding: '60px 20px' }}>
        <h2 style={{ fontSize: '1.5rem', fontWeight: 700, marginBottom: '8px' }}>Revision & Exam Prep</h2>
        <p style={{ color: 'var(--text-secondary)', marginBottom: '20px' }}>Please sign in to view your personalized revision topics.</p>
        <button onClick={onOpenAuth} className="btn btn-primary">Sign In</button>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="page-container" style={{ textAlign: 'center', padding: '60px' }}>
        <RefreshCw className="spin" size={28} style={{ margin: '0 auto 12px', color: 'var(--accent-blue)' }} />
        <p>Analyzing learning history...</p>
      </div>
    );
  }

  const revisableLevels = revisionData?.revisable_levels || [];
  const weakLevels = revisionData?.weak_levels || [];
  const recentAttempts = revisionData?.recent_quiz_attempts || [];

  return (
    <div className="page-container" style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      <div>
        <h2 style={{ fontSize: '1.4rem', fontWeight: 800, marginBottom: '6px' }}>
          Revision & Knowledge Mastery
        </h2>
        <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
          Review completed concepts, reinforce areas where past exam scores were low, and build lasting programming fluency.
        </p>
      </div>

      {/* Weak Topics Notice if any */}
      {weakLevels.length > 0 && (
        <div className="card" style={{ borderLeft: '4px solid var(--accent-gold)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--accent-gold)', fontWeight: 700, marginBottom: '8px' }}>
            <AlertTriangle size={18} />
            Recommended Areas for Reinforcement
          </div>
          <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginBottom: '12px' }}>
            Based on your previous examination submissions, reviewing these topics will solidify your fundamentals:
          </p>
          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
            {weakLevels.map((lvl) => (
              <button
                key={lvl.id}
                onClick={() => onOpenLevel(lvl.id)}
                className="btn btn-secondary"
                style={{ fontSize: '0.85rem' }}
              >
                Level {lvl.number}: {lvl.title}
                <ArrowRight size={14} />
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Mastered Levels Available for Free Revisit */}
      <div>
        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '12px' }}>
          Mastered Levels ({revisableLevels.length})
        </h3>

        {revisableLevels.length === 0 ? (
          <div className="card" style={{ textAlign: 'center', padding: '40px' }}>
            <BookOpen size={32} style={{ margin: '0 auto 12px', color: 'var(--text-muted)' }} />
            <p style={{ color: 'var(--text-secondary)' }}>You haven't completed any levels yet. Start with World 1, Level 1!</p>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: '14px' }}>
            {revisableLevels.map((lvl) => (
              <div key={lvl.id} className="card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                    <span style={{ fontSize: '0.75rem', fontWeight: 700, padding: '2px 8px', borderRadius: '10px', background: 'var(--accent-green-bg)', color: 'var(--accent-green)' }}>
                      LEVEL {lvl.number}
                    </span>
                    <CheckCircle size={16} color="var(--accent-green)" />
                  </div>
                  <h4 style={{ fontSize: '0.95rem', fontWeight: 700, marginBottom: '4px' }}>{lvl.title}</h4>
                  <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '12px' }}>{lvl.description}</p>
                </div>
                <button
                  onClick={() => onOpenLevel(lvl.id)}
                  className="btn btn-secondary"
                  style={{ width: '100%', fontSize: '0.85rem' }}
                >
                  <RotateCcw size={14} />
                  Revisit Level
                </button>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Recent Exam History */}
      {recentAttempts.length > 0 && (
        <div className="card">
          <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: '12px' }}>
            Recent Examination Scores
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {recentAttempts.map((att) => (
              <div key={att.id} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-tertiary)', fontSize: '0.85rem' }}>
                <span>Level {att.level_id} Examination</span>
                <span style={{ fontWeight: 700, color: att.passed ? 'var(--accent-green)' : 'var(--accent-red)' }}>
                  {att.score_percent}% ({att.correct_count}/{att.total_questions})
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
