# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetMerge.ui'
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
        GdalToolsWidget.resize(371, 284)
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
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.noDataCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.noDataCheck.setObjectName(_fromUtf8("noDataCheck"))
        self.gridLayout.addWidget(self.noDataCheck, 4, 0, 1, 1)
        self.noDataSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.noDataSpin.setMinimum(-100000)
        self.noDataSpin.setMaximum(65000)
        self.noDataSpin.setObjectName(_fromUtf8("noDataSpin"))
        self.gridLayout.addWidget(self.noDataSpin, 4, 1, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 1, 1, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 3, 1, 1, 1)
        self.inputDirCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.inputDirCheck.setObjectName(_fromUtf8("inputDirCheck"))
        self.gridLayout.addWidget(self.inputDirCheck, 0, 0, 1, 2)
        self.recurseCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.recurseCheck.setObjectName(_fromUtf8("recurseCheck"))
        self.gridLayout.addWidget(self.recurseCheck, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.separateCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.separateCheck.setObjectName(_fromUtf8("separateCheck"))
        self.verticalLayout.addWidget(self.separateCheck)
        self.intersectCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.intersectCheck.setEnabled(False)
        self.intersectCheck.setObjectName(_fromUtf8("intersectCheck"))
        self.verticalLayout.addWidget(self.intersectCheck)
        self.pctCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.pctCheck.setObjectName(_fromUtf8("pctCheck"))
        self.verticalLayout.addWidget(self.pctCheck)
        self.creationOptionsGroupBox = QgsCollapsibleGroupBox(GdalToolsWidget)
        self.creationOptionsGroupBox.setCheckable(True)
        self.creationOptionsGroupBox.setChecked(False)
        self.creationOptionsGroupBox.setProperty("collapsed", False)
        self.creationOptionsGroupBox.setProperty("saveCollapsedState", True)
        self.creationOptionsGroupBox.setObjectName(_fromUtf8("creationOptionsGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.creationOptionsGroupBox)
        self.verticalLayout_2.setMargin(9)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.creationOptionsWidget = QgsRasterFormatSaveOptionsWidget(self.creationOptionsGroupBox)
        self.creationOptionsWidget.setObjectName(_fromUtf8("creationOptionsWidget"))
        self.verticalLayout_2.addWidget(self.creationOptionsWidget)
        self.verticalLayout.addWidget(self.creationOptionsGroupBox)
        self.label.setBuddy(self.inSelector)
        self.label_2.setBuddy(self.outSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Merge", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input files", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file", None))
        self.noDataCheck.setText(_translate("GdalToolsWidget", "&No data value", None))
        self.inputDirCheck.setText(_translate("GdalToolsWidget", "Choose input directory instead of files", None))
        self.recurseCheck.setText(_translate("GdalToolsWidget", "Recurse subdirectories", None))
        self.separateCheck.setText(_translate("GdalToolsWidget", "Place each input file into a separate band", None))
        self.intersectCheck.setText(_translate("GdalToolsWidget", "Use intersected extent", None))
        self.pctCheck.setText(_translate("GdalToolsWidget", "Grab pseudocolor table from the first image", None))
        self.creationOptionsGroupBox.setTitle(_translate("GdalToolsWidget", "&Creation Options", None))

from qgis.gui import QgsCollapsibleGroupBox, QgsRasterFormatSaveOptionsWidget
from .inOutSelector import GdalToolsInOutSelector
