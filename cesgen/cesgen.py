from PyQt4 import QtGui
import sys, os, shutil

import design

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

    # Skeleton generation functions

    def create_file( self, file_path ):
        if not os.path.exists( file_path ):
            new_file = open( file_path, 'w' )

            #TODO: fill in with code
            new_file.flush( )
            new_file.close( )

    def create_and_copy_directory( self, project_path, dir_name, dir_to_copy ):
        dir_path = os.path.join( project_path, dir_name )
        if not os.path.exists( dir_path ):
            os.makedirs( dir_path )

        source_dir = dir_to_copy
        if len( dir_to_copy ) > 0:
            for temp_file in os.listdir( source_dir ):
                full_temp_file_path = os.path.join( source_dir, temp_file )
                if os.path.isfile( full_temp_file_path ):
                    shutil.copy( full_temp_file_path, dir_path )


    def generate_manifest_boiler( self, project_name ):
        manifest_boiler = \
'{\n\
    "manifest_version"  :     2,\n\
    "name"              :     "' + project_name + '",\n\
    "short_name"        :     "' + project_name.replace(" ", "") + '",\n\
    "version"           :     "1.0.0",\n\
    "description"       :     "' + project_name + '."\n\
}\n' 

        return manifest_boiler

    # TODO: Move this to a thread & show progress
    def generate_skeleton( self ):
        # Create the overall directory
        project_path = os.path.join( str( self.leDirectory.text() ), str( self.leProjectName.text( ) ) )
        if not os.path.exists( project_path ):
            os.makedirs( project_path )
        
        # Create the scripts directory
        if self.chkIncludeBgScripts.isChecked( ) or self.chkIncludeContentScripts.isChecked( ) or \
            self.chkIncludeOptions.isChecked( ) or self.chkPermContentMenus.isChecked( ) or \
            self.chkPermNotifications.isChecked( ) or self.chkPermStorage.isChecked( ):

            scripts_path = os.path.join( project_path, "scripts" )
            if not os.path.exists( scripts_path ):
                os.makedirs( scripts_path )

            if self.chkIncludeBgScripts.isChecked( ):
                bg_script_path = os.path.join( scripts_path, "background.js" )
                self.create_file( bg_script_path )
                
            if self.chkIncludeContentScripts.isChecked( ):
                content_script_path = os.path.join( scripts_path, "injected.js" )
                self.create_file( content_script_path )

            if self.chkIncludeOptions.isChecked( ):
                options_script_path = os.path.join( scripts_path, "settings.js" )
                popup_options_script_path = os.path.join( scripts_path, "popup_settings.js" )

                self.create_file( options_script_path )
                self.create_file( popup_options_script_path )

        # Create the layout section
        if self.chkIncludeLayouts.isChecked( ) or self.chkIncludeOptions( ).isChecked( ) or \
            self.chkPermNewTab.isChecked( ):
            layouts_path = os.path.join( project_path, "pages" )
            if not os.path.exists( layouts_path ):
                os.makedirs( layouts_path )

            if self.chkPermNewTab.isChecked( ):
                new_tab_layout_path = os.path.join( layouts_path, "newtab.html" )
                self.create_file( new_tab_layout_path )

            if self.chkIncludeOptions.isChecked( ):
                options_layout_path = os.path.join( layouts_path, "settings.html" )
                popup_options_layout_path = os.path.join( layouts_path, "popup_settings.html" )

                self.create_file( options_layout_path )
                self.create_file( popup_options_layout_path )

        # Create the css section
        if self.chkIncludeCss.isChecked():
            self.create_and_copy_directory( project_path, "css", str( self.leIncludeCssDirectory.text() ) )

        # Create the img section
        if self.chkIncludeImgs.isChecked():
            self.create_and_copy_directory( project_path, "imgs", str( self.leIncludeImgsDirectory.text() ) )
        
        # Create the manifest file
        manifest_path = os.path.join( project_path, "manifest.json" )
        if not os.path.exists( manifest_path ):
            manifest_file = open( manifest_path, 'w' )
            manifest_file.write( self.generate_manifest_boiler( str( self.leProjectName.text() ) ) )

            #TODO: fill in with bg/content scripts, permissions, etc.

            manifest_file.flush( )
            manifest_file.close( )

if __name__ == '__main__':
    app = QtGui.QApplication( sys.argv )
    form = CesgenApp( )
    form.show( )
    app.exec_( )