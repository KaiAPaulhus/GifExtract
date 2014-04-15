from ui_screen import Ui_wnd_pyjiff
from PyQt5 import QtWidgets,QtCore
import sys
import listener, config, ffmpeg, test, queue


class Screen(QtWidgets.QMainWindow):
  
    def __init__(self, parent=None):
        def setupFFMpeg():
            fileloc = self.config.getKey("ffmpeg")
            self.ffmpeg = ffmpeg.FFmpeg(fileloc)

        def setupConfig():
            self.config = config.Config()
            self.config.updateScreen(self.ui)

        def setupQueue():
            self.queue = queue.JobQueue(self.ui)

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_wnd_pyjiff()
        self.ui.setupUi(self)
        
        self.slots = listener.Slots(self)
        self.createLinks()
        
        setupConfig()
        setupFFMpeg()
        setupQueue()

    def createLinks(self):
        self.ui.chk_vidprefdur.stateChanged.connect(self.slots.useDuration)
        self.ui.cmb_fps.currentIndexChanged.connect(self.slots.fpsComboChanged)
        self.ui.btn_ffmpegbrowse.clicked.connect(self.slots.locateExtractor)
        self.ui.btn_ffmpegsave.clicked.connect(self.slots.saveFFmpegLocation)
        self.ui.btn_browsevideofile.clicked.connect(self.slots.locateVideo)
        self.ui.btn_vidanalyze.clicked.connect(self.slots.scanVideo)
        self.ui.btn_loadsubs.clicked.connect(self.slots.loadExternalSubs)
        self.ui.actionPreferences.triggered.connect(self.openOptions)
        self.ui.btn_extract_queue.clicked.connect(self.slots.addToQueue)
        self.ui.btn_extract_exe.clicked.connect(self.slots.extractFrames)
        
    def openOptions(self):
        options = config.ConfigMenu(self, self.config)
        options.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    program = Screen()
    program.show()
    sys.exit(app.exec_())