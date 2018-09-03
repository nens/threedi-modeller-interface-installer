# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/optionsTable.ui'
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

class Ui_GdalToolsOptionsTable(object):
    def setupUi(self, GdalToolsOptionsTable):
        GdalToolsOptionsTable.setObjectName(_fromUtf8("GdalToolsOptionsTable"))
        GdalToolsOptionsTable.resize(297, 90)
        self.verticalLayout = QtGui.QVBoxLayout(GdalToolsOptionsTable)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.creationOptionsWidget = QtGui.QWidget(GdalToolsOptionsTable)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creationOptionsWidget.sizePolicy().hasHeightForWidth())
        self.creationOptionsWidget.setSizePolicy(sizePolicy)
        self.creationOptionsWidget.setObjectName(_fromUtf8("creationOptionsWidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.creationOptionsWidget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.table = QtGui.QTableWidget(self.creationOptionsWidget)
        self.table.setMinimumSize(QtCore.QSize(204, 0))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.horizontalHeader().setMinimumSectionSize(30)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.table)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnAdd = QtGui.QPushButton(self.creationOptionsWidget)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.btnDel = QtGui.QPushButton(self.creationOptionsWidget)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.verticalLayout_2.addWidget(self.btnDel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.creationOptionsWidget)

        self.retranslateUi(GdalToolsOptionsTable)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsOptionsTable)

    def retranslateUi(self, GdalToolsOptionsTable):
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("GdalToolsOptionsTable", "Name", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("GdalToolsOptionsTable", "Value", None))
        self.btnAdd.setText(_translate("GdalToolsOptionsTable", "Add", None))
        self.btnDel.setText(_translate("GdalToolsOptionsTable", "Remove", None))

