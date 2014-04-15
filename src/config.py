from ui_options import Ui_wnd_pyjiff_options

from PyQt5 import QtWidgets
from PyQt5 import QtCore

import json


def setDefaults():
        default_ffmpeg = "Please select FFmpeg's 'Bin' folder."
        default_imagemagick = "Please select ImageMagick's 'Bin' folder."
        default_autoanalyze = False
        default_roundfps = True

        defaults = {'ffmpeg': default_ffmpeg,
                    'imagemagick': default_imagemagick,
                    'autoanalyze': default_autoanalyze,
                    'roundfps': default_roundfps}
        return defaults


def createSaveDialog(screen):
    msg = QtWidgets.QMessageBox(screen)
    msg.setText("This will overwrite your current configuration. Continue?")
    msg.setWindowTitle("Confirm Save")
    yesbtn = QtWidgets.QMessageBox.Yes
    nobtn = QtWidgets.QMessageBox.No
    msg.addButton(yesbtn)
    msg.addButton(nobtn)
    msg.setDefaultButton(nobtn)
    msg.setEscapeButton(nobtn)
    result = msg.exec_()
    return result


class Config(object):
    
    def __init__(self):
        self.config = {'JSON_NOT_LOADED': 'YET'}
        self.fileloc = 'settings.json'
        self.defaults = setDefaults()
        self.loadConfig()
             
    def createDefaultConfig(self):
        self.config = self.defaults
        self.performSave("default.json")

    def loadConfig(self):
        try:
            with open(self.fileloc, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            #TODO: POPUP INFORMING USER
                self.createDefaultConfig()

    def getKey(self, key):
        try:
            return self.config[key]
        except KeyError:
            return "KEY_NOT_FOUND"
            
    def saveConfig(self, screen=None):
        if screen is not None:
            result = createSaveDialog(screen)
            if result == QtWidgets.QMessageBox.Yes:
                self.performSave()
        else:
            self.performSave()
            
    def performSave(self, newloc=False):
        if not newloc:
            loc = self.fileloc
        else:
            loc = newloc
        with open(loc, 'w') as configfile:
            json.dump(self.config, configfile, indent=4)
            
    def updateConfig(self, key, value):
        self.config[key] = value
        
    def updateScreen(self, screen):
        ffkey = self.getKey('ffmpeg')
        screen.line_ffmpeg.setText(ffkey)


class ConfigMenu(QtWidgets.QMainWindow):

    def __init__(self, parent, config):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_wnd_pyjiff_options()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.config = config
        
        self.fillElements()
    
    #This exists only to save typing and space in the fillElements function
    def get(self,key):
        return self.config.getKey(key)

    def fillElements(self):
        self.ui.line_ffmpegfolder.setText(self.get('ffmpeg'))
        self.ui.line_imfolder.setText(self.get('imagemagick'))
        self.ui.check_autoscan.setChecked(self.get('autoanalyze'))
        self.ui.check_fpsrounding.setChecked(self.get('roundfps'))