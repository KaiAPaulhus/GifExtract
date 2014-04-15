from PyQt5 import QtWidgets
import json


class JobQueue(object):
    
    def __init__(self, ui, stringlist=None):
        self.ui = ui
        if stringlist is not None:
            self.jobs = stringlist
        else:
            self.jobs = []
            
    def addItem(self, job):
        self.jobs.append(job)
        
    def removeItem(self, index):
        self.jobs[index].remove()
        
    def listJobs(self):
        self.ui.tree_queue.clear()
        for job in self.jobs:
            root = QtWidgets.QTreeWidgetItem(self.ui.tree_queue,
                                             [job["srcfile"], job["desc"]])
            sub01 = QtWidgets.QTreeWidgetItem(root, ["Start Time",
                                                     job['time_start']])
            sub02 = QtWidgets.QTreeWidgetItem(root, ["Duration",
                                                     job['duration']])
            sub03 = QtWidgets.QTreeWidgetItem(root, ["Frames/Sec.",
                                                     job['fps']])
            sub04 = QtWidgets.QTreeWidgetItem(root, "Subtitle File",
                                              job["subs"])
            
    
def addToQueue(queue, job):
    queue.addItem(job)


def convertToString(ui):
    srcfile = ui.line_videoin.text()
    time_start = ui.time_start.text()
    
    isDuration = ui.chk_vidprefdur.isChecked()
    if isDuration:
        duration = ui.time_end.text()
    else:
        #Duration = End - Start
        duration = "00:00:01"
        
    subs = ui.cmb_subs.currentText()
    fps = ui.line_fps.text()
    
    pydict = {
        "srcfile": srcfile,
        "time_start": time_start,
        "duration": duration,
        "subs": subs,
        "fps": fps,
        "desc": "description",
    }
    #string = json.dumps(pydict)
    #return string
    return pydict


def convertToJob(string):
    job = json.loads(string)
    return job