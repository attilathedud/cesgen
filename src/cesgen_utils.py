import sys, os, shutil

class Cesgen_Utils:

    project_name = ''

    @staticmethod
    def create_file( file_path, str_to_write ):
        if not os.path.exists( file_path ):
            new_file = open( file_path, 'w' )

            new_file.write( str_to_write )

            new_file.flush( )
            new_file.close( )

    @staticmethod
    def create_and_copy_directory( project_path, dir_name, dir_to_copy ):
        dir_path = os.path.join( project_path, dir_name )
        if not os.path.exists( dir_path ):
            os.makedirs( dir_path )

        source_dir = dir_to_copy
        if len( dir_to_copy ) > 0:
            for temp_file in os.listdir( source_dir ):
                full_temp_file_path = os.path.join( source_dir, temp_file )
                if os.path.isfile( full_temp_file_path ):
                    shutil.copy( full_temp_file_path, dir_path )

    @staticmethod
    def generate_manifest_boiler( perm_new_tab, perm_storage, 
                                    perm_context_menus, perm_notifications, 
                                    background_scripts, content_scripts, 
                                    option_pages, include_css, include_icons ):
        manifest_boiler = \
'{\n\
    "manifest_version"  :     2,\n\
    "name"              :     "' + Cesgen_Utils.project_name + '",\n\
    "short_name"        :     "' + Cesgen_Utils.project_name.replace( " ", "" ) + '",\n\
    "version"           :     "1.0.0",\n\
    "description"       :     "' + Cesgen_Utils.project_name + '."' 

        if perm_storage == True or perm_context_menus == True or perm_notifications == True:
            manifest_boiler = manifest_boiler + \
',\n\
    "permissions" : [\n'

            if perm_storage == True:
                manifest_boiler = manifest_boiler + '        "storage"'

                if perm_storage + perm_context_menus + perm_notifications > 1:
                    manifest_boiler = manifest_boiler + ',\n'

            if perm_context_menus == True:
                manifest_boiler = manifest_boiler + '        "contextMenus"'

                if perm_storage + perm_context_menus + perm_notifications > 2:
                    manifest_boiler = manifest_boiler + ',\n'

            if perm_notifications == True:
                manifest_boiler = manifest_boiler + '        "notifications"'

            manifest_boiler = manifest_boiler + '\n    ]'

        if include_icons == True:
            manifest_boiler = manifest_boiler + \
',\n\
    "icons" : {\n\
        "16" : "imgs/icon16.png",\n\
        "32" : "imgs/icon32.png",\n\
        "48" : "imgs/icon48.png",\n\
        "64" : "imgs/icon64.png",\n\
        "128": "imgs/icon128.png"\n\
    }'

        if perm_new_tab == True:
            manifest_boiler = manifest_boiler + \
',\n\
    "chrome_url_overrides" : {\n\
        "newtab" : "pages/newtab.html"\n\
    }'

        if background_scripts == True or perm_context_menus == True:
            manifest_boiler = manifest_boiler + \
',\n\
    "background" : {\n\
        "scripts" : [ "scripts/background.js" ]\n\
    }'

        if content_scripts == True:
            manifest_boiler = manifest_boiler + \
',\n\
    "content_scripts" : [ {\n\
        "matches" : [ "<all_urls>" ],\n'

            if include_css == True:
                manifest_boiler = manifest_boiler + \
        '\t"css" : [ "css/injected.css" ],\n'

            manifest_boiler = manifest_boiler + \
        '\t"js" : [\n\
            "scripts/injected.js"\n\
        ]\n\
    } ]'

        if option_pages == True:
            manifest_boiler = manifest_boiler + \
',\n\
    "options_page" : "pages/settings.html",\n\
    "browser_action" : {\n\
        "name"  : "' + Cesgen_Utils.project_name + '",\n\
        "default_popup": "pages/popup_settings.html"\n\
    }'
    
        manifest_boiler = manifest_boiler + \
'\n\
}\n'

        return manifest_boiler

    @staticmethod
    def generate_layout_boiler( is_option_page, option_page_name ):
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
	<script src="'
    
        if is_option_page == True:
            html_boiler = html_boiler + '../scripts/' + option_page_name + '.js'

        html_boiler = html_boiler + \
'"></script>\n\
</body>\n\
</html>'

        return html_boiler

    @staticmethod
    def generate_script_boiler( file_name, perm_storage, perm_context_menus ):
        script_boiler = '"use strict";\n\n'

        if perm_storage == True:
            script_boiler = script_boiler + \
'//Option related settings\n\
var options = {\n\
    //"Option_1" : "Value_1",\n\
    //"Option 2" : "Value 2"\n\
};\n\
\n\
chrome.storage.onChanged.addListener( function( changes, namespace ) {\n\
    for ( var key in changes ) {\n\
        var storageChange = changes[ key ];\n\
\n\
        options[ key ] = storageChange.newValue;\n\
    }\n\
});\n\
\n\
chrome.storage.local.get({\n\
    options\n\
}, function( items ) {\n\
    for( var key in items ) {\n\
        options[ key ] = items[ key ];\n\
    }\n\
});\n\n'

        if perm_context_menus == True and file_name == "background.js":
            script_boiler = script_boiler + \
'function contextMenu_onclick( info, tab ) {\n\
    var text_selected = info.selectionText;\n\
    /* Uncomment to send a message out to content-scripts\n\
    var tab_id = 0;\n\
\n\
    chrome.tabs.query({\n\
        "active"        : true,\n\
        "currentWindow" : true\n\
    }, function (tabs) {\n\
        tab_id = tabs[ 0 ].id;\n\
\n\
        chrome.tabs.sendMessage( tab_id, {\n\
            "function" : "context_menu_clicked",\n\
            "text_selected" : text_selected\n\
        });\n\
    });\n\
    */\n\
};\n\
\n\
chrome.contextMenus.create({\n\
    "title"     : "' + Cesgen_Utils.project_name + '",\n\
    "contexts"  : [ "all" ],\n\
    "onclick"   : contextMenu_onclick\n\
});\n'
        if perm_context_menus == True and file_name == "injected.js":
            script_boiler = script_boiler + \
'chrome.extension.onMessage.addListener( function ( message, sender, callback ) {\n\
    if ( message.function == "context_menu_clicked" ) {\n\
        //execute context_menu function\n\
    }\n\
});\n'

        return script_boiler
