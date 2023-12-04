# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QTranslator()."""

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
        self.setWindowTitle(
            self.application.translate(
                'window_title',
                'Python e Qt 6: PySide6 QTranslator() e translate.',
            ),
        )
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        label = QtWidgets.QLabel()
        label.setText(
            self.application.translate(
                'label',
                'Após trocar o idioma é necessário reiniciar o aplicativo.',
            ),
        )
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(label)

        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItem(
            self.application.translate(
                'combobox',
                'Selecione um idioma.',
            ),
        )
        self.combobox.addItem('en_US')
        self.combobox.addItem('pt_BR')
        self.combobox.setCurrentText(app_settings.value('language'))
        self.combobox.currentIndexChanged.connect(self.set_translate)
        vbox.addWidget(self.combobox)

    def set_translate(self, index):
        combobox_text = self.combobox.currentText()
        if index != 0:
            if combobox_text == 'pt_BR':
                app_settings.setValue('language', 'default')
            else:
                app_settings.setValue('language', f'{combobox_text}')


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
