from PyQt4 import QtGui
import sys, os

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
        
        # Create the manifest file
        manifest_path = os.path.join( project_path, "manifest.json" )
        if not os.path.exists( manifest_path ):
            manifest_file = open( manifest_path, 'w' )
            manifest_file.write( self.generate_manifest_boiler( str( self.leProjectName.text() ) ) )

            manifest_file.flush( )
            manifest_file.close( )

if __name__ == '__main__':
    app = QtGui.QApplication( sys.argv )
    form = CesgenApp( )
    form.show( )
    app.exec_( )