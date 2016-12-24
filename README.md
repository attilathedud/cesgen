# Chrome Extension Skeleton Generator

Chrome Extension Skeleton Generator (or cesgen) is a python utility designed to allow rapid prototyping of Chrome Extensions.

![Application Main Screen](/promos/promo_1.png?raw=true "Application Main Screen")

Some of the features:
- Crafts a maintainable folder structure for development.
- Takes cares of permissions and script syntax in the manifest file.
- Copies over css/img directories into your projects.
- Creates background and content-scripts with options and context-menu code added.
- Quick creation of custom homepage extensions.

The code is licensed under the Apache License, which means you are free to modify it however you desire.

## 1.1.1 Changelog
- Fixed a bug where iterating through options wouldn't work on newer versions of Chrome.
- Streamlined the option retrieval boilerplate.

## 1.1.0 Changelog
- Added "external" folder for any third-party javascript libraries.
- Added support for generation of css-partnered content-script generation.
- "use strict"; set as default mode for all created javascript files.
- Added visual feedback when generation is finally complete.
- Added support for icon generation and boiler code.
- Fixed a bug where blank spaces caused some weird unicode-rendering errors.
- Cleaned up the folder structure. 

### Custom Homepage
Creating a custom homepage is a classic "Hello World" type project when it comes to programming. Instead of loading your custom homepage off of file://, cesgen makes it easy to package your homepage as an Extension and distribute it.

Simply select the "New Tab" permission like so:

![New Tab Main Screen](/promos/promo_2.png?raw=true "New Tab Main Screen")

(If you already have a css file you are using, put it in the "Include CSS" section so it will be imported automatically.)

The following folder structure will be created:

![New Tab Folder](/promos/promo_2a.png?raw=true "New Tab Folder")

Your newtab page is located at pages/newtab.html. Modify it however you want.

Now all you have to do is choose to load the extension:

![Load Unpacked Extension](/promos/promo_3.png?raw=true "Load Unpacked Extension")

And just like that, your newtab is ready for use, no messing around with config files:

![Extension Loaded](/promos/promo_4.png?raw=true "Extension Loaded")

### Simple Custom Extension
How about we create a simple extension that allows you to change the page title to whatever you select and right-click on. The end result:

![Custom Extension](/promos/promo_7.png?raw=true "Custom Extension")

For this project we need background scripts (to listen for context-menu clicks), content-scripts (to modify the DOM of the page), and the context-menu permission:

![Custom Extension Options](/promos/promo_5.png?raw=true "Custom Extension Options")

It generates the following structure:

![Custom Extension Folders](/promos/promo_6.png?raw=true "Custom Extension Folders")

Open scripts/background.js and uncomment the code like it directs:
```js
function contextMenu_onclick( info, tab ) {
    var text_selected = info.selectionText;
    /* Uncomment to send a message out to content-scripts */
    var tab_id = 0;

    chrome.tabs.query({
        "active"        : true,
        "currentWindow" : true
    }, function (tabs) {
        tab_id = tabs[ 0 ].id;

        chrome.tabs.sendMessage( tab_id, {
            "function" : "context_menu_clicked",
            "text_selected" : text_selected
        });
    });
};

chrome.contextMenus.create({
    "title"     : "My Custom Extension",
    "contexts"  : [ "all" ],
    "onclick"   : contextMenu_onclick
});
```

We see that the selected text is being passed via the text_selected member. In scripts/injected.js, set the document.title to this:
```js
chrome.extension.onMessage.addListener( function ( message, sender, callback ) {
    if ( message.function == "context_menu_clicked" ) {
        //execute context_menu function
        document.title = message.text_selected;
    }
});
```

With one line of code we have easily accomplished our job!

### Build & Development
cesgen is built with Python 2.7 and Qt4. To change the Qt interface, make sure you run ./build_res.sh after modifying the .ui file.
