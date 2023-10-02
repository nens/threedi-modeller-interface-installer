QGIS_VERSION_MAJOR = 3
QGIS_VERSION_MINOR = 28
QGIS_VERSION_PATCH = 11
QGIS_VERSION_BINARY = 1

INSTALLER_BUILDDIR = installer-build
QGIS_INSTALLER_NAME = QGIS-OSGeo4W

QGIS_VERSION = $(QGIS_VERSION_MAJOR).$(QGIS_VERSION_MINOR).$(QGIS_VERSION_PATCH)-$(QGIS_VERSION_BINARY)
QGIS_URL = https://download.qgis.org/downloads/
PACKAGE_NAME = 3DiModellerInterface
SHORTCUT_NAME = 3Di Modeller Interface
# 3Di ModellerInterface version (note that this is additional postfix than 
# can be used when plugins are updated etc)
PACKAGE_BINARY = 2

# Our plugins (note trailing slash)
NENS_PLUGIN_URL = https://plugins.3di.live/

TOOLBOX_FILENAME = threedi_results_analysis.3.1.11
MODELSIM_FILENAME = threedi_models_and_simulations.3.6.0
CUSTOMIZATION_FILENAME = ThreeDiCustomizations.1.2.6
SCHEMATISATION_FILENAME = threedi_schematisation_editor.1.7.0

# External plugins we want to add to the installer 
QGIS_PLUGIN_URL = https://plugins.qgis.org/plugins/
CRAYFISH_NAME = crayfish
CRAYFISH_VERSION = 3.6.0

PROFILE_TOOL_NAME = profiletool
PROFILE_TOOL_VERSION = 4.2.6

QMS_NAME = quick_map_services
QMS_VERSION = 0.19.33

VALUE_TOOL_NAME = valuetool
VALUE_TOOL_VERSION = 3.0.17

SERVAL_NAME = Serval
SERVAL_VERSION = 3.10.5

PLUGIN_DIR = profiles/default/python/plugins/

clean:
	@echo
	@echo "-------------------------------------------"
	@echo "Removing Installer build files and plugins."
	@echo "-------------------------------------------"
	rm -fr ./$(INSTALLER_BUILDDIR)
	rm -fr ./$(PLUGIN_DIR)
	rm -f *.exe

installer: clean
	@echo
	@echo "---------------------------"
	@echo "Creating Windows Installer."
	@echo "---------------------------"
	
	@echo "Creating installation folder"
	mkdir -p ./$(INSTALLER_BUILDDIR)

	@echo "Creating plugin folder"
	mkdir -p ./$(PLUGIN_DIR)
	
	@echo "Downloading QGIS"
	wget -N -P ./$(INSTALLER_BUILDDIR) $(QGIS_URL)$(QGIS_INSTALLER_NAME)-$(QGIS_VERSION).msi

	@echo "Downloading and extracting plugins"
	wget -N -P ./$(INSTALLER_BUILDDIR) $(NENS_PLUGIN_URL)$(TOOLBOX_FILENAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(TOOLBOX_FILENAME).zip -d ./$(PLUGIN_DIR) 

	wget -N -P ./$(INSTALLER_BUILDDIR) $(NENS_PLUGIN_URL)$(SCHEMATISATION_FILENAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(SCHEMATISATION_FILENAME).zip -d ./$(PLUGIN_DIR) 

	wget -N -P ./$(INSTALLER_BUILDDIR) $(NENS_PLUGIN_URL)$(CUSTOMIZATION_FILENAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(CUSTOMIZATION_FILENAME).zip -d ./$(PLUGIN_DIR) 

	wget -N -P ./$(INSTALLER_BUILDDIR) $(NENS_PLUGIN_URL)$(MODELSIM_FILENAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(MODELSIM_FILENAME).zip -d ./$(PLUGIN_DIR) 

	curl $(QGIS_PLUGIN_URL)$(CRAYFISH_NAME)/version/$(CRAYFISH_VERSION)/download/ --output ./$(INSTALLER_BUILDDIR)/$(CRAYFISH_NAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(CRAYFISH_NAME).zip -d ./$(PLUGIN_DIR)

	curl $(QGIS_PLUGIN_URL)$(PROFILE_TOOL_NAME)/version/$(PROFILE_TOOL_VERSION)/download/ --output ./$(INSTALLER_BUILDDIR)/$(PROFILE_TOOL_NAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(PROFILE_TOOL_NAME).zip -d ./$(PLUGIN_DIR)

	curl $(QGIS_PLUGIN_URL)$(QMS_NAME)/version/$(QMS_VERSION)/download/ --output ./$(INSTALLER_BUILDDIR)/$(QMS_NAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(QMS_NAME).zip -d ./$(PLUGIN_DIR)

	curl $(QGIS_PLUGIN_URL)$(VALUE_TOOL_NAME)/version/$(VALUE_TOOL_VERSION)/download/ --output ./$(INSTALLER_BUILDDIR)/$(VALUE_TOOL_NAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(VALUE_TOOL_NAME).zip -d ./$(PLUGIN_DIR)

	curl $(QGIS_PLUGIN_URL)$(SERVAL_NAME)/version/$(SERVAL_VERSION)/download/ --output ./$(INSTALLER_BUILDDIR)/$(SERVAL_NAME).zip
	unzip -o ./$(INSTALLER_BUILDDIR)/$(SERVAL_NAME).zip -d ./$(PLUGIN_DIR)

	makensis 	-DINSTALLER_NAME='$(PACKAGE_NAME)-OSGeo4W-$(QGIS_VERSION)-$(PACKAGE_BINARY)-Setup-x86_64.exe' \
	 			-DDISPLAYED_NAME='$(PACKAGE_NAME) $(QGIS_VERSION)' \
				-DARCH='x86_64' \
				-DQGIS_BASE='$(PACKAGE_NAME) $(QGIS_VERSION_MAJOR).$(QGIS_VERSION_MINOR)' \
				-DPROFILE_FOLDER='profiles' \
				-DVERSION_NUMBER='$(QGIS_VERSION)' \
				-DLICENSE_FILE='LICENSE.txt' \
				-DQGIS_SHORTCUT_NAME='$(SHORTCUT_NAME) $(QGIS_VERSION_MAJOR).$(QGIS_VERSION_MINOR)' \
				./installer.nsi

upload:
	./upload-modeller-interface.sh $(PACKAGE_NAME)-OSGeo4W-$(QGIS_VERSION)-$(PACKAGE_BINARY)-Setup-x86_64.exe