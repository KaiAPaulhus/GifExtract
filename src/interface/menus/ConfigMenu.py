from PyQt5 import QtWidgets, QtCore

from interface.design.ui_options import Ui_wnd_gifextract_options


class ConfigMenu(QtWidgets.QMainWindow):

    def __init__(self, parent, config):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_wnd_gifextract_options()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.config = config
        
        self.fillElements()
        self.connectElements()

    #This exists only to save typing and space in the fillElements function
    def get(self, key):
        return self.config.getKey(key)

    def widgetList(self):
        wdg = list()
        wdg.append([self.ui.line_ffmpegfolder.text,
                    'gen_ffmpeg'])
        wdg.append([self.ui.line_imfolder.text,
                    'gen_imagemagick'])
        wdg.append([self.ui.check_autoscan.isChecked,
                    'vid_autoanalyze'])
        wdg.append([self.ui.check_fpsrounding.isChecked,
                    'vid_roundfps'])
        wdg.append([self.ui.check_usedurationalways.isChecked,
                    'vid_alwaysduration'])
        wdg.append(([self.ui.spin_defaultdelay.value,
                     'gif_dfltdelay']))
        return wdg

    def fillElements(self):
        self.ui.line_ffmpegfolder.setText(self.get('gen_ffmpeg'))
        self.ui.line_imfolder.setText(self.get('gen_imagemagick'))
        self.ui.check_autoscan.setChecked(self.get('vid_autoanalyze'))
        self.ui.check_fpsrounding.setChecked(self.get('vid_roundfps'))
        self.ui.check_usedurationalways.setChecked(
            self.get('vid_alwaysduration'))
        self.ui.spin_defaultdelay.setValue(self.get('gif_dfltdelay'))

    def connectElements(self):
        self.ui.btn_saveconfig.clicked.connect(self.saveConfig)

    def getJSONValues(self):
        vardict = dict()
        for element in self.widgetList():
            vardict[element[1]] = element[0]()
        return vardict

    def saveConfig(self):
        vardict = self.getJSONValues()
        for k, v in vardict.items():
            self.config.updateConfig(k, v)
        self.config.saveConfig()