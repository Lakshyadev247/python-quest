# Python Quest 🐍⚡
### Gamified Interactive Python Learning Adventure

[![Status: Beta](https://img.shields.io/badge/Status-Beta%20(Active%20Development)-orange?style=for-the-badge)](https://github.com)
[![Platform: Android & Windows](https://img.shields.io/badge/Platform-Android%20%7C%20Windows%20%7C%20Web-blue?style=for-the-badge)](https://github.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge&logo=python)](https://python.org)
[![React: 19](https://img.shields.io/badge/Frontend-React%2019%20%2B%20Vite-61dafb?style=for-the-badge&logo=react)](https://react.dev)

> ⚠️ **Project Status: Public Beta (Early Testing & Active Development)**  
> Python Quest is currently in public Beta. It was born out of a personal learning journey and built with AI assistance in just 2 days. While all 12 Worlds and 126 Levels are fully playable, some explanations, edge-case test cases, or higher-level challenges may still have quirks. Community feedback, issue reports, and pull requests are warmly welcomed!

---

## 📖 My Story & Why I Built This

I was learning Python, and I usually find it easier to understand things when they're broken down into simple explanations, followed by examples and small challenges. I also enjoy learning through quizzes and games because they make the whole process more fun, interactive, and interesting.

I was doing exactly that with ChatGPT — learning Python step by step, solving quizzes, and testing my knowledge. At some point, I thought: **Why not build my own quiz game where I can learn Python while playing?**

And that's how this project started!

I wanted something that would make learning Python feel less like studying and more like playing a game. I also wanted the freedom to continue learning even when I'm away from my PC, so I'm working on making the app mobile-friendly, allowing me to read lessons, write code, and solve challenges directly from my phone.

### A Little About The Project

- **Gamified Progression**: Built around 12 themed worlds, 126 sequential levels, detailed lessons, interactive quizzes, and hands-on coding challenges.
- **Bite-Sized Lessons**: Concepts are broken down into simple, approachable language without academic jargon.
- **Learn By Doing**: You read the concept, examine live code examples, answer comprehension questions, and write code directly in an integrated editor.
- **No Overwhelm**: The goal is to make learning Python enjoyable and rewarding rather than intimidating.
- **Everywhere You Go**: Available on desktop PC and on mobile devices with **100% offline standalone capability**.

### A Small Disclaimer

I'm still learning Python myself, and this project is part of my learning journey. I built the initial version in just **2 days**, with the help of AI.

The project is still in its early stages, so there might be mistakes, especially in the higher levels. Some explanations, questions, or coding challenges might not be perfect yet.

**That's where I'd love your help!**

If you find something incorrect, confusing, broken, or something that could be improved, please let me know. Feel free to [open an issue](../../issues) or even contribute a fix if you'd like.

I'm not presenting this as a perfect Python learning platform. I'm building it while learning Python myself, and I want to improve it along the way.

> **If you're learning Python too, I hope this little project makes your journey a bit more fun.**  
> *Happy coding!* 🐍

---

## 📥 Download Ready-to-Play Apps (No Setup Required!)

If you just want to play and learn without compiling from source, download the pre-built binaries directly from **[GitHub Releases](../../releases/latest)**:

| Platform | Download | Description |
| :--- | :--- | :--- |
| 📱 **Android** | [**`python-quest.apk`**](../../releases/latest) | Standalone APK for phones & tablets. **100% offline** with built-in client-side Python execution engine. No PC, Python, or server required! |
| 💻 **Windows Desktop** | [**`PythonQuest.exe`**](../../releases/latest) | Portable single-executable desktop app. Standalone with bundled Python runtime; extract and double-click to play! |
| 📦 **Windows ZIP** | [**`PythonQuest.zip`**](../../releases/latest) | Standalone desktop package in a portable archive. |

---

## 🌟 Key Features

* 🗺️ **12 Themed Worlds & 126 Levels**: From absolute fundamentals (`print()`, variables, math operators) through data structures, OOP, file handling, error handling, up to advanced decorators, regex, and SQLite databases.
* 🔄 **4-Stage Mastery Loop**:
  1. **Learn**: Structured lesson with syntax breakdown, line-by-line traces, expected outputs, and common pitfalls.
  2. **Coding Challenges**: Hands-on exercises evaluated against automated test cases with progressive hints.
  3. **Examination Quiz**: Immediate-feedback multiple-choice questions with explanations for right and wrong choices.
  4. **Boss Challenge**: Comprehensive capstone coding problem to conquer the level.
* 🐾 **Mini Reaper Companion Mascot**: An animated floating companion that reacts to your code, encourages you during errors, and celebrates your test triumphs.
* 📴 **100% Offline Capability**: Runs entirely on your local machine or phone. No mandatory cloud accounts, no subscriptions, and no internet connection required to write code.
* 🎨 **Customizable Interface**: Dark and light themes, classic and modern card layouts, and optional curriculum unlock controls.

---

## 🛠️ How It's Built & Technical Architecture

Python Quest is designed with a lightweight, decoupled architecture capable of running both in a full client-server stack and in a 100% client-side offline sandbox:

```text
┌────────────────────────────────────────────────────────┐
│                   Python Quest UI                      │
│        (React 19 + Monaco Editor + Lucide Icons)       │
└───────────────────────────┬────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
    [ Desktop / Web Mode ]       [ Mobile / Offline Mode ]
    Flask Backend (Port 5000)    Client-Side Python Engine
    ├── Python Subprocess Runner ├── AST & Keyword Remapper
    ├── AST Security Validator   ├── In-Memory SQLite Engine
    └── SQLite ORM Storage       └── Regex & Mock Standard Lib
```

### 1. Frontend
* **React 19 & Vite 8**: Ultra-fast component rendering and hot-module reloading.
* **Monaco Editor**: Industry-standard code editor (powers VS Code) with syntax highlighting, line numbering, and bracket matching.
* **Tailwind & Custom CSS**: Responsive layout with smooth transitions, animated companion mascot, and high-contrast dark theme.
* **Capacitor 8**: Native mobile bridge packaging the web application into an Android APK.

### 2. Backend & Code Sandbox (Desktop/Server Mode)
* **Python 3 & Flask**: Clean RESTful API serving curriculum data and progress tracking.
* **SQLAlchemy & SQLite**: Normalized relational schema storing levels, challenges, test cases, and quiz options.
* **Sandboxed Subprocess Execution**: User code runs inside isolated subprocesses with AST static analysis, strict execution timeouts (4 seconds), and forbidden dangerous imports (`ctypes`, `subprocess`, socket manipulation).

### 3. In-App Offline Runner (Android APK Mode)
* To allow full offline functionality on phones without running a heavy server, Python Quest features a dedicated offline engine (`pythonRunner.js`).
* It transpiles Python expressions, functions, list comprehensions, classes, decorators, raw strings, and recursion into safe JavaScript.
* Includes an **in-memory SQLite mock engine** capable of executing `CREATE TABLE`, `INSERT`, `UPDATE`, `DELETE`, and parameterized `SELECT` queries directly in memory on mobile devices!

---

## 💻 Running From Source (For Developers & Tinkers)

If you'd like to inspect the code, modify levels, or run the developer environment locally:

### Prerequisites
* **[Node.js 18+](https://nodejs.org/)** and npm
* **[Python 3.10+](https://python.org/)** (ensure `Add Python to PATH` is enabled during installation)

---

### Quick Launchers (Windows)

* **`start_app.bat`**: Double-click to automatically set up the Python venv, install missing packages, start both backend (port 5000) and frontend (port 5173), and open your browser.
* **`stop_app.bat`**: Double-click to cleanly terminate all running Python Quest processes.
* **`frontend/run_dev.bat`**: Double-click inside the `frontend` folder to install dependencies and launch Vite directly.

---

### Manual Setup (Step-by-Step)

#### 1. Clone the Repository
```bash
git clone https://github.com/Lakshyadev247/python-quest.git
cd python-quest
```

#### 2. Start the Backend
```bash
cd backend

# Create virtual environment (optional but recommended)
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask API server (http://localhost:5000)
python run.py
```

#### 3. Start the Frontend
Open a new terminal window:
```bash
cd frontend

# Install dependencies (first time only)
npm install

# Start the Vite development server (http://localhost:5173)
npm run dev
```

Visit **`http://localhost:5173`** in your browser.

---

## 🔨 Building Standalone Releases (EXE & APK)

To build your own release packages from source:

### 1. Windows Desktop Executable (`.exe`)
Python Quest uses PyInstaller to package the desktop version:
```bash
# In the project root directory:
pip install pyinstaller
python -m PyInstaller python_quest.spec --clean --noconfirm
```
The compiled standalone executable will be located in the `dist/` directory.

### 2. Android Standalone APK (`.apk`)
```bash
cd frontend

# Build frontend production assets
npm run build

# Sync assets to Capacitor Android project
npx cap sync android

# Build debug APK with Gradle (requires Android SDK & JDK 17/21)
cd android
./gradlew assembleDebug
```
The output APK will be generated at `android/app/build/outputs/apk/debug/app-debug.apk`.

*(Or simply run the automated `build_releases.bat` script on Windows!)*

---

## 🤝 Contributing & Community Help

Because this project is in **Active Beta** and created while learning Python:
* Did you spot a typo in a lesson?
* Is a quiz question misleading or incorrect?
* Did a test case fail unexpectedly on a valid Python solution?
* Do you have an idea for a cool new feature or level?

**All contributions are welcome!**

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/CoolImprovement`).
3. Commit your Changes (`git commit -m "Fix typo in World 4 Level 2 lesson"`).
4. Push to the Branch (`git push origin feature/CoolImprovement`).
5. Open a Pull Request!

You can also submit questions and bug reports on the [GitHub Issues](../../issues) page.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## 🙏 Acknowledgements

* [Python Software Foundation](https://www.python.org/) for the incredible language.
* [Monaco Editor](https://microsoft.github.io/monaco-editor/) for providing the rich browser code editing experience.
* [Capacitor](https://capacitorjs.com/) for enabling smooth cross-platform mobile packaging.
* Everyone in the open-source community learning and sharing knowledge every day.
