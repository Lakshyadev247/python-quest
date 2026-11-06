import React, { createContext, useContext, useState, useEffect, useRef } from 'react';

const PetContext = createContext(null);

const STORAGE_PET_ENABLED = 'pyquest_pet_enabled';

export function PetProvider({ children }) {
  // 1. Pet Mascot Toggle State (Default: true)
  const [petEnabled, setPetEnabledState] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_PET_ENABLED);
      return saved !== null ? saved === 'true' : true;
    } catch {
      return true;
    }
  });

  const setPetEnabled = (val) => {
    setPetEnabledState(val);
    try {
      localStorage.setItem(STORAGE_PET_ENABLED, String(val));
    } catch {}
  };

  // 2. Pet Animation & Speech Bubble State
  const [action, setAction] = useState('idle');
  const [message, setMessage] = useState(null);
  const actionTimerRef = useRef(null);

  const triggerReaction = (newAction, newMsg = null, duration = 3000) => {
    if (actionTimerRef.current) clearTimeout(actionTimerRef.current);
    setAction(newAction);
    if (newMsg !== undefined) setMessage(newMsg);

    if (duration > 0 && newAction !== 'idle' && newAction !== 'sleeping') {
      actionTimerRef.current = setTimeout(() => {
        setAction('idle');
        setMessage(null);
      }, duration);
    }
  };

  // 3. Inactivity Sleeping Detection (60s timeout)
  const lastActiveRef = useRef(Date.now());
  const isSleepingRef = useRef(false);

  useEffect(() => {
    const onUserActivity = () => {
      lastActiveRef.current = Date.now();
      if (isSleepingRef.current) {
        isSleepingRef.current = false;
        triggerReaction('waving', "I'm awake and ready for your code!", 2500);
      }
    };

    window.addEventListener('mousemove', onUserActivity, { passive: true });
    window.addEventListener('keydown', onUserActivity, { passive: true });
    window.addEventListener('click', onUserActivity, { passive: true });
    window.addEventListener('scroll', onUserActivity, { passive: true });

    const interval = setInterval(() => {
      if (Date.now() - lastActiveRef.current >= 60000 && !isSleepingRef.current) {
        isSleepingRef.current = true;
        setAction('sleeping');
        setMessage("Zzz... wake me when you're ready.");
      }
    }, 5000);

    return () => {
      window.removeEventListener('mousemove', onUserActivity);
      window.removeEventListener('keydown', onUserActivity);
      window.removeEventListener('click', onUserActivity);
      window.removeEventListener('scroll', onUserActivity);
      clearInterval(interval);
    };
  }, []);

  // 4. Live Student Context Tracking (for reactions)
  const [liveContext, setLiveContext] = useState({
    worldTitle: 'Free Exploration',
    levelNumber: null,
    levelTitle: '',
    tab: 'general',
    challengeTitle: '',
    challengeInstructions: '',
    code: '',
    lastError: '',
    lastStdout: '',
    testResults: null,
    hints: [],
    isModalOpen: false
  });

  const updateLiveContext = (partial) => {
    setLiveContext(prev => ({ ...prev, ...partial }));
  };

  // 5. Custom Global Event Listeners for mascot reactions
  useEffect(() => {
    const handlePetReactionEvent = (e) => {
      const { action: act, message: msg, duration } = e.detail || {};
      if (act) triggerReaction(act, msg, duration ?? 3000);
    };

    const handlePetContextEvent = (e) => {
      if (e.detail) updateLiveContext(e.detail);
    };

    window.addEventListener('pyquest:pet-reaction', handlePetReactionEvent);
    window.addEventListener('pyquest:pet-context', handlePetContextEvent);

    return () => {
      window.removeEventListener('pyquest:pet-reaction', handlePetReactionEvent);
      window.removeEventListener('pyquest:pet-context', handlePetContextEvent);
    };
  }, []);

  return (
    <PetContext.Provider
      value={{
        petEnabled,
        setPetEnabled,
        action,
        message,
        triggerReaction,
        liveContext,
        updateLiveContext,
      }}
    >
      {children}
    </PetContext.Provider>
  );
}

export function usePet() {
  const ctx = useContext(PetContext);
  if (!ctx) throw new Error('usePet must be used within a PetProvider');
  return ctx;
}
