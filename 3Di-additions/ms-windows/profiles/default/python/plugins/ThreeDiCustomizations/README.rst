ThreeDiCustomizations
=====================

A QGIS plugin containing N&S 3Di styles. To be used together with the ThreeDiToolbox plugin, as part of the 3Di-modeller-interface.

Installation Requirements
-------------------------
- Repository contains an already compiled gui file ``gui/generated/resources_rc.py``. In case of style changes (icons and/or splashscreen), new style must be rebuilt by running 
``# pyrcc5 ui/resources.qrc -o gui/generated/resources_rc.py``.
pyrcc5 is part of the Debian package ``pyqt-dev-tools``.

Installation
------------
- Does not require manual istallation, is supposed to be delivered as part of the 3Di-modeller-interface and will be downloaded while running the 3Di-modeller-interface-installer build script.
- When installing manually, copy the directory ThreeDiCustomizations to ``$HOME/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`` (Linux) or ``C:\\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`` (Windows).

