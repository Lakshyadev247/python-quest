import React, { useRef } from 'react';
import { usePet } from '../../context/PetContext';
import MiniReaper from './MiniReaper';

const REAPER_CHEERS = [
  { action: 'waving', msg: "Hey adventurer! Let's conquer this quest! ⚔️✨" },
  { action: 'celebrating', msg: "You've got this! Write clean Python code! 🚀" },
  { action: 'happy', msg: "I'm Mini Reaper, your quest companion! Keep going! 💀💜" },
  { action: 'typing', msg: "Tip: Read the instructions carefully and test each line!" },
  { action: 'explaining', msg: "Every error solved is a step closer to mastery! 💡" },
  { action: 'hint', msg: "Take your time, think through the logic, and you will win!" }
];

export default function CompanionPet() {
  const { petEnabled, action, message, triggerReaction } = usePet();
  const cheerIndexRef = useRef(0);

  if (!petEnabled) return null;

  const handleClick = () => {
    const cheer = REAPER_CHEERS[cheerIndexRef.current % REAPER_CHEERS.length];
    cheerIndexRef.current += 1;
    triggerReaction(cheer.action, cheer.msg, 3200);
  };

  return (
    <div
      className="companion-pet-container"
      style={{
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        zIndex: 99999,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        transition: 'transform 0.25s ease, opacity 0.25s ease',
        cursor: 'pointer',
      }}
      onClick={handleClick}
      title="Mini Reaper — Your Quest Mascot"
    >
      {/* Floating Mini Reaper Mascot */}
      <div style={{ position: 'relative' }}>
        <MiniReaper
          action={action}
          message={message}
          size={145}
          autoIdle={true}
          actionDuration={3200}
        />
      </div>

      {/* Responsive mobile positioning style */}
      <style>{`
        @media (max-width: 768px) {
          .companion-pet-container {
            bottom: 74px !important;
            right: 14px !important;
            transform: scale(0.85);
            transform-origin: bottom right;
          }
        }
      `}</style>
    </div>
  );
}
