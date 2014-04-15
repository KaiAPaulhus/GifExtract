class Tester(object):
    
    def __init__(self, app):
        self.app = app
        
    def runTests(self):
        self.analyzeVideo()
        self.loadExternalSubs()
        
    def analyzeVideo(self):
        self.app.ui.line_videoin.setText("C:/test/vid.mp4")
        self.app.slots.scanVideo()
        
    def loadExternalSubs(self):
        self.app.slots.fileSelected(self.app.ui.cmb_subs, "C:/test/subs.ass")