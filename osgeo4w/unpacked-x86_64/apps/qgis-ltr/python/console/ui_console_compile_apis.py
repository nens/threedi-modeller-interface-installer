# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/console/console_compile_apis.ui'
#
# Created: Sat Jun 23 07:59:27 2018
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_APIsDialogPythonConsole(object):
    def setupUi(self, APIsDialogPythonConsole):
        APIsDialogPythonConsole.setObjectName(_fromUtf8("APIsDialogPythonConsole"))
        APIsDialogPythonConsole.resize(320, 280)
        APIsDialogPythonConsole.setMinimumSize(QtCore.QSize(320, 0))
        APIsDialogPythonConsole.setWindowTitle(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(APIsDialogPythonConsole)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(APIsDialogPythonConsole)
        self.label.setMinimumSize(QtCore.QSize(320, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtGui.QProgressBar(APIsDialogPythonConsole)
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.plainTextEdit = QtGui.QPlainTextEdit(APIsDialogPythonConsole)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.textEdit_Qsci = Qsci.QsciScintilla(APIsDialogPythonConsole)
        self.textEdit_Qsci.setToolTip(_fromUtf8(""))
        self.textEdit_Qsci.setWhatsThis(_fromUtf8(""))
        self.textEdit_Qsci.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_Qsci.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_Qsci.setObjectName(_fromUtf8("textEdit_Qsci"))
        self.verticalLayout.addWidget(self.textEdit_Qsci)
        self.buttonBox = QtGui.QDialogButtonBox(APIsDialogPythonConsole)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(APIsDialogPythonConsole)
        QtCore.QMetaObject.connectSlotsByName(APIsDialogPythonConsole)

    def retranslateUi(self, APIsDialogPythonConsole):
        self.label.setText(_translate("APIsDialogPythonConsole", "Generating prepared API file (please wait)...", None))

from PyQt4 import Qsci
