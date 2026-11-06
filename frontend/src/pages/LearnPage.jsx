import React, { useState, useEffect } from 'react';
import {
  Lock, CheckCircle2, Play, Trophy, Sparkles,
  ChevronRight, RefreshCw, AlertCircle
} from 'lucide-react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';
import curriculumData from '../data/curriculum.json';

function getGuestProgress(levelId) {
  try {
    return JSON.parse(localStorage.getItem(`pyquest_guest_prog_${levelId}`) || '{}');
  } catch {
    return {};
  }
}

function isGuestWorldUnlocked(world, allWorlds) {
  if (Number(world.number) === 1) return true;
  const previous = (allWorlds || []).find(item => Number(item.number) === Number(world.number) - 1);
  const bundledPrevious = (curriculumData.worlds || []).find(item => Number(item.number) === Number(world.number) - 1);
  const levels = previous?.levels || bundledPrevious?.levels || [];
  return levels.length > 0 && levels.every(level => getGuestProgress(level.id || level.number).is_level_completed === true);
}

export default function LearnPage({ onOpenLevel, refreshKey = 0 }) {
  const { user, progressionMode } = useAuth();
  const unlockAll = progressionMode === 'all';
  const isGuest = !user || user.is_guest;
  const [worlds, setWorlds] = useState(() => curriculumData.worlds || []);
  const [selectedWorldId, setSelectedWorldId] = useState(() => {
    try {
      const saved = Number(localStorage.getItem('pyquest_selected_world_id'));
      if (saved) return saved;
    } catch {}
    return user?.current_world_id || 1;
  });
  const [worldDetails, setWorldDetails] = useState(() => {
    const initialWId = Number(localStorage.getItem('pyquest_selected_world_id')) || user?.current_world_id || 1;
    const w = (curriculumData.worlds || []).find(item => item.id === initialWId) || (curriculumData.worlds || [])[0];
    if (!w) return null;
    const mapped = (w.levels || []).map(lvl => {
      const guestProg = localStorage.getItem(`pyquest_guest_prog_${lvl.id}`);
      return {
        ...lvl,
        is_unlocked: unlockAll || (isGuest
          ? (Number(lvl.number) === 1 || getGuestProgress(Number(lvl.number) - 1).is_level_completed === true)
          : Boolean(lvl.is_unlocked)),
        user_progress: lvl.user_progress || (guestProg ? JSON.parse(guestProg) : null)
      };
    });
    return { ...w, levels: mapped };
  });
  const [loading, setLoading] = useState(false);
  const [loadingWorld, setLoadingWorld] = useState(false);

  const handleSelectWorld = (worldId) => {
    setSelectedWorldId(worldId);
    try {
      localStorage.setItem('pyquest_selected_world_id', String(worldId));
    } catch {}
  };

  // Sync selectedWorldId to localStorage
  useEffect(() => {
    if (selectedWorldId) {
      try {
        localStorage.setItem('pyquest_selected_world_id', String(selectedWorldId));
      } catch {}
    }
  }, [selectedWorldId]);

  // Load all worlds
  useEffect(() => {
    async function loadWorlds() {
      setLoading(true);
      try {
        const res = await api.get('/worlds');
        const availableWorlds = (res.worlds || []).map(world => ({
          ...world,
          is_unlocked: unlockAll || (isGuest
            ? isGuestWorldUnlocked(world, res.worlds)
            : (Boolean(world.is_unlocked) || Number(world.number) === 1))
        }));
        setWorlds(availableWorlds);
        if (availableWorlds.length > 0) {
          setSelectedWorldId(prev => {
            if (prev && availableWorlds.some(w => w.id === prev && (unlockAll || w.is_unlocked))) {
              return prev;
            }
            try {
              const saved = Number(localStorage.getItem('pyquest_selected_world_id'));
              if (saved && availableWorlds.some(w => w.id === saved && (unlockAll || w.is_unlocked))) {
                return saved;
              }
            } catch {}
            const currentW = availableWorlds.find(w => w.id === user?.current_world_id && (unlockAll || w.is_unlocked))
              || availableWorlds.find(w => unlockAll || w.is_unlocked)
              || availableWorlds[0];
            return currentW ? currentW.id : 1;
          });
        }
      } catch (err) {
        console.error('Failed to load worlds, using bundled curriculum:', err);
        const fallbackWorlds = curriculumData.worlds || [];
        const availableWorlds = fallbackWorlds.map(world => ({
          ...world,
          is_unlocked: unlockAll || isGuestWorldUnlocked(world, fallbackWorlds)
        }));
        setWorlds(availableWorlds);
        if (availableWorlds.length > 0) {
          setSelectedWorldId(prev => {
            if (prev && availableWorlds.some(w => w.id === prev && (unlockAll || w.is_unlocked))) {
              return prev;
            }
            try {
              const saved = Number(localStorage.getItem('pyquest_selected_world_id'));
              if (saved && availableWorlds.some(w => w.id === saved && (unlockAll || w.is_unlocked))) {
                return saved;
              }
            } catch {}
            const currentW = availableWorlds.find(w => w.id === user?.current_world_id && (unlockAll || w.is_unlocked))
              || availableWorlds.find(w => unlockAll || w.is_unlocked)
              || availableWorlds[0];
            return currentW ? currentW.id : 1;
          });
        }
      } finally {
        setLoading(false);
      }
    }
    loadWorlds();
  }, [user, refreshKey, progressionMode]);

  // Load levels for selected world
  useEffect(() => {
    async function loadWorldDetails() {
      if (!selectedWorldId) return;
      setLoadingWorld(true);
      try {
        const res = await api.get(`/worlds/${selectedWorldId}`);
        if (res.world?.levels) {
          res.world.levels = res.world.levels.map(lvl => {
            const guestProg = localStorage.getItem(`pyquest_guest_prog_${lvl.id}`);
            return {
              ...lvl,
              is_unlocked: unlockAll || (isGuest
                ? (Number(lvl.number) === 1 || getGuestProgress(Number(lvl.number) - 1).is_level_completed === true)
                : Boolean(lvl.is_unlocked)),
              user_progress: lvl.user_progress || (guestProg ? JSON.parse(guestProg) : null)
            };
          });
        }
        setWorldDetails(res.world);
      } catch (err) {
        console.error('Failed to load world details, using bundled curriculum:', err);
        const w = (curriculumData.worlds || []).find(item => item.id === selectedWorldId) || curriculumData.worlds[0];
        if (w) {
          const mappedLevels = (w.levels || []).map(lvl => {
            const guestProg = localStorage.getItem(`pyquest_guest_prog_${lvl.id}`);
            return {
              ...lvl,
              is_unlocked: unlockAll || (isGuest
                ? (Number(lvl.number) === 1 || getGuestProgress(Number(lvl.number) - 1).is_level_completed === true)
                : Boolean(lvl.is_unlocked)),
              user_progress: lvl.user_progress || (guestProg ? JSON.parse(guestProg) : null)
            };
          });
          setWorldDetails({ ...w, levels: mappedLevels });
        }
      } finally {
        setLoadingWorld(false);
      }
    }
    loadWorldDetails();
  }, [selectedWorldId, user, refreshKey, progressionMode]);

  if (loading) {
    return (
      <div className="page-container" style={{ textAlign: 'center', padding: '60px' }}>
        <RefreshCw className="spin" size={32} style={{ margin: '0 auto 16px', color: 'var(--accent-blue)' }} />
        <p>Loading Python Quest Worlds...</p>
      </div>
    );
  }

  const selectedWorld = worlds.find(w => w.id === selectedWorldId) || worlds[0];

  return (
    <div className="page-container" style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {/* World Selector Pills */}
      <div>
        <h3 style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', fontWeight: 700, textTransform: 'uppercase', marginBottom: '12px' }}>
          Select World (12 Worlds)
        </h3>
        <div style={{
          display: 'flex',
          gap: '8px',
          overflowX: 'auto',
          paddingBottom: '8px'
        }}>
          {worlds.map((w) => {
            const isSelected = w.id === selectedWorldId;
            const isUnlocked = unlockAll || w.is_unlocked;
            return (
              <button
                key={w.id}
                onClick={() => { if (isUnlocked) handleSelectWorld(w.id); }}
                disabled={!isUnlocked}
                aria-disabled={!isUnlocked}
                title={!isUnlocked ? 'Complete the previous world to unlock this world.' : `Open World ${w.number}`}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  padding: '8px 16px',
                  borderRadius: 'var(--radius-full)',
                  border: isSelected ? '1px solid var(--accent-blue)' : '1px solid var(--border-color)',
                  background: isSelected ? 'var(--accent-blue-bg)' : 'var(--bg-secondary)',
                  color: isSelected ? 'var(--accent-blue)' : 'var(--text-primary)',
                  cursor: isUnlocked ? 'pointer' : 'not-allowed',
                  fontSize: '0.85rem',
                  fontWeight: 600,
                  whiteSpace: 'nowrap',
                  opacity: isUnlocked ? 1 : 0.65,
                  transition: 'all 0.15s ease'
                }}
              >
                {!isUnlocked ? <Lock size={14} color="var(--accent-gold)" /> : isSelected ? <Sparkles size={14} /> : null}
                <span>W{w.number}: {w.title}</span>
                {!isUnlocked && (
                  <span style={{ fontSize: '0.68rem', padding: '1px 6px', borderRadius: '8px', background: 'rgba(210, 153, 34, 0.18)', color: 'var(--accent-gold)', fontWeight: 700 }}>
                    Locked
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* World Overview Card */}
      {selectedWorld && (
        <div className="card" style={{
          background: 'linear-gradient(135deg, var(--bg-card), var(--bg-tertiary))',
          borderLeft: '4px solid var(--accent-blue)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '12px', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.8rem', fontWeight: 800, color: 'var(--accent-blue)', textTransform: 'uppercase' }}>
              WORLD {selectedWorld.number}
            </span>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', fontWeight: 600 }}>
              {selectedWorld.completed_levels || 0} / {selectedWorld.total_levels || 10} Levels Mastered ({selectedWorld.completion_percent || 0}%)
            </span>
          </div>
          <h2 style={{ fontSize: '1.5rem', fontWeight: 800, marginBottom: '6px' }}>{selectedWorld.title}</h2>
          <p style={{ fontSize: '0.95rem', color: 'var(--text-secondary)', marginBottom: '12px' }}>{selectedWorld.description}</p>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '0.85rem', color: 'var(--accent-gold)' }}>
            <Trophy size={16} />
            <span>Capstone Project: <strong>{selectedWorld.final_project_title}</strong></span>
          </div>
        </div>
      )}

      {/* Level Nodes Grid */}
      {loadingWorld ? (
        <div style={{ textAlign: 'center', padding: '40px' }}>
          <RefreshCw className="spin" size={24} style={{ margin: '0 auto 12px', color: 'var(--accent-blue)' }} />
          <p style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>Loading Levels...</p>
        </div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '16px' }}>
          {worldDetails?.levels?.map((lvl) => {
            const isCompleted = lvl.user_progress?.is_level_completed;
            const isUnlocked = unlockAll || (selectedWorld?.is_unlocked && lvl.is_unlocked);

            let cardStyle = {
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'space-between',
              cursor: 'pointer',
              opacity: isUnlocked ? 1 : 0.58,
              transition: 'transform 0.15s, border-color 0.15s, box-shadow 0.15s',
              border: '1px solid var(--border-color)',
            };

            if (isCompleted) {
              cardStyle.borderColor = 'rgba(46, 160, 67, 0.4)';
              cardStyle.background = 'rgba(46, 160, 67, 0.05)';
            } else if (isUnlocked) {
              cardStyle.borderColor = 'var(--accent-blue)';
              cardStyle.boxShadow = '0 0 12px rgba(56, 139, 253, 0.15)';
            } else {
              cardStyle.borderColor = 'var(--border-color)';
              cardStyle.background = 'rgba(255, 255, 255, 0.02)';
            }

            return (
              <div
                key={lvl.id}
                onClick={() => { if (isUnlocked) onOpenLevel(lvl.id); }}
                role="button"
                tabIndex={isUnlocked ? 0 : -1}
                aria-disabled={!isUnlocked}
                title={!isUnlocked ? 'Complete the previous level and world to unlock this level.' : `Open Level ${lvl.number}`}
                className="card"
                style={cardStyle}
              >
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
                    <span style={{
                      fontSize: '0.75rem',
                      fontWeight: 800,
                      padding: '2px 8px',
                      borderRadius: '10px',
                      background: isCompleted ? 'var(--accent-green-bg)' : isUnlocked ? 'var(--accent-blue-bg)' : 'var(--bg-tertiary)',
                      color: isCompleted ? 'var(--accent-green)' : isUnlocked ? 'var(--accent-blue)' : 'var(--text-secondary)'
                    }}>
                      LEVEL {lvl.number}
                    </span>

                    {isCompleted ? (
                      <CheckCircle2 size={20} color="var(--accent-green)" />
                    ) : isUnlocked ? (
                      <span style={{ fontSize: '0.75rem', color: 'var(--accent-blue)', fontWeight: 600 }}>Unlocked</span>
                    ) : (
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: '0.75rem', color: 'var(--accent-gold)', fontWeight: 600 }}>
                        <Lock size={14} color="var(--accent-gold)" /> Locked
                      </span>
                    )}
                  </div>

                  <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: '6px', color: 'var(--text-primary)' }}>
                    {lvl.title}
                  </h3>

                  <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', lineHeight: 1.5, marginBottom: '12px' }}>
                    {lvl.description}
                  </p>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderTop: '1px solid var(--border-color)', paddingTop: '10px', fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                  <span>{lvl.total_challenges || 1} coding | {lvl.total_questions || 2} MCQs</span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px', color: isUnlocked ? 'var(--accent-blue)' : 'var(--accent-gold)', fontWeight: 600 }}>
                    {isUnlocked ? 'Open' : 'Locked'} <ChevronRight size={14} />
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
