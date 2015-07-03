/**
 * @license Copyright (c) 2003-2014, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.on('instanceReady', function( evt ) {
    var editor = evt.editor;
    editor.execCommand('maximize');
});


CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
    //config.uiColor = '#AADC6E';


    // Bug fixed: <mark> tag was escaped into &lt;mark&gt;
    // Solution: Add the following
    //config.entities = false;
    //config.basicEntities = false;

    //config.entities_greek = false;
    //config.entities_latin = false;
    //config.entities_additional = '';

    //config.htmlEncodeOutput = false;
    //config.extraAllowedContent = 'mark';

    //config.plugins = '';
    //Use the same styles as the main page
    config.contentsCss = ['/static/css/paper_theme/bootstrap_theme.css', '/static/djangocms_text_ckeditor/ckeditor/contents.css'];

};

