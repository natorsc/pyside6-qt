# -*- coding: utf-8 -*-
"""."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
APP_DIR = ROOT_DIR.joinpath('src', 'qmainwindow')
HOME_DIR = Path.home()
APPLICATIONS_DIR = HOME_DIR.joinpath('.local', 'share', 'applications')

APP_NAME = 'br.com.justCode.PySide6'
APP_ICON = ROOT_DIR.joinpath('_resources', 'icons', f'{APP_NAME}.png')
APP_EXEC = APP_DIR.joinpath('pdm run MainWindow.py')
APP_DESKTOP_ENTRY = APPLICATIONS_DIR.joinpath(f'{APP_NAME}.desktop')

TEMPLATE = f'''[Desktop Entry]
Encoding=UTF-8
Type=Application
Version=1.0
Name={APP_NAME}
Comment=Criando interfaces gráficas com Python e Qt 6.
Path={APP_DIR}
Icon={APP_ICON}
Exec={APP_EXEC}
Terminal=false
Categories=Qt;Education;Languages;
Keywords=Qt;Python;
'''

with open(file=APP_DESKTOP_ENTRY, mode='w+', encoding='utf-8') as file:
    file.write(TEMPLATE)
    file.close()
