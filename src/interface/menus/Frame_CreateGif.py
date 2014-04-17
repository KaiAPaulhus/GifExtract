from PyQt5.QtWidgets import QFrame
from interface.design.ui_tab_gif import Ui_frame_tab_gif
import interface.tab_gif
from magick import CommandFormatter


class Frame(QFrame):

    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.ui = Ui_frame_tab_gif()
        self.ui.setupUi(self)
        self.screen = parent
        self.formatter = CommandFormatter(self.ui.line_console, self.screen)
        self.listener = Listener(self.screen, self, self.formatter)
        self.connectSlots()
        interface.tab_gif.addCustomWidgets(self)
        interface.tab_gif.fillElementsFromConfig(self, self.screen.config)
        self.ui.group_advsettings.setDisabled(True)
        self.ui.line_console.hide()

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
        self.ui.btn_savegifsettings.clicked.connect(
            self.listener.updateDebugConsole)
        self.ui.radio_custom.toggled.connect(
            self.listener.radioCustomChecked)
        self.formatter.progress.connect(
            self.listener.progressUpdate)


class Listener(object):

    def __init__(self, screen, tab, formatter):
        self.screen = screen
        self.tab = tab
        self.formatter = formatter

    def refreshJobList(self):
        interface.tab_gif.populateJobList(self.screen)

    def resizeCheckboxStateChanged(self):
        interface.tab_gif.resizeCheckboxStateChanged(self.screen)

    def createAnimatedImage(self):
        #interface.tab_gif.createAnimatedImage(self.screen)
        valdict = dict()
        if self.screen.tab_gif.ui.radio_custom.isChecked():
            valdict = createValueDict(self.screen)
        elif self.screen.tab_gif.ui.radio_quality.isChecked():
            valdict = getQualityValueDict(self.screen)
        elif self.screen.tab_gif.ui.radio_size.isChecked():
            valdict = getSizeValueDict(self.screen)
        elif self.screen.tab_gif.ui.radio_balanced.isChecked():
            valdict = getBalancedValueDict(self.screen)

        self.formatter.updateString(valdict)
        self.formatter.finished.connect(self.taskFinished)
        self.formatter.start()

    def taskFinished(self, args=None):
        self.tab.ui.progress_gif_sub.setValue(0)
        self.tab.ui.lbl_gif_currtask.setText('Finished')

    def jobSelectionChanged(self):
        interface.tab_gif.jobSelected(self.screen)

    def ratioCheckChanged(self):
        interface.tab_gif.keepProportionsCheckboxStateChanged(self.screen)

    def updateDebugConsole(self):
        pass
        # valdict = createValueDict(self.screen)
        # for k, v in valdict.items():
        #     print(k, v)
        # self.formatter.updateString(valdict)
        # self.formatter.start()

    def radioCustomChecked(self):
        if self.screen.tab_gif.ui.radio_custom.isChecked():
            self.screen.tab_gif.ui.group_advsettings.setEnabled(True)
        else:
            self.screen.tab_gif.ui.group_advsettings.setDisabled(True)

    def progressUpdate(self, arg0, arg1, arg2):
        interface.tab_gif.progressUpdate(arg0, arg1, arg2)


def getMainSet(screen):
    valdict = dict()
    valdict['delay'] = int(screen.tab_gif.ui.spin_delay.value())
    valdict['loops'] = int(screen.tab_gif.ui.spin_loops.value())
    valdict['input'] = str(screen.tab_gif.ui.cmb_job.currentText())
    valdict['coalesce'] = True
    valdict['output'] = str(screen.tab_gif.ui.cmb_job.currentText())
    return valdict


def getSizeValueDict(screen):
    valdict = getMainSet(screen)
    valdict['optimize_plustrans'] = True
    valdict['nocomments'] = True
    return valdict


def getQualityValueDict(screen):
    valdict = getMainSet(screen)
    return valdict


def getBalancedValueDict(screen):
    valdict = getMainSet(screen)
    valdict['optimize_plus'] = True
    return valdict


def createValueDict(screen):
    valdict = getMainSet(screen)

    optimethod = screen.tab_gif.ui.cmb_optimizationmethod.currentIndex()
    if optimethod == 1:
        valdict['optimize'] = True
    elif optimethod == 2:
        valdict['optimize_plustrans'] = True
    elif optimethod == 3:
        valdict['optimize_plus'] = True
    elif optimethod == 4:
        valdict['optimize_frame'] = True
    elif optimethod == 5:
        valdict['optimize_trans'] = True

    if screen.tab_gif.ui.check_usefuzz.isChecked():
        valdict['fuzzfactor'] = str(screen.tab_gif.ui.spin_fuzzfactor.value())
    if screen.tab_gif.ui.check_noaa.isChecked():
        valdict['noaa'] = True
    if screen.tab_gif.ui.check_flattencolors.isChecked():
        valdict['flattencolors'] = True
    if screen.tab_gif.ui.check_nocomments.isChecked():
        valdict['nocomments'] = True

    return valdict