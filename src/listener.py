from PyQt5 import QtWidgets
import queue


#A custom file dialog, containing a reference to the field
#that it's file's text will go into.
class FileDialog(QtWidgets.QFileDialog):

    def __init__(self, parent=None, destfield=None, slots=None,
                 folder=False, app=None):
        QtWidgets.QFileDialog.__init__(self, parent)
        
        if folder is True:
            self.setFileMode(QtWidgets.QFileDialog.Directory)
            self.setOptions(QtWidgets.QFileDialog.ShowDirsOnly)
        else:
            self.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        
        self.slots = slots
        self.fileSelected.connect(self.fileReady)
        self.destfield = destfield
        self.app = app
        
    def fileReady(self):
        self.slots.fileSelected(self.destfield, self.selectedFiles()[0])
        if self.app is not None:
            if self.app.config.getKey('autoanalyze'):
                self.app.slots.scanVideo()
        

#Contains functions that will be used by widgets.        
class Slots(object):

    def __init__(self, screen):
        self.ui = screen.ui
        self.screen = screen

    def useDuration(self):
        state = self.ui.chk_vidprefdur.checkState()
        print(state)
        if state == 2:
            self.ui.lbl_endtime.setText("Duration")
        else:
            self.ui.lbl_endtime.setText("End Time")
        
    def fpsComboChanged(self):
        curr = self.ui.cmb_fps.currentText()
        if curr is "":
            pass
        else:
            val = curr[curr.find(' (')+2:curr.find('FPS)')-1]
            self.ui.line_fps.setText(val)
        
    def locateVideo(self, checked):
        dir = "C:/"
        filter = "Videos (*.avi *.mp4 *.mkv *.mov *.wmv *.divx *.vidx)"
        dest = self.ui.line_videoin
        self.openDialog(dir, filter, dest, False)
        
    def locateExtractor(self, checked):
        dir = "C:/"
        filter = None
        dest = self.ui.line_ffmpeg
        self.openDialog(dir, filter, dest, True)
        
    def saveFFmpegLocation(self):
        newval = self.ui.line_ffmpeg.text()
        self.screen.config.updateConfig('ffmpeg',newval)
        self.screen.config.saveConfig(self.screen)
        
    def saveImageMagickLocation(self):
        newval = self.ui.line_im.text()
        self.screen.config.updateConfig('FILES', 'ImageMagick', newval)
        self.screen.config.saveConfig()
        
    def loadExternalSubs(self):
        dir = "C:/"
        filter = "Subtitles (*.srt *.ass *.sub)"
        dest = self.ui.cmb_subs
        self.openDialog(dir, filter, dest, False)
        
    def scanVideo(self):
        video = self.ui.line_videoin.text()
        info = self.screen.ffmpeg.getVideoInfo(video)
        subs = info.getSubtitleList()
        fps = info.getFramesPerSecond()
        
        sfps = str(fps)
        
        combo_items = self.getFpsValues(fps)
        self.ui.cmb_fps.clear()
        self.ui.cmb_fps.addItems(combo_items[1:])
        self.ui.cmb_fps.setCurrentIndex(3)
        
        self.ui.line_fps.setText(combo_items[0])
        
        sub_list = ["No Subtitles"]
        for x in range(0, len(subs)):
            index = subs[x][0]
            name = subs[x][1]
            lang = subs[x][2]
            string = "%s: %s (%s)" % (index,name,lang.upper())
            sub_list.append(string)
            
        self.ui.cmb_subs.clear()
        self.ui.cmb_subs.addItems(sub_list)
        
    def addToQueue(self):
        string = queue.convertToString(self.ui)
        self.screen.queue.addItem(string)
        self.screen.queue.listJobs()
        
    def extractFrames(self):
        dict = queue.convertToString(self.ui)
        self.screen.ffmpeg.extractFrames(dict)
        
    #Secondary functions. Not to be called by signals.
    def openDialog(self, startdir, typefilter, dest, dirmode=False):
        browser = FileDialog(self.screen, dest, self, dirmode, self.screen)
        browser.setDirectory(startdir)
        browser.setNameFilter(typefilter)
        browser.show()

    def fileSelected(self, field, file):
        # kids = self.screen.children()
        # cw = None
        # for x in range(0,len(kids)):
            # if kids[x].objectName() == "centralwidget":
                # cw = kids[x].children()
        # if cw != None:
            # for x in range(0,len(cw)):
                # if type(cw[x]) == type(QtWidgets.QTabWidget()):
                    # print(cw[x].children())
                
    
        # if type(field) == type(QtWidgets.QLineEdit()):
            # field.setText(file)
        # elif type(field) == type(QtWidgets.QComboBox()):
            # field.insertItem(0,file)
            # field.setCurrentIndex(0)
        # else:
            # print(type(field))
        pass

    def getFpsValues(self, fps):
        isrounded = self.screen.config.getKey('roundfps')
        if isrounded:
            fpslist = [str(round(fps))]
        else:
            fpslist = [str(round(fps, 2))]
            
        for x in range(25, 225, 25):
            if isrounded:
                newfps = round(fps*(x/100))
            else:
                newfps = round(fps*(x/100), 2)
            #newentry = [str(x) + "%% (%s FPS)" % str(newfps),newfps]
            newentry = str(x) + "%% (%s FPS)" % str(newfps)
            fpslist.append(newentry)
        return fpslist