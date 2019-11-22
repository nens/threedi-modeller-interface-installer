# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ThreeDiCustomizations
                                 A QGIS plugin
 SplashScreen and other customizations for the 3Di_Modeler_Interface
                             -------------------
        begin                : 2018-08-22
        Marco Duiker - MD-kwadraat
        email                : md@md-kwadraat.nl

        Adapted from All4GIS/Load-QSS and All4GIS/fake_splash
        Both by Francisco Raga
 ***************************************************************************/



/***************************************************************************
 *                                                                         *
 *   This program is free software you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation either version 2 of the License, or     *
 #   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""
import os
import re
import webbrowser

from qgis.PyQt.Qt import QAction
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtCore import QFileSystemWatcher
from qgis.PyQt.QtCore import QSettings
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtGui import QPixmap
from qgis.PyQt.QtWidgets import qApp
from qgis.PyQt.QtWidgets import QApplication
from qgis.PyQt.QtWidgets import QSplashScreen

from ThreeDiCustomizations.gui.generated import resources_rc


def reload_style(path):
    # Some applications will remove a file and rewrite it.  QFileSystemWatcher will
    # ignore the file if the file handle goes away so we have to keep adding it.
    watch.removePaths(watch.files())
    watch.addPath(path)
    with open(path, "r") as f:
        stylesheet = f.read()
        # Update the image paths to use full paths. Fixes image loading in styles
        path = os.path.dirname(path).replace("\\", "/")
        stylesheet = re.sub(r'url\((.*?)\)', r'url("{}/\1")'.format(path), stylesheet)
        QApplication.instance().setStyleSheet(stylesheet)


watch = QFileSystemWatcher()
watch.fileChanged.connect(reload_style)


class SplashScreen(object):
    def __init__(self, iface):

        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)

        self.windowTitle = '3Di Modeler Interface - Powered by QGIS'

        self.app = QApplication.instance()
        self.QApp = QCoreApplication.instance()

        if self.QApp is None:
            self.QApp = QApplication(sys.argv)

        self.QApp.startingUp()
        self.QApp.processEvents()
        self.app.startDragTime()

        self.iface.initializationCompleted.connect(self.customization)
        qApp.processEvents()

        self.applyStyle()

    def initGui(self):
        QSettings().setValue("/qgis/hideSplash", True)
        qApp.processEvents()

        icon = QIcon(":/3Di_images/3Di_images/images/logo.png")
        self.app.setWindowIcon(icon)
        self.iface.mainWindow().setWindowIcon(icon)

        self.iface.mainWindow().setWindowTitle(self.windowTitle)

        qApp.processEvents()

        if not self.iface.mainWindow().isVisible():
            self.splash_pix = QPixmap(':/3Di_images/3Di_images/images/splash.png')
            self.splash = QSplashScreen(self.splash_pix, Qt.WindowStaysOnTopHint)
            self.splash = QSplashScreen(self.splash_pix)
            self.splash.setMask(self.splash_pix.mask())
            self.splash.show()
            qApp.processEvents()
        self.applyStyle()
        self.addHelpMenuItem()
        return

    def run(self):
        pass

    def unload(self):
        qApp.processEvents()
        self.iface.initializationCompleted.disconnect(self.customization)
        self.helpAction.deleteLater()
        return

    def customization(self):
        self.splash.finish(self.iface.mainWindow())
        self.iface.mainWindow().setWindowTitle(self.windowTitle)
        qApp.processEvents()
        self.applyStyle()

    def applyStyle(self):
        path = os.path.abspath(os.path.join(self.plugin_dir, 'Modeler Interface', 'stylesheet.qss'))
        watch.removePaths(watch.files())
        reload_style(path)

    def open3DiHelp(self):
        webbrowser.open_new("https://docs.3di.lizard.net/en/stable/")

    def addHelpMenuItem(self):
        if self.iface.firstRightStandardMenu().objectName() == 'mHelpMenu':
            # help menu is in the expected location
            self.helpAction = QAction(QIcon(":/3Di_images/3Di_images/images/logo.png"),
                                      "3Di Help", self.iface.mainWindow())
            self.helpAction.triggered.connect(self.open3DiHelp)
            self.helpAction.setWhatsThis("3Di Help")

            self.iface.firstRightStandardMenu().addAction(self.helpAction)
