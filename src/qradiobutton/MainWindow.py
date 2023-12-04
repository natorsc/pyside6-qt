# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QRadioButton()."""

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
        self.setWindowTitle('Python e Qt 6: PySide6 QRadioButton()')
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        vbox = QtWidgets.QVBoxLayout()
        vbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Layout que será utilizado dentro do groupbox.
        groupbox_vbox = QtWidgets.QVBoxLayout()

        groupbox = QtWidgets.QGroupBox()
        groupbox.setTitle('Selecione o gênero')
        groupbox.setLayout(groupbox_vbox)
        vbox.addWidget(groupbox)

        # QButtonGroup gerência quando o radio button é clicado.
        button_group = QtWidgets.QButtonGroup(self)
        button_group.buttonClicked.connect(self.on_button_toggled)

        radio_button_male = QtWidgets.QRadioButton()
        radio_button_male.setObjectName('radio_button_male')
        radio_button_male.setText('Masculino')
        button_group.addButton(radio_button_male)
        groupbox_vbox.addWidget(radio_button_male)

        radio_button_female = QtWidgets.QRadioButton()
        radio_button_female.setObjectName('radio_button_female')
        radio_button_female.setText('Feminino')
        button_group.addButton(radio_button_female)
        groupbox_vbox.addWidget(radio_button_female)

    def on_button_toggled(self, radio_button):
        radio_button_text = radio_button.text()
        print(f'Texto do radio button: {radio_button_text}.')
        radio_button_object_name = radio_button.objectName()
        print(f'Nome do objecto: {radio_button_object_name}.')
        if radio_button_object_name == 'male':
            print(
                f'Faça algo específico com radio button {radio_button_text}.'
            )
        elif radio_button_object_name == 'female':
            print(
                f'Faça algo específico com radio button {radio_button_text}.'
            )


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
