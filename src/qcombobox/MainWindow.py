# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QComboBox()."""

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
        self.setWindowTitle('Python e Qt 6: PySide6 QComboBox()')
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.label_result = QtWidgets.QLabel()
        self.label_result.setText('Este texto será alterado...')
        self.label_result.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.label_result)

        label = QtWidgets.QLabel()
        label.setText('Selecione um dos itens:')
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft |
                           QtCore.Qt.AlignmentFlag.AlignBottom)
        vbox.addWidget(label)

        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItem('Selecione.')
        for item in range(1, 4):
            self.combobox.addItem(f'Item {item}')

        # Outra forma de acionar novos itens.
        # Passando uma lista de itens.
        itens = ['Item 4', 'Item 5', 'Item 6']
        self.combobox.addItems(itens)

        # Conectando o sinal a um slot.
        self.combobox.currentIndexChanged.connect(
            self.on_current_index_changed)
        vbox.addWidget(self.combobox)

    def on_current_index_changed(self, index):
        if index != 0:
            combobox_text = self.combobox.currentText()
            print(combobox_text)
            self.label_result.setText(combobox_text)


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
