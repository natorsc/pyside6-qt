# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QtCharts()."""

import random
import sys
from pathlib import Path

from PySide6 import QtCharts, QtCore, QtGui, QtWidgets

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
        self.setWindowTitle('Python e Qt 6: PySide6 QtCharts()')
        self.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.PySide6'))

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        bar_set_01 = QtCharts.QBarSet('Título 01')
        bar_set_01.append(random.sample(range(1, 15), 2))
        self.bar_set_02 = QtCharts.QBarSet('Título 02')
        self.bar_set_02.append(random.sample(range(1, 15), 2))

        series = QtCharts.QBarSeries()
        series.append(bar_set_01)
        series.append(self.bar_set_02)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle('Título do gráfico')
        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        chart.setAnimationOptions(
            QtCharts.QChart.AnimationOption.SeriesAnimations)

        categories = ['Jan', 'Feb']
        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, QtCore.Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, 15)
        chart.addAxis(axis_y, QtCore.Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        chart_view = QtCharts.QChartView()
        chart_view.setChart(chart)
        chart_view.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        vbox.addWidget(chart_view)

        push_button = QtWidgets.QPushButton()
        push_button.setText('Atualizar')
        push_button.clicked.connect(self.on_button_clicked)
        vbox.addWidget(push_button)

    def on_button_clicked(self):
        self.bar_set_02.remove(0, self.bar_set_02.count())
        self.bar_set_02.append(random.sample(range(1, 15), 2))


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
