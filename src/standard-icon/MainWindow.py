# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QMainWindow()."""

import sys
from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_RC_PY = BASE_DIR.joinpath('resources_rc.py')
_SCRIPTS = BASE_DIR.parent.parent.joinpath('_scripts')

sys.path.append(str(_SCRIPTS))

import _tools

_tools.compile_resources(output=RESOURCES_RC_PY)

import resources_rc

RESOURCES_RC = resources_rc


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, application):
        super().__init__()
        self.application = application

        primary_screen = self.application.primaryScreen()
        primary_screen_geometry = primary_screen.geometry()
        primary_screen_height = primary_screen_geometry.height()
        primary_screen_width = primary_screen_geometry.width()

        window_width = int(primary_screen_width / 2)
        window_height = int(primary_screen_height / 2)

        self.setGeometry(0, 0, window_width, window_height)
        self.setMinimumSize(window_width, window_height)
        self.setWindowTitle('Python e Qt 6: PySide6 QMainWindow()')
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        # self.setCentralWidget(central_widget)

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidget(central_widget)
        self.setCentralWidget(scroll_area)

        vbox.addWidget(QtWidgets.QPushButton('data'))

        # for data in dir(QtWidgets.QStyle.StandardPixmap):

        #     if data.startswith('SP_'):
        #         vbox.addWidget(QtWidgets.QPushButton('data'))
        # for teste in range(2):
        #     vbox.addWidget(QtWidgets.QPushButton('data'))
        # for n, icon in enumerate(icons):
        #     # value = getattr(QtWidgets.QStyle.StandardPixmap, icon)
        #     # print(f'- `QtWidgets.QStyle.StandardPixmap.{icon}`. Valor = {value}')
        #     push_button = QtWidgets.QPushButton()
        #     push_button.setText('Botão')
        #     # push_button.setIcon(
        #     #     self.style().standardIcon(
        #     #         eval(f'QtWidgets.QStyle.StandardPixmap.{icon}'),
        #     #     )

        #     # )

        #     vbox.addWidget(push_button)

        # push_button = QtWidgets.QPushButton()
        # push_button.setText('Clique Aqui!')
        # vbox.addWidget(push_button)

        # for icon in icons:
        #     print(f'- `QtWidgets.QStyle.StandardPixmap.{icon}`.')

        # icon = self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowBack)

        # btn = QtWidgets.QPushButton()
        # btn.setIcon(icon)
        # vbox.addWidget(btn)

        # Código aqui...


if __name__ == "__main__":
    APPLICATION_NAME = 'br.com.justcode.PySide6'
    ORGANIZATION_NAME = APPLICATION_NAME.split('.')[2]
    ORGANIZATION_DOMAIN = '.'.join(APPLICATION_NAME.split('.')[0:3])

    application = QtWidgets.QApplication(sys.argv)
    application.setOrganizationName(ORGANIZATION_NAME)
    application.setOrganizationDomain(ORGANIZATION_DOMAIN)
    application.setApplicationName(APPLICATION_NAME)
    application.setDesktopFileName(APPLICATION_NAME)

    if QtCore.QSysInfo.productType() == 'windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APPLICATION_NAME,
        )

    window = MainWindow(application=application)
    window.show()

    sys.exit(application.exec())
