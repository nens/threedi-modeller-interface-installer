# SetCompressor /SOLID lzma
SetCompress off

Unicode True
# Allow privilege elevation in vista
RequestExecutionLevel highest

!include "x64.nsh"
!include "MUI.nsh"
!include "LogicLib.nsh"
!include "FileFunc.nsh"
!include "StrFunc.nsh"
${StrRep} # Required by StrFunc
!include "TextFunc.nsh"
${StrTrimNewLines} ; <-- REQUIRED to register the macro
!include "StrFunc.nsh"
${StrTok}
!define PUBLISHER "Nelen en Schuurmans"
!define WEB_SITE "https://nelen-schuurmans.nl/"
!define WIKI_PAGE "https://www.ranawaterintelligence.com/"

# General Definitions (passed as parameter)

# Name of the application shown during install
Name "${DISPLAYED_NAME}"
# Name of the output file (installer executable)
OutFile "${INSTALLER_NAME}"

# Tell the installer to hide Install and Uninstall details
ShowInstDetails hide
ShowUnInstDetails hide

!define MUI_ABORTWARNING
!define MUI_ICON ".\resources\install_rana.ico"
!define MUI_UNICON ".\resources\uninstall_rana.ico"
!define MUI_HEADERIMAGE_BITMAP_NOSTETCH ".\resources\InstallHeaderImage3Di.bmp"
!define MUI_HEADERIMAGE_UNBITMAP_NOSTRETCH ".\resources\UnInstallHeaderImage3Di.bmp"
!define MUI_WELCOMEFINISHPAGE_BITMAP ".\resources\WelcomeFinishPageRana.bmp"
!define MUI_UNWELCOMEFINISHPAGE_BITMAP ".\resources\WelcomeFinishPageRana.bmp"
!define MUI_COMPONENTSPAGE_TEXT_TOP "Check the components you want to install.$\r$\n $\r$\nNOTE: Rana Desktop Client will be installed for ALL users."

# Installer Pages
!define MUI_WELCOMEPAGE_TITLE_3LINES
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE ${LICENSE_FILE}
!insertmacro MUI_PAGE_COMPONENTS
!define MUI_PAGE_CUSTOMFUNCTION_PRE dir_pre_callback
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!define MUI_FINISHPAGE_TITLE_3LINES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH
!insertmacro MUI_LANGUAGE "English"

Var RealUserProfile
Var CurrentUser
Var IsAdmin
Var PSReturn
Var ConsoleUser

Function GetRealUserProfile

    UserInfo::GetAccountType
    Pop $IsAdmin

    ${If} $IsAdmin == "Admin"

        ; Get interactive console user (DOMAIN\User)
        nsExec::ExecToStack 'powershell -NoProfile -Command "(Get-CimInstance Win32_ComputerSystem).UserName"'
        Pop $PSReturn
        Pop $ConsoleUser
        ${StrTrimNewLines} $ConsoleUser $ConsoleUser

        ; If no user detected, fallback to current account
        ${If} $ConsoleUser == ""
			MessageBox MB_OK 'Unable to retrieve the retrieve the console user, falling back to current user profile. This might cause the profile to be installed in the wrong user folder. In that case, please run the installer again without elevation and only install the profile component.'
            UserInfo::GetName
            Pop $0
            StrCpy $RealUserProfile $0
        ${Else}
			; Extract username only (remove DOMAIN\)
			${StrTok} $CurrentUser $ConsoleUser "\\" "2" ""
			${If} $CurrentUser == ""
				${StrTok} $CurrentUser $ConsoleUser "\\" "1" ""
			${EndIf}
			StrCpy $RealUserProfile $CurrentUser
        ${EndIf}

    ${Else}
        ; Not elevated → current user
        UserInfo::GetName
        Pop $0
        StrCpy $RealUserProfile $0
    ${EndIf}

FunctionEnd

