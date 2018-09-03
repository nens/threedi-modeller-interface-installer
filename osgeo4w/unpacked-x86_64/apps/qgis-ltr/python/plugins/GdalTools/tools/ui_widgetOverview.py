# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetOverview.ui'
#
# Created: Sat Jun 23 08:09:34 2018
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
        GdalToolsWidget.resize(376, 342)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GdalToolsWidget.sizePolicy().hasHeightForWidth())
        GdalToolsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(GdalToolsWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.batchCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.batchCheck.setEnabled(True)
        self.batchCheck.setObjectName(_fromUtf8("batchCheck"))
        self.verticalLayout.addWidget(self.batchCheck)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(GdalToolsWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.cleanCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.cleanCheck.setObjectName(_fromUtf8("cleanCheck"))
        self.verticalLayout.addWidget(self.cleanCheck)
        self.mPyramidOptionsWidget = QgsRasterPyramidsOptionsWidget(GdalToolsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mPyramidOptionsWidget.sizePolicy().hasHeightForWidth())
        self.mPyramidOptionsWidget.setSizePolicy(sizePolicy)
        self.mPyramidOptionsWidget.setObjectName(_fromUtf8("mPyramidOptionsWidget"))
        self.verticalLayout.addWidget(self.mPyramidOptionsWidget)
        self.progressBar = QtGui.QProgressBar(GdalToolsWidget)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.label.setBuddy(self.inSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Build overviews (Pyramids)", None))
        self.batchCheck.setText(_translate("GdalToolsWidget", "Batch mode (for processing whole directory)", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input file", None))
        self.cleanCheck.setToolTip(_translate("GdalToolsWidget", "Remove all overviews.", None))
        self.cleanCheck.setText(_translate("GdalToolsWidget", "Clean", None))

from qgis.gui import QgsRasterPyramidsOptionsWidget
from .inOutSelector import GdalToolsInOutSelector
