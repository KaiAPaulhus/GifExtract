from interface.design.ui_screen import Ui_wnd_gifextract
from PyQt5 import QtWidgets
import sys
import listener
import config
import ffmpeg
import queue
import interface.menus.Frame_CreateGif
import interface.menus.Frame_ExtractFrames
import interface.menus.Frame_Queue


class Screen(QtWidgets.QMainWindow):
  
    def __init__(self, parent=None):
        def setupFFMpeg():
            self.ffmpeg = ffmpeg.FFmpeg(self.config)

        def setupConfig():
            self.config = config.Config(self)

        def setupQueue():
            self.queue = queue.JobQueue(self)

        def setupTabs():
            self.tab_video = interface.menus.Frame_ExtractFrames.Frame(self)
            self.ui.tabWidget.addTab(self.tab_video, "Frame Extraction")
            self.tab_gif = interface.menus.Frame_CreateGif.Frame(self)
            self.ui.tabWidget.addTab(self.tab_gif, "Gif Creation")
            self.tab_queue = interface.menus.Frame_Queue.Frame(self)
            self.ui.tabWidget.addTab(self.tab_queue, "Queue")

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_wnd_gifextract()
        self.ui.setupUi(self)
        
        self.slots = listener.Slots(self)
        self.createLinks()

        setupConfig()
        setupTabs()
        setupFFMpeg()
        setupQueue()


    def createLinks(self):
        self.ui.actionPreferences.triggered.connect(self.openOptions)
        
    def openOptions(self):
        import interface.menus.ConfigMenu
        options = interface.menus.ConfigMenu.ConfigMenu(self, self.config)
        options.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    program = Screen()
    program.show()
    sys.exit(app.exec_())