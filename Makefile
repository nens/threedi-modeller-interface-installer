QGIS_VERSION_MAJOR = 3
QGIS_VERSION_MINOR = 22
QGIS_VERSION_PATCH = 7
QGIS_VERSION_BINARY = 1

INSTALLER_BUILDDIR = installer-build
QGIS_INSTALLER_NAME = QGIS-OSGeo4W

QGIS_VERSION = $(QGIS_VERSION_MAJOR).$(QGIS_VERSION_MINOR).$(QGIS_VERSION_PATCH)-$(QGIS_VERSION_BINARY)
QGIS_URL = https://download.qgis.org/downloads/
PACKAGE_NAME = 3DiModellerInterface

PLUGIN_URL = https://plugins.lizard.net/
TOOLBOX_FILENAME = ThreeDiToolbox.2.0
MODELSIM_FILENAME = threedi_models_and_simulations.3.0.3
CUSTOMIZATION_FILENAME = ThreeDiCustomizations.1.2.6

PLUGIN_DIR = 3Di-additions/ms-windows/profiles/default/python/plugins/

clean:
	@echo
	@echo "-------------------------------------------"
	@echo "Removing Installer build files and folders."
	@echo "-------------------------------------------"
	rm -fr ./$(INSTALLER_BUILDDIR)
	rm -f *.exe

installer: 
	@echo
	@echo "---------------------------"
	@echo "Creating Windows Installer."
	@echo "---------------------------"
	
	@echo "Creating installation folder"
	mkdir -p ./$(INSTALLER_BUILDDIR)
	
	@echo "Downloading QGIS"
	wget -N -P ./$(INSTALLER_BUILDDIR) $(QGIS_URL)$(QGIS_INSTALLER_NAME)-$(QGIS_VERSION).msi

	@echo "Downloading and extracting plugins"
	wget -N -P ./$(INSTALLER_BUILDDIR) $(PLUGIN_URL)$(TOOLBOX_FILENAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(TOOLBOX_FILENAME).zip -d ./$(PLUGIN_DIR) 

	wget -N -P ./$(INSTALLER_BUILDDIR) $(PLUGIN_URL)$(CUSTOMIZATION_FILENAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(CUSTOMIZATION_FILENAME).zip -d ./$(PLUGIN_DIR) 

	wget -N -P ./$(INSTALLER_BUILDDIR) $(PLUGIN_URL)$(MODELSIM_FILENAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(MODELSIM_FILENAME).zip -d ./$(PLUGIN_DIR) 

	makensis 	-DINSTALLER_NAME='$(PACKAGE_NAME)-OSGeo4W-$(QGIS_VERSION)-Setup-x86_64.exe' \
	 			-DDISPLAYED_NAME='$(PACKAGE_NAME) $(QGIS_VERSION)' \
				-DARCH='x86_64' \
				-DQGIS_BASE='$(PACKAGE_NAME) $(QGIS_VERSION_MAJOR).$(QGIS_VERSION_MINOR)' \
				-DPROFILE_FOLDER='3Di-additions/ms-windows/profiles' \
				-DVERSION_NUMBER='$(QGIS_VERSION)' \
				./installer.nsi
