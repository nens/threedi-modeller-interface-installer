# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/dialogBase.ui'
#
# Created: Sat Jun 23 08:09:31 2018
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

class Ui_GdalToolsDialog(object):
    def setupUi(self, GdalToolsDialog):
        GdalToolsDialog.setObjectName(_fromUtf8("GdalToolsDialog"))
        GdalToolsDialog.resize(285, 179)
        self.verticalLayout_2 = QtGui.QVBoxLayout(GdalToolsDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.controlsWidget = QtGui.QWidget(GdalToolsDialog)
        self.controlsWidget.setObjectName(_fromUtf8("controlsWidget"))
        self.pluginLayout = QtGui.QVBoxLayout(self.controlsWidget)
        self.pluginLayout.setMargin(0)
        self.pluginLayout.setObjectName(_fromUtf8("pluginLayout"))
        self.verticalLayout_2.addWidget(self.controlsWidget)
        self.loadCheckBox = QtGui.QCheckBox(GdalToolsDialog)
        self.loadCheckBox.setChecked(True)
        self.loadCheckBox.setObjectName(_fromUtf8("loadCheckBox"))
        self.verticalLayout_2.addWidget(self.loadCheckBox)
        self.commandWidget = QtGui.QWidget(GdalToolsDialog)
        self.commandWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.commandWidget.setObjectName(_fromUtf8("commandWidget"))
        self.gridLayout = QtGui.QGridLayout(self.commandWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEditCommand = QtGui.QPlainTextEdit(self.commandWidget)
        self.textEditCommand.setMinimumSize(QtCore.QSize(0, 0))
        self.textEditCommand.setReadOnly(True)
        self.textEditCommand.setObjectName(_fromUtf8("textEditCommand"))
        self.gridLayout.addWidget(self.textEditCommand, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.editCmdBtn = QtGui.QToolButton(self.commandWidget)
        self.editCmdBtn.setCheckable(True)
        self.editCmdBtn.setObjectName(_fromUtf8("editCmdBtn"))
        self.verticalLayout.addWidget(self.editCmdBtn)
        self.resetCmdBtn = QtGui.QToolButton(self.commandWidget)
        self.resetCmdBtn.setEnabled(False)
        self.resetCmdBtn.setObjectName(_fromUtf8("resetCmdBtn"))
        self.verticalLayout.addWidget(self.resetCmdBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.commandWidget)
        self.buttonBox = QtGui.QDialogButtonBox(GdalToolsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(GdalToolsDialog)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsDialog)

    def retranslateUi(self, GdalToolsDialog):
        GdalToolsDialog.setWindowTitle(_translate("GdalToolsDialog", "Dialog", None))
        self.loadCheckBox.setText(_translate("GdalToolsDialog", "&Load into canvas when finished", None))
        self.editCmdBtn.setToolTip(_translate("GdalToolsDialog", "Edit", None))
        self.editCmdBtn.setText(_translate("GdalToolsDialog", "Edit", None))
        self.resetCmdBtn.setToolTip(_translate("GdalToolsDialog", "Reset", None))
        self.resetCmdBtn.setText(_translate("GdalToolsDialog", "Reset", None))

