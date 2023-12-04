# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QVBoxLayout()."""

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
        self.setWindowTitle('Python e Qt 6: PySide6 QVBoxLayout()')
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        menu_bar = self.menuBar()

        menu_file = menu_bar.addMenu(self.tr('Arquivo'))
        action_exit = QtGui.QAction()
        action_exit.setParent(menu_file)
        action_exit.setText('Sair')
        action_exit.setToolTip('Sair')
        action_exit.setIcon(
            QtGui.QIcon.fromTheme(
                'application-exit',
                QtGui.QIcon(':/icons/application-exit'),
            ),
        )
        action_exit.setIconText('Sair')
        # action_exit.setShortcut(QtGui.QKeySequence('Ctrl+q'))
        action_exit.setShortcut(QtCore.Qt.CTRL | QtCore.Qt.Key.Key_Q)
        action_exit.triggered.connect(self.on_action_exit_clicked)
        menu_file.addAction(action_exit)

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        push_button_01 = QtWidgets.QPushButton()
        push_button_01.setText('Botão 01')
        vbox.addWidget(push_button_01)

        push_button_02 = QtWidgets.QPushButton()
        push_button_02.setText('Botão 02')
        vbox.addWidget(push_button_02)

        push_button_03 = QtWidgets.QPushButton()
        push_button_03.setText('Botão 03')
        vbox.addWidget(push_button_03)

    


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
