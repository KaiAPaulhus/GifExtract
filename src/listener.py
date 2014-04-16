import queue
import interface_video
import interface_giffer


#Contains functions that will be used by widgets.        
class Slots(object):

    def __init__(self, screen):
        self.ui = screen.ui
        self.screen = screen

    #Interfaces for the gif making screen
    def createAnimatedImage(self):
        interface_giffer.createAnimatedImage(self.screen)

    def refreshJobList(self):
        interface_giffer.populateJobList(self.screen)

    def resizeCheckboxStateChanged(self, state=False):
        interface_giffer.resizeCheckboxStateChanged(self.screen)

    def jobSelectionChanged(self):
        interface_giffer.jobSelected(self.screen)

    def ratioCheckChanged(self):
        interface_giffer.keepProportionsCheckboxStateChanged(self.screen)

    #Interfaces from the options screen.
    def saveFFmpegLocation(self):
        newval = self.ui.line_ffmpeg.text()
        self.screen.config.updateConfig('ffmpeg', newval)
        self.screen.config.saveConfig(self.screen)
        
    def saveImageMagickLocation(self):
        newval = self.ui.line_im.text()
        self.screen.config.updateConfig('FILES', 'ImageMagick', newval)
        self.screen.config.saveConfig()

    #Interfaces from the "Extract Frames" tab.
    def loadExternalSubs(self):
        interface_video.setExternalSubtitles(self.screen)

    def fpsComboChanged(self):
        interface_video.updateFPSLineEdit(self.screen)

    def scanVideo(self):
        interface_video.analyzeVideoFile(self.screen)

    def extractFrames(self):
        interface_video.extractFramesFromVideo(self.screen)

    def locateVideo(self):
        interface_video.setVideoFile(self.screen)

    def useDuration(self):
        interface_video.preferDurationOverEndtime(self.screen)

    def locateExtractor(self):
        interface_video.setExtractorLocations(self.screen)

    #Interfaces relating to the queue functions.
    def addToQueue(self):
        string = queue.convertToString(self.screen)
        if string is not None:
            result = self.screen.queue.addItem(string)
            if not result:
                #TODO: Properly handle error.
                print("Error adding to queue. Non-unique description")
            self.screen.queue.listJobs()

    def executeQueueItem(self):
        curritem = self.ui.tree_queue.currentItem()
        if curritem is not None:
            text = curritem.text(1)
            job = self.screen.queue.getJobByDescription(text)
            if job is not None:
                self.screen.ffmpeg.extractFrames(job)

    def executeAllQueue(self):
        for item in self.screen.queue.getJobs():
            self.screen.ffmpeg.extractFrames(item)