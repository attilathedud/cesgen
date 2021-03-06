from PyQt4 import QtGui, QtCore
from functools import partial
import sys, os, png

import design
from cesgen_utils import Cesgen_Utils

class CesgenApp( QtGui.QMainWindow, design.Ui_MainWindow ):
    def __init__( self ):
        super( self.__class__, self ).__init__( )
        self.setupUi( self )

        # Set up button handlers
        self.btnDirectoryChoose.clicked.connect( partial( self.browse_directory, associatedLe = self.leDirectory ) )
        self.btnCssDirectoryChoose.clicked.connect( partial( self.browse_directory, associatedLe = self.leIncludeCssDirectory ) )
        self.btnImgDirectoryChoose.clicked.connect( partial( self.browse_directory, associatedLe = self.leIncludeImgsDirectory ) )
        self.btnIconDirectoryChoose.clicked.connect( partial( self.browse_directory, associatedLe = self.leIncludeIconsDirectory ) )
        self.btnGenerate.clicked.connect( self.ui_generate )

        # Set up timer
        self.creationTimer = QtCore.QTimer( )
        self.lblCreation.hide( )

    def browse_directory( self, associatedLe ):
        directory = QtGui.QFileDialog.getExistingDirectory( self, "Pick a directory" )

        if directory:
            associatedLe.setText( directory )

    def ui_generate( self ):
        if len( str( self.leProjectName.text( ) ).strip( ) ) == 0 or len( str( self.leDirectory.text() ).strip( ) ) == 0:
            msgBox = QtGui.QMessageBox( )
            msgBox.setText("Please provide the project name and the project directory.")
            msgBox.exec_()
        else:
            self.generate_skeleton( )
            self.lblCreation.show( )
            self.creationTimer.singleShot( 3000, self.hide_creation_label )

    def hide_creation_label( self ):
        self.lblCreation.hide( )

    def generate_skeleton( self ):
        Cesgen_Utils.project_name = str( self.leProjectName.text( ) ).strip( )

        # Create the overall directory
        project_path = os.path.join( str( self.leDirectory.text() ).strip( ), str( self.leProjectName.text( ) ).strip( ) )
        if not os.path.exists( project_path ):
            os.makedirs( project_path )
        
        # Create the scripts directory
        if self.chkIncludeBgScripts.isChecked( ) or self.chkIncludeContentScripts.isChecked( ) or \
            self.chkIncludeOptions.isChecked( ) or self.chkPermContextMenus.isChecked( ) or \
            self.chkPermNotifications.isChecked( ) or self.chkPermStorage.isChecked( ):

            scripts_path = os.path.join( project_path, "scripts" )
            if not os.path.exists( scripts_path ):
                os.makedirs( scripts_path )

            script_external_path = os.path.join( scripts_path, "external" )
            if not os.path.exists( script_external_path ):
                os.makedirs( script_external_path )

            if self.chkIncludeBgScripts.isChecked( ) or self.chkPermContextMenus.isChecked( ):
                bg_script_path = os.path.join( scripts_path, "background.js" )
                Cesgen_Utils.create_file( bg_script_path, Cesgen_Utils.generate_script_boiler(
                    "background.js", self.chkPermStorage.isChecked( ), self.chkPermContextMenus.isChecked( ) ) 
                )
                
            if self.chkIncludeContentScripts.isChecked( ):
                content_script_path = os.path.join( scripts_path, "injected.js" )
                Cesgen_Utils.create_file( content_script_path, Cesgen_Utils.generate_script_boiler(
                    "injected.js", self.chkPermStorage.isChecked( ), self.chkPermContextMenus.isChecked( ) ) 
                )

            if self.chkIncludeOptions.isChecked( ):
                options_script_path = os.path.join( scripts_path, "settings.js" )
                popup_options_script_path = os.path.join( scripts_path, "popup_settings.js" )

                Cesgen_Utils.create_file( options_script_path, Cesgen_Utils.generate_script_boiler(
                    "settings.js", self.chkPermStorage.isChecked( ), self.chkPermContextMenus.isChecked( ) ) 
                    )
                Cesgen_Utils.create_file( popup_options_script_path, Cesgen_Utils.generate_script_boiler(
                    "popup_settings.js", self.chkPermStorage.isChecked( ), self.chkPermContextMenus.isChecked( ) ) 
                )

        # Create the layout section
        if self.chkIncludeLayouts.isChecked( ) or self.chkIncludeOptions.isChecked( ) or \
            self.chkPermNewTab.isChecked( ):
            layouts_path = os.path.join( project_path, "pages" )
            if not os.path.exists( layouts_path ):
                os.makedirs( layouts_path )

            if self.chkPermNewTab.isChecked( ):
                new_tab_layout_path = os.path.join( layouts_path, "newtab.html" )
                Cesgen_Utils.create_file( new_tab_layout_path, Cesgen_Utils.generate_layout_boiler( False, '' ) )

            if self.chkIncludeOptions.isChecked( ):
                options_layout_path = os.path.join( layouts_path, "settings.html" )
                popup_options_layout_path = os.path.join( layouts_path, "popup_settings.html" )

                Cesgen_Utils.create_file( options_layout_path, Cesgen_Utils.generate_layout_boiler( True, 'settings' ) )
                Cesgen_Utils.create_file( popup_options_layout_path, Cesgen_Utils.generate_layout_boiler( True, 'popup_settings' ) )

        # Create the css section
        if self.chkIncludeCss.isChecked():
            Cesgen_Utils.create_and_copy_directory( project_path, "css", str( self.leIncludeCssDirectory.text() ).strip( ) )
            if self.chkIncludeContentScripts.isChecked( ):
                Cesgen_Utils.create_file( os.path.join( os.path.join( project_path, "css" ), 'injected.css' ), '' )

        # Create the img section
        if self.chkIncludeImgs.isChecked() or self.chkIncludeIcons.isChecked( ):
            Cesgen_Utils.create_and_copy_directory( project_path, "imgs", str( self.leIncludeImgsDirectory.text() ).strip( ) )
            Cesgen_Utils.create_and_copy_directory( project_path, "imgs", str( self.leIncludeIconsDirectory.text() ).strip( ) )

            if len( str( self.leIncludeIconsDirectory.text( ) ) ) == 0:
                icons_path = os.path.join( project_path, "imgs")

                for icon_size in [ 16, 32, 48, 64, 128 ]:
                    rows = [ [ icon_size - 1 ] * 4 * icon_size ] * icon_size
                    icon_writer = png.Writer( width = icon_size, height = icon_size, alpha= 'RGBA' )
                    with open( os.path.join( icons_path, "icon" + str( icon_size ) + ".png" ), 'wb' ) as icon_file:
                        icon_writer.write( icon_file, rows )

        # Create the manifest file
        manifest_path = os.path.join( project_path, "manifest.json" )
        Cesgen_Utils.create_file( manifest_path, 
            Cesgen_Utils.generate_manifest_boiler( 
                self.chkPermNewTab.isChecked( ),
                self.chkPermStorage.isChecked( ),
                self.chkPermContextMenus.isChecked( ),
                self.chkPermNotifications.isChecked( ),
                self.chkIncludeBgScripts.isChecked( ),
                self.chkIncludeContentScripts.isChecked( ),
                self.chkIncludeOptions.isChecked( ),
                self.chkIncludeCss.isChecked( ),
                self.chkIncludeIcons.isChecked( )
            ) 
        )

if __name__ == '__main__':
    app = QtGui.QApplication( sys.argv )
    form = CesgenApp( )
    form.show( )
    form.raise_( )
    app.exec_( )
