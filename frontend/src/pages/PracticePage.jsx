import React, { useState } from 'react';
import CodeEditor from '../components/CodeEditor';

const TEMPLATES = [
  {
    name: 'Hello World',
    code: '# Welcome to Python Quest Playground!\nprint("Hello, World!")\nprint("Coding in Python is fun!")\n'
  },
  {
    name: 'Variables & Math',
    code: '# Variables and Arithmetic\nhero_name = "Alex"\nlevel = 5\nxp_per_level = 150\n\ntotal_xp = level * xp_per_level\nprint("Hero:", hero_name)\nprint("Level:", level)\nprint("Calculated XP:", total_xp)\n'
  },
  {
    name: 'Conditionals',
    code: '# If-Else Decision Making\nscore = 85\n\nif score >= 90:\n    grade = "A"\nelif score >= 80:\n    grade = "B"\nelif score >= 70:\n    grade = "C"\nelse:\n    grade = "Needs Practice"\n\nprint("Exam Score:", score)\nprint("Final Grade:", grade)\n'
  },
  {
    name: 'For Loop & Range',
    code: '# Repeating with for and range\nprint("Countdown to launch:")\nfor i in range(5, 0, -1):\n    print(i)\nprint("Liftoff! 🚀")\n'
  },
  {
    name: 'Functions',
    code: '# Defining Reusable Functions\ndef calculate_damage(attack_power, defense):\n    net = attack_power - defense\n    return max(0, net)\n\ndmg = calculate_damage(50, 15)\nprint("Net Damage Dealt:", dmg)\n'
  }
];

export default function PracticePage() {
  const [activeTemplate, setActiveTemplate] = useState(TEMPLATES[0]);
  const [templateKey, setTemplateKey] = useState(0);

  const handleSelectTemplate = (tmpl) => {
    setActiveTemplate(tmpl);
    setTemplateKey((prev) => prev + 1);
  };

  return (
    <div className="page-container" style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
      <div>
        <h2 style={{ fontSize: '1.4rem', fontWeight: 800, marginBottom: '6px' }}>
          Interactive Python Playground
        </h2>
        <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
          Write, experiment, and run real Python code instantly in a secure sandboxed environment.
        </p>
      </div>

      {/* Template Starter Selector */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
        <span style={{ fontSize: '0.8rem', fontWeight: 600, color: 'var(--text-muted)' }}>Load Template:</span>
        {TEMPLATES.map((tmpl) => (
          <button
            key={tmpl.name}
            type="button"
            onClick={() => handleSelectTemplate(tmpl)}
            className={`btn ${activeTemplate.name === tmpl.name ? 'btn-blue' : 'btn-secondary'}`}
            style={{ padding: '6px 12px', fontSize: '0.85rem' }}
          >
            {tmpl.name}
          </button>
        ))}
      </div>

      {/* Editor Component */}
      <div className="card" style={{ padding: '20px' }}>
        <CodeEditor
          key={`${activeTemplate.name}_${templateKey}`}
          initialCode={activeTemplate.code}
          challenge={{
            initial_code: activeTemplate.code
          }}
          height="450px"
        />
      </div>
    </div>
  );
}
