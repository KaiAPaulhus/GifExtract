# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Kyras\Google Drive\coding_projects\PyCharm\GifExtractor\data\tab_video.ui'
#
# Created: Thu Apr 17 21:14:16 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frame_tab_video(object):
    def setupUi(self, frame_tab_video):
        frame_tab_video.setObjectName("frame_tab_video")
        frame_tab_video.resize(381, 273)
        frame_tab_video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_tab_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(frame_tab_video)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(frame_tab_video)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.line_videoin = QtWidgets.QLineEdit(frame_tab_video)
        self.line_videoin.setObjectName("line_videoin")
        self.horizontalLayout_3.addWidget(self.line_videoin)
        self.btn_browsevideofile = QtWidgets.QPushButton(frame_tab_video)
        self.btn_browsevideofile.setObjectName("btn_browsevideofile")
        self.horizontalLayout_3.addWidget(self.btn_browsevideofile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(frame_tab_video)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.time_start = QtWidgets.QTimeEdit(frame_tab_video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_start.sizePolicy().hasHeightForWidth())
        self.time_start.setSizePolicy(sizePolicy)
        self.time_start.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.time_start.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.time_start.setDisplayFormat("hh:mm:ss.zzz")
        self.time_start.setTime(QtCore.QTime(0, 0, 0))
        self.time_start.setObjectName("time_start")
        self.horizontalLayout_4.addWidget(self.time_start)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_endtime = QtWidgets.QLabel(frame_tab_video)
        self.lbl_endtime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_endtime.setObjectName("lbl_endtime")
        self.horizontalLayout_5.addWidget(self.lbl_endtime)
        self.time_end = QtWidgets.QTimeEdit(frame_tab_video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_end.sizePolicy().hasHeightForWidth())
        self.time_end.setSizePolicy(sizePolicy)
        self.time_end.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.time_end.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.time_end.setTime(QtCore.QTime(0, 0, 0))
        self.time_end.setObjectName("time_end")
        self.horizontalLayout_5.addWidget(self.time_end)
        self.chk_vidprefdur = QtWidgets.QCheckBox(frame_tab_video)
        self.chk_vidprefdur.setObjectName("chk_vidprefdur")
        self.horizontalLayout_5.addWidget(self.chk_vidprefdur)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line_3 = QtWidgets.QFrame(frame_tab_video)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.btn_vidanalyze = QtWidgets.QPushButton(frame_tab_video)
        self.btn_vidanalyze.setObjectName("btn_vidanalyze")
        self.verticalLayout.addWidget(self.btn_vidanalyze)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(frame_tab_video)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.cmb_subs = QtWidgets.QComboBox(frame_tab_video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_subs.sizePolicy().hasHeightForWidth())
        self.cmb_subs.setSizePolicy(sizePolicy)
        self.cmb_subs.setObjectName("cmb_subs")
        self.horizontalLayout_6.addWidget(self.cmb_subs)
        self.btn_loadsubs = QtWidgets.QPushButton(frame_tab_video)
        self.btn_loadsubs.setObjectName("btn_loadsubs")
        self.horizontalLayout_6.addWidget(self.btn_loadsubs)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(frame_tab_video)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.line_fps = QtWidgets.QLineEdit(frame_tab_video)
        self.line_fps.setObjectName("line_fps")
        self.horizontalLayout_7.addWidget(self.line_fps)
        self.cmb_fps = QtWidgets.QComboBox(frame_tab_video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_fps.sizePolicy().hasHeightForWidth())
        self.cmb_fps.setSizePolicy(sizePolicy)
        self.cmb_fps.setModelColumn(0)
        self.cmb_fps.setObjectName("cmb_fps")
        self.horizontalLayout_7.addWidget(self.cmb_fps)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.line_4 = QtWidgets.QFrame(frame_tab_video)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_extract_queue = QtWidgets.QPushButton(frame_tab_video)
        self.btn_extract_queue.setObjectName("btn_extract_queue")
        self.horizontalLayout_10.addWidget(self.btn_extract_queue)
        self.btn_extract_exe = QtWidgets.QPushButton(frame_tab_video)
        self.btn_extract_exe.setObjectName("btn_extract_exe")
        self.horizontalLayout_10.addWidget(self.btn_extract_exe)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.progbar_videoextract = QtWidgets.QProgressBar(frame_tab_video)
        self.progbar_videoextract.setProperty("value", 0)
        self.progbar_videoextract.setTextVisible(False)
        self.progbar_videoextract.setObjectName("progbar_videoextract")
        self.verticalLayout.addWidget(self.progbar_videoextract)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(358, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.retranslateUi(frame_tab_video)
        QtCore.QMetaObject.connectSlotsByName(frame_tab_video)

    def retranslateUi(self, frame_tab_video):
        _translate = QtCore.QCoreApplication.translate
        frame_tab_video.setWindowTitle(_translate("frame_tab_video", "Frame"))
        self.label.setText(_translate("frame_tab_video", "Video File"))
        self.btn_browsevideofile.setText(_translate("frame_tab_video", "Browse"))
        self.label_3.setText(_translate("frame_tab_video", "Start Time"))
        self.lbl_endtime.setText(_translate("frame_tab_video", "End Time"))
        self.time_end.setDisplayFormat(_translate("frame_tab_video", "hh:mm:ss.zzz"))
        self.chk_vidprefdur.setText(_translate("frame_tab_video", "Use Duration Instead Of Time"))
        self.btn_vidanalyze.setText(_translate("frame_tab_video", "Analyze Video"))
        self.label_5.setText(_translate("frame_tab_video", "Subtitles"))
        self.btn_loadsubs.setText(_translate("frame_tab_video", "Load External Subs"))
        self.label_6.setText(_translate("frame_tab_video", "Frame Rate"))
        self.btn_extract_queue.setText(_translate("frame_tab_video", "Add To Queue"))
        self.btn_extract_exe.setText(_translate("frame_tab_video", "Execute"))