Function dir_pre_callback
	# Don't show install directory page when account type is user
	UserInfo::GetAccountType
	Pop $0
	StrCmp $0 "User" 0 +2 ; Note: Win9x always returns "Admin"
		abort # Aborting the pre_callback skips the page
	DetailPrint "Finished directoy pre_callback"
Functionend

Section "Rana Desktop Client" SecQGIS

	SetOutPath $INSTDIR
    File .\installer-build/QGIS-OSGeo4W-${VERSION_NUMBER}.msi
    File ./resources/splash.png

    # Run the original QGIS installer
	ClearErrors
	# It is possible to set certain properties in the underlying Wix MSI
    ExecWait '"msiexec" /i "$INSTDIR\QGIS-OSGeo4W-${VERSION_NUMBER}.msi" INSTALLDIR="$INSTDIR" INSTALLDESKTOPSHORTCUTS="0" INSTALLMENUSHORTCUTS="0" /passive /L*V "$INSTDIR\install.log"' $0
	${IfNot} $0 == "0"
		MessageBox MB_ICONSTOP "Installer failed, please check install.log in installation folder"
		Abort # Install stops. Only button enabled is Cancel.
	${EndIf}

	# Copy some resources for uninstaller
	SetOutPath $INSTDIR\icons
	File ./resources/rana.ico

	# Copy global settings file, these settings replace the original inline default ones, but the user profiles’ settings will be set on top of those.
	SetOutPath $INSTDIR\apps\qgis-ltr\resources
	File /oname=qgis_global_settings.ini ${PROFILE_FOLDER}\default\QGIS\QGIS3.ini

	# Create some reg keys to add entries to the Add/Remove Programs section in the Control Pannel
	# Note that all registry entries are stored in LOCAL MACHINE namespace
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "DisplayName" "${DISPLAYED_NAME}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "DisplayVersion" "${VERSION_NUMBER}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "UninstallString" "$INSTDIR\uninstall.exe"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "DisplayIcon" "$INSTDIR\icons\rana.ico"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "HelpLink" "${WIKI_PAGE}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "URLInfoAbout" "${WEB_SITE}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}" "Publisher" "${PUBLISHER}"

	# Start and Desktop links (also pass the profile folder and global (default) setting file) for ALL users
	SetShellVarContext all

	# Only global vars are currently supported
	Var /GLOBAL UserFolder
	${GetParent} $PROFILE $UserFolder # Typically C:\Users
	# This is QGIS profile folder using Windows' %username% variable
	Var /GLOBAL GenericProfileFolder
	StrCpy $GenericProfileFolder "$UserFolder\%username%\AppData\Roaming\Rana\QGIS3"

	# C:\Users\Public\Desktop
	CreateDirectory "$DESKTOP\${QGIS_BASE}"
	CreateShortCut "$DESKTOP\${QGIS_BASE}\${QGIS_SHORTCUT_NAME}.lnk" "$INSTDIR\bin\qgis-ltr.bat" '--globalsettingsfile "$INSTDIR\apps\qgis-ltr\resources\qgis_global_settings.ini" --profiles-path "$GenericProfileFolder"' "$INSTDIR\icons\rana.ico"
	CreateShortCut "$DESKTOP\${QGIS_BASE}\OSGeo4W Shell.lnk" "$INSTDIR\OSGeo4W.bat" "" "$INSTDIR\OSGeo4W.ico"
	
	# C:\ProgramData\Microsoft\Windows\Start Menu\Programs
	CreateDirectory "$SMPROGRAMS\${QGIS_BASE}"
	CreateShortCut "$SMPROGRAMS\${QGIS_BASE}\${QGIS_SHORTCUT_NAME}.lnk" "$INSTDIR\bin\qgis-ltr.bat" '--globalsettingsfile "$INSTDIR\apps\qgis-ltr\resources\qgis_global_settings.ini" --profiles-path "$GenericProfileFolder"' "$INSTDIR\icons\rana.ico"
	CreateShortCut "$SMPROGRAMS\${QGIS_BASE}\OSGeo4W Shell.lnk" "$INSTDIR\OSGeo4W.bat" "" "$INSTDIR\OSGeo4W.ico"

	# Write some registry to set up Protocol Handler
	${StrRep} $0 $GenericProfileFolder "%" "%%"
	WriteRegStr HKCR "rana" "" "URL:rana Protocol"
    WriteRegStr HKCR "rana" "URL Protocol" ""
	WriteRegStr HKCR "rana\shell" "" ""
	WriteRegStr HKCR "rana\shell\open" "" ""
	WriteRegStr HKCR "rana\shell\open\command" "" '"$INSTDIR\bin\qgis-ltr.bat" --globalsettingsfile "$INSTDIR\apps\qgis-ltr\resources\qgis_global_settings.ini" --profiles-path "$0" -F "%1"' 
	
    WriteUninstaller $INSTDIR\uninstall.exe
