# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QSlider()."""

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
        self.setWindowTitle('Python e Qt 6: PySide6 QSlider()')
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        hbox = QtWidgets.QHBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(hbox)
        self.setCentralWidget(central_widget)

        vslider = QtWidgets.QSlider()
        vslider.sliderMoved.connect(self.on_slider_moved)
        hbox.addWidget(vslider)

        hslider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        hslider.sliderMoved.connect(self.on_slider_moved)
        hbox.addWidget(hslider)

    def on_slider_moved(self, value):
        print(f'Valor: {value}')


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
