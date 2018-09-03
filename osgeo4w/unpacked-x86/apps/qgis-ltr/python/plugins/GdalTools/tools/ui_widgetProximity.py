# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetProximity.ui'
#
# Created: Sat Aug 18 08:04:34 2018
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
        GdalToolsWidget.resize(327, 229)
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
        self.valuesCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.valuesCheck.setObjectName(_fromUtf8("valuesCheck"))
        self.gridLayout.addWidget(self.valuesCheck, 2, 0, 1, 1)
        self.distUnitsCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.distUnitsCheck.setChecked(True)
        self.distUnitsCheck.setObjectName(_fromUtf8("distUnitsCheck"))
        self.gridLayout.addWidget(self.distUnitsCheck, 3, 0, 1, 1)
        self.distUnitsCombo = QtGui.QComboBox(GdalToolsWidget)
        self.distUnitsCombo.setObjectName(_fromUtf8("distUnitsCombo"))
        self.distUnitsCombo.addItem(_fromUtf8(""))
        self.distUnitsCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.distUnitsCombo, 3, 1, 1, 1)
        self.maxDistCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.maxDistCheck.setObjectName(_fromUtf8("maxDistCheck"))
        self.gridLayout.addWidget(self.maxDistCheck, 4, 0, 1, 1)
        self.maxDistSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.maxDistSpin.setMaximum(65000)
        self.maxDistSpin.setObjectName(_fromUtf8("maxDistSpin"))
        self.gridLayout.addWidget(self.maxDistSpin, 4, 1, 1, 1)
        self.noDataCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.noDataCheck.setObjectName(_fromUtf8("noDataCheck"))
        self.gridLayout.addWidget(self.noDataCheck, 5, 0, 1, 1)
        self.noDataSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.noDataSpin.setMinimum(-100000)
        self.noDataSpin.setMaximum(65000)
        self.noDataSpin.setObjectName(_fromUtf8("noDataSpin"))
        self.gridLayout.addWidget(self.noDataSpin, 5, 1, 1, 1)
        self.fixedBufValCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.fixedBufValCheck.setObjectName(_fromUtf8("fixedBufValCheck"))
        self.gridLayout.addWidget(self.fixedBufValCheck, 6, 0, 1, 1)
        self.fixedBufValSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.fixedBufValSpin.setMaximum(65000)
        self.fixedBufValSpin.setObjectName(_fromUtf8("fixedBufValSpin"))
        self.gridLayout.addWidget(self.fixedBufValSpin, 6, 1, 1, 1)
        self.valuesEdit = QtGui.QLineEdit(GdalToolsWidget)
        self.valuesEdit.setObjectName(_fromUtf8("valuesEdit"))
        self.gridLayout.addWidget(self.valuesEdit, 2, 1, 1, 1)
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
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Proximity (Raster distance)", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input file", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file", None))
        self.valuesCheck.setText(_translate("GdalToolsWidget", "&Values", None))
        self.distUnitsCheck.setText(_translate("GdalToolsWidget", "&Dist units", None))
        self.distUnitsCombo.setItemText(0, _translate("GdalToolsWidget", "GEO", None))
        self.distUnitsCombo.setItemText(1, _translate("GdalToolsWidget", "PIXEL", None))
        self.maxDistCheck.setText(_translate("GdalToolsWidget", "&Max dist", None))
        self.noDataCheck.setText(_translate("GdalToolsWidget", "&No data", None))
        self.fixedBufValCheck.setText(_translate("GdalToolsWidget", "&Fixed buf val", None))
        self.valuesEdit.setText(_translate("GdalToolsWidget", "0", None))

from .inOutSelector import GdalToolsInOutSelector