SectionEnd

Section "Rana User Profile" SecProfile

	SetOverwrite try

	SetShellVarContext current
	Var /GLOBAL INSTDIR_PROFILE_DATA

	# Store the real user profile name in a global variable, this is needed to
	# correctly set the profile path when the installer is run with elevated privileges.
	Call GetRealUserProfile
	Var /GLOBAL UsersFolder
	${GetParent} $PROFILE $UsersFolder # Typically C:\Users
	StrCpy $INSTDIR_PROFILE_DATA "$UsersFolder\$RealUserProfile\AppData\Roaming\Rana\QGIS3\profiles"
    CreateDirectory "$INSTDIR_PROFILE_DATA"
    
	; Add Profile files
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
    ExecWait '"msiexec" /x "$INSTDIR\QGIS-OSGeo4W-${VERSION_NUMBER}.msi" INSTALLDIR="$INSTDIR" /quiet /L*V "$APPDATA\Rana\QGIS3\uninstall.log"'

	# Remove the program from the Add/Remove Programs section in the Control Pannel
	DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${QGIS_BASE}"
 
	SetShellVarContext all
	
	# Remove start and desktop links
	RMDir /r "$DESKTOP\${QGIS_BASE}"
	RMDir /r "$SMPROGRAMS\${QGIS_BASE}"
	
	Delete $INSTDIR\uninstall.exe
    RMDir /r $INSTDIR

    # No need to remove profile data
SectionEnd

# .onInit Function (called when the installer is nearly finished initializing)
Function .onInit
	SetShellVarContext current
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

	UserInfo::GetAccountType
	Pop $0
	StrCmp $0 "User" user_is_user user_is_admin
	user_is_user:
		!insertmacro UnselectSection  ${SecQGIS}
		!insertmacro SetSectionFlag ${SecQGIS} ${SF_RO}
		MessageBox MB_OK 'You do not have administrator privileges. You cannot use it for installing the Rana Desktop Client application.'
	user_is_admin:
		DetailPrint "Checking existing profile"

	# Uncheck profile install when default profile is present
	Var /GLOBAL INSTDIR_PROFILE_FOLDER
	Call GetRealUserProfile
	Var /GLOBAL CUsers
	${GetParent} $PROFILE $CUsers # Typically C:\Users
	StrCpy $INSTDIR_PROFILE_FOLDER "$CUsers\$RealUserProfile\AppData\Roaming\Rana\QGIS3\profiles"
	IfFileExists "$INSTDIR_PROFILE_FOLDER\default\*.*" present missing
	present:
		!insertmacro UnselectSection  ${SecProfile}
	missing:


FunctionEnd

; Set section descriptions
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
!insertmacro MUI_DESCRIPTION_TEXT ${SecQGIS} "Installs the QGIS application (for all users)."
!insertmacro MUI_DESCRIPTION_TEXT ${SecProfile} "Installs a default user profile. WARNING: an existing default profile will be overwritten!"
!insertmacro MUI_FUNCTION_DESCRIPTION_END
