# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetContour.ui'
#
# Created: Sat Jun 23 08:09:32 2018
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
        GdalToolsWidget.resize(520, 163)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GdalToolsWidget.sizePolicy().hasHeightForWidth())
        GdalToolsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtGui.QVBoxLayout(GdalToolsWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(GdalToolsWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(GdalToolsWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.intervalDSpinBox = QtGui.QDoubleSpinBox(GdalToolsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intervalDSpinBox.sizePolicy().hasHeightForWidth())
        self.intervalDSpinBox.setSizePolicy(sizePolicy)
        self.intervalDSpinBox.setDecimals(3)
        self.intervalDSpinBox.setMaximum(2140000000.0)
        self.intervalDSpinBox.setObjectName(_fromUtf8("intervalDSpinBox"))
        self.gridLayout.addWidget(self.intervalDSpinBox, 2, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.attributeCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.attributeCheck.setObjectName(_fromUtf8("attributeCheck"))
        self.verticalLayout.addWidget(self.attributeCheck)
        self.label_5 = QtGui.QLabel(GdalToolsWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setIndent(16)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.attributeEdit = QtGui.QLineEdit(GdalToolsWidget)
        self.attributeEdit.setObjectName(_fromUtf8("attributeEdit"))
        self.verticalLayout_2.addWidget(self.attributeEdit)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 1, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 1, 1, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.label.setBuddy(self.inSelector)
        self.label_2.setBuddy(self.outSelector)
        self.label_3.setBuddy(self.intervalDSpinBox)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Contour", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input file (raster)", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file for contour lines (vector)", None))
        self.label_3.setText(_translate("GdalToolsWidget", "I&nterval between contour lines", None))
        self.attributeCheck.setText(_translate("GdalToolsWidget", "&Attribute name", None))
        self.label_5.setText(_translate("GdalToolsWidget", "If not provided, no elevation attribute is attached.", None))
        self.attributeEdit.setText(_translate("GdalToolsWidget", "ELEV", None))

from .inOutSelector import GdalToolsInOutSelector
