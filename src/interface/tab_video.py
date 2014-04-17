#Contains functions from widgets on the "Extract Frames" tag, except
#for those relating to the queue system.

import queue
from interface.core import openDialog


#Basic function, keep at top of file.
def fillElementsFromConfig(screen, config):
    screen.ui.chk_vidprefdur.setChecked(config.getKey('vid_alwaysduration'))


def extractFramesFromVideo(screen):
    jobdict = queue.convertToString(screen)
    screen.ffmpeg.extractFrames(jobdict)


def analyzeVideoFile(screen):
    video = screen.ui.line_videoin.text()
    info = screen.ffmpeg.getVideoInfo(video)
    subs = info.getSubtitleList()
    fps = info.getFramesPerSecond()

    combo_items = getFPSComboBoxValues(screen, fps)
    screen.ui.cmb_fps.clear()
    screen.ui.cmb_fps.addItems(combo_items[1:])
    screen.ui.cmb_fps.setCurrentIndex(3)
    screen.ui.line_fps.setText(combo_items[0])

    sub_list = ["No Subtitles"]
    for x in range(0, len(subs)):
        index = subs[x][0]
        name = subs[x][1]
        lang = subs[x][2]
        string = "%s: %s (%s)" % (index, name, lang.upper())
        sub_list.append(string)

    screen.ui.cmb_subs.clear()
    screen.ui.cmb_subs.addItems(sub_list)


def updateFPSLineEdit(screen):
    curr = screen.ui.cmb_fps.currentText()
    if curr is "":
        pass
    else:
        val = curr[curr.find(' (')+2:curr.find('FPS)')-1]
        screen.ui.line_fps.setText(val)


def setExternalSubtitles(screen):
    startdir = "C:/"
    typefilter = "Subtitles (*.srt *.ass *.sub)"
    dest = screen.ui.cmb_subs
    openDialog(screen, startdir, typefilter, dest, False)


def setVideoFile(screen):
    startdir = "C:/test"
    typefilter = "Videos (*.avi *.mp4 *.mkv *.mov *.wmv *.divx *.vidx)"
    dest = screen.ui.line_videoin
    openDialog(screen, startdir, typefilter, dest, False)


def getFPSComboBoxValues(screen, fps):
    isrounded = screen.config.getKey('vid_roundfps')
    if isrounded:
        fpslist = [str(round(fps))]
    else:
        fpslist = [str(round(fps, 2))]

    for x in range(25, 225, 25):
        if isrounded:
            newfps = round(fps*(x/100))
        else:
            newfps = round(fps*(x/100), 2)
        newentry = str(x) + "%% (%s FPS)" % str(newfps)
        fpslist.append(newentry)
    return fpslist


def preferDurationOverEndtime(screen):
    state = screen.ui.chk_vidprefdur.checkState()
    if state == 2:
        screen.ui.lbl_endtime.setText("Duration")
    else:
        screen.ui.lbl_endtime.setText("End Time")
