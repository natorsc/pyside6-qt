# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QToolBar()."""

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
        self.setWindowTitle('Python e Qt 6: PySide6 QToolBar()')
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        toolbar = self.addToolBar('nome-da-barra')
        toolbar.setMovable(False)

        tool_button_copy = QtWidgets.QToolButton()
        tool_button_copy.setParent(toolbar)
        tool_button_copy.setText(self.tr('Copiar'))
        tool_button_copy.setIcon(
            QtGui.QIcon.fromTheme(
                'edit-copy',
                QtGui.QIcon(':/icons/edit-copy'),
            ),
        )
        tool_button_copy.setToolTip(self.tr('Copiar'))
        tool_button_copy.setShortcut(QtCore.Qt.CTRL | QtCore.Qt.Key.Key_C)
        tool_button_copy.clicked.connect(self.on_tool_button_copy_clicked)
        toolbar.addWidget(tool_button_copy)

        tool_button_cut = QtWidgets.QToolButton()
        tool_button_cut.setParent(toolbar)
        tool_button_cut.setText(self.tr('Recortar'))
        tool_button_cut.setIcon(
            QtGui.QIcon.fromTheme(
                'edit-cut',
                QtGui.QIcon(':/icons/edit-cut'),
            ),
        )
        tool_button_cut.setToolTip(self.tr('Recortar'))
        tool_button_cut.setShortcut(QtCore.Qt.CTRL | QtCore.Qt.Key.Key_X)
        tool_button_cut.clicked.connect(self.on_tool_button_cut_clicked)
        toolbar.addWidget(tool_button_cut)

        tool_button_about_qt = QtWidgets.QToolButton()
        tool_button_about_qt.setParent(toolbar)
        tool_button_about_qt.setText(self.tr('Sobre o Qt'))
        tool_button_about_qt.setToolTip(self.tr('Sobre o Qt'))
        tool_button_about_qt.clicked.connect(self.on_tool_button_about_qt_clicked)
        toolbar.addWidget(tool_button_about_qt)

        tool_button_exit = QtWidgets.QToolButton()
        tool_button_exit.setParent(toolbar)
        tool_button_exit.setText(self.tr('Sair'))
        tool_button_exit.setIcon(
            QtGui.QIcon.fromTheme(
                'application-exit',
                QtGui.QIcon(':/icons/application-exit'),
            ),
        )
        tool_button_exit.setToolTip(self.tr('Sair'))
        tool_button_exit.setShortcut(QtCore.Qt.CTRL | QtCore.Qt.Key.Key_Q)
        tool_button_exit.clicked.connect(self.on_tool_button_exit_clicked)
        toolbar.addWidget(tool_button_exit)

    def on_tool_button_exit_clicked(self):
        self.application.quit()

    def on_tool_button_copy_clicked(self):
        print('Copiar')

    def on_tool_button_cut_clicked(self):
        print('Recortar')

    def on_tool_button_about_qt_clicked(self):
        self.application.aboutQt()


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
