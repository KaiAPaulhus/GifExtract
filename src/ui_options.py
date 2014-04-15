# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/options.ui'
#
# Created: Wed Jan  8 13:39:02 2014
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wnd_pyjiff_options(object):
    def setupUi(self, wnd_pyjiff_options):
        wnd_pyjiff_options.setObjectName("wnd_pyjiff_options")
        wnd_pyjiff_options.resize(369, 162)
        self.centralwidget = QtWidgets.QWidget(wnd_pyjiff_options)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_ffmpegfolder = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ffmpegfolder.setObjectName("line_ffmpegfolder")
        self.horizontalLayout.addWidget(self.line_ffmpegfolder)
        self.btn_ffmpegbrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ffmpegbrowse.setObjectName("btn_ffmpegbrowse")
        self.horizontalLayout.addWidget(self.btn_ffmpegbrowse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_imfolder = QtWidgets.QLineEdit(self.centralwidget)
        self.line_imfolder.setObjectName("line_imfolder")
        self.horizontalLayout_2.addWidget(self.line_imfolder)
        self.btn_imbrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_imbrowse.setObjectName("btn_imbrowse")
        self.horizontalLayout_2.addWidget(self.btn_imbrowse)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.check_fpsrounding = QtWidgets.QCheckBox(self.centralwidget)
        self.check_fpsrounding.setObjectName("check_fpsrounding")
        self.verticalLayout.addWidget(self.check_fpsrounding)
        self.check_autoscan = QtWidgets.QCheckBox(self.centralwidget)
        self.check_autoscan.setObjectName("check_autoscan")
        self.verticalLayout.addWidget(self.check_autoscan)
        wnd_pyjiff_options.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(wnd_pyjiff_options)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 369, 21))
        self.menubar.setObjectName("menubar")
        wnd_pyjiff_options.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(wnd_pyjiff_options)
        self.statusbar.setObjectName("statusbar")
        wnd_pyjiff_options.setStatusBar(self.statusbar)

        self.retranslateUi(wnd_pyjiff_options)
        QtCore.QMetaObject.connectSlotsByName(wnd_pyjiff_options)

    def retranslateUi(self, wnd_pyjiff_options):
        _translate = QtCore.QCoreApplication.translate
        wnd_pyjiff_options.setWindowTitle(_translate("wnd_pyjiff_options", "PyJiff - Preferences"))
        self.label.setText(_translate("wnd_pyjiff_options", "FFmpeg Bin Folder"))
        self.btn_ffmpegbrowse.setText(_translate("wnd_pyjiff_options", "Browse"))
        self.label_2.setText(_translate("wnd_pyjiff_options", "ImageMagick Bin Folder"))
        self.btn_imbrowse.setText(_translate("wnd_pyjiff_options", "Browse"))
        self.check_fpsrounding.setText(_translate("wnd_pyjiff_options", "Round Frames Per Second"))
        self.check_autoscan.setText(_translate("wnd_pyjiff_options", "Automatically Scan Videos"))

