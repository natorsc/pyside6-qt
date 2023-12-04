# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QMainWindow()."""

import sys
from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_RC_PY = BASE_DIR.joinpath('resources_rc.py')
_SCRIPTS = BASE_DIR.parent.parent.parent.joinpath('_scripts')

sys.path.append(str(_SCRIPTS))

import _tools

_tools.compile_resources(output=RESOURCES_RC_PY)
_tools.compile_ui_file(ui_dir=BASE_DIR)

import resources_rc

from Ui_MainWindow import Ui_MainWindow

RESOURCES_RC = resources_rc


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent)
        self.application = kwargs.get('application')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    APPLICATION_NAME = 'br.com.justcode.PySide6'
    ORGANIZATION_NAME = APPLICATION_NAME.split('.')[2]
    ORGANIZATION_DOMAIN = '.'.join(APPLICATION_NAME.split('.')[0:3])

    QtGui.QIcon.setThemeName('breeze')

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
