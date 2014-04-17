from PyQt5.QtWidgets import QFrame
from interface.design.ui_tab_gif import Ui_frame_tab_gif
import interface.tab_gif


class Frame(QFrame):

    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.ui = Ui_frame_tab_gif()
        self.ui.setupUi(self)
        self.screen = parent
        self.listener = Listener(self.screen, self)
        self.connectSlots()

        interface.tab_gif.addCustomWidgets(self)
        interface.tab_gif.fillElementsFromConfig(self, self.screen.config)

    def connectSlots(self):
        self.ui.btn_refreshjobs.clicked.connect(
            self.listener.refreshJobList)
        self.ui.check_resize.stateChanged.connect(
            self.listener.resizeCheckboxStateChanged)
        self.ui.btn_creategif.clicked.connect(
            self.listener.createAnimatedImage)
        self.ui.cmb_job.currentIndexChanged.connect(
            self.listener.jobSelectionChanged)
        self.ui.check_resize_keepratio.stateChanged.connect(
            self.listener.ratioCheckChanged)


class Listener(object):

    def __init__(self, screen, tab):
        self.screen = screen
        self.tab = tab

    def refreshJobList(self):
        interface.tab_gif.populateJobList(self.screen)

    def resizeCheckboxStateChanged(self):
        interface.tab_gif.resizeCheckboxStateChanged(self.screen)

    def createAnimatedImage(self):
        interface.tab_gif.createAnimatedImage(self.screen)

    def jobSelectionChanged(self):
        interface.tab_gif.jobSelected(self.screen)

    def ratioCheckChanged(self):
        interface.tab_gif.keepProportionsCheckboxStateChanged(self.screen)