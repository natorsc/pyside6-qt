# -*- coding: utf-8 -*-
"""."""

import subprocess
import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

VENV_EXECUTABLE = ROOT_DIR.joinpath('venv', 'bin', 'python')
if sys.platform == 'win32':
    VENV_EXECUTABLE = ROOT_DIR.joinpath('venv', 'Scripts', 'python')

print('[!] Instalando dependências [!]\n')
subprocess.run(
    args=f'{VENV_EXECUTABLE} -m pip install -r requirements.txt',
    cwd=ROOT_DIR,
    shell=True,
    check=True,
)
print('[!] Dependências instaladas [!]\n')
