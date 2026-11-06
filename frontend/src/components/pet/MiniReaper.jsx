import React, { useEffect, useState } from "react";
import "./MiniReaper.css";

/**
 * MiniReaper — a lightweight, dependency-free mascot for Python Quest.
 *
 * Props:
 *  action: one of the supported actions below
 *  message: optional speech-bubble text
 *  size: CSS size, e.g. 220, "240px", "18rem"
 *  autoIdle: return to idle after actionDuration (default true)
 *  actionDuration: milliseconds before returning to idle (default 2600)
 *  showScythe: show/hide the decorative scythe (default true)
 *  onClick: optional click handler
 *  className: optional wrapper class
 *  label: accessible label
 *
 * Supported actions:
 * idle, thinking, searching, reading, typing, explaining, listening,
 * happy, celebrating, correct, wrong, confused, sleeping, waving,
 * levelUp, error, hint, loading, greeting, goodbye
 */

const ACTIONS = [
  "idle", "thinking", "searching", "reading", "typing", "explaining",
  "listening", "happy", "celebrating", "correct", "wrong", "confused",
  "sleeping", "waving", "levelUp", "error", "hint", "loading",
  "greeting", "goodbye",
];

const DEFAULT_MESSAGES = {
  thinking: "Hmm... let me think.",
  searching: "Looking for the answer...",
  reading: "Let me read that carefully.",
  typing: "Working on it...",
  explaining: "Let me explain this step by step!",
  listening: "I'm listening!",
  happy: "Nice work!",
  celebrating: "YOU DID IT!",
  correct: "That's correct! Brilliant!",
  wrong: "Not quite. Let's try again!",
  confused: "Wait... what happened here?",
  sleeping: "Zzz... wake me when you're ready.",
  waving: "Hey there, Python adventurer!",
  levelUp: "A NEW LEVEL! Incredible!",
  error: "Oops! Something went wrong.",
  hint: "Psst... here's a little hint.",
  loading: "Summoning the answer...",
  greeting: "Welcome back, adventurer!",
  goodbye: "See you on the next quest!",
};

