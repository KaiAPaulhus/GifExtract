from PyQt5 import QtWidgets
from interface.design.ui_addtoqueue import Ui_Dialog


class RequestDescription(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def getDescription(self):
        return self.ui.line_description.text()