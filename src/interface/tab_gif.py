#Contains interfaces from widgets on the "Create Gifs" tab.

import os
from interface.controls import LinkedRatioBox
import magick


#Basic function, keep at top of file.
def fillElementsFromConfig(tab_gif, config):
    tab_gif.ui.spin_delay.setValue(config.getKey('gif_dfltdelay'))
    populatePresetsList(tab_gif, config)


#Basic function, keep at top of file.
def addCustomWidgets(tab_gif):
    tab_gif.ui.line_resize_height = LinkedRatioBox.LinkedRatioBox()
    tab_gif.ui.line_resize_width = LinkedRatioBox.LinkedRatioBox()
    tab_gif.ui.layout_resize.insertWidget(1, tab_gif.ui.line_resize_width)
    tab_gif.ui.layout_resize.insertWidget(3, tab_gif.ui.line_resize_height)
    tab_gif.ui.line_resize_height.setMode('HEIGHT')
    tab_gif.ui.line_resize_width.setMode('WIDTH')
    tab_gif.ui.line_resize_height.setPartner(tab_gif.ui.line_resize_width)
    tab_gif.ui.line_resize_width.setPartner(tab_gif.ui.line_resize_height)


def jobSelected(screen):
    currjob = screen.tab_gif.ui.cmb_job.currentText()
    if currjob != '':
        screen.sizer = magick.getImageSize(screen, currjob)
        screen.sizer.update.connect(jobSelectionUpdate)
        screen.sizer.start()


def jobSelectionUpdate(screen, width, height):
    screen.tab_gif.ui.line_resize_height.setOriginalSize(
        height=int(height), width=int(width))
    screen.tab_gif.ui.line_resize_width.setOriginalSize(
        height=int(height), width=int(width))
    screen.tab_gif.ui.line_resize_height.setText(height)
    screen.tab_gif.ui.line_resize_width.setText(width)


def populateJobList(screen):
    screen.tab_gif.ui.cmb_job.clear()
    path = "imgs/"
    if not os.path.exists(path):
        os.mkdir(path)
    dirlist = os.listdir(path)

    for entry in dirlist:
        if os.path.isdir("imgs/" + entry):
            if entry != 'out':
                screen.tab_gif.ui.cmb_job.addItem(entry)


def populatePresetsList(tab_gif, config):
    #TODO: Add presets to list
    key = config.getKey("savedgifsettings")
    for k, v in key.items():
        tab_gif.ui.cmb_loadgifsettings.addItem(v['name'])


def resizeCheckboxStateChanged(screen):
    state = screen.ui.check_resize.isChecked()

    widgetlist = [
        screen.tab_gif.ui.check_resize_keepratio,
        screen.tab_gif.ui.lbl_resize_width,
        screen.tab_gif.ui.lbl_resize_height,
        screen.tab_gif.ui.line_resize_width,
        screen.tab_gif.ui.line_resize_height
    ]

    if state:
        for widget in widgetlist:
            widget.setEnabled(True)
    elif not state:
        for widget in widgetlist:
            widget.setEnabled(False)


def keepProportionsCheckboxStateChanged(screen):
    state = screen.tab_gif.ui.check_resize_keepratio.isChecked()

    if state:
        screen.tab_gif.ui.line_resize_height.setLinked(True)
        screen.tab_gif.ui.line_resize_width.setLinked(True)
    elif not state:
        screen.tab_gif.ui.line_resize_height.setLinked(False)
        screen.tab_gif.ui.line_resize_width.setLinked(False)


def createAnimatedImage(screen):
    currjob = screen.tab_gif.ui.cmb_job.currentText()
    if currjob is not None:
        args = dict()
        args['name'] = currjob
        args['resize'] = screen.tab_gif.ui.check_resize.isChecked()
        args['loop'] = screen.tab_gif.ui.check_gif_loop.isChecked()
        args['width'] = screen.tab_gif.ui.line_resize_width.text()
        args['height'] = screen.tab_gif.ui.line_resize_height.text()
        args['delay'] = screen.tab_gif.ui.spin_delay.value()
        screen.creator = magick.GifWorker(screen, args)
        screen.creator.progress.connect(progressUpdate)
        screen.creator.start()


def progressUpdate(screen, value, action):
    screen.tab_gif.ui.progress_gif_sub.setValue(value)
    screen.tab_gif.ui.lbl_gif_currtask.setText(action)