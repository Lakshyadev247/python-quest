import curriculumData from '../data/curriculum.json';
import { runPythonCodeOffline, runTestCasesOffline } from '../utils/pythonRunner';

// Distinguish between native Capacitor mobile app and web browser
export const isCapacitorApp = () => {
  return typeof window !== 'undefined' && (
    (window.Capacitor && window.Capacitor.isNativePlatform && window.Capacitor.isNativePlatform()) ||
    window.location.protocol === 'capacitor:'
  );
};

const ENV_API_URL = (import.meta.env.VITE_API_URL || '').trim();
const DEFAULT_BROWSER_API_URL = ENV_API_URL || '/api';

let isServerOnline = true;

const OFFLINE_ACHIEVEMENTS = [
  { id: 1, code: "FIRST_PROGRAM", title: "First Program", description: "Executed your very first Python program.", icon: "Terminal", xp_bonus: 50 },
  { id: 2, code: "FIRST_CHALLENGE", title: "First Coding Challenge", description: "Successfully solved your first coding challenge.", icon: "CheckCircle", xp_bonus: 50 },
  { id: 3, code: "PERFECT_EXAM", title: "Perfect Examination", description: "Scored 100% on a level MCQ examination.", icon: "Award", xp_bonus: 100 },
  { id: 4, code: "FIVE_LEVELS", title: "Five Levels Completed", description: "Mastered and completed 5 curriculum levels.", icon: "Zap", xp_bonus: 150 },
  { id: 5, code: "TEN_LEVELS", title: "Ten Levels Completed", description: "Mastered and completed 10 curriculum levels.", icon: "Star", xp_bonus: 200 },
  { id: 6, code: "DEBUGGING_EXPERT", title: "Debugging Expert", description: "Passed 10 practical coding exercises.", icon: "Wrench", xp_bonus: 100 },
  { id: 7, code: "LOOP_MASTER", title: "Loop Master", description: "Conquered loops and iteration in World 5.", icon: "Repeat", xp_bonus: 200 },
  { id: 8, code: "FUNCTION_SPECIALIST", title: "Function Specialist", description: "Mastered modular programming and functions in World 7.", icon: "Code", xp_bonus: 250 },
  { id: 9, code: "OOP_EXPERT", title: "OOP Expert", description: "Built object-oriented software architectures in World 10.", icon: "Layers", xp_bonus: 300 },
  { id: 10, code: "PYTHON_GRADUATE", title: "Python Graduate", description: "Completed all 12 Worlds of Python Quest.", icon: "GraduationCap", xp_bonus: 500 }
];

/** Normalise user input such as "192.168.1.8:5000" into a full /api URL. */
export function normalizeApiUrl(url) {
  let value = String(url || '').trim();
  if (!value) return '';

  if (value.toLowerCase() === 'offline') return 'offline';

  if (value.startsWith('/')) {
    return value.replace(/\/+$/, '') || '/api';
  }

  if (!/^https?:\/\//i.test(value)) {
    value = `http://${value}`;
  }
  value = value.replace(/\/+$/, '');
  if (!/\/api$/i.test(value)) {
    value = `${value}/api`;
  }
  return value;
}

export function getBaseApiUrl() {
  const stored = localStorage.getItem('pyquest_api_url');
  if (stored) {
    return normalizeApiUrl(stored);
  }
  if (isCapacitorApp()) {
    // Mobile runs 100% offline standalone out-of-the-box!
    return 'offline';
  }
  if (typeof window !== 'undefined' && window.location.protocol === 'file:') {
    // Desktop standalone pywebview / local executable runs against local Flask server
    return 'http://127.0.0.1:5000/api';
  }
  return normalizeApiUrl(DEFAULT_BROWSER_API_URL);
}

export function setBaseApiUrl(url) {
  const normalized = normalizeApiUrl(url);
  if (!normalized) return;
  localStorage.setItem('pyquest_api_url', normalized);
}

export function resetBaseApiUrl() {
  localStorage.removeItem('pyquest_api_url');
  isServerOnline = true;
}

export function getAuthToken() {
  return localStorage.getItem('pyquest_token');
}

export function setAuthToken(token) {
  if (token) {
    localStorage.setItem('pyquest_token', token);
  } else {
    localStorage.removeItem('pyquest_token');
  }
}

function getCacheScope() {
  return localStorage.getItem('pyquest_cache_scope') || 'anonymous';
}

export function setCacheScope(scope) {
  localStorage.setItem('pyquest_cache_scope', scope || 'anonymous');
}

export function clearApiCache() {
  Object.keys(localStorage)
    .filter((key) => key.startsWith('cache_'))
    .forEach((key) => localStorage.removeItem(key));
}

function cacheKey(endpoint) {
  return `cache_${getCacheScope()}_${endpoint}`;
}

