# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetConvert.ui'
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
        GdalToolsWidget.resize(356, 191)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GdalToolsWidget.sizePolicy().hasHeightForWidth())
        GdalToolsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(GdalToolsWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.batchCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.batchCheck.setObjectName(_fromUtf8("batchCheck"))
        self.verticalLayout.addWidget(self.batchCheck)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(GdalToolsWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.colorsCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.colorsCheck.setObjectName(_fromUtf8("colorsCheck"))
        self.gridLayout.addWidget(self.colorsCheck, 2, 0, 1, 1)
        self.colorsSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.colorsSpin.setMinimum(2)
        self.colorsSpin.setMaximum(256)
        self.colorsSpin.setObjectName(_fromUtf8("colorsSpin"))
        self.gridLayout.addWidget(self.colorsSpin, 2, 1, 1, 1)
        self.bandSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.bandSpin.setMinimum(1)
        self.bandSpin.setMaximum(256)
        self.bandSpin.setObjectName(_fromUtf8("bandSpin"))
        self.gridLayout.addWidget(self.bandSpin, 3, 1, 1, 1)
        self.bandCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.bandCheck.setObjectName(_fromUtf8("bandCheck"))
        self.gridLayout.addWidget(self.bandCheck, 3, 0, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.progressBar = QtGui.QProgressBar(GdalToolsWidget)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.label.setBuddy(self.inSelector)
        self.label_2.setBuddy(self.outSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Convert RGB image to paletted", None))
        self.batchCheck.setText(_translate("GdalToolsWidget", "Batch mode (for processing whole directory)", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input file", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file", None))
        self.colorsCheck.setText(_translate("GdalToolsWidget", "Number of colors", None))
        self.bandCheck.setText(_translate("GdalToolsWidget", "Band to convert", None))

from .inOutSelector import GdalToolsInOutSelector
