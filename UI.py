import subprocess
import sys

import requests
from PyQt5 import QtCore
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QLineEdit, \
    QHBoxLayout
from memory_profiler import profile


class WebServerUI(QWidget):
    @profile()
    def __init__(self):
        super().__init__()
        self.status = None

        self.portLabel = QLabel()
        self.portLabel.setText("Port Select:")
        self.portLabel.setFont(QFont('Roboto', 13, QFont.Bold))

        self.startLabel = QLabel()
        self.startLabel.setText("Server Started!")
        self.startLabel.setFont(QFont('Roboto', 13, QFont.Bold))
        self.startLabel.setVisible(False)

        self.stopLabel = QLabel()
        self.stopLabel.setText("Server Stopped!")
        self.stopLabel.setFont(QFont('Roboto', 13, QFont.Bold))

        self.stopLabel.setVisible(False)

        self.maintenance = QRadioButton("Maintenance")
        self.maintenance.setFont(QFont('Roboto', 13, QFont.Bold))

        self.portInput = QLineEdit()
        self.portInput.setValidator(QIntValidator())
        self.portInput.setMaxLength(5)
        self.portInput.setFont(QFont("Roboto", 12, QFont.Bold))
        self.portInput.setStyleSheet("background-color : white")

        self.startButton = QPushButton("Start")
        self.startButton.setFont(QFont('Roboto', 14, QFont.Bold))
        self.startButton.setStyleSheet("background-color : green")
        self.startButton.styleSheet()

        self.stopButton = QPushButton("Stop")
        self.stopButton.setFont(QFont('Roboto', 14, QFont.Bold))
        self.stopButton.setStyleSheet("background-color : red")

        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle("Web Server UI")
        self.setStyleSheet("background-color : #8cdbb8")

        self.outerLayout = QVBoxLayout()

        self.topLayout = QHBoxLayout()
        self.topLayout.addWidget(self.portLabel)
        self.topLayout.addWidget(self.portInput)

        self.maintenanceLayout = QVBoxLayout()
        self.maintenanceLayout.addWidget(self.maintenance)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addWidget(self.startButton)
        self.buttonsLayout.addWidget(self.stopButton)

        self.buttonsStatusLayout = QHBoxLayout()
        self.buttonsStatusLayout.addWidget(self.startLabel, alignment=QtCore.Qt.AlignCenter)
        self.buttonsStatusLayout.addWidget(self.stopLabel, alignment=QtCore.Qt.AlignCenter)

        self.outerLayout.addLayout(self.topLayout)
        self.outerLayout.addLayout(self.maintenanceLayout)
        self.outerLayout.addLayout(self.buttonsLayout)
        self.outerLayout.addLayout(self.buttonsStatusLayout)
        self.setLayout(self.outerLayout)

        self.startButton.clicked.connect(self.startApp)
        self.stopButton.clicked.connect(self.stopApp)
        self.maintenance.toggled['bool'].connect(self.maintenanceMode)

    def getPortNr(self):
        self.portNumber = self.portInput.text()

    def maintenanceMode(self):

        try:
            if self.portInput.text() == '':
                requests.get('http://127.0.0.1:' + '8080' + '/maintenance')
                if self.maintenance.isChecked():
                    self.portInput.setReadOnly(True)

            else:
                requests.get('http://127.0.0.1:' + self.portInput.text() + '/maintenance')

                if self.maintenance.isChecked():
                    self.portInput.setReadOnly(True)

        except:
            self.maintenance.setChecked(False)

    def startApp(self):
        if self.status != 1:
            self.result = subprocess.Popen(['python', 'webserver.py', self.portInput.text()], stdout=subprocess.PIPE,
                                           shell=True)
            self.portInput.setReadOnly(True)
            self.startLabel.setVisible(True)
            self.startLabel.setStyleSheet("color : green")
            self.stopLabel.setVisible(False)
            self.status = 1

    def stopApp(self):
        try:
            subprocess.Popen(['taskkill', '/F', '/T', '/PID', str(self.result.pid)])
            if self.maintenance.isChecked() == False:
                self.portInput.setReadOnly(False)
            else:
                self.maintenance.setChecked(False)
            self.startLabel.setVisible(False)
            self.stopLabel.setStyleSheet("color : red")
            self.stopLabel.setVisible(True)
            self.status = 0

        except:
            pass

    def closeEvent(self, event):
        try:
            subprocess.Popen(['taskkill', '/F', '/T', '/PID', str(self.result.pid)])
            event.accept()
        except:
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WebServerUI()
    ex.show()
    sys.exit(app.exec_())