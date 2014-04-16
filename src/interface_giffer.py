#Contains interfaces from widgets on the "Create Gifs" tab.

import os
from PyQt5 import QtWidgets
import magick


class LinkedRatioBox(QtWidgets.QLineEdit):

    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.linked = True
        self.partner = QtWidgets.QLineEdit()
        self.originalheight = 1
        self.originalwidth = 1
        self.mode = "WIDTH"

        self.setInputMask("0000000000000000")
        self.setDisabled(True)

    def setPartner(self, buddy):
        self.partner = buddy

    def setOriginalSize(self, width, height):
        self.originalheight = height
        self.originalwidth = width

    def setMode(self, mode):
        if mode is not "WIDTH" and mode is not "HEIGHT":
            #TODO: Raise Error
            print("Error, invalid mode in LinkedRatioBox::setMode")
        else:
            self.mode = mode

    def setLinked(self, linked):
        self.linked = linked

    def textChanged(self):
        if self.linked:
            self.partner.setText(self.calculatePartnerValue(int(self.text())))

    def calculatePartnerValue(self, currnum):
        if self.mode == "WIDTH":
            return (currnum / self.originalwidth) * int(self.partner.text())
        elif self.mode == "HEIGHT":
            return (currnum / self.originalheight) * int(self.partner.text())


def populateJobList(screen):
    screen.ui.cmb_job.clear()
    path = "imgs/"
    dirlist = os.listdir(path)

    for entry in dirlist:
        if os.path.isdir("imgs/" + entry):
            screen.ui.cmb_job.addItem(entry)


def populatePresetsList(screen):
    #TODO: Add presets to list
    config = screen.config.getKey("savedgifsettings")


def resizeCheckboxStateChanged(screen):
    state = screen.ui.check_resize.isChecked()

    widgetlist = [
        screen.ui.check_resize_keepratio,
        screen.ui.line_resize_width,
        screen.ui.line_resize_height,
        screen.ui.lbl_resize_width,
        screen.ui.lbl_resize_height
    ]

    if state:
        for widget in widgetlist:
            widget.setEnabled(True)
    elif not state:
        for widget in widgetlist:
            widget.setEnabled(False)


def keepProportionsCheckboxStateChanged(screen):
    state = screen.ui.check_resize_keepratio.isChecked()

    if state:
        screen.ui.line_resize_height.setLinked(True)
        screen.ui.line_resize_width.setLinked(True)
    elif not state:
        screen.ui.line_resize_height.setLinked(False)
        screen.ui.line_resize_width.setLinked(False)


def createAnimatedImage(screen):
    currjob = screen.ui.cmb_job.currentText()
    if currjob is not None:
        args = dict()
        args['name'] = currjob
        args['resize'] = screen.ui.check_resize.isChecked()
        args['loop'] = screen.ui.check_gif_loop.isChecked()
        args['width'] = screen.ui.line_resize_width.text()
        args['height'] = screen.ui.line_resize_height.text()
        args['delay'] = screen.ui.spin_delay.value()
        screen.creator = magick.GifWorker(screen, args)
        screen.creator.progress.connect(progressUpdate)
        screen.creator.start()


def progressUpdate(screen, value):
    screen.ui.progress_gif.setValue(value)