# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/dialogAbout.ui'
#
# Created: Sat Aug 18 08:04:30 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GdalToolsAboutDialog(object):
    def setupUi(self, GdalToolsAboutDialog):
        GdalToolsAboutDialog.setObjectName(_fromUtf8("GdalToolsAboutDialog"))
        GdalToolsAboutDialog.resize(434, 300)
        self.verticalLayout = QtGui.QVBoxLayout(GdalToolsAboutDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(GdalToolsAboutDialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lblVersion = QtGui.QLabel(GdalToolsAboutDialog)
        self.lblVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVersion.setObjectName(_fromUtf8("lblVersion"))
        self.verticalLayout.addWidget(self.lblVersion)
        self.textEdit = QtGui.QTextEdit(GdalToolsAboutDialog)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textEdit.setPalette(palette)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnWeb = QtGui.QPushButton(GdalToolsAboutDialog)
        self.btnWeb.setObjectName(_fromUtf8("btnWeb"))
        self.horizontalLayout.addWidget(self.btnWeb)
        self.btnClose = QtGui.QPushButton(GdalToolsAboutDialog)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(GdalToolsAboutDialog)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL(_fromUtf8("clicked()")), GdalToolsAboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsAboutDialog)

    def retranslateUi(self, GdalToolsAboutDialog):
        GdalToolsAboutDialog.setWindowTitle(_translate("GdalToolsAboutDialog", "About Gdal Tools", None))
        self.label_2.setText(_translate("GdalToolsAboutDialog", "GDAL Tools", None))
        self.lblVersion.setText(_translate("GdalToolsAboutDialog", "Version x.x-xxxxxx", None))
        self.textEdit.setHtml(_translate("GdalToolsAboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"></p></body></html>", None))
        self.btnWeb.setText(_translate("GdalToolsAboutDialog", "Web", None))
        self.btnClose.setText(_translate("GdalToolsAboutDialog", "Close", None))

