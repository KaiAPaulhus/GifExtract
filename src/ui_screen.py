# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Kyras\Google Drive\coding_projects\PyCharm\GifExtractor\data\screen.ui'
#
# Created: Tue Apr 15 22:27:21 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wnd_pyjiff(object):
    def setupUi(self, wnd_pyjiff):
        wnd_pyjiff.setObjectName("wnd_pyjiff")
        wnd_pyjiff.resize(404, 370)
        self.centralwidget = QtWidgets.QWidget(wnd_pyjiff)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_video = QtWidgets.QWidget()
        self.tab_video.setObjectName("tab_video")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_video)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_video)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_ffmpeg = QtWidgets.QLineEdit(self.tab_video)
        self.line_ffmpeg.setObjectName("line_ffmpeg")
        self.horizontalLayout_2.addWidget(self.line_ffmpeg)
        self.btn_ffmpegbrowse = QtWidgets.QPushButton(self.tab_video)
        self.btn_ffmpegbrowse.setObjectName("btn_ffmpegbrowse")
        self.horizontalLayout_2.addWidget(self.btn_ffmpegbrowse)
        self.btn_ffmpegsave = QtWidgets.QPushButton(self.tab_video)
        self.btn_ffmpegsave.setObjectName("btn_ffmpegsave")
        self.horizontalLayout_2.addWidget(self.btn_ffmpegsave)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.tab_video)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.line_videoin = QtWidgets.QLineEdit(self.tab_video)
        self.line_videoin.setObjectName("line_videoin")
        self.horizontalLayout_3.addWidget(self.line_videoin)
        self.btn_browsevideofile = QtWidgets.QPushButton(self.tab_video)
        self.btn_browsevideofile.setObjectName("btn_browsevideofile")
        self.horizontalLayout_3.addWidget(self.btn_browsevideofile)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab_video)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.time_start = QtWidgets.QTimeEdit(self.tab_video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_start.sizePolicy().hasHeightForWidth())
        self.time_start.setSizePolicy(sizePolicy)
        self.time_start.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 5, 0)))
        self.time_start.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.time_start.setDisplayFormat("hh:mm:ss")
        self.time_start.setObjectName("time_start")
        self.horizontalLayout_4.addWidget(self.time_start)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_endtime = QtWidgets.QLabel(self.tab_video)
        self.lbl_endtime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_endtime.setObjectName("lbl_endtime")
        self.horizontalLayout_5.addWidget(self.lbl_endtime)
        spacerItem = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.time_end = QtWidgets.QTimeEdit(self.tab_video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_end.sizePolicy().hasHeightForWidth())
        self.time_end.setSizePolicy(sizePolicy)
        self.time_end.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 5)))
        self.time_end.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.time_end.setObjectName("time_end")
        self.horizontalLayout_5.addWidget(self.time_end)
        self.chk_vidprefdur = QtWidgets.QCheckBox(self.tab_video)
        self.chk_vidprefdur.setObjectName("chk_vidprefdur")
        self.horizontalLayout_5.addWidget(self.chk_vidprefdur)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.btn_vidanalyze = QtWidgets.QPushButton(self.tab_video)
        self.btn_vidanalyze.setObjectName("btn_vidanalyze")
        self.verticalLayout.addWidget(self.btn_vidanalyze)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.tab_video)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.cmb_subs = QtWidgets.QComboBox(self.tab_video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_subs.sizePolicy().hasHeightForWidth())
        self.cmb_subs.setSizePolicy(sizePolicy)
        self.cmb_subs.setObjectName("cmb_subs")
        self.horizontalLayout_6.addWidget(self.cmb_subs)
        self.btn_loadsubs = QtWidgets.QPushButton(self.tab_video)
        self.btn_loadsubs.setObjectName("btn_loadsubs")
        self.horizontalLayout_6.addWidget(self.btn_loadsubs)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.tab_video)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.line_fps = QtWidgets.QLineEdit(self.tab_video)
        self.line_fps.setObjectName("line_fps")
        self.horizontalLayout_7.addWidget(self.line_fps)
        self.cmb_fps = QtWidgets.QComboBox(self.tab_video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_fps.sizePolicy().hasHeightForWidth())
        self.cmb_fps.setSizePolicy(sizePolicy)
        self.cmb_fps.setModelColumn(0)
        self.cmb_fps.setObjectName("cmb_fps")
        self.horizontalLayout_7.addWidget(self.cmb_fps)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_extract_queue = QtWidgets.QPushButton(self.tab_video)
        self.btn_extract_queue.setObjectName("btn_extract_queue")
        self.horizontalLayout_10.addWidget(self.btn_extract_queue)
        self.btn_extract_exe = QtWidgets.QPushButton(self.tab_video)
        self.btn_extract_exe.setObjectName("btn_extract_exe")
        self.horizontalLayout_10.addWidget(self.btn_extract_exe)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.progbar_videoextract = QtWidgets.QProgressBar(self.tab_video)
        self.progbar_videoextract.setProperty("value", 0)
        self.progbar_videoextract.setTextVisible(False)
        self.progbar_videoextract.setObjectName("progbar_videoextract")
        self.verticalLayout.addWidget(self.progbar_videoextract)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_video, "")
        self.tab_gif = QtWidgets.QWidget()
        self.tab_gif.setObjectName("tab_gif")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_gif)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.tab_gif)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_15.addWidget(self.label_8)
        self.cmb_job = QtWidgets.QComboBox(self.tab_gif)
        self.cmb_job.setObjectName("cmb_job")
        self.horizontalLayout_15.addWidget(self.cmb_job)
        self.label_9 = QtWidgets.QLabel(self.tab_gif)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_15.addWidget(self.label_9)
        self.cmb_loadgifsettings = QtWidgets.QComboBox(self.tab_gif)
        self.cmb_loadgifsettings.setObjectName("cmb_loadgifsettings")
        self.horizontalLayout_15.addWidget(self.cmb_loadgifsettings)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.check_resize = QtWidgets.QCheckBox(self.tab_gif)
        self.check_resize.setObjectName("check_resize")
        self.horizontalLayout_13.addWidget(self.check_resize)
        self.check_resize_keepratio = QtWidgets.QCheckBox(self.tab_gif)
        self.check_resize_keepratio.setInputMethodHints(QtCore.Qt.ImhNone)
        self.check_resize_keepratio.setObjectName("check_resize_keepratio")
        self.horizontalLayout_13.addWidget(self.check_resize_keepratio)
        self.check_resize_percent = QtWidgets.QCheckBox(self.tab_gif)
        self.check_resize_percent.setObjectName("check_resize_percent")
        self.horizontalLayout_13.addWidget(self.check_resize_percent)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.tab_gif)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.line_resize_width = QtWidgets.QLineEdit(self.tab_gif)
        self.line_resize_width.setObjectName("line_resize_width")
        self.horizontalLayout_12.addWidget(self.line_resize_width)
        self.label_7 = QtWidgets.QLabel(self.tab_gif)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.line_resize_height = QtWidgets.QLineEdit(self.tab_gif)
        self.line_resize_height.setObjectName("line_resize_height")
        self.horizontalLayout_12.addWidget(self.line_resize_height)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.tab_gif)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.spin_delay = QtWidgets.QSpinBox(self.tab_gif)
        self.spin_delay.setObjectName("spin_delay")
        self.horizontalLayout_14.addWidget(self.spin_delay)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.check_gif_loop = QtWidgets.QCheckBox(self.tab_gif)
        self.check_gif_loop.setObjectName("check_gif_loop")
        self.verticalLayout_5.addWidget(self.check_gif_loop)
        self.check_gif_deletesource = QtWidgets.QCheckBox(self.tab_gif)
        self.check_gif_deletesource.setObjectName("check_gif_deletesource")
        self.verticalLayout_5.addWidget(self.check_gif_deletesource)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.btn_creategif = QtWidgets.QPushButton(self.tab_gif)
        self.btn_creategif.setObjectName("btn_creategif")
        self.horizontalLayout_16.addWidget(self.btn_creategif)
        self.btn_savegifsettings = QtWidgets.QPushButton(self.tab_gif)
        self.btn_savegifsettings.setObjectName("btn_savegifsettings")
        self.horizontalLayout_16.addWidget(self.btn_savegifsettings)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        spacerItem2 = QtWidgets.QSpacerItem(20, 76, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_gif, "")
        self.tab_queue = QtWidgets.QWidget()
        self.tab_queue.setObjectName("tab_queue")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_queue)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tree_queue = QtWidgets.QTreeWidget(self.tab_queue)
        self.tree_queue.setColumnCount(2)
        self.tree_queue.setObjectName("tree_queue")
        self.tree_queue.header().setDefaultSectionSize(75)
        self.verticalLayout_2.addWidget(self.tree_queue)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_queue_remove = QtWidgets.QPushButton(self.tab_queue)
        self.btn_queue_remove.setObjectName("btn_queue_remove")
        self.horizontalLayout_8.addWidget(self.btn_queue_remove)
        self.btn_queue_exe = QtWidgets.QPushButton(self.tab_queue)
        self.btn_queue_exe.setObjectName("btn_queue_exe")
        self.horizontalLayout_8.addWidget(self.btn_queue_exe)
        self.btn_queue_exeall = QtWidgets.QPushButton(self.tab_queue)
        self.btn_queue_exeall.setObjectName("btn_queue_exeall")
        self.horizontalLayout_8.addWidget(self.btn_queue_exeall)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_queue, "")
        self.tab_console = QtWidgets.QWidget()
        self.tab_console.setObjectName("tab_console")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_console)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.text_console = QtWidgets.QTextBrowser(self.tab_console)
        self.text_console.setObjectName("text_console")
        self.horizontalLayout_11.addWidget(self.text_console)
        self.tabWidget.addTab(self.tab_console, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        wnd_pyjiff.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(wnd_pyjiff)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        wnd_pyjiff.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(wnd_pyjiff)
        self.statusbar.setObjectName("statusbar")
        wnd_pyjiff.setStatusBar(self.statusbar)
        self.actionQui_t = QtWidgets.QAction(wnd_pyjiff)
        self.actionQui_t.setObjectName("actionQui_t")
        self.actionQuit = QtWidgets.QAction(wnd_pyjiff)
        self.actionQuit.setObjectName("actionQuit")
        self.actionClose = QtWidgets.QAction(wnd_pyjiff)
        self.actionClose.setObjectName("actionClose")
        self.actionPreferences = QtWidgets.QAction(wnd_pyjiff)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(wnd_pyjiff)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wnd_pyjiff)
        wnd_pyjiff.setTabOrder(self.tabWidget, self.line_ffmpeg)
        wnd_pyjiff.setTabOrder(self.line_ffmpeg, self.btn_ffmpegbrowse)
        wnd_pyjiff.setTabOrder(self.btn_ffmpegbrowse, self.btn_ffmpegsave)
        wnd_pyjiff.setTabOrder(self.btn_ffmpegsave, self.line_videoin)
        wnd_pyjiff.setTabOrder(self.line_videoin, self.btn_browsevideofile)
        wnd_pyjiff.setTabOrder(self.btn_browsevideofile, self.time_start)
        wnd_pyjiff.setTabOrder(self.time_start, self.time_end)
        wnd_pyjiff.setTabOrder(self.time_end, self.chk_vidprefdur)
        wnd_pyjiff.setTabOrder(self.chk_vidprefdur, self.cmb_subs)
        wnd_pyjiff.setTabOrder(self.cmb_subs, self.btn_loadsubs)

    def retranslateUi(self, wnd_pyjiff):
        _translate = QtCore.QCoreApplication.translate
        wnd_pyjiff.setWindowTitle(_translate("wnd_pyjiff", "PyJiff"))
        self.label_2.setText(_translate("wnd_pyjiff", "FFmpeg Bin Folder"))
        self.btn_ffmpegbrowse.setText(_translate("wnd_pyjiff", "Browse"))
        self.btn_ffmpegsave.setText(_translate("wnd_pyjiff", "Save"))
        self.label.setText(_translate("wnd_pyjiff", "Video File"))
        self.btn_browsevideofile.setText(_translate("wnd_pyjiff", "Browse"))
        self.label_3.setText(_translate("wnd_pyjiff", "Start Time"))
        self.lbl_endtime.setText(_translate("wnd_pyjiff", "End Time"))
        self.time_end.setDisplayFormat(_translate("wnd_pyjiff", "hh:mm:ss"))
        self.chk_vidprefdur.setText(_translate("wnd_pyjiff", "Use Duration Instead Of Time"))
        self.btn_vidanalyze.setText(_translate("wnd_pyjiff", "Analyze Video"))
        self.label_5.setText(_translate("wnd_pyjiff", "Subtitles"))
        self.btn_loadsubs.setText(_translate("wnd_pyjiff", "Load External Subs"))
        self.label_6.setText(_translate("wnd_pyjiff", "Frame Rate"))
        self.btn_extract_queue.setText(_translate("wnd_pyjiff", "Add To Queue"))
        self.btn_extract_exe.setText(_translate("wnd_pyjiff", "Execute"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_video), _translate("wnd_pyjiff", "Extract Frames"))
        self.label_8.setText(_translate("wnd_pyjiff", "Job"))
        self.label_9.setText(_translate("wnd_pyjiff", "Load Settings"))
        self.check_resize.setText(_translate("wnd_pyjiff", "Resize"))
        self.check_resize_keepratio.setText(_translate("wnd_pyjiff", "Maintain Proportions"))
        self.check_resize_percent.setText(_translate("wnd_pyjiff", "As Percentage"))
        self.label_4.setText(_translate("wnd_pyjiff", "Width"))
        self.label_7.setText(_translate("wnd_pyjiff", "Height"))
        self.label_10.setText(_translate("wnd_pyjiff", "Delay"))
        self.check_gif_loop.setText(_translate("wnd_pyjiff", "Loop"))
        self.check_gif_deletesource.setText(_translate("wnd_pyjiff", "Delete Source Images"))
        self.btn_creategif.setText(_translate("wnd_pyjiff", "Create Gif"))
        self.btn_savegifsettings.setText(_translate("wnd_pyjiff", "Save Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gif), _translate("wnd_pyjiff", "Create Gifs"))
        self.tree_queue.headerItem().setText(0, _translate("wnd_pyjiff", "Property"))
        self.tree_queue.headerItem().setText(1, _translate("wnd_pyjiff", "Value"))
        self.btn_queue_remove.setText(_translate("wnd_pyjiff", "Remove From Queue"))
        self.btn_queue_exe.setText(_translate("wnd_pyjiff", "Execute Job"))
        self.btn_queue_exeall.setText(_translate("wnd_pyjiff", "Execute All Jobs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_queue), _translate("wnd_pyjiff", "Job Queue"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_console), _translate("wnd_pyjiff", "Console"))
        self.menuFile.setTitle(_translate("wnd_pyjiff", "File"))
        self.actionQui_t.setText(_translate("wnd_pyjiff", "Qui_t"))
        self.actionQuit.setText(_translate("wnd_pyjiff", "Quit"))
        self.actionClose.setText(_translate("wnd_pyjiff", "Close"))
        self.actionPreferences.setText(_translate("wnd_pyjiff", "Preferences"))

