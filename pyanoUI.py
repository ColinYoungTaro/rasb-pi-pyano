# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet("#frame{\n"
"    border-image:url(:/assets/ui.png);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(706, 240, 311, 251))
        self.listWidget.setStyleSheet("QListWidget {\n"
"    background-color:transparent;\n"
"    font-size:20px;\n"
"    font-family: \'Franklin Gothic Medium\', \'Arial Narrow\', Arial, sans-serif \'等线\';\n"
"    color: #ffffff;\n"
"    outline: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding-top: 10px;\n"
"    padding-bottom: 10px;\n"
"}\n"
"\n"
"QListWidget::item:hover{\n"
"    background-color:3a4047 \n"
"    color:#080F0;\n"
"}\n"
"QListWidget::item:selected:!active{\n"
"    background-color:3a4047 \n"
"    color:#080F0;\n"
"}\n"
"\n"
"QListWidget::item:selected:active\n"
"{\n"
"    background-color:#40444b;\n"
"    color:#050505;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.playButton = QtWidgets.QPushButton(self.frame)
        self.playButton.setGeometry(QtCore.QRect(92, 511, 70, 70))
        self.playButton.setStyleSheet("#playButton{\n"
"    background-color:transparent;\n"
"    background-image:url(:/assets/pause_idle.png);\n"
"    outline:0px;\n"
"}")
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        self.nextButton = QtWidgets.QPushButton(self.frame)
        self.nextButton.setGeometry(QtCore.QRect(173, 525, 48, 48))
        self.nextButton.setStyleSheet("#nextButton{\n"
"    background-color:transparent;\n"
"    border-image:url(:/assets/next_idle.png);\n"
"    outline:0px\n"
"}\n"
"#nextButton:pressed{\n"
"    background-color:transparent;\n"
"    border-image:url(:/assets/next_selected.png)\n"
"}")
        self.nextButton.setText("")
        self.nextButton.setObjectName("nextButton")
        self.prevButton = QtWidgets.QPushButton(self.frame)
        self.prevButton.setGeometry(QtCore.QRect(35, 524, 48, 50))
        self.prevButton.setStyleSheet("#prevButton{\n"
"    background-color:transparent;\n"
"    border-image:url(:/assets/prev_idle.png);\n"
"    outline:0px;\n"
"}\n"
"#prevButton:pressed{\n"
"    background-color:transparent;\n"
"    border-image:url(:/assets/prev_selected.png)\n"
"}")
        self.prevButton.setText("")
        self.prevButton.setObjectName("prevButton")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(250, 566, 400, 5))
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
"   background-color: #11A4F0;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.songLabel = QtWidgets.QLabel(self.frame)
        self.songLabel.setGeometry(QtCore.QRect(250, 518, 461, 31))
        self.songLabel.setStyleSheet("#songLabel{\n"
"    font-family:\'consolas\',\'等线\';\n"
"    font-size:25px;\n"
"    color:white;\n"
"}")
        self.songLabel.setObjectName("songLabel")
        self.uploadButton = QtWidgets.QPushButton(self.frame)
        self.uploadButton.setGeometry(QtCore.QRect(690, 528, 48, 48))
        self.uploadButton.setStyleSheet("#uploadButton{\n"
"    background-color:transparent;\n"
"    border-image:url(:/assets/upload_idle.png);\n"
"    outline:0px\n"
"}\n"
"#uploadButton:pressed{\n"
"    background-color:transparent;\n"
"    border-image:url(:/assets/upload_selected.png)\n"
"}")
        self.uploadButton.setText("")
        self.uploadButton.setObjectName("uploadButton")
        self.hardwareTipLabel = QtWidgets.QLabel(self.frame)
        self.hardwareTipLabel.setGeometry(QtCore.QRect(240, 220, 231, 61))
        self.hardwareTipLabel.setObjectName("hardwareTipLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "fuck"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "you"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.songLabel.setText(_translate("Form", "歌名"))
        self.hardwareTipLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff; font-size:20px; font-family:等线 \">机械臂准备中，请稍后...</span></p></body></html>"))
