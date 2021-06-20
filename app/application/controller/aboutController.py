import sys
from pathlib import Path
from PyQt6 import QtWidgets, uic

qt_creator_file = Path(__file__).parent.parent.parent.absolute().__str__() + "/templates/about.ui"
UI_QDialog, QtBaseClass = uic.loadUiType(qt_creator_file)


class AboutController(QtWidgets.QDialog, UI_QDialog):
    def __init__(self):
        super().__init__()

        # init Main Window
        QtWidgets.QDialog.__init__(self)
        UI_QDialog.__init__(self)
        self.setupUi(self)

        # add events to template elements
        self.button_ok.clicked.connect(self.exit_application)

        self.show()
        # TODO it's necessary exec?
        self.exec()

    def exit_application(self):
        self.close()
