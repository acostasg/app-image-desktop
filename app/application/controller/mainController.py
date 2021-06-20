import sys
from pathlib import Path
from PyQt6 import QtWidgets, QtGui, uic
from app.application.controller import aboutController
from app.application.use_case.getReferencesByCampaignUseCase import GetReferencesByCampaignUseCase
from app.infrastucture.repository.referencesRepository import ReferencesRepository

qt_creator_file = Path(__file__).parent.parent.parent.absolute().__str__() + "/templates/main.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class MainController(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # init Main Window
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # add events to template elements
        self.action_exit.triggered.connect(self.event_exit_application)
        self.action_open_image.triggered.connect(self.event_open_image)
        self.action_about.triggered.connect(self.event_about)
        self.button_add_image.clicked.connect(self.event_open_image)
        self.button_load_refences.clicked.connect(self.event_load_references)

        # init values
        self.treeRefences.setHeaderLabels(["id", "name", "campaign_id", "details", "created", "modified"])

        return

    def event_exit_application(self):
        sys.exit()

    def event_about(self):
        aboutController.AboutController()

    def event_open_image(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                      '/', "Image files (*.jpg *.gif)")

        if not fname[0]:
            return

        label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(fname[0])
        label.setPixmap(pixmap)
        self.scroll_area.setWidget(label)

    def event_load_references(self):
        # TODO injector depedency
        references = GetReferencesByCampaignUseCase(ReferencesRepository()).execute()

        for reference in references.get_references():
            item = QtWidgets.QTreeWidgetItem([str(reference.id), reference.name])
            item_child = QtWidgets.QTreeWidgetItem([
                str(reference.id),
                reference.name,
                str(reference.campaign_id),
                reference.details,
                reference.created.strftime("%m/%d/%Y, %H:%M:%S"),
                reference.modified.strftime("%m/%d/%Y, %H:%M:%S")
            ])
            item.addChild(item_child)

            self.treeRefences.addTopLevelItem(item)
