# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetProjection.ui'
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
        GdalToolsWidget.resize(369, 244)
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
        self.label_3 = QtGui.QLabel(GdalToolsWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
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
        self.label_4 = QtGui.QLabel(GdalToolsWidget)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.desiredSRSEdit = QtGui.QLineEdit(GdalToolsWidget)
        self.desiredSRSEdit.setObjectName(_fromUtf8("desiredSRSEdit"))
        self.horizontalLayout_2.addWidget(self.desiredSRSEdit)
        self.selectDesiredSRSButton = QtGui.QPushButton(GdalToolsWidget)
        self.selectDesiredSRSButton.setObjectName(_fromUtf8("selectDesiredSRSButton"))
        self.horizontalLayout_2.addWidget(self.selectDesiredSRSButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.progressBar = QtGui.QProgressBar(GdalToolsWidget)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.label.setBuddy(self.inSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Assign projection", None))
        self.batchCheck.setText(_translate("GdalToolsWidget", "Batch mode (for processing whole directory)", None))
        self.label_3.setText(_translate("GdalToolsWidget", "WARNING: current projection definition will be cleared", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input file", None))
        self.recurseCheck.setText(_translate("GdalToolsWidget", "Recurse subdirectories", None))
        self.label_2.setText(_translate("GdalToolsWidget", "Desired SRS", None))
        self.label_4.setText(_translate("GdalToolsWidget", "Output will be:\n"
"- new GeoTiff if input file is not GeoTiff\n"
"- overwritten if input is GeoTiff", None))
        self.selectDesiredSRSButton.setText(_translate("GdalToolsWidget", "Select...", None))

from .inOutSelector import GdalToolsInOutSelector
