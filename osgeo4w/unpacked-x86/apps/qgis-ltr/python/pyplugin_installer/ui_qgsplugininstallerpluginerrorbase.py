# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/pyplugin_installer/qgsplugininstallerpluginerrorbase.ui'
#
# Created: Sat Aug 18 07:52:34 2018
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

class Ui_QgsPluginInstallerPluginErrorDialogBase(object):
    def setupUi(self, QgsPluginInstallerPluginErrorDialogBase):
        QgsPluginInstallerPluginErrorDialogBase.setObjectName(_fromUtf8("QgsPluginInstallerPluginErrorDialogBase"))
        QgsPluginInstallerPluginErrorDialogBase.resize(521, 383)
        QgsPluginInstallerPluginErrorDialogBase.setMinimumSize(QtCore.QSize(480, 300))
        self.gridlayout = QtGui.QGridLayout(QgsPluginInstallerPluginErrorDialogBase)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(QgsPluginInstallerPluginErrorDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(QgsPluginInstallerPluginErrorDialogBase)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridlayout.addWidget(self.textBrowser, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(503, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridlayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label1 = QtGui.QLabel(QgsPluginInstallerPluginErrorDialogBase)
        self.label1.setFrameShape(QtGui.QFrame.NoFrame)
        self.label1.setFrameShadow(QtGui.QFrame.Plain)
        self.label1.setWordWrap(True)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.gridlayout.addWidget(self.label1, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QgsPluginInstallerPluginErrorDialogBase)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 6, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridlayout.addItem(spacerItem1, 0, 0, 1, 1)

        self.retranslateUi(QgsPluginInstallerPluginErrorDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QgsPluginInstallerPluginErrorDialogBase.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QgsPluginInstallerPluginErrorDialogBase.accept)
        QtCore.QMetaObject.connectSlotsByName(QgsPluginInstallerPluginErrorDialogBase)

    def retranslateUi(self, QgsPluginInstallerPluginErrorDialogBase):
        QgsPluginInstallerPluginErrorDialogBase.setWindowTitle(_translate("QgsPluginInstallerPluginErrorDialogBase", "Error loading plugin", None))
        self.label.setText(_translate("QgsPluginInstallerPluginErrorDialogBase", "The plugin seems to be invalid or have unfulfilled dependencies. It has been installed, but can\'t be loaded. If you really need this plugin, you can contact its author or <a href=\"http://lists.osgeo.org/mailman/listinfo/qgis-user\">QGIS users group</a> and try to solve the problem. If not, you can just uninstall it. Here is the error message below:", None))
        self.label1.setText(_translate("QgsPluginInstallerPluginErrorDialogBase", "Do you want to uninstall this plugin now? If you\'re unsure, probably you would like to do this.", None))

