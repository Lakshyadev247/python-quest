# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

block_cipher = None

backend_dir = os.path.abspath('backend')
frontend_dist = os.path.abspath('frontend/dist')
data_db = os.path.abspath('backend/data/python_quest.db')
curriculum_dir = os.path.abspath('backend/app/curriculum')
curriculum_json = os.path.abspath('frontend/src/data/curriculum.json')

datas = [
    (frontend_dist, 'frontend_dist'),
    (data_db, 'data'),
    (curriculum_dir, 'app/curriculum'),
    (curriculum_json, 'data'),
]

datas += collect_data_files('pywebview')

hiddenimports = [
    'flask',
    'flask_cors',
    'sqlalchemy',
    'sqlalchemy.sql.default_comparator',
    'sqlalchemy.dialects.sqlite',
    'sqlite3',
    'pydantic',
    'webview',
    'webview.platforms.winforms',
    'webview.platforms.edgechromium',
    'clr_loader',
    'pythonnet',
    'app',
    'app.config',
    'app.database',
    'app.models',
    'app.models.user',
    'app.models.curriculum',
    'app.models.progress',
    'app.models.gamification',
    'app.routes',
    'app.routes.auth_routes',
    'app.routes.curriculum_routes',
    'app.routes.progress_routes',
    'app.routes.quiz_routes',
    'app.routes.code_routes',
    'app.routes.gamification_routes',
    'app.routes.admin_routes',
    'app.services',
    'app.services.auth_service',
    'app.services.progress_service',
    'app.services.gamification_service',
    'app.services.executor_service',
    'app.services.sandbox_runner',
    'app.services.rate_limit',
    'app.curriculum',
    'app.curriculum.world1',
    'app.seed_curriculum',
]
hiddenimports += collect_submodules('sqlalchemy')

a = Analysis(
    ['backend/desktop_app.py'],
    pathex=[backend_dir],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'matplotlib', 'numpy', 'scipy', 'pandas'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PythonQuest',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PythonQuest',
)
