# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QCheckBox()."""

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
    checkboxes = []

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
        self.setWindowTitle('Python e Qt 6: PySide6 QCheckBox()')
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        vbox = QtWidgets.QVBoxLayout()
        # vbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Layout que será utilizado dentro do groupbox.
        groupbox_vbox_01 = QtWidgets.QVBoxLayout()

        groupbox_01 = QtWidgets.QGroupBox()
        groupbox_01.setTitle('Selecione o gênero')
        groupbox_01.setLayout(groupbox_vbox_01)
        vbox.addWidget(groupbox_01)

        # QButtonGroup gerência quando o checkbox é clicado.
        button_group_01 = QtWidgets.QButtonGroup(self)
        button_group_01.buttonClicked.connect(self.on_button_clicked)

        checkbox_male = QtWidgets.QCheckBox()
        checkbox_male.setObjectName('male')
        checkbox_male.setText('Masculino')
        button_group_01.addButton(checkbox_male)
        groupbox_vbox_01.addWidget(checkbox_male)

        checkbox_female = QtWidgets.QCheckBox()
        checkbox_female.setObjectName('female')
        checkbox_female.setText('Feminino')
        button_group_01.addButton(checkbox_female)
        groupbox_vbox_01.addWidget(checkbox_female)

        # Segundo groupbox.
        groupbox_02_hbox = QtWidgets.QHBoxLayout()

        groupbox_02 = QtWidgets.QGroupBox()
        groupbox_02.setTitle('Aceitar o termo?')
        groupbox_02.setLayout(groupbox_02_hbox)
        vbox.addWidget(groupbox_02)

        checkbox_item_yes = QtWidgets.QCheckBox()
        checkbox_item_yes.setObjectName('checkbox_item_yes')
        checkbox_item_yes.setText('Sim')
        checkbox_item_yes.stateChanged.connect(self.on_state_changed)
        groupbox_02_hbox.addWidget(checkbox_item_yes)

        # terceiro groupbox.
        groupbox_03_hbox = QtWidgets.QHBoxLayout()

        groupbox_03 = QtWidgets.QGroupBox()
        groupbox_03.setTitle('Selecione os itens')
        groupbox_03.setLayout(groupbox_03_hbox)
        vbox.addWidget(groupbox_03)

        checkbox_item_01 = QtWidgets.QCheckBox()
        checkbox_item_01.setObjectName('item_01')
        checkbox_item_01.setText('Item 01')
        checkbox_item_01.stateChanged.connect(
            lambda: self.on_state_changed_lambda(checkbox_item_01),
        )
        groupbox_03_hbox.addWidget(checkbox_item_01)

        checkbox_item_02 = QtWidgets.QCheckBox()
        checkbox_item_02.setObjectName('item_02')
        checkbox_item_02.setText('Item 02')
        checkbox_item_02.stateChanged.connect(
            lambda: self.on_state_changed_lambda(checkbox_item_02),
        )
        groupbox_03_hbox.addWidget(checkbox_item_02)

        checkbox_item_03 = QtWidgets.QCheckBox()
        checkbox_item_03.setObjectName('item_02')
        checkbox_item_03.setText('Item 02')
        checkbox_item_03.stateChanged.connect(
            lambda: self.on_state_changed_lambda(checkbox_item_03),
        )
        groupbox_03_hbox.addWidget(checkbox_item_03)

    def on_button_clicked(self, radio_button):
        radio_button_text = radio_button.text()
        print(f'Texto do checkbox: {radio_button_text}.')
        radio_button_object_name = radio_button.objectName()
        print(f'Nome do objecto: {radio_button_object_name}.')
        if radio_button_object_name == 'male':
            print(f'Faça algo específico com checkbox {radio_button_text}.')
        elif radio_button_object_name == 'female':
            print(f'Faça algo específico com checkbox {radio_button_text}.')

    def on_state_changed(self, state):
        if state == QtCore.Qt.CheckState.Checked.value:
            print('Checkbox está MARCADO')
        else:
            print('Checkbox está DESMARCADO')

    def on_state_changed_lambda(self, checkbox):
        if checkbox.isChecked():
            self.checkboxes.append(checkbox)
        else:
            self.checkboxes.remove(checkbox)
        print(f'Checkboxes que estão na lista: {self.checkboxes}')


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
