from PyQt5.QtWidgets import QFrame
from interface.design.ui_tab_video import Ui_frame_tab_video
import interface.tab_video
import interface.tab_queue

class Frame(QFrame):

    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.ui = Ui_frame_tab_video()
        self.ui.setupUi(self)
        self.screen = parent
        self.listener = Listener(parent, self)
        self.connectSignals()

        interface.tab_video.fillElementsFromConfig(self,
                                                   self.screen.config)


    def connectSignals(self):
        self.ui.chk_vidprefdur.stateChanged.connect(self.listener.useDuration)
        self.ui.cmb_fps.currentIndexChanged.connect(
            self.listener.fpsComboChanged)
        self.ui.btn_browsevideofile.clicked.connect(self.listener.locateVideo)
        self.ui.btn_vidanalyze.clicked.connect(self.listener.scanVideo)
        self.ui.btn_loadsubs.clicked.connect(self.listener.loadExternalSubs)
        self.ui.btn_extract_queue.clicked.connect(self.listener.addToQueue)
        self.ui.btn_extract_exe.clicked.connect(self.listener.extractFrames)


class Listener(object):

    def __init__(self, screen, tab):
        self.screen = screen
        self.tab = tab

    def useDuration(self):
        interface.tab_video.preferDurationOverEndtime(self.tab)

    def fpsComboChanged(self):
        interface.tab_video.updateFPSLineEdit(self.tab)

    def locateVideo(self):
        interface.tab_video.setVideoFile(self.screen)

    def scanVideo(self):
        interface.tab_video.analyzeVideoFile(self.screen)

    def loadExternalSubs(self):
        interface.tab_video.setExternalSubtitles(self.screen)

    def addToQueue(self):
        interface.tab_queue.addToQueue(self.screen)

    def extractFrames(self):
        interface.tab_video.extractFramesFromVideo(self.screen)