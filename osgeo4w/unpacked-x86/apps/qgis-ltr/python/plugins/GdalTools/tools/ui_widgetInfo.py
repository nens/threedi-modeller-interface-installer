# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetInfo.ui'
#
# Created: Sat Aug 18 08:04:33 2018
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

class Ui_GdalToolsWidget(object):
    def setupUi(self, GdalToolsWidget):
        GdalToolsWidget.setObjectName(_fromUtf8("GdalToolsWidget"))
        GdalToolsWidget.resize(426, 292)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GdalToolsWidget.sizePolicy().hasHeightForWidth())
        GdalToolsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(GdalToolsWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(GdalToolsWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.rasterInfoList = QtGui.QListWidget(GdalToolsWidget)
        self.rasterInfoList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.rasterInfoList.setAlternatingRowColors(True)
        self.rasterInfoList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.rasterInfoList.setObjectName(_fromUtf8("rasterInfoList"))
        self.verticalLayout.addWidget(self.rasterInfoList)
        self.suppressGCPCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.suppressGCPCheck.setObjectName(_fromUtf8("suppressGCPCheck"))
        self.verticalLayout.addWidget(self.suppressGCPCheck)
        self.suppressMDCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.suppressMDCheck.setObjectName(_fromUtf8("suppressMDCheck"))
        self.verticalLayout.addWidget(self.suppressMDCheck)
        self.label.setBuddy(self.inSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Info", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input file", None))
        self.label_2.setText(_translate("GdalToolsWidget", "Raster info", None))
        self.suppressGCPCheck.setText(_translate("GdalToolsWidget", "Suppress GCP printing", None))
        self.suppressMDCheck.setText(_translate("GdalToolsWidget", "Suppress metadata printing", None))

from .inOutSelector import GdalToolsInOutSelector
