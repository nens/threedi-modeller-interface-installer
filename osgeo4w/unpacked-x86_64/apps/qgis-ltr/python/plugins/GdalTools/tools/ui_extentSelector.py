# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/extentSelector.ui'
#
# Created: Sat Jun 23 08:09:31 2018
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

class Ui_GdalToolsExtentSelector(object):
    def setupUi(self, GdalToolsExtentSelector):
        GdalToolsExtentSelector.setObjectName(_fromUtf8("GdalToolsExtentSelector"))
        GdalToolsExtentSelector.resize(343, 134)
        self.gridLayout = QtGui.QGridLayout(GdalToolsExtentSelector)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(GdalToolsExtentSelector)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(GdalToolsExtentSelector)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 2)
        self.widget = QtGui.QWidget(GdalToolsExtentSelector)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 0, 2, 1, 1)
        self.x1CoordEdit = QtGui.QLineEdit(self.widget)
        self.x1CoordEdit.setObjectName(_fromUtf8("x1CoordEdit"))
        self.gridLayout_3.addWidget(self.x1CoordEdit, 0, 3, 1, 1)
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 0, 7, 1, 1)
        self.x2CoordEdit = QtGui.QLineEdit(self.widget)
        self.x2CoordEdit.setObjectName(_fromUtf8("x2CoordEdit"))
        self.gridLayout_3.addWidget(self.x2CoordEdit, 0, 8, 1, 1)
        self.y1CoordEdit = QtGui.QLineEdit(self.widget)
        self.y1CoordEdit.setObjectName(_fromUtf8("y1CoordEdit"))
        self.gridLayout_3.addWidget(self.y1CoordEdit, 1, 3, 1, 1)
        self.y2CoordEdit = QtGui.QLineEdit(self.widget)
        self.y2CoordEdit.setObjectName(_fromUtf8("y2CoordEdit"))
        self.gridLayout_3.addWidget(self.y2CoordEdit, 1, 8, 1, 1)
        self.label_15 = QtGui.QLabel(self.widget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 1, 7, 1, 1)
        self.label_14 = QtGui.QLabel(self.widget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setIndent(20)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 6, 2, 1)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 1, 2, 1)
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 2)
        self.btnEnable = QtGui.QPushButton(GdalToolsExtentSelector)
        self.btnEnable.setObjectName(_fromUtf8("btnEnable"))
        self.gridLayout.addWidget(self.btnEnable, 1, 1, 1, 1)

        self.retranslateUi(GdalToolsExtentSelector)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsExtentSelector)

    def retranslateUi(self, GdalToolsExtentSelector):
        self.label.setText(_translate("GdalToolsExtentSelector", "Select the extent by drag on canvas", None))
        self.label_7.setText(_translate("GdalToolsExtentSelector", "or change the extent coordinates", None))
        self.label_11.setText(_translate("GdalToolsExtentSelector", "x", None))
        self.label_13.setText(_translate("GdalToolsExtentSelector", "x", None))
        self.label_15.setText(_translate("GdalToolsExtentSelector", "y", None))
        self.label_14.setText(_translate("GdalToolsExtentSelector", "y", None))
        self.label_12.setText(_translate("GdalToolsExtentSelector", "2", None))
        self.label_10.setText(_translate("GdalToolsExtentSelector", "1", None))
        self.btnEnable.setText(_translate("GdalToolsExtentSelector", "Re-Enable", None))

