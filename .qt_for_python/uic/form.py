# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 600)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet(u"#frame{\n"
"	border-image:url(:/assets/ui.png);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.listWidget = QListWidget(self.frame)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(706, 240, 311, 251))
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	background-color:transparent;\n"
"    font-size:20px;\n"
"    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif '\u7b49\u7ebf';\n"
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
"	color:#080F0;\n"
"}\n"
"QListWidget::item:selected:!active{\n"
"    background-color:3a4047 \n"
"	color:#080F0;\n"
"}\n"
"\n"
"QListWidget::item:selected:active\n"
"{\n"
"	background-color:#40444b;\n"
"	color:#050505;\n"
"}")
        self.playButton = QPushButton(self.frame)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setGeometry(QRect(92, 511, 70, 70))
        self.playButton.setStyleSheet(u"#playButton{\n"
"	background-color:transparent;\n"
"	background-image:url(:/assets/pause_idle.png);\n"
"	outline:0px;\n"
"}")
        self.nextButton = QPushButton(self.frame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(173, 525, 48, 48))
        self.nextButton.setStyleSheet(u"#nextButton{\n"
"	background-color:transparent;\n"
"	border-image:url(:/assets/next_idle.png);\n"
"	outline:0px\n"
"}\n"
"#nextButton:pressed{\n"
"	background-color:transparent;\n"
"	border-image:url(:/assets/next_selected.png)\n"
"}")
        self.prevButton = QPushButton(self.frame)
        self.prevButton.setObjectName(u"prevButton")
        self.prevButton.setGeometry(QRect(35, 524, 48, 50))
        self.prevButton.setStyleSheet(u"#prevButton{\n"
"	background-color:transparent;\n"
"	border-image:url(:/assets/prev_idle.png);\n"
"	outline:0px;\n"
"}\n"
"#prevButton:pressed{\n"
"	background-color:transparent;\n"
"	border-image:url(:/assets/prev_selected.png)\n"
"}")
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(250, 566, 400, 5))
        self.progressBar.setStyleSheet(u"QProgressBar::chunk {\n"
"   background-color: #11A4F0;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.songLabel = QLabel(self.frame)
        self.songLabel.setObjectName(u"songLabel")
        self.songLabel.setGeometry(QRect(250, 518, 461, 31))
        self.songLabel.setStyleSheet(u"#songLabel{\n"
"	font-family:'consolas','\u7b49\u7ebf';\n"
"	font-size:25px;\n"
"	color:white;\n"
"}")
        self.uploadButton = QPushButton(self.frame)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(690, 528, 48, 48))
        self.uploadButton.setStyleSheet(u"#uploadButton{\n"
"	background-color:transparent;\n"
"	border-image:url(:/assets/upload_idle.png);\n"
"	outline:0px\n"
"}\n"
"#uploadButton:pressed{\n"
"	background-color:transparent;\n"
"	border-image:url(:/assets/upload_selected.png)\n"
"}")
        self.hardwareTipLabel = QLabel(self.frame)
        self.hardwareTipLabel.setObjectName(u"hardwareTipLabel")
        self.hardwareTipLabel.setGeometry(QRect(240, 220, 231, 61))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"fuck", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"you", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.playButton.setText("")
        self.nextButton.setText("")
        self.prevButton.setText("")
        self.songLabel.setText(QCoreApplication.translate("Form", u"\u6b4c\u540d", None))
        self.uploadButton.setText("")
        self.hardwareTipLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff; font-size:20px; font-family:\u7b49\u7ebf \">\u673a\u68b0\u81c2\u51c6\u5907\u4e2d\uff0c\u8bf7\u7a0d\u540e...</span></p></body></html>", None))
    # retranslateUi

