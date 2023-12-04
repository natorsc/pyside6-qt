# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QProgressBar() com QThread()."""

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


class Thread(QtCore.QThread):
    # Nome do signal (sinal) que será emitido.
    signal_name = QtCore.Signal(int)

    def __init__(self):
        super(Thread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        # Operação que será realizada na tread.
        for value in range(101):
            sleep(0.1)
            # Emitindo o signal e passando o valor.
            self.signal_name.emit(value)


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
            'Python e Qt 6: PySide6 QProgressBar() com QThread()',
        )
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.progressbar = QtWidgets.QProgressBar()
        self.progressbar.valueChanged.connect(self.on_progressbar_value_change)
        vbox.addWidget(self.progressbar)

        self.button = QtWidgets.QPushButton()
        self.button.setText('Iniciar')
        self.button.clicked.connect(self.on_button_clicked)
        vbox.addWidget(self.button)

    def on_button_clicked(self):
        self.thread = Thread()
        self.thread.signal_name.connect(self.start_tread)
        self.thread.start()
        self.button.setEnabled(False)

    def on_progressbar_value_change(self, value):
        print(f'Valor do QProgressBar: {value}.')

    def start_tread(self, value):
        self.progressbar.setValue(int(value))
        if self.progressbar.value() == 100:
            self.progressbar.setValue(0)
            self.button.setEnabled(True)
            self.thread.quit()
            del self.thread


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