export async function testServerConnection(customUrl) {
  const base = normalizeApiUrl(customUrl || getBaseApiUrl());
  if (base === 'offline') {
    return { ok: true, data: { status: 'offline_standalone', message: 'Running 100% standalone on device' } };
  }
  const url = `${base.replace(/\/+$/, '')}/health`;
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 3000);
    const res = await fetch(url, { signal: controller.signal });
    clearTimeout(timeoutId);
    if (res.ok) {
      const data = await res.json().catch(() => ({}));
      isServerOnline = true;
      return { ok: true, data };
    }
    isServerOnline = false;
    return { ok: false, error: `HTTP ${res.status}` };
  } catch (err) {
    isServerOnline = false;
    return { ok: false, error: err.name === 'AbortError' ? 'Timeout (server unreachable)' : (err.message || 'Connection failed') };
  }
}

/**
 * OFFLINE STANDALONE PROVIDER
 * Guarantees that on phone and offline, all 12 Worlds, 126 Levels,
 * Quizzes, Challenges, Lessons, Achievements, Profile, and Revision work
 * flawlessly without requiring any server or internet!
 */
export async function getOfflineCurriculumResponse(endpoint, method = 'GET', body = null) {
  const parsedBody = body ? (typeof body === 'string' ? JSON.parse(body) : body) : null;

  // 1. GET /worlds
  if (method === 'GET' && endpoint === '/worlds') {
    return { worlds: curriculumData.worlds || [] };
  }

  // 2. GET /worlds/:id
  if (method === 'GET' && endpoint.startsWith('/worlds/')) {
    const id = Number(endpoint.split('/worlds/')[1]);
    const w = (curriculumData.worlds || []).find((item) => Number(item.id) === id) || curriculumData.worlds[0];
    return { world: w };
  }

  // 3. GET /levels/:id
  if (method === 'GET' && endpoint.startsWith('/levels/')) {
    const id = Number(endpoint.split('/levels/')[1]);
    const lvl = curriculumData.levels[id] || curriculumData.levels[1];
    if (lvl) {
      let gProg = {};
      try {
        const stored = localStorage.getItem(`pyquest_guest_prog_${id}`);
        if (stored) gProg = JSON.parse(stored);
      } catch (e) {}
      return {
        level: {
          ...lvl,
          user_progress: { ...(lvl.user_progress || {}), ...gProg }
        }
      };
    }
  }

  // 4. GET /lessons/:id
  if (method === 'GET' && endpoint.startsWith('/lessons/')) {
    const id = Number(endpoint.split('/lessons/')[1]);
    const lsn = curriculumData.lessons[id] || curriculumData.lessons[1];
    return { lesson: lsn };
  }

  // 5. GET /progress
  if (method === 'GET' && endpoint === '/progress') {
    let completedCount = 0;
    for (let i = 1; i <= 126; i++) {
      const p = localStorage.getItem(`pyquest_guest_prog_${i}`);
      if (p) {
        try {
          if (JSON.parse(p).is_level_completed) completedCount++;
        } catch (e) {}
      }
    }
    return {
      completed_levels_count: completedCount,
      total_levels: 126,
      completion_percentage: Math.round((completedCount / 126) * 100),
      current_world: curriculumData.worlds[0],
      current_level: curriculumData.levels[1]
    };
  }

  // 6. GET /auth/me
  if (method === 'GET' && endpoint === '/auth/me') {
    let completedCount = 0;
    for (let i = 1; i <= 126; i++) {
      const p = localStorage.getItem(`pyquest_guest_prog_${i}`);
      if (p) {
        try {
          if (JSON.parse(p).is_level_completed) completedCount++;
        } catch (e) {}
      }
    }
    const xp = Number(localStorage.getItem('pyquest_guest_xp') || 0);
    const rank = localStorage.getItem('pyquest_guest_rank') || 'Beginner';
    return {
      user: {
        id: 1,
        username: 'Python Explorer',
        is_guest: true,
        current_level_id: Math.min(126, completedCount + 1),
        current_world_id: 1,
        xp: xp
      }
    };
  }

  // 7. POST /progress/lesson
  if (method === 'POST' && endpoint === '/progress/lesson') {
    const { level_id, completed } = parsedBody || {};
    let gProg = {};
    try {
      const stored = localStorage.getItem(`pyquest_guest_prog_${level_id}`);
      if (stored) gProg = JSON.parse(stored);
    } catch (e) {}
    gProg.lesson_completed = completed;
    localStorage.setItem(`pyquest_guest_prog_${level_id}`, JSON.stringify(gProg));
    return { success: true };
  }

  // 8. POST /quizzes/:id/submit
  if (method === 'POST' && endpoint.includes('/quizzes/') && endpoint.endsWith('/submit')) {
    const levelId = Number(endpoint.split('/quizzes/')[1].split('/submit')[0]);
    const answers = parsedBody?.answers || {};
    const lvl = curriculumData.levels[levelId] || curriculumData.levels[1];
    const questions = lvl?.quiz_questions || [];

    let correctCount = 0;
    const feedback = [];

    for (const q of questions) {
      const correctOpt = (q.options || []).find((o) => Boolean(o.is_correct));
      const userOptId = answers[q.id];
      const isCorrect = Boolean(correctOpt && userOptId === correctOpt.id);
      if (isCorrect) correctCount++;
      feedback.push({
        question_id: q.id,
        is_correct: isCorrect,
        correct_option_id: correctOpt?.id,
        explanation: q.explanation || correctOpt?.explanation || ''
      });
    }

    const total = questions.length;
    const scorePercent = total > 0 ? Math.round((correctCount / total) * 100) : 100;
    const passed = scorePercent >= 80;

    let gProg = {};
    try {
      const stored = localStorage.getItem(`pyquest_guest_prog_${levelId}`);
      if (stored) gProg = JSON.parse(stored);
    } catch (e) {}
    gProg.mcq_score = scorePercent;
    gProg.mcq_passed = passed;
    if (gProg.lesson_completed && gProg.mcq_passed) {
      gProg.is_level_completed = true;
    }
    localStorage.setItem(`pyquest_guest_prog_${levelId}`, JSON.stringify(gProg));

    return {
      success: true,
      passed,
      score_percent: scorePercent,
      correct_count: correctCount,
      total_questions: total,
      feedback
    };
  }

  // 9. POST /code/execute
  if (method === 'POST' && endpoint === '/code/execute') {
    return await runPythonCodeOffline(parsedBody?.code || '', parsedBody?.input || '');
  }

  // 10. POST /code/submit
  if (method === 'POST' && endpoint === '/code/submit') {
    const challengeId = parsedBody?.challenge_id;
    const code = parsedBody?.code || '';
    
    let foundChallenge = null;
    for (const lvlId in curriculumData.levels) {
      const chList = curriculumData.levels[lvlId].challenges || [];
      const c = chList.find(item => item.id === challengeId || String(item.id) === String(challengeId) || (typeof challengeId === 'number' && challengeId <= 126 && item.id === challengeId + 1299));
      if (c) {
        foundChallenge = c;
        break;
      }
    }

    if (foundChallenge && foundChallenge.test_cases) {
      const evalRes = await runTestCasesOffline(code, foundChallenge.test_cases);
      if (evalRes.passed && foundChallenge.level_id) {
        let gProg = {};
        try {
          const stored = localStorage.getItem(`pyquest_guest_prog_${foundChallenge.level_id}`);
          if (stored) gProg = JSON.parse(stored);
        } catch (e) {}
        if (foundChallenge.is_boss) {
          gProg.boss_completed = true;
        } else {
          gProg.challenges_passed = Math.max(gProg.challenges_passed || 0, 1);
        }
        localStorage.setItem(`pyquest_guest_prog_${foundChallenge.level_id}`, JSON.stringify(gProg));
      }
      return evalRes;
    }

    return await runPythonCodeOffline(code);
  }

  // 11. GET /achievements
  if (method === 'GET' && endpoint === '/achievements') {
    let completedCount = 0;
    for (let i = 1; i <= 126; i++) {
      const p = localStorage.getItem(`pyquest_guest_prog_${i}`);
      if (p) {
        try {
          if (JSON.parse(p).is_level_completed) completedCount++;
        } catch (e) {}
      }
    }
    const achs = OFFLINE_ACHIEVEMENTS.map(ach => {
      let unlocked = false;
      if (ach.code === 'FIRST_PROGRAM' && completedCount >= 1) unlocked = true;
      if (ach.code === 'FIRST_CHALLENGE' && completedCount >= 1) unlocked = true;
      if (ach.code === 'FIVE_LEVELS' && completedCount >= 5) unlocked = true;
      if (ach.code === 'TEN_LEVELS' && completedCount >= 10) unlocked = true;
      return {
        ...ach,
        unlocked,
        unlocked_at: unlocked ? new Date().toISOString() : null
      };
    });
    return {
      total: achs.length,
      unlocked_count: achs.filter(a => a.unlocked).length,
      achievements: achs
    };
  }

  // 12. GET /profile
  if (method === 'GET' && endpoint === '/profile') {
    let completedCount = 0;
    for (let i = 1; i <= 126; i++) {
      const p = localStorage.getItem(`pyquest_guest_prog_${i}`);
      if (p) {
        try {
          if (JSON.parse(p).is_level_completed) completedCount++;
        } catch (e) {}
      }
    }
    const xp = Number(localStorage.getItem('pyquest_guest_xp') || 0);
    const rank = localStorage.getItem('pyquest_guest_rank') || 'Beginner';
    return {
      user: {
        id: 1,
        username: 'Python Explorer',
        email: 'offline@pythonquest.local',
        rank: rank,
        xp: xp
      },
      stats: {
        completed_levels: completedCount,
        total_submissions: completedCount * 2,
        passed_submissions: completedCount * 2,
        unlocked_achievements: Math.min(OFFLINE_ACHIEVEMENTS.length, Math.floor(completedCount / 2))
      },
      achievements: [],
      recent_xp: []
    };
  }

  // 13. GET /revision
  if (method === 'GET' && endpoint === '/revision') {
    const revisable = [];
    for (let i = 1; i <= 126; i++) {
      const p = localStorage.getItem(`pyquest_guest_prog_${i}`);
      if (p) {
        try {
          if (JSON.parse(p).is_level_completed && curriculumData.levels[i]) {
            revisable.push(curriculumData.levels[i]);
          }
        } catch (e) {}
      }
    }
    return {
      revisable_levels: revisable,
      weak_levels: [],
      recent_quiz_attempts: []
    };
  }

  return null;
}

