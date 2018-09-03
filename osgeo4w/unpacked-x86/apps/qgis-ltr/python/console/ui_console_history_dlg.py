# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/console/console_history_dlg.ui'
#
# Created: Sat Aug 18 07:52:20 2018
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

class Ui_HistoryDialogPythonConsole(object):
    def setupUi(self, HistoryDialogPythonConsole):
        HistoryDialogPythonConsole.setObjectName(_fromUtf8("HistoryDialogPythonConsole"))
        HistoryDialogPythonConsole.resize(587, 375)
        self.gridLayout = QtGui.QGridLayout(HistoryDialogPythonConsole)
        self.gridLayout.setContentsMargins(2, 4, 2, 4)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(HistoryDialogPythonConsole)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)
        self.listView = QtGui.QListView(HistoryDialogPythonConsole)
        self.listView.setFrameShape(QtGui.QFrame.NoFrame)
        self.listView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 3)
        self.reloadHistory = QtGui.QPushButton(HistoryDialogPythonConsole)
        self.reloadHistory.setObjectName(_fromUtf8("reloadHistory"))
        self.gridLayout.addWidget(self.reloadHistory, 2, 0, 1, 1)
        self.saveHistory = QtGui.QPushButton(HistoryDialogPythonConsole)
        self.saveHistory.setEnabled(True)
        self.saveHistory.setObjectName(_fromUtf8("saveHistory"))
        self.gridLayout.addWidget(self.saveHistory, 2, 1, 1, 1)

        self.retranslateUi(HistoryDialogPythonConsole)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HistoryDialogPythonConsole.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HistoryDialogPythonConsole.reject)
        QtCore.QMetaObject.connectSlotsByName(HistoryDialogPythonConsole)

    def retranslateUi(self, HistoryDialogPythonConsole):
        HistoryDialogPythonConsole.setWindowTitle(_translate("HistoryDialogPythonConsole", "Dialog", None))
        self.reloadHistory.setText(_translate("HistoryDialogPythonConsole", "Reload", None))
        self.saveHistory.setText(_translate("HistoryDialogPythonConsole", "Save", None))

