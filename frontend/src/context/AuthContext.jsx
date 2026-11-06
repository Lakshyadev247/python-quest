import React, { createContext, useContext, useState, useEffect } from 'react';
import { api, setAuthToken, getAuthToken, clearApiCache, setCacheScope } from '../api/client';

const AuthContext = createContext(null);

const STORED_USER_KEY = 'pyquest_user';
const GUEST_USER_KEY = 'pyquest_guest_user';

export const RANKS = [
  { minXp: 0, name: 'Beginner', desc: 'Starting your programming journey (World 1)' },
  { minXp: 3000, name: 'Python Apprentice', desc: 'Grasping variables, logic, and data types (World 2+)' },
  { minXp: 9000, name: 'Code Explorer', desc: 'Mastering operators, conditions, and branching (World 4+)' },
  { minXp: 18000, name: 'Logic Builder', desc: 'Structuring loops, collections, and algorithms (World 6+)' },
  { minXp: 28000, name: 'Python Developer', desc: 'Building modular functions and error handling (World 8+)' },
  { minXp: 38000, name: 'Advanced Developer', desc: 'Creating OOP architectures and pipelines (World 10+)' },
  { minXp: 46000, name: 'Python Master', desc: 'Full capstone programming authority & databases (World 12)' },
];

export function calculateRank(totalXp) {
  let rank = 'Beginner';
  for (const r of RANKS) {
    if (totalXp >= r.minXp) {
      rank = r.name;
    } else {
      break;
    }
  }
  return rank;
}

export function calculateGuestTotalXP() {
  let totalXp = 0;
  let completedCount = 0;

  for (let i = 1; i <= 126; i++) {
    try {
      const raw = localStorage.getItem(`pyquest_guest_prog_${i}`);
      if (!raw) continue;
      const prog = JSON.parse(raw);
      if (prog.lesson_completed) totalXp += 50;
      if (prog.challenges_passed >= 1) totalXp += 100;
      if (prog.boss_completed) totalXp += 150;
      if (prog.mcq_passed) totalXp += 50;
      if (prog.is_level_completed) {
        totalXp += 100; // Perfect level completion bonus
        completedCount++;
      }
    } catch (e) {}
  }

  // Achievement bonuses
  if (completedCount >= 1) totalXp += 50; // First Program / First Challenge bonus
  if (completedCount >= 5) totalXp += 150; // Five Levels bonus
  if (completedCount >= 10) totalXp += 200; // Ten Levels bonus

  try {
    const extra = Number(localStorage.getItem('pyquest_guest_extra_xp') || 0);
    totalXp += extra;
  } catch (e) {}

  return totalXp;
}

function readStoredUser(key) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : null;
  } catch (e) {
    return null;
  }
}

