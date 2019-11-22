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


def classFactory(iface):
    from .SplashScreen import SplashScreen
    return SplashScreen(iface)
