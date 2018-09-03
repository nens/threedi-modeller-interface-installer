# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/inOutSelector.ui'
#
# Created: Sat Aug 18 08:04:32 2018
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

class Ui_GdalToolsInOutSelector(object):
    def setupUi(self, GdalToolsInOutSelector):
        GdalToolsInOutSelector.setObjectName(_fromUtf8("GdalToolsInOutSelector"))
        GdalToolsInOutSelector.resize(294, 28)
        self.horizontalLayout = QtGui.QHBoxLayout(GdalToolsInOutSelector)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fileEdit = QtGui.QLineEdit(GdalToolsInOutSelector)
        self.fileEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.fileEdit.setObjectName(_fromUtf8("fileEdit"))
        self.horizontalLayout.addWidget(self.fileEdit)
        self.combo = QtGui.QComboBox(GdalToolsInOutSelector)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo.sizePolicy().hasHeightForWidth())
        self.combo.setSizePolicy(sizePolicy)
        self.combo.setEditable(True)
        self.combo.setFrame(True)
        self.combo.setObjectName(_fromUtf8("combo"))
        self.horizontalLayout.addWidget(self.combo)
        self.selectBtn = QtGui.QPushButton(GdalToolsInOutSelector)
        self.selectBtn.setObjectName(_fromUtf8("selectBtn"))
        self.horizontalLayout.addWidget(self.selectBtn)

        self.retranslateUi(GdalToolsInOutSelector)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsInOutSelector)

    def retranslateUi(self, GdalToolsInOutSelector):
        self.selectBtn.setText(_translate("GdalToolsInOutSelector", "Select...", None))

