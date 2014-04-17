# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Kyras\Google Drive\coding_projects\PyCharm\GifExtractor\data\tab_queue.ui'
#
# Created: Thu Apr 17 17:55:23 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frame_tab_queue(object):
    def setupUi(self, frame_tab_queue):
        frame_tab_queue.setObjectName("frame_tab_queue")
        frame_tab_queue.resize(306, 124)
        frame_tab_queue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_tab_queue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(frame_tab_queue)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tree_queue = QtWidgets.QTreeWidget(frame_tab_queue)
        self.tree_queue.setColumnCount(2)
        self.tree_queue.setObjectName("tree_queue")
        font = QtGui.QFont()
        font.setItalic(True)
        self.tree_queue.headerItem().setFont(0, font)
        self.tree_queue.headerItem().setTextAlignment(1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setItalic(True)
        self.tree_queue.headerItem().setFont(1, font)
        self.tree_queue.header().setDefaultSectionSize(75)
        self.verticalLayout_2.addWidget(self.tree_queue)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_queue_remove = QtWidgets.QPushButton(frame_tab_queue)
        self.btn_queue_remove.setObjectName("btn_queue_remove")
        self.horizontalLayout_8.addWidget(self.btn_queue_remove)
        self.btn_queue_exe = QtWidgets.QPushButton(frame_tab_queue)
        self.btn_queue_exe.setObjectName("btn_queue_exe")
        self.horizontalLayout_8.addWidget(self.btn_queue_exe)
        self.btn_queue_exeall = QtWidgets.QPushButton(frame_tab_queue)
        self.btn_queue_exeall.setObjectName("btn_queue_exeall")
        self.horizontalLayout_8.addWidget(self.btn_queue_exeall)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(frame_tab_queue)
        QtCore.QMetaObject.connectSlotsByName(frame_tab_queue)

    def retranslateUi(self, frame_tab_queue):
        _translate = QtCore.QCoreApplication.translate
        frame_tab_queue.setWindowTitle(_translate("frame_tab_queue", "Frame"))
        self.tree_queue.setSortingEnabled(True)
        self.tree_queue.headerItem().setText(0, _translate("frame_tab_queue", "Job Name"))
        self.tree_queue.headerItem().setText(1, _translate("frame_tab_queue", "Properties"))
        self.btn_queue_remove.setText(_translate("frame_tab_queue", "Remove From Queue"))
        self.btn_queue_exe.setText(_translate("frame_tab_queue", "Execute Job"))
        self.btn_queue_exeall.setText(_translate("frame_tab_queue", "Execute All Jobs"))

