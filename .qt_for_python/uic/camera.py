# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet(u"#Dialog{\n"
"	border-image:url(:/assets/subWidget.png)\n"
"}")
        self.image = QLabel(Dialog)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(36, 18, 571, 341))
        self.buttonOk = QPushButton(Dialog)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setGeometry(QRect(380, 428, 93, 41))
        self.buttonOk.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgba(255,255,255,128); /*\u80cc\u666f\u8272*/ \n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-radius:10px; /*\u8fb9\u754c\u5706\u6ed1*/\n"
"	border-color: white;\n"
"	font: bold 20px;\n"
"	min-width:2em;\n"
"	color:white; /*\u5b57\u4f53\u989c\u8272*/\n"
"	font-family:'\u7b49\u7ebf';\n"
"	padding: 5px;\n"
"	outline:none;\n"
"\n"
"}")
        self.buttonCancel = QPushButton(Dialog)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(490, 428, 93, 40))
        self.buttonCancel.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgba(255,255,255,128); /*\u80cc\u666f\u8272*/ \n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-radius:10px; /*\u8fb9\u754c\u5706\u6ed1*/\n"
"	border-color: white;\n"
"	font: bold 20px;\n"
"	min-width:2em;\n"
"	color:white; /*\u5b57\u4f53\u989c\u8272*/\n"
"	font-family:'\u7b49\u7ebf';\n"
"	padding: 5px;\n"
"	outline:none;\n"
"\n"
"}")
        self.load_button = QPushButton(Dialog)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setGeometry(QRect(270, 428, 93, 41))
        self.load_button.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgba(255,255,255,128); /*\u80cc\u666f\u8272*/ \n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-radius:10px; /*\u8fb9\u754c\u5706\u6ed1*/\n"
"	border-color: white;\n"
"	font: bold 20px;\n"
"	min-width:2em;\n"
"	color:white; /*\u5b57\u4f53\u989c\u8272*/\n"
"	font-family:'\u7b49\u7ebf';\n"
"	padding: 5px;\n"
"	outline:none;\n"
"\n"
"}")
        self.inputName = QLineEdit(Dialog)
        self.inputName.setObjectName(u"inputName")
        self.inputName.setGeometry(QRect(130, 380, 451, 31))
        self.inputName.setStyleSheet(u"#inputName{\n"
"	background-color:rgba(255,255,255,180);\n"
"	border:none\n"
"}")
        self.labelTip = QLabel(Dialog)
        self.labelTip.setObjectName(u"labelTip")
        self.labelTip.setGeometry(QRect(30, 430, 231, 31))
        self.labelTip.setStyleSheet(u"font-weight:bold;\n"
"font-family:'\u7b49\u7ebf';\n"
"font-size:20px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.image.setText("")
        self.buttonOk.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.buttonCancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.load_button.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u4f20", None))
        self.labelTip.setText(QCoreApplication.translate("Dialog", u"tishi", None))
    # retranslateUi

