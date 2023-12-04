# -*- coding: utf-8 -*-
"""."""

import shutil
import subprocess
import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
VENV_DIR = ROOT_DIR.joinpath('venv')

print('[!] Iniciando a criação do ambiente virtual [!]')

if VENV_DIR.exists():
    print('[!] removendo ambiente já existente [!]')
    shutil.rmtree(VENV_DIR)

print('[!] Criando ambiente virtual [!]')
subprocess.run(
    args=f'{sys.executable} -m venv "{VENV_DIR}"',
    cwd=ROOT_DIR,
    shell=True,
    check=True,
)

print('[!] Ambiente virtual criado [!]')
