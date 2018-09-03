# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetPolygonize.ui'
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
        GdalToolsWidget.resize(446, 121)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GdalToolsWidget.sizePolicy().hasHeightForWidth())
        GdalToolsWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(GdalToolsWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(GdalToolsWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 1, 1, 1, 1)
        self.fieldCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.fieldCheck.setObjectName(_fromUtf8("fieldCheck"))
        self.gridLayout.addWidget(self.fieldCheck, 2, 0, 1, 1)
        self.fieldEdit = QtGui.QLineEdit(GdalToolsWidget)
        self.fieldEdit.setObjectName(_fromUtf8("fieldEdit"))
        self.gridLayout.addWidget(self.fieldEdit, 2, 1, 1, 1)
        self.maskCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.maskCheck.setObjectName(_fromUtf8("maskCheck"))
        self.gridLayout.addWidget(self.maskCheck, 3, 0, 1, 1)
        self.maskSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.maskSelector.setObjectName(_fromUtf8("maskSelector"))
        self.gridLayout.addWidget(self.maskSelector, 3, 1, 1, 1)
        self.label.setBuddy(self.inSelector)
        self.label_2.setBuddy(self.outSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Polygonize (Raster to vector)", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input file (raster)", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file for polygons (shapefile)", None))
        self.fieldCheck.setText(_translate("GdalToolsWidget", "&Field name", None))
        self.fieldEdit.setText(_translate("GdalToolsWidget", "DN", None))
        self.maskCheck.setText(_translate("GdalToolsWidget", "Use mask", None))

from .inOutSelector import GdalToolsInOutSelector
