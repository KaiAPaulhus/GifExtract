from PyQt5 import QtWidgets, QtCore

from interface.design.ui_options import Ui_wnd_pyjiff_options


class ConfigMenu(QtWidgets.QMainWindow):

    def __init__(self, parent, config):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_wnd_pyjiff_options()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.config = config
        
        self.fillElements()
    
    #This exists only to save typing and space in the fillElements function
    def get(self, key):
        return self.config.getKey(key)

    def fillElements(self):
        self.ui.line_ffmpegfolder.setText(self.get('gen_ffmpeg'))
        self.ui.line_imfolder.setText(self.get('gen_imagemagick'))
        self.ui.check_autoscan.setChecked(self.get('vid_autoanalyze'))
        self.ui.check_fpsrounding.setChecked(self.get('vid_roundfps'))
        self.ui.check_usedurationalways.setChecked(
            self.get('vid_alwaysduration'))
        self.ui.spin_defaultdelay.setValue(self.get('gif_dfltdelay'))
        self.ui.btn_saveconfig.clicked.connect(self.config.saveButtonPressed)