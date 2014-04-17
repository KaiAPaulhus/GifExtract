import interface.tab_video
import interface.tab_queue
import interface.tab_gif


#Contains functions that will be used by widgets.        
class Slots(object):

    def __init__(self, screen):
        self.ui = screen.ui
        self.screen = screen

    #Interfaces for the gif making screen
    def createAnimatedImage(self):
        interface.tab_gif.createAnimatedImage(self.screen)

    def refreshJobList(self):
        interface.tab_gif.populateJobList(self.screen)

    def resizeCheckboxStateChanged(self, state=False):
        interface.tab_gif.resizeCheckboxStateChanged(self.screen)

    def jobSelectionChanged(self):
        interface.tab_gif.jobSelected(self.screen)

    def ratioCheckChanged(self):
        interface.tab_gif.keepProportionsCheckboxStateChanged(self.screen)

    #Interfaces from the "Extract Frames" tab.
    def loadExternalSubs(self):
        interface.tab_video.setExternalSubtitles(self.screen)

    def fpsComboChanged(self):
        interface.tab_video.updateFPSLineEdit(self.screen)

    def scanVideo(self):
        interface.tab_video.analyzeVideoFile(self.screen)

    def extractFrames(self):
        interface.tab_video.extractFramesFromVideo(self.screen)

    def locateVideo(self):
        interface.tab_video.setVideoFile(self.screen)

    def useDuration(self):
        interface.tab_video.preferDurationOverEndtime(self.screen)

    #Interfaces relating to the queue functions.
    def addToQueue(self):
        interface.tab_queue.addToQueue(self.screen)

    def executeQueueItem(self):
        interface.tab_queue.addToQueue(self.screen)

    def executeAllQueue(self):
        interface.tab_queue.addToQueue(self.screen)