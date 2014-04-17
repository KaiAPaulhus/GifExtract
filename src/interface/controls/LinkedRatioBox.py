from PyQt5 import QtWidgets, QtGui


class LinkedRatioBox(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.linked = False
        self.partner = QtWidgets.QLineEdit()
        self.originalheight = 1
        self.originalwidth = 1
        self.mode = "WIDTH"
        self.setValidator(QtGui.QIntValidator(1, 99999, self))
        self.setEnabled(False)
        self.editingFinished.connect(self.updatePartner)

    def setPartner(self, buddy):
        self.partner = buddy

    def setOriginalSize(self, width=1, height=0):
        self.originalheight = height
        self.originalwidth = width

    def setMode(self, mode):
        if mode is not "WIDTH" and mode is not "HEIGHT":
            #TODO: Raise Error
            print("Error, invalid mode in LinkedRatioBox::setMode")
        else:
            self.mode = mode

    def setLinked(self, linked):
        self.linked = linked

    def updatePartner(self):
        if self.linked:
            text = self.text()
            currval = int(text)
            partnerval = self.calculatePartnerValue(currval)
            self.partner.setText(str(partnerval))

    def calculatePartnerValue(self, currnum):
        if self.mode == "WIDTH":
            base = currnum / self.originalwidth
            final = base * self.originalheight
            return int(round(final))
        elif self.mode == "HEIGHT":
            base = currnum / self.originalheight
            final = base * self.originalwidth
            return int(round(final))