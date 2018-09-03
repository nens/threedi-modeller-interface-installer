# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetTileIndex.ui'
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
        GdalToolsWidget.resize(400, 153)
        self.verticalLayout = QtGui.QVBoxLayout(GdalToolsWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(GdalToolsWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.recurseCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.recurseCheck.setObjectName(_fromUtf8("recurseCheck"))
        self.gridLayout.addWidget(self.recurseCheck, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.indexFieldCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.indexFieldCheck.setObjectName(_fromUtf8("indexFieldCheck"))
        self.gridLayout.addWidget(self.indexFieldCheck, 3, 0, 1, 1)
        self.indexFieldEdit = QtGui.QLineEdit(GdalToolsWidget)
        self.indexFieldEdit.setEnabled(True)
        self.indexFieldEdit.setObjectName(_fromUtf8("indexFieldEdit"))
        self.gridLayout.addWidget(self.indexFieldEdit, 3, 1, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.skipDifferentProjCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.skipDifferentProjCheck.setObjectName(_fromUtf8("skipDifferentProjCheck"))
        self.verticalLayout.addWidget(self.skipDifferentProjCheck)
        self.label.setBuddy(self.inSelector)
        self.label_2.setBuddy(self.outSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Raster tile index", None))
        self.label.setText(_translate("GdalToolsWidget", "Input directory", None))
        self.recurseCheck.setText(_translate("GdalToolsWidget", "Recurse subdirectories", None))
        self.label_2.setText(_translate("GdalToolsWidget", "Output shapefile", None))
        self.indexFieldCheck.setText(_translate("GdalToolsWidget", "Tile index field", None))
        self.indexFieldEdit.setText(_translate("GdalToolsWidget", "location", None))
        self.skipDifferentProjCheck.setText(_translate("GdalToolsWidget", "Skip files with different projection ref", None))

from .inOutSelector import GdalToolsInOutSelector
