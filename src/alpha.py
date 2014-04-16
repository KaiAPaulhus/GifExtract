from ui_screen import Ui_wnd_pyjiff
from PyQt5 import QtWidgets
import sys
import listener
import config
import ffmpeg
import queue
import interface_giffer

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
        interface_giffer.addCustomWidgets(self)

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
        self.ui.btn_queue_exe.clicked.connect(self.slots.executeQueueItem)
        self.ui.btn_queue_exeall.clicked.connect(self.slots.executeAllQueue)

        self.ui.btn_refreshjobs.clicked.connect(self.slots.refreshJobList)
        self.ui.check_resize.stateChanged.connect(
            self.slots.resizeCheckboxStateChanged)
        self.ui.btn_creategif.clicked.connect(self.slots.createAnimatedImage)
        self.ui.cmb_job.currentIndexChanged.connect(
            self.slots.jobSelectionChanged)
        self.ui.check_resize_keepratio.stateChanged.connect(
            self.slots.ratioCheckChanged)
        
    def openOptions(self):
        options = config.ConfigMenu(self, self.config)
        options.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    program = Screen()
    program.show()
    sys.exit(app.exec_())