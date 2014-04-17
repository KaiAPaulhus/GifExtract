from PyQt5.QtWidgets import QFrame
from interface.design.ui_tab_queue import Ui_frame_tab_queue
import interface.tab_queue


class Frame(QFrame):

    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.ui = Ui_frame_tab_queue()
        self.ui.setupUi(self)
        self.screen = parent
        self.listener = Listener(self.screen, self)
        self.connectSignals()

    def connectSignals(self):
        self.ui.btn_queue_exe.clicked.connect(self.listener.executeQueueItem)
        self.ui.btn_queue_exeall.clicked.connect(self.listener.executeAllQueue)


class Listener(object):

    def __init__(self, screen, tab):
        self.screen = screen
        self.tab = tab

    def executeQueueItem(self):
        interface.tab_queue.executeQueueItem(self.screen)

    def executeAllQueue(self):
        interface.tab_queue.executeAllQueue(self.screen)