#Contains interfaces from widgets on the "Create Gifs" tab.

import os
from PyQt5 import QtWidgets, QtGui
import magick


class LinkedRatioBox(QtWidgets.QLineEdit):
    #TODO: FIX AUTOFILLING NUMBERS
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.linked = False
        self.partner = QtWidgets.QLineEdit()
        self.originalheight = 1
        self.originalwidth = 1
        self.mode = "WIDTH"
        self.setValidator(QtGui.QIntValidator(1, 99999, self))
        self.setEnabled(False)
        self.editingFinished.connect(self.updatePartner)

    def setPartner(self, buddy):
        self.partner = buddy

    def setOriginalSize(self, width=1, height=0):
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

    def updatePartner(self):
        if self.linked:
            text = self.text()
            currval = int(text)
            partnerval = self.calculatePartnerValue(currval)
            self.partner.setText(str(partnerval))

    def calculatePartnerValue(self, currnum):
        if self.mode == "WIDTH":
            base = currnum / self.originalwidth
            final = base * self.originalheight
            return int(round(final))
        elif self.mode == "HEIGHT":
            base = currnum / self.originalheight
            final = base * self.originalwidth
            return int(round(final))


def addCustomWidgets(screen):
    screen.ui.line_resize_height = LinkedRatioBox()
    screen.ui.line_resize_width = LinkedRatioBox()
    screen.ui.layout_resize.insertWidget(1, screen.ui.line_resize_width)
    screen.ui.layout_resize.insertWidget(3, screen.ui.line_resize_height)
    screen.ui.line_resize_height.setMode('HEIGHT')
    screen.ui.line_resize_width.setMode('WIDTH')
    screen.ui.line_resize_height.setPartner(screen.ui.line_resize_width)
    screen.ui.line_resize_width.setPartner(screen.ui.line_resize_height)


def jobSelected(screen):
    currjob = screen.ui.cmb_job.currentText()
    if currjob != '':
        screen.sizer = magick.getImageSize(screen, currjob)
        screen.sizer.update.connect(jobSelectionUpdate)
        screen.sizer.start()


def jobSelectionUpdate(screen, width, height):
    screen.ui.line_resize_height.setOriginalSize(
        height=int(height), width=int(width))
    screen.ui.line_resize_width.setOriginalSize(
        height=int(height), width=int(width))
    screen.ui.line_resize_height.setText(height)
    screen.ui.line_resize_width.setText(width)


def populateJobList(screen):
    screen.ui.cmb_job.clear()
    path = "imgs/"
    dirlist = os.listdir(path)

    for entry in dirlist:
        if os.path.isdir("imgs/" + entry):
            if entry != 'out':
                screen.ui.cmb_job.addItem(entry)


def populatePresetsList(screen):
    #TODO: Add presets to list
    config = screen.config.getKey("savedgifsettings")


def resizeCheckboxStateChanged(screen):
    state = screen.ui.check_resize.isChecked()

    widgetlist = [
        screen.ui.check_resize_keepratio,
        screen.ui.lbl_resize_width,
        screen.ui.lbl_resize_height,
        screen.ui.line_resize_width,
        screen.ui.line_resize_height
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


def progressUpdate(screen, value, action):
    screen.ui.progress_gif_sub.setValue(value)
    screen.ui.lbl_gif_currtask.setText(action)