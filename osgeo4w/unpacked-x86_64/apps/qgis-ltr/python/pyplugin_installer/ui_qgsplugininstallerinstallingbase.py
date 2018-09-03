# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/pyplugin_installer/qgsplugininstallerinstallingbase.ui'
#
# Created: Sat Jun 23 07:59:43 2018
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

class Ui_QgsPluginInstallerInstallingDialogBase(object):
    def setupUi(self, QgsPluginInstallerInstallingDialogBase):
        QgsPluginInstallerInstallingDialogBase.setObjectName(_fromUtf8("QgsPluginInstallerInstallingDialogBase"))
        QgsPluginInstallerInstallingDialogBase.resize(520, 175)
        self.gridlayout = QtGui.QGridLayout(QgsPluginInstallerInstallingDialogBase)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        spacerItem = QtGui.QSpacerItem(502, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.gridlayout.addItem(spacerItem, 0, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(QgsPluginInstallerInstallingDialogBase)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.labelName = QtGui.QLabel(QgsPluginInstallerInstallingDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)
        self.labelName.setText(_fromUtf8(""))
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.hboxlayout.addWidget(self.labelName)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.labelState = QtGui.QLabel(QgsPluginInstallerInstallingDialogBase)
        self.labelState.setObjectName(_fromUtf8("labelState"))
        self.gridlayout.addWidget(self.labelState, 2, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(QgsPluginInstallerInstallingDialogBase)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridlayout.addWidget(self.progressBar, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(502, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridlayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QgsPluginInstallerInstallingDialogBase)
        self.buttonBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.retranslateUi(QgsPluginInstallerInstallingDialogBase)
        QtCore.QMetaObject.connectSlotsByName(QgsPluginInstallerInstallingDialogBase)

    def retranslateUi(self, QgsPluginInstallerInstallingDialogBase):
        QgsPluginInstallerInstallingDialogBase.setWindowTitle(_translate("QgsPluginInstallerInstallingDialogBase", "QGIS Python Plugin Installer", None))
        self.label.setText(_translate("QgsPluginInstallerInstallingDialogBase", "Installing plugin:", None))
        self.labelState.setText(_translate("QgsPluginInstallerInstallingDialogBase", "Connecting...", None))