function storeUser(user) {
  if (user && !user.is_guest) {
    localStorage.setItem(STORED_USER_KEY, JSON.stringify(user));
  } else {
    localStorage.removeItem(STORED_USER_KEY);
  }
}

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const [theme, setTheme] = useState(localStorage.getItem('pyquest_theme') || 'dark');
  const [uiTheme, setUiTheme] = useState(localStorage.getItem('pyquest_ui_theme') || 'classic');
  const [progressionMode, setProgressionMode] = useState(localStorage.getItem('pyquest_progression_mode') || 'sequential');

  // Monitor network status
  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  // Sync theme
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('pyquest_theme', theme);
  }, [theme]);

  useEffect(() => {
    document.documentElement.setAttribute('data-ui-theme', uiTheme);
    localStorage.setItem('pyquest_ui_theme', uiTheme);
  }, [uiTheme]);

  useEffect(() => {
    localStorage.setItem('pyquest_progression_mode', progressionMode);
  }, [progressionMode]);

  // Load user on mount
  useEffect(() => {
    async function loadUser() {
      const token = getAuthToken();
      if (!token) {
        setLoading(false);
        return;
      }

      try {
        const data = await api.get('/auth/me');
        setUser(data.user);
        storeUser(data.user);
        if (data.user?.theme) {
          setTheme(data.user.theme);
        }
      } catch (err) {
        // Only discard the session for an actual auth failure.  A transient
        // network error must not log the learner out.
        const authFailed = err.status === 401 || err.status === 403;
        if (authFailed) {
          setAuthToken(null);
          localStorage.removeItem(STORED_USER_KEY);
          setUser(null);
        } else {
          const cachedUser = readStoredUser(STORED_USER_KEY);
          if (cachedUser) {
            setUser(cachedUser);
          }
        }
      } finally {
        setLoading(false);
      }
    }

    const guestData = readStoredUser(GUEST_USER_KEY);
    if (guestData && !getAuthToken()) {
      const currentXp = calculateGuestTotalXP();
      const currentRank = calculateRank(currentXp);
      try {
        localStorage.setItem('pyquest_guest_xp', String(currentXp));
        localStorage.setItem('pyquest_guest_rank', currentRank);
      } catch {}
      const updatedGuest = { ...guestData, total_xp: currentXp, current_rank: currentRank };
      setUser(updatedGuest);
      try {
        localStorage.setItem(GUEST_USER_KEY, JSON.stringify(updatedGuest));
      } catch {}
      setCacheScope('guest');
      setLoading(false);
      return;
    }

    loadUser();
  }, []);

  const continueAsGuest = () => {
    const currentXp = calculateGuestTotalXP();
    const currentRank = calculateRank(currentXp);
    try {
      localStorage.setItem('pyquest_guest_xp', String(currentXp));
      localStorage.setItem('pyquest_guest_rank', currentRank);
    } catch {}
    const guestUser = {
      id: 0,
      username: 'Guest Explorer',
      email: 'guest@pythonquest.local',
      avatar: 'snake_novice',
      total_xp: currentXp,
      current_rank: currentRank,
      current_world_id: 1,
      current_level_id: 1,
      is_guest: true,
      created_at: new Date().toISOString()
    };
    setUser(guestUser);
    localStorage.setItem(GUEST_USER_KEY, JSON.stringify(guestUser));
    localStorage.removeItem(STORED_USER_KEY);
    setCacheScope('guest');
    return guestUser;
  };

  const login = async (username, password) => {
    localStorage.removeItem(GUEST_USER_KEY);
    const data = await api.post('/auth/login', { username, password });
    setAuthToken(data.token);
    setUser(data.user);
    storeUser(data.user);
    setCacheScope(username || data.user?.username || 'learner');
    if (data.user?.theme) setTheme(data.user.theme);
    return data;
  };

  const register = async (username, email, password) => {
    localStorage.removeItem(GUEST_USER_KEY);
    const data = await api.post('/auth/register', { username, email, password });
    setAuthToken(data.token);
    setUser(data.user);
    storeUser(data.user);
    setCacheScope(username || data.user?.username || 'learner');
    return data;
  };

  const logout = async () => {
    try {
      if (!user?.is_guest) {
        await api.post('/auth/logout', {});
      }
    } catch (e) {}
    setAuthToken(null);
    localStorage.removeItem(GUEST_USER_KEY);
    localStorage.removeItem(STORED_USER_KEY);
    setCacheScope('anonymous');
    clearApiCache();
    setUser(null);
  };

  const deleteGuestAccount = () => {
    if (!user?.is_guest) return false;
    Object.keys(localStorage).forEach(key => {
      if (key === GUEST_USER_KEY || key === 'pyquest_guest_xp' || key.startsWith('pyquest_guest_prog_') || key.startsWith('pyquest_guest_unlocked_')) {
        localStorage.removeItem(key);
      }
    });
    setCacheScope('anonymous');
    clearApiCache();
    setUser(null);
    return true;
  };

  const updateProfile = async (updates) => {
    const data = await api.put('/auth/profile', updates);
    setUser(data.user);
    storeUser(data.user);
    if (updates.theme) setTheme(updates.theme);
    return data.user;
  };

  const refreshUser = async () => {
    if (isGuest || !getAuthToken()) {
      const currentXp = calculateGuestTotalXP();
      const currentRank = calculateRank(currentXp);
      try {
        localStorage.setItem('pyquest_guest_xp', String(currentXp));
        localStorage.setItem('pyquest_guest_rank', currentRank);
      } catch {}
      setUser(prev => {
        if (!prev) return prev;
        const updated = {
          ...prev,
          total_xp: currentXp,
          current_rank: currentRank
        };
        try {
          localStorage.setItem(GUEST_USER_KEY, JSON.stringify(updated));
        } catch {}
        return updated;
      });
      return;
    }
    try {
      const data = await api.get('/auth/me');
      setUser(data.user);
      storeUser(data.user);
    } catch (e) {}
  };

  const isGuest = Boolean(user?.is_guest) || !user;

  return (
    <AuthContext.Provider
      value={{
        user,
        isGuest,
        loading,
        isOnline,
        theme,
        setTheme,
        uiTheme,
        setUiTheme,
        progressionMode,
        setProgressionMode,
        login,
        register,
        logout,
        deleteGuestAccount,
        continueAsGuest,
        updateProfile,
        refreshUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
