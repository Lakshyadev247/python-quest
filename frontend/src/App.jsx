import React, { useState, useEffect } from 'react';
import { AuthProvider } from './context/AuthContext';
import { PetProvider } from './context/PetContext';
import Sidebar from './components/Sidebar';
import Navbar from './components/Navbar';
import DashboardPage from './pages/DashboardPage';
import LearnPage from './pages/LearnPage';
import PracticePage from './pages/PracticePage';
import RevisionPage from './pages/RevisionPage';
import AchievementsPage from './pages/AchievementsPage';
import ProfilePage from './pages/ProfilePage';
import SettingsPage from './pages/SettingsPage';
import LevelModal from './components/LevelModal';
import AuthModal from './components/AuthModal';
import CompanionPet from './components/pet/CompanionPet';
import curriculumData from './data/curriculum.json';
import { LayoutDashboard, Map, Code2, RotateCcw, Trophy, User, Settings } from 'lucide-react';

function MainApp() {
  const [activePage, setActivePage] = useState('dashboard');
  const [activeLevelId, setActiveLevelId] = useState(null);
  const [authModalOpen, setAuthModalOpen] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);

  const handleLevelUpdate = () => {
    setRefreshKey(prev => prev + 1);
  };

  const handleOpenLevel = (levelId) => {
    const worldId = curriculumData.levels?.[String(levelId)]?.world_id || curriculumData.levels?.[levelId]?.world_id;
    if (worldId) {
      try {
        localStorage.setItem('pyquest_selected_world_id', String(worldId));
      } catch {}
    }
    setActiveLevelId(levelId);
  };

  const handleCloseLevel = () => {
    setActiveLevelId(null);
    window.dispatchEvent(new CustomEvent('pyquest:pet-context', {
      detail: {
        levelNumber: null,
        levelTitle: 'Python Quest Dashboard',
        challengeTitle: '',
        challengeInstructions: '',
        code: '',
        lastError: '',
        lastStdout: ''
      }
    }));
  };

  const mobileNavItems = [
    { id: 'dashboard', label: 'Home', icon: LayoutDashboard },
    { id: 'learn', label: 'Learn', icon: Map },
    { id: 'practice', label: 'Practice', icon: Code2 },
    { id: 'revision', label: 'Revision', icon: RotateCcw },
    { id: 'achievements', label: 'Trophies', icon: Trophy },
    { id: 'profile', label: 'Profile', icon: User },
    { id: 'settings', label: 'Settings', icon: Settings },
  ];

  // Allow components to ask for modals/settings without threading props
  useEffect(() => {
    const openAuth = () => setAuthModalOpen(true);
    const openSettings = () => setActivePage('settings');
    window.addEventListener('pyquest:open-auth', openAuth);
    window.addEventListener('pyquest:open-settings', openSettings);
    return () => {
      window.removeEventListener('pyquest:open-auth', openAuth);
      window.removeEventListener('pyquest:open-settings', openSettings);
    };
  }, []);

  // Android hardware back: close modal, then go home, then exit the app.
  useEffect(() => {
    let remove = null;
    let cancelled = false;

    async function setupBackButton() {
      if (!window.Capacitor?.isNativePlatform?.()) return;
      try {
        const { App: CapacitorApp } = await import('@capacitor/app');
        const listener = await CapacitorApp.addListener('backButton', () => {
          if (activeLevelId) {
            handleCloseLevel();
          } else if (authModalOpen) {
            setAuthModalOpen(false);
          } else if (activePage !== 'dashboard') {
            setActivePage('dashboard');
          } else {
            CapacitorApp.exitApp();
          }
        });
        if (cancelled) {
          listener.remove();
        } else {
          remove = () => listener.remove();
        }
      } catch (e) {
        // Plugin unavailable on this build; default back behaviour applies.
      }
    }

    setupBackButton();
    return () => {
      cancelled = true;
      if (remove) remove();
    };
  }, [activeLevelId, authModalOpen, activePage]);

  return (
    <div className="app-layout">
      {/* Desktop Sidebar */}
      <Sidebar
        activePage={activePage}
        setActivePage={setActivePage}
        onOpenAuth={() => setAuthModalOpen(true)}
      />

      {/* Main Container */}
      <div className="main-content">
        <Navbar
          activePage={activePage}
          setActivePage={setActivePage}
          onOpenAuth={() => setAuthModalOpen(true)}
        />

        <main style={{ flex: 1 }}>
          {activePage === 'dashboard' && (
            <DashboardPage
              setActivePage={setActivePage}
              onOpenLevel={handleOpenLevel}
              onOpenAuth={() => setAuthModalOpen(true)}
            />
          )}

          {activePage === 'learn' && (
            <LearnPage onOpenLevel={handleOpenLevel} refreshKey={refreshKey} />
          )}

          {activePage === 'practice' && (
            <PracticePage />
          )}

          {activePage === 'revision' && (
            <RevisionPage
              onOpenLevel={handleOpenLevel}
              onOpenAuth={() => setAuthModalOpen(true)}
            />
          )}

          {activePage === 'achievements' && (
            <AchievementsPage onOpenAuth={() => setAuthModalOpen(true)} />
          )}

          {activePage === 'profile' && (
            <ProfilePage onOpenAuth={() => setAuthModalOpen(true)} />
          )}

          {activePage === 'settings' && (
            <SettingsPage />
          )}
        </main>
      </div>

      {/* Mobile Bottom Navigation Bar */}
      <nav className="mobile-nav">
        {mobileNavItems.map((item) => {
          const Icon = item.icon;
          const isActive = activePage === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActivePage(item.id)}
              className={`mobile-nav-item ${isActive ? 'active' : ''}`}
            >
              <Icon size={18} />
              <span>{item.label}</span>
            </button>
          );
        })}
      </nav>

      {/* Active Level Modal */}
      {activeLevelId && (
        <LevelModal
          levelId={activeLevelId}
          onClose={handleCloseLevel}
          onLevelUpdate={handleLevelUpdate}
          onNavigateLevel={(nextLvlId) => {
            const nextWorldId = curriculumData.levels?.[String(nextLvlId)]?.world_id || curriculumData.levels?.[nextLvlId]?.world_id;
            if (nextWorldId) {
              try {
                localStorage.setItem('pyquest_selected_world_id', String(nextWorldId));
              } catch {}
            }
            setActiveLevelId(nextLvlId);
            handleLevelUpdate();
          }}
          onOpenAuth={() => setAuthModalOpen(true)}
        />
      )}

      {/* Authentication Modal */}
      <AuthModal
        isOpen={authModalOpen}
        onClose={() => setAuthModalOpen(false)}
      />

      {/* Interactive AI Companion Pet ("Mini Reaper") - Always floats in front! */}
      <CompanionPet />

    </div>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <PetProvider>
        <MainApp />
      </PetProvider>
    </AuthProvider>
  );
}
