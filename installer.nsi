# SetCompressor /SOLID lzma
SetCompress off

Unicode True
# Allow privilege elevation in vista
RequestExecutionLevel admin 

!include "x64.nsh"
!include "MUI.nsh"
!include "LogicLib.nsh"

!define PUBLISHER "Nelen en Schuurmans"
!define WEB_SITE "https://nelen-schuurmans.nl/"
!define WIKI_PAGE "https://docs.3di.live/"

# General Definitions (passed as parameter)

# Name of the application shown during install
Name "${DISPLAYED_NAME}"
# Name of the output file (installer executable)
OutFile "${INSTALLER_NAME}"

# Tell the installer to show Install and Uninstall details as default
ShowInstDetails hide
ShowUnInstDetails hide

# .onInit Function (called when the installer is nearly finished initializing)
Function .onInit
	${If} ${ARCH} == "x86_64"
		${If} ${RunningX64}
			DetailPrint "Installer running on 64-bit host"
			; disable registry redirection (enable access to 64-bit portion of registry)
			SetRegView 64
			; change install dir
			${If} $INSTDIR == ""
			  StrCpy $INSTDIR "$PROGRAMFILES64\${QGIS_BASE}"
			${EndIf}
		${EndIf}
	${EndIf}

	${If} $INSTDIR == ""
		StrCpy $INSTDIR "$PROGRAMFILES\${QGIS_BASE}"
	${EndIf}
FunctionEnd

!define MUI_ABORTWARNING
!define MUI_ICON ".\resources\Install_3Di.ico"
!define MUI_UNICON ".\resources\Uninstall_3Di.ico"
!define MUI_HEADERIMAGE_BITMAP_NOSTETCH ".\resources\InstallHeaderImage3Di.bmp"
!define MUI_HEADERIMAGE_UNBITMAP_NOSTRETCH ".\resources\UnInstallHeaderImage3Di.bmp"
!define MUI_WELCOMEFINISHPAGE_BITMAP ".\resources\WelcomeFinishPage3Di.bmp"
!define MUI_UNWELCOMEFINISHPAGE_BITMAP ".\resources\WelcomeFinishPage3Di.bmp"

# Installer Pages
!define MUI_WELCOMEPAGE_TITLE_3LINES
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE ${LICENSE_FILE}
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES
!define MUI_FINISHPAGE_TITLE_3LINES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH
!insertmacro MUI_LANGUAGE "English"

Section "3Di Modeller Interface" SecQGIS
	SectionIn RO
	SetOutPath $INSTDIR
    File .\installer-build/QGIS-OSGeo4W-${VERSION_NUMBER}.msi
    File ./resources/splash.png

    # Run the original QGIS installer
	ClearErrors
	# It is possible to set certain properties in the underlying Wix MSI
    ExecWait '"msiexec" /i "$INSTDIR\QGIS-OSGeo4W-${VERSION_NUMBER}.msi" INSTALLDIR="$INSTDIR" INSTALLDESKTOPSHORTCUTS="0" INSTALLMENUSHORTCUTS="0" /passive /L*V "$INSTDIR\install.log"' $0
	${IfNot} $0 == "0"
		MessageBox MB_ICONSTOP "Installer failed, please check install.log in installation folder"
		Abort
	${EndIf}

    # Sets registry keys so we get default (python) plugin loading
    !include plugins-3di.nsh
    !include python_plugins-3di.nsh

	# Start and Desktop links (also pass the profile folder)
	CreateDirectory "$DESKTOP\${QGIS_BASE}"
	CreateShortCut "$DESKTOP\${QGIS_BASE}\${QGIS_SHORTCUT_NAME}.lnk" "$INSTDIR\bin\qgis.bat" "--profiles-path $APPDATA\3Di\QGIS3" "$INSTDIR\icons\3Di.ico"
	CreateShortCut "$DESKTOP\${QGIS_BASE}\OSGeo4W Shell.lnk" "$INSTDIR\OSGeo4W.bat" "" "$INSTDIR\OSGeo4W.ico"
	
	CreateDirectory "$SMPROGRAMS\${QGIS_BASE}"
	CreateShortCut "$SMPROGRAMS\${QGIS_BASE}\${QGIS_SHORTCUT_NAME}.lnk" "$INSTDIR\bin\qgis.bat" "--profiles-path $APPDATA\3Di\QGIS3" "$INSTDIR\icons\3Di.ico"
	CreateShortCut "$SMPROGRAMS\${QGIS_BASE}\OSGeo4W Shell.lnk" "$INSTDIR\OSGeo4W.bat" "" "$INSTDIR\OSGeo4W.ico"

	# Copy some resources for uninstaller
	SetOutPath $INSTDIR\icons
	File ./resources/3Di.ico

	# Create some reg keys to add entries to the Add/Remove Programs section in the Control Pannel
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "DisplayName" "${DISPLAYED_NAME}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "DisplayVersion" "${VERSION_NUMBER}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "UninstallString" "$INSTDIR\uninstall.exe"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "DisplayIcon" "$INSTDIR\icons\3Di.ico"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "HelpLink" "${WIKI_PAGE}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "URLInfoAbout" "${WEB_SITE}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "Publisher" "${PUBLISHER}"

    WriteUninstaller $INSTDIR\uninstall.exe
SectionEnd

Section "3Di Profile" SecProfile
	SectionIn RO
	SetOverwrite try

    SetShellVarContext current
    Var /GLOBAL INSTDIR_PROFILE_DATA
    StrCpy $INSTDIR_PROFILE_DATA "$APPDATA\3Di\QGIS3\profiles\"
    CreateDirectory "$INSTDIR_PROFILE_DATA"
    
	; add Profile files
	SetOutPath "$INSTDIR_PROFILE_DATA"
	File /r ${PROFILE_FOLDER}\*.*

SectionEnd

Section "Uninstall"
 	${If} ${ARCH} == "x86_64"
		${If} ${RunningX64}
			DetailPrint "Installer running on 64-bit host"
			SetRegView 64
		${EndIf}
	${EndIf}
    # Use the original msi to deinstall qgis
    ExecWait '"msiexec" /x "$INSTDIR\QGIS-OSGeo4W-${VERSION_NUMBER}.msi" INSTALLDIR="$INSTDIR" /quiet /L*V "$APPDATA\3Di\QGIS3\uninstall.log"'

	# Remove the program from the Add/Remove Programs section in the Control Pannel
	DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}"
 
	# Remove start and desktop links
	RMDir /r "$DESKTOP\${QGIS_BASE}"
	RMDir /r "$SMPROGRAMS\${QGIS_BASE}"
	
	Delete $INSTDIR\uninstall.exe
    RMDir /r $INSTDIR

    # TODO: do we need to remove profile data?
SectionEnd
