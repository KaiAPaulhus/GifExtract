from PyQt5 import QtWidgets
import json
from ui_addtoqueue import Ui_Dialog


class RequestDescription(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def getDescription(self):
        return self.ui.line_description.text()


class JobQueue(object):
    
    def __init__(self, ui, stringlist=None):
        self.ui = ui
        if stringlist is not None:
            self.jobs = stringlist
        else:
            self.jobs = []
            
    def addItem(self, job):
        if self.checkUnique(job["desc"]):
            self.jobs.append(job)
            return True
        else:
            return False
        
    def removeItem(self, index):
        self.jobs[index].remove()

    def checkUnique(self, key):
        for job in self.jobs:
            if job["desc"] == key:
                return False
        return True

    def listJobs(self):
        self.ui.tree_queue.clear()
        for job in self.jobs:
            root = QtWidgets.QTreeWidgetItem(self.ui.tree_queue,
                                             [job["srcfile"], job["desc"]])
            sub01 = QtWidgets.QTreeWidgetItem(root, ["Start Time",
                                                     job['time_start']])
            sub02 = QtWidgets.QTreeWidgetItem(root, ["Duration",
                                                     job['duration']])
            sub03 = QtWidgets.QTreeWidgetItem(root, ["Frames/Sec",
                                                     job['fps']])
            sub04 = QtWidgets.QTreeWidgetItem(root, ["Subtitles",
                                              job["subs"]])

    def getJobByDescription(self, desc):
        for job in self.jobs:
            print(job["desc"], desc)
            if job["desc"] == desc:
                print(type(job))
                return job

    def getJobs(self):
        return self.jobs


def addToQueue(queue, job):
    queue.addItem(job)


def convertToString(screen):
    srcfile = screen.ui.line_videoin.text()
    time_start = screen.ui.time_start.text()
    
    isDuration = screen.ui.chk_vidprefdur.isChecked()
    if isDuration:
        duration = screen.ui.time_end.text()
    else:
        #TODO:Calculate duration
        duration = "00:00:01"
        
    subs = screen.ui.cmb_subs.currentText()
    fps = screen.ui.line_fps.text()

    popup = RequestDescription(screen)
    result = popup.exec()
    print(result)
    if result is 1:
        description = popup.getDescription()
        pydict = {
            "srcfile": srcfile,
            "time_start": time_start,
            "duration": duration,
            "subs": subs,
            "fps": fps,
            "desc": description,
        }
        return pydict
    return None


def convertToJob(string):
    job = json.loads(string)
    return job