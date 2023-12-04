# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QPrintDialog()."""

from PySide6 import QtGui, QtWidgets, QtPrintSupport

import resources_rc

RESOURCES_RC = resources_rc

template = '''# Exemplo de uso do QPrintDialog().

Esse texto será renderizado no `QtWidgets.QTextEdit()`.

Edite o conteudo ou simplesmente <b>clique no botão</b> para
<span style="color:blue">imprimir</span>.
'''


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
        
        self.setWindowTitle('Python e Qt 6: PySide6 QPrintDialog()')
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

        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setMarkdown(template)
        vbox.addWidget(self.text_edit)

        push_button = QtWidgets.QPushButton()
        push_button.setText('Clique Aqui!')
        push_button.clicked.connect(self.on_button_clicked)
        vbox.addWidget(push_button)

    def showEvent(self, event):
        print(f'Janela aberta: {event}')

    def focusInEvent(self, event):
        print(f'Janela ganhou foco: {event}')

    def closeEvent(self, event):
        print(f'Janela fechada: {event}')

    

    def on_button_clicked(self):
        print_dialog = QtPrintSupport.QPrintDialog(self)
        # Verificando a resposta do dialogo.
        if print_dialog.exec():
            # Enviado o conteudo do QTextEdit para o QPrinter.
            self.text_edit.print_(print_dialog.printer())


if __name__ == "__main__":
    APPLICATION_NAME = 'br.com.justcode.PySide6'
    ORGANIZATION_NAME = APPLICATION_NAME.split('.')[2]
    ORGANIZATION_DOMAIN = '.'.join(APPLICATION_NAME.split('.')[0:3])

    current_platform = sys.platform
    if current_platform == 'win32' or current_platform == 'win64':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APPLICATION_NAME,
        )
    elif current_platform == 'linux':
        from os import environ, getenv

        XDG_SESSION_TYPE = getenv('XDG_SESSION_TYPE')
        if XDG_SESSION_TYPE == 'wayland':
            environ['QT_QPA_PLATFORM'] = 'wayland'
        elif XDG_SESSION_TYPE is None:
            environ['QT_QPA_PLATFORM'] = 'xcb'

    application = QtWidgets.QApplication(sys.argv)
    application.setOrganizationName(ORGANIZATION_NAME)
    application.setOrganizationDomain(ORGANIZATION_DOMAIN)
    application.setApplicationName(APPLICATION_NAME)
    application.setDesktopFileName(APPLICATION_NAME)

    window = MainWindow(application=application)
    window.show()

    sys.exit(application.exec())
