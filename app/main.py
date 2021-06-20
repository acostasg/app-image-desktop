import sys
from envyaml import EnvYAML
from PyQt6 import QtWidgets
from app.application.controller import mainController

config = EnvYAML('config/config.yml')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mainController.MainController()
    window.show()
    app.exec()