export default function MiniReaper({
  action = "idle",
  message,
  size = 220,
  autoIdle = false,
  actionDuration = 2600,
  showScythe = true,
  onClick,
  className = "",
  label = "Mini Reaper, your Python Quest companion",
}) {
  const [currentAction, setCurrentAction] = useState(action);

  useEffect(() => {
    setCurrentAction(ACTIONS.includes(action) ? action : "idle");
  }, [action]);

  useEffect(() => {
    if (!autoIdle || currentAction === "idle" || currentAction === "sleeping") return;
    const timer = window.setTimeout(() => setCurrentAction("idle"), actionDuration);
    return () => window.clearTimeout(timer);
  }, [currentAction, autoIdle, actionDuration]);

  const bubbleText = message ?? DEFAULT_MESSAGES[currentAction];
  const style = { "--reaper-size": typeof size === "number" ? `${size}px` : size };

  return (
    <div
      className={`mini-reaper ${className} action-${currentAction}`}
      style={style}
      onClick={onClick}
      role={onClick ? "button" : "img"}
      tabIndex={onClick ? 0 : undefined}
      aria-label={label}
      onKeyDown={onClick ? (event) => {
        if (event.key === "Enter" || event.key === " ") onClick(event);
      } : undefined}
    >
      {bubbleText && (
        <div className="reaper-bubble" aria-live="polite">
          <span>{bubbleText}</span>
          <i />
        </div>
      )}

      <div className="reaper-stage">
        <div className="reaper-aura" />
        <div className="reaper-spark spark-one">✦</div>
        <div className="reaper-spark spark-two">✧</div>
        <div className="reaper-spark spark-three">✦</div>

        <svg className="reaper-svg" viewBox="0 0 240 260" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="cloakGradient" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stopColor="#514080" />
              <stop offset=".55" stopColor="#211936" />
              <stop offset="1" stopColor="#100d1d" />
            </linearGradient>
            <linearGradient id="hoodGradient" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stopColor="#7254a9" />
              <stop offset=".48" stopColor="#30224f" />
              <stop offset="1" stopColor="#171126" />
            </linearGradient>
            <radialGradient id="eyeGlow">
              <stop offset="0" stopColor="#f4d7ff" />
              <stop offset=".45" stopColor="#c084fc" />
              <stop offset="1" stopColor="#9333ea" />
            </radialGradient>
            <filter id="purpleGlow" x="-100%" y="-100%" width="300%" height="300%">
              <feGaussianBlur stdDeviation="3" result="blur" />
              <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
            </filter>
          </defs>

          {/* Decorative scythe */}
          {showScythe && (
            <g className="reaper-scythe">
              <path d="M184 194 L205 49" stroke="#8f78b8" strokeWidth="7" strokeLinecap="round" />
              <path d="M204 54 Q171 17 132 31 Q165 35 178 65 Q190 76 204 54Z"
                    fill="#d9d2ee" stroke="#8b78b4" strokeWidth="3" />
              <path d="M143 34 Q174 36 190 56" fill="none" stroke="#fff" strokeWidth="2" opacity=".8" />
              <circle cx="184" cy="191" r="6" fill="#b79add" />
            </g>
          )}

          {/* Shadow */}
          <ellipse cx="118" cy="239" rx="69" ry="10" fill="#090713" opacity=".35" />

          {/* Feet */}
          <g className="reaper-feet">
            <ellipse cx="91" cy="225" rx="20" ry="12" fill="#171126" stroke="#6d5795" strokeWidth="2" />
            <ellipse cx="145" cy="225" rx="20" ry="12" fill="#171126" stroke="#6d5795" strokeWidth="2" />
            <circle cx="91" cy="225" r="4" fill="#bba5df" opacity=".8" />
            <circle cx="145" cy="225" r="4" fill="#bba5df" opacity=".8" />
          </g>

          {/* Cloak body */}
          <path className="reaper-body"
            d="M66 133 Q48 160 52 210 Q76 235 118 235 Q163 235 183 210 Q188 164 166 132
               Q145 116 118 119 Q88 118 66 133Z"
            fill="url(#cloakGradient)" stroke="#8065a9" strokeWidth="3" />
          <path d="M74 204 Q117 221 162 204" fill="none" stroke="#8e75b5" strokeWidth="2" opacity=".5" />
          <path d="M83 145 Q70 175 79 203" fill="none" stroke="#b49bd8" strokeWidth="3" opacity=".25" />

          {/* Arms */}
          <g className="reaper-arms">
            <path className="reaper-arm arm-left" d="M66 151 Q37 155 45 183 Q51 194 69 180"
                  fill="none" stroke="#302348" strokeWidth="15" strokeLinecap="round" />
            <circle cx="48" cy="184" r="9" fill="#e8ddf7" />
            <path className="reaper-arm arm-right" d="M169 151 Q195 157 184 181"
                  fill="none" stroke="#302348" strokeWidth="15" strokeLinecap="round" />
            <circle cx="184" cy="183" r="9" fill="#e8ddf7" />
          </g>

          {/* Skull face */}
          <g className="reaper-head">
            <path d="M52 103 Q48 44 117 34 Q185 39 184 105 Q179 148 119 158 Q61 151 52 103Z"
                  fill="url(#hoodGradient)" stroke="#987cc2" strokeWidth="3" />
            <path d="M63 102 Q65 55 118 50 Q169 53 173 102 Q168 135 119 143 Q70 135 63 102Z"
                  fill="#eee8f6" />
            {/* Hood rim */}
            <path d="M49 105 Q38 42 111 23 Q176 19 190 91 Q166 65 145 68 Q106 76 83 112 Q68 125 49 105Z"
                  fill="#241a39" stroke="#8e72b9" strokeWidth="5" />
            <path d="M56 91 Q66 44 115 35 Q161 31 180 78" fill="none"
                  stroke="#b39ad8" strokeWidth="3" opacity=".6" />

            {/* Eye sockets */}
            <ellipse className="eye-socket eye-left" cx="94" cy="103" rx="17" ry="21" fill="#21172f" />
            <ellipse className="eye-socket eye-right" cx="143" cy="103" rx="17" ry="21" fill="#21172f" />
            <ellipse className="reaper-eye eye-left-glow" cx="95" cy="104" rx="9" ry="13" fill="url(#eyeGlow)" filter="url(#purpleGlow)" />
            <ellipse className="reaper-eye eye-right-glow" cx="144" cy="104" rx="9" ry="13" fill="url(#eyeGlow)" filter="url(#purpleGlow)" />
            <path d="M111 126 Q119 119 127 126 Q120 137 111 126Z" fill="#c7b8d9" opacity=".7" />
            <path d="M83 144 Q118 159 153 143" fill="none" stroke="#c9b9dc" strokeWidth="2" opacity=".5" />
          </g>

          {/* Skull emblem */}
          <g className="reaper-emblem">
            <circle cx="119" cy="184" r="15" fill="#2c2042" stroke="#987bc2" strokeWidth="2" />
            <path d="M111 180 Q111 172 119 172 Q127 172 127 180 L125 188 L113 188Z" fill="#eee8f6" />
            <circle cx="115" cy="180" r="2.5" fill="#302342" />
            <circle cx="123" cy="180" r="2.5" fill="#302342" />
            <path d="M116 187 L116 191 M122 187 L122 191" stroke="#302342" strokeWidth="2" />
          </g>

          {/* Action props */}
          <g className="prop-book">
            <path d="M154 159 Q170 153 181 161 L181 184 Q168 178 154 186Z" fill="#6c4ca0" stroke="#d1b8ff" strokeWidth="2"/>
            <path d="M154 159 L154 186" stroke="#eee2ff" strokeWidth="2"/>
            <path d="M160 166 L174 166 M160 172 L174 172" stroke="#eee2ff" strokeWidth="1.5"/>
          </g>
          <g className="prop-magnifier">
            <circle cx="181" cy="78" r="13" fill="none" stroke="#d7c4ff" strokeWidth="5"/>
            <path d="M190 88 L202 100" stroke="#d7c4ff" strokeWidth="6" strokeLinecap="round"/>
          </g>
          <g className="prop-keyboard">
            <rect x="151" y="175" width="45" height="20" rx="4" fill="#49366c" stroke="#b99ae9" strokeWidth="2"/>
            {Array.from({length: 6}, (_, i) => <rect key={i} x={157 + (i % 3) * 11} y={180 + Math.floor(i / 3) * 7} width="6" height="4" rx="1" fill="#e8d9ff"/>)}
          </g>
          <g className="prop-hint">
            <path d="M185 42 Q185 29 197 29 Q209 29 209 40 Q209 47 198 52 L198 57"
                  fill="none" stroke="#f3d78b" strokeWidth="5" strokeLinecap="round"/>
            <circle cx="198" cy="66" r="3" fill="#f3d78b"/>
          </g>
          <g className="prop-loading">
            <path d="M119 7 L119 16 M97 14 L103 21 M141 14 L135 21" stroke="#c084fc" strokeWidth="4" strokeLinecap="round"/>
          </g>
          <g className="prop-confetti">
            <path d="M44 72 l-7 -9 M196 120 l8 -8 M61 34 l3 -11 M177 27 l8 -5"
                  stroke="#f0c7ff" strokeWidth="4" strokeLinecap="round"/>
            <circle cx="43" cy="119" r="4" fill="#f7cf72"/>
            <circle cx="202" cy="151" r="4" fill="#a78bfa"/>
          </g>
          <g className="prop-error">
            <path d="M188 30 L204 46 M204 30 L188 46" stroke="#fb7185" strokeWidth="5" strokeLinecap="round"/>
          </g>
        </svg>

        <div className="reaper-ground-glow" />
        <div className="reaper-zzz">Zzz</div>
        <div className="reaper-question">?</div>
        <div className="reaper-exclamation">!</div>
        <div className="reaper-levelup">LEVEL UP!</div>
      </div>
    </div>
  );
}

export { ACTIONS, DEFAULT_MESSAGES };
