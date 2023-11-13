# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(563, 311)
        about_window.setMinimumSize(QtCore.QSize(563, 311))
        about_window.setMaximumSize(QtCore.QSize(563, 311))
        self.icon = QtWidgets.QLabel(about_window)
        self.icon.setGeometry(QtCore.QRect(20, 20, 171, 171))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("icon/icon.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.title = QtWidgets.QLabel(about_window)
        self.title.setGeometry(QtCore.QRect(200, 20, 463, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.version = QtWidgets.QLabel(about_window)
        self.version.setGeometry(QtCore.QRect(200, 55, 463, 31))
        self.version.setObjectName("version")
        self.textBrowser = QtWidgets.QTextBrowser(about_window)
        self.textBrowser.setGeometry(QtCore.QRect(200, 90, 351, 201))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "About"))
        self.title.setText(_translate("about_window", "ECG Viewer"))
        self.version.setText(_translate("about_window", "VERSION PLACEHOLDER + BUILD DATE"))
        self.textBrowser.setHtml(_translate("about_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Written by Kevin Williams</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />ECG Viewer is intended to interface with the DIYECG sensor for interpreting ECG signals. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">WARNING</span>: This program was designed for educational purposes only. This program was not designed or tested for medical purposes and MUST NOT be used in place of a proper ECG. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is FREE and OPEN SOURCE licensed under GNU GPLv2.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
