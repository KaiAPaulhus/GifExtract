from PyQt5 import QtWidgets


#A custom file dialog, containing a reference to the field
#that it's file's text will go into.
class FileDialog(QtWidgets.QFileDialog):

    def __init__(self, parent=None, destfield=None,
                 folder=False, app=None):
        QtWidgets.QFileDialog.__init__(self, parent)

        if folder is True:
            self.setFileMode(QtWidgets.QFileDialog.Directory)
            self.setOptions(QtWidgets.QFileDialog.ShowDirsOnly)
        else:
            self.setFileMode(QtWidgets.QFileDialog.ExistingFile)

        self.fileSelected.connect(self.fileReady)
        self.destfield = destfield
        self.app = app

    def fileReady(self):
        self.fileChosen(self.app, self.destfield, self.selectedFiles()[0])
        if self.app is not None:
            if self.app.config.getKey('autoanalyze'):
                self.app.slots.scanVideo()

    @staticmethod
    def fileChosen(screen, field, file):
        kids = screen.children()
        cw = None
        for x in range(0, len(kids)):
            if kids[x].objectName() == "centralwidget":
                cw = kids[x].children()
        if cw is not None:
            for x in range(0, len(cw)):
                if isinstance(cw[x], QtWidgets.QTabWidget):
                    #print(cw[x].children())
                    pass

        if isinstance(field, QtWidgets.QLineEdit):
            field.setText(file)
        elif isinstance(field, QtWidgets.QComboBox):
            field.insertItem(0, file)
            field.setCurrentIndex(0)
        else:
            print(type(field))