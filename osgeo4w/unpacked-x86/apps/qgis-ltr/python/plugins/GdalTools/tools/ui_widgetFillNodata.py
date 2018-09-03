# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetFillNodata.ui'
#
# Created: Sat Aug 18 08:04:33 2018
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
        GdalToolsWidget.resize(368, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GdalToolsWidget.sizePolicy().hasHeightForWidth())
        GdalToolsWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(GdalToolsWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.batchCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.batchCheck.setObjectName(_fromUtf8("batchCheck"))
        self.gridLayout.addWidget(self.batchCheck, 0, 0, 1, 2)
        self.label = QtGui.QLabel(GdalToolsWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 1, 1, 1, 1)
        self.label_1 = QtGui.QLabel(GdalToolsWidget)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 2, 1, 1, 1)
        self.formatLabel = QtGui.QLabel(GdalToolsWidget)
        self.formatLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.formatLabel.setObjectName(_fromUtf8("formatLabel"))
        self.gridLayout.addWidget(self.formatLabel, 3, 0, 1, 1)
        self.formatCombo = QtGui.QComboBox(GdalToolsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatCombo.sizePolicy().hasHeightForWidth())
        self.formatCombo.setSizePolicy(sizePolicy)
        self.formatCombo.setObjectName(_fromUtf8("formatCombo"))
        self.gridLayout.addWidget(self.formatCombo, 3, 1, 1, 1)
        self.distanceCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.distanceCheck.setObjectName(_fromUtf8("distanceCheck"))
        self.gridLayout.addWidget(self.distanceCheck, 4, 0, 1, 1)
        self.distanceSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.distanceSpin.setMinimum(1)
        self.distanceSpin.setMaximum(1000000)
        self.distanceSpin.setProperty("value", 100)
        self.distanceSpin.setObjectName(_fromUtf8("distanceSpin"))
        self.gridLayout.addWidget(self.distanceSpin, 4, 1, 1, 1)
        self.smoothCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.smoothCheck.setObjectName(_fromUtf8("smoothCheck"))
        self.gridLayout.addWidget(self.smoothCheck, 5, 0, 1, 1)
        self.smoothSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.smoothSpin.setMinimum(0)
        self.smoothSpin.setProperty("value", 0)
        self.smoothSpin.setObjectName(_fromUtf8("smoothSpin"))
        self.gridLayout.addWidget(self.smoothSpin, 5, 1, 1, 1)
        self.bandCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.bandCheck.setObjectName(_fromUtf8("bandCheck"))
        self.gridLayout.addWidget(self.bandCheck, 6, 0, 1, 1)
        self.bandSpin = QtGui.QSpinBox(GdalToolsWidget)
        self.bandSpin.setMinimum(1)
        self.bandSpin.setObjectName(_fromUtf8("bandSpin"))
        self.gridLayout.addWidget(self.bandSpin, 6, 1, 1, 1)
        self.maskCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.maskCheck.setObjectName(_fromUtf8("maskCheck"))
        self.gridLayout.addWidget(self.maskCheck, 7, 0, 1, 1)
        self.maskSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.maskSelector.setObjectName(_fromUtf8("maskSelector"))
        self.gridLayout.addWidget(self.maskSelector, 7, 1, 1, 1)
        self.nomaskCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.nomaskCheck.setObjectName(_fromUtf8("nomaskCheck"))
        self.gridLayout.addWidget(self.nomaskCheck, 8, 0, 1, 2)
        self.progressBar = QtGui.QProgressBar(GdalToolsWidget)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 9, 0, 1, 2)
        self.label.setBuddy(self.inSelector)
        self.label_1.setBuddy(self.outSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Fill Nodata", None))
        self.batchCheck.setText(_translate("GdalToolsWidget", "Batch mode (for processing whole directory)", None))
        self.label.setText(_translate("GdalToolsWidget", "&Input Layer", None))
        self.label_1.setText(_translate("GdalToolsWidget", "&Output file", None))
        self.formatLabel.setText(_translate("GdalToolsWidget", "Output format", None))
        self.distanceCheck.setText(_translate("GdalToolsWidget", "Search distance", None))
        self.smoothCheck.setText(_translate("GdalToolsWidget", "Smooth iterations", None))
        self.bandCheck.setText(_translate("GdalToolsWidget", "Band to operate on", None))
        self.maskCheck.setText(_translate("GdalToolsWidget", "Validity mask", None))
        self.nomaskCheck.setText(_translate("GdalToolsWidget", "Do not use the default validity mask", None))

from .inOutSelector import GdalToolsInOutSelector
