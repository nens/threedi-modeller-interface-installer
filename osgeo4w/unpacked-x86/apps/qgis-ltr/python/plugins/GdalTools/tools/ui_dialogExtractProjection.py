# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/dialogExtractProjection.ui'
#
# Created: Sat Aug 18 08:04:31 2018
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

class Ui_GdalToolsDialog(object):
    def setupUi(self, GdalToolsDialog):
        GdalToolsDialog.setObjectName(_fromUtf8("GdalToolsDialog"))
        GdalToolsDialog.resize(400, 192)
        self.verticalLayout = QtGui.QVBoxLayout(GdalToolsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.batchCheck = QtGui.QCheckBox(GdalToolsDialog)
        self.batchCheck.setObjectName(_fromUtf8("batchCheck"))
        self.verticalLayout.addWidget(self.batchCheck)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(GdalToolsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.inSelector = GdalToolsInOutSelector(GdalToolsDialog)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.horizontalLayout.addWidget(self.inSelector)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.recurseCheck = QtGui.QCheckBox(GdalToolsDialog)
        self.recurseCheck.setObjectName(_fromUtf8("recurseCheck"))
        self.verticalLayout.addWidget(self.recurseCheck)
        self.prjCheck = QtGui.QCheckBox(GdalToolsDialog)
        self.prjCheck.setObjectName(_fromUtf8("prjCheck"))
        self.verticalLayout.addWidget(self.prjCheck)
        self.progressBar = QtGui.QProgressBar(GdalToolsDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.buttonBox = QtGui.QDialogButtonBox(GdalToolsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.inSelector)

        self.retranslateUi(GdalToolsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GdalToolsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GdalToolsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsDialog)

    def retranslateUi(self, GdalToolsDialog):
        GdalToolsDialog.setWindowTitle(_translate("GdalToolsDialog", "Extract projection", None))
        self.batchCheck.setText(_translate("GdalToolsDialog", "Batch mode (for processing whole directory)", None))
        self.label.setText(_translate("GdalToolsDialog", "&Input file", None))
        self.recurseCheck.setText(_translate("GdalToolsDialog", "Recurse subdirectories", None))
        self.prjCheck.setText(_translate("GdalToolsDialog", "Create also prj file", None))

from .inOutSelector import GdalToolsInOutSelector