async function request(endpoint, options = {}) {
  const baseUrl = getBaseApiUrl();
  const method = options.method || 'GET';
  const body = options.body;
  const isCodeAction = endpoint === '/code/execute' || endpoint === '/code/submit';
  const isAiAction = endpoint.startsWith('/ai/');
  const isNativeOffline = baseUrl === 'offline' && (isCapacitorApp() || window.location.protocol === 'file:');

  // Keep native/file-based builds fully offline. In a browser, still try the
  // local Python API for code actions and AI routes.
  if (baseUrl === 'offline' && (!isCodeAction && !isAiAction || isNativeOffline)) {
    const offlineRes = await getOfflineCurriculumResponse(endpoint, method, body);
    if (offlineRes !== null) {
      return offlineRes;
    }
  }

  // For code execution / submission / AI, or if user hasn't explicitly set 'offline', ALWAYS attempt server first
  if (!isServerOnline && !isCodeAction && !isAiAction) {
    const offlineRes = await getOfflineCurriculumResponse(endpoint, method, body);
    if (offlineRes !== null) {
      return offlineRes;
    }
  }

  const isWebBrowser = typeof window !== 'undefined'
    && window.location.protocol.startsWith('http');
  const shouldUseLocalPythonApi = (isCodeAction || isAiAction) && isWebBrowser;
  // Use the app's own origin so the Vite /api proxy can forward requests to
  // the local Python bridge. Calling port 5000 directly from the browser failed
  // in the live preview and silently selected the limited JS fallback.
  const requestBaseUrl = shouldUseLocalPythonApi
    ? '/api'
    : (baseUrl === 'offline' ? DEFAULT_BROWSER_API_URL : baseUrl);
  const url = `${requestBaseUrl}${endpoint}`;
  const token = getAuthToken();

  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Bearer ${token}`  } : {}),
    ...options.headers,
  };

  const timeoutMs = isAiAction ? 60000 : (isCapacitorApp() ? 2500 : 8000);
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const res = await fetch(url, {
      ...options,
      headers,
      signal: controller.signal,
    });

    const data = await res.json().catch(() => ({}));

    if (!res.ok) {
      const error = new Error(data.error || `Request failed with status ${res.status}`);
      error.status = res.status;
      error.data = data;
      throw error;
    }

    isServerOnline = true;

    if (method === 'GET') {
      try {
        localStorage.setItem(cacheKey(endpoint), JSON.stringify(data));
      } catch (e) {}
    }

    return data;
  } catch (err) {
    isServerOnline = false;

    // Fallback to offline standalone provider
    const offlineRes = await getOfflineCurriculumResponse(endpoint, method, body);
    if (offlineRes !== null) {
      console.warn(`[Python Quest] Serving from offline standalone curriculum for: ${endpoint}`);
      return offlineRes;
    }

    if (isCodeAction && isLoopbackBrowser) {
      const detail = err?.name === 'AbortError'
        ? 'The local Python service did not respond in time.'
        : (err?.message || 'The local Python service could not be reached.');
      throw new Error(`Python execution service unavailable: ${detail}`);
    }

    // Secondary cache fallback
    const cached = localStorage.getItem(cacheKey(endpoint));
    if (cached) {
      try {
        return JSON.parse(cached);
      } catch (e) {}
    }

    throw err;
  } finally {
    clearTimeout(timeoutId);
  }
}

export const api = {
  get: (endpoint) => request(endpoint, { method: 'GET' }),
  post: (endpoint, body) => request(endpoint, { method: 'POST', body: JSON.stringify(body) }),
  put: (endpoint, body) => request(endpoint, { method: 'PUT', body: JSON.stringify(body) }),
  delete: (endpoint) => request(endpoint, { method: 'DELETE' }),
};
