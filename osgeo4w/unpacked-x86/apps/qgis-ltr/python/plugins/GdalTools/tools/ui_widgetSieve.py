# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetSieve.ui'
#
# Created: Sat Aug 18 08:04:35 2018
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
        GdalToolsWidget.resize(365, 129)
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
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.thresholdCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.thresholdCheck.setObjectName(_fromUtf8("thresholdCheck"))
        self.gridLayout.addWidget(self.thresholdCheck, 2, 0, 1, 1)
        self.thresholdSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.thresholdSpin.setMaximum(65000)
        self.thresholdSpin.setObjectName(_fromUtf8("thresholdSpin"))
        self.gridLayout.addWidget(self.thresholdSpin, 2, 1, 1, 1)
        self.connectionsCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.connectionsCheck.setObjectName(_fromUtf8("connectionsCheck"))
        self.gridLayout.addWidget(self.connectionsCheck, 3, 0, 1, 1)
        self.connectionsCombo = QtGui.QComboBox(GdalToolsWidget)
        self.connectionsCombo.setObjectName(_fromUtf8("connectionsCombo"))
        self.connectionsCombo.addItem(_fromUtf8(""))
        self.connectionsCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.connectionsCombo, 3, 1, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label.setBuddy(self.inSelector)
        self.label_2.setBuddy(self.outSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Sieve", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input file", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file", None))
        self.thresholdCheck.setText(_translate("GdalToolsWidget", "&Threshold", None))
        self.connectionsCheck.setText(_translate("GdalToolsWidget", "&Pixel connections", None))
        self.connectionsCombo.setItemText(0, _translate("GdalToolsWidget", "4", None))
        self.connectionsCombo.setItemText(1, _translate("GdalToolsWidget", "8", None))

from .inOutSelector import GdalToolsInOutSelector
