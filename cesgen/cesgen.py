from PyQt4 import QtGui
import sys, os

import design
from cesgen_utils import Cesgen_Utils

class CesgenApp( QtGui.QMainWindow, design.Ui_MainWindow ):
    def __init__( self ):
        super( self.__class__, self ).__init__( )
        self.setupUi( self )

        # Set up button handlers
        self.btnDirectoryChoose.clicked.connect( self.browse_directory )
        self.btnGenerate.clicked.connect( self.generate_skeleton )

    def browse_directory( self ):
        directory = QtGui.QFileDialog.getExistingDirectory( self, "Pick a directory" )

        if directory:
            self.leDirectory.setText( directory )

    # TODO: Move this to a thread & show progress
    def generate_skeleton( self ):
        Cesgen_Utils.project_name = str( self.leProjectName.text( ) )

        # Create the overall directory
        project_path = os.path.join( str( self.leDirectory.text() ), str( self.leProjectName.text( ) ) )
        if not os.path.exists( project_path ):
            os.makedirs( project_path )
        
        # Create the scripts directory
        if self.chkIncludeBgScripts.isChecked( ) or self.chkIncludeContentScripts.isChecked( ) or \
            self.chkIncludeOptions.isChecked( ) or self.chkPermContextMenus.isChecked( ) or \
            self.chkPermNotifications.isChecked( ) or self.chkPermStorage.isChecked( ):

            scripts_path = os.path.join( project_path, "scripts" )
            if not os.path.exists( scripts_path ):
                os.makedirs( scripts_path )

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
            Cesgen_Utils.create_and_copy_directory( project_path, "css", str( self.leIncludeCssDirectory.text() ) )

        # Create the img section
        if self.chkIncludeImgs.isChecked():
            Cesgen_Utils.create_and_copy_directory( project_path, "imgs", str( self.leIncludeImgsDirectory.text() ) )
        
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
                self.chkIncludeOptions.isChecked( )
            ) 
        )

if __name__ == '__main__':
    app = QtGui.QApplication( sys.argv )
    form = CesgenApp( )
    form.show( )
    app.exec_( )
