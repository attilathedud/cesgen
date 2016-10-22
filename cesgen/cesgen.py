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

    def create_file( self, file_path, str_to_write ):
        if not os.path.exists( file_path ):
            new_file = open( file_path, 'w' )

            new_file.write( str_to_write )

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


    def generate_manifest_boiler( self, project_name, new_tab ):
        manifest_boiler = \
'{\n\
    "manifest_version"  :     2,\n\
    "name"              :     "' + project_name + '",\n\
    "short_name"        :     "' + project_name.replace(" ", "") + '",\n\
    "version"           :     "1.0.0",\n\
    "description"       :     "' + project_name + '."' 

        if new_tab == True:
            manifest_boiler = manifest_boiler + \
',\n\
    "chrome_url_overrides" : {\n\
        "newtab" : "main.html"\n\
    }'
    
        manifest_boiler = manifest_boiler + \
'\n\
}\n'

        return manifest_boiler

    def generate_layout_boiler( self ):
        html_boiler = \
'<!DOCTYPE html>\n\
<html lang="en">\n\
<head>\n\
	<title></title>\n\
\n\
    <!-- css -->\n\
	<link rel="stylesheet" href="" type="text/css">\n\
</head>\n\
\n\
<body>\n\
\n\
    <!-- scripts -->\n\
	<script src=""></script>\n\
</body>\n\
</html>'

        return html_boiler

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
                self.create_file( bg_script_path, '' )
                
            if self.chkIncludeContentScripts.isChecked( ):
                content_script_path = os.path.join( scripts_path, "injected.js" )
                self.create_file( content_script_path, '' )

            if self.chkIncludeOptions.isChecked( ):
                options_script_path = os.path.join( scripts_path, "settings.js" )
                popup_options_script_path = os.path.join( scripts_path, "popup_settings.js" )

                self.create_file( options_script_path, '' )
                self.create_file( popup_options_script_path, '' )

        # Create the layout section
        if self.chkIncludeLayouts.isChecked( ) or self.chkIncludeOptions.isChecked( ) or \
            self.chkPermNewTab.isChecked( ):
            layouts_path = os.path.join( project_path, "pages" )
            if not os.path.exists( layouts_path ):
                os.makedirs( layouts_path )

            if self.chkPermNewTab.isChecked( ):
                new_tab_layout_path = os.path.join( layouts_path, "newtab.html" )
                self.create_file( new_tab_layout_path, self.generate_layout_boiler( ) )

            if self.chkIncludeOptions.isChecked( ):
                options_layout_path = os.path.join( layouts_path, "settings.html" )
                popup_options_layout_path = os.path.join( layouts_path, "popup_settings.html" )

                self.create_file( options_layout_path, self.generate_layout_boiler( ) )
                self.create_file( popup_options_layout_path, self.generate_layout_boiler( ) )

        # Create the css section
        if self.chkIncludeCss.isChecked():
            self.create_and_copy_directory( project_path, "css", str( self.leIncludeCssDirectory.text() ) )

        # Create the img section
        if self.chkIncludeImgs.isChecked():
            self.create_and_copy_directory( project_path, "imgs", str( self.leIncludeImgsDirectory.text() ) )
        
        # Create the manifest file
        manifest_path = os.path.join( project_path, "manifest.json" )
        self.create_file( manifest_path, 
            self.generate_manifest_boiler( 
                str( self.leProjectName.text( ) ),
                self.chkPermNewTab.isChecked( )
                ) 
        )

if __name__ == '__main__':
    app = QtGui.QApplication( sys.argv )
    form = CesgenApp( )
    form.show( )
    app.exec_( )
