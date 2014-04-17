# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Kyras\Google Drive\coding_projects\PyCharm\GifExtractor\data\screen.ui'
#
# Created: Thu Apr 17 21:13:33 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wnd_gifextract(object):
    def setupUi(self, wnd_gifextract):
        wnd_gifextract.setObjectName("wnd_gifextract")
        wnd_gifextract.resize(403, 370)
        self.centralwidget = QtWidgets.QWidget(wnd_gifextract)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout.addWidget(self.tabWidget)
        wnd_gifextract.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(wnd_gifextract)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        wnd_gifextract.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(wnd_gifextract)
        self.statusbar.setObjectName("statusbar")
        wnd_gifextract.setStatusBar(self.statusbar)
        self.actionQui_t = QtWidgets.QAction(wnd_gifextract)
        self.actionQui_t.setObjectName("actionQui_t")
        self.actionQuit = QtWidgets.QAction(wnd_gifextract)
        self.actionQuit.setObjectName("actionQuit")
        self.actionClose = QtWidgets.QAction(wnd_gifextract)
        self.actionClose.setObjectName("actionClose")
        self.actionPreferences = QtWidgets.QAction(wnd_gifextract)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(wnd_gifextract)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(wnd_gifextract)

    def retranslateUi(self, wnd_gifextract):
        _translate = QtCore.QCoreApplication.translate
        wnd_gifextract.setWindowTitle(_translate("wnd_gifextract", "GifExtract"))
        self.menuFile.setTitle(_translate("wnd_gifextract", "File"))
        self.actionQui_t.setText(_translate("wnd_gifextract", "Qui_t"))
        self.actionQuit.setText(_translate("wnd_gifextract", "Quit"))
        self.actionClose.setText(_translate("wnd_gifextract", "Close"))
        self.actionPreferences.setText(_translate("wnd_gifextract", "Preferences"))

