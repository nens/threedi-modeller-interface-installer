# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetNearBlack.ui'
#
# Created: Sat Jun 23 08:09:33 2018
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

class Ui_GdalToolsWidget(object):
    def setupUi(self, GdalToolsWidget):
        GdalToolsWidget.setObjectName(_fromUtf8("GdalToolsWidget"))
        GdalToolsWidget.resize(443, 125)
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
        self.nearCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.nearCheck.setObjectName(_fromUtf8("nearCheck"))
        self.gridLayout.addWidget(self.nearCheck, 2, 0, 1, 1)
        self.nearSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.nearSpin.setMaximum(255)
        self.nearSpin.setObjectName(_fromUtf8("nearSpin"))
        self.gridLayout.addWidget(self.nearSpin, 2, 1, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.whiteCheckBox = QtGui.QCheckBox(GdalToolsWidget)
        self.whiteCheckBox.setObjectName(_fromUtf8("whiteCheckBox"))
        self.verticalLayout.addWidget(self.whiteCheckBox)
        self.label.setBuddy(self.inSelector)
        self.label_2.setBuddy(self.outSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Near Black", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input file", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file", None))
        self.nearCheck.setText(_translate("GdalToolsWidget", "How &far from black (or white)", None))
        self.whiteCheckBox.setText(_translate("GdalToolsWidget", "Search for nearly &white (255) pixels instead of black ones", None))

from .inOutSelector import GdalToolsInOutSelector
