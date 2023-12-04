# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QFileDialog() salvar."""

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
        self.setWindowTitle('Python e Qt 6: PySide6 QFileDialog() salvar')
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setMarkdown(template)
        vbox.addWidget(self.text_edit)

        push_button = QtWidgets.QPushButton()
        push_button.setText('Clique Aqui!')
        push_button.clicked.connect(self.on_button_clicked)
        vbox.addWidget(push_button)

    def on_button_clicked(self):
        save_dialog = QtWidgets.QFileDialog(self)

        # [!] Método 1 [!].
        # save_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        # save_dialog.setDefaultSuffix('.txt')
        # save_dialog.setMimeTypeFilters(MINE_TYPE_FILTERS)
        # if save_dialog.exec():
        #    file = QFile(save_dialog.selectedFiles()[0])
        #    if file.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Text):
        #        file.write(self.text_edit.toPlainText().encode('utf-8'))
        #        file.close()

        # [!] Método 2 [!].
        file_path, filter = save_dialog.getSaveFileName(
            parent=self,
            caption='',
            dir=HOME,
            filter=FILTERS,
            selectedFilter='',
            # Apenas para exemplo.
            # options=QtWidgets.QFileDialog.Option.DontUseNativeDialog,
        )

        if file_path:
            file = QtCore.QFile(f'{file_path}.txt')
            if file.open(QtCore.QIODevice.OpenModeFlag.WriteOnly |
                         QtCore.QIODevice.OpenModeFlag.Text):
                file.write(self.text_edit.toPlainText().encode('utf-8'))
                file.close()


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
