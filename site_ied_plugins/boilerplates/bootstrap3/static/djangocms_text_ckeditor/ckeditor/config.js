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

//http://ckeditor.com/forums/CKEditor/Support-Bootstrap-Tables

CKEDITOR.on('dialogDefinition', function (ev) {
  var dialogName = ev.data.name;
  var dialogDefinition = ev.data.definition;

  if (dialogName == 'table' || dialogName == 'tableProperties') {

    var info = dialogDefinition.getContents('info');

    // Remove fields
    var cellSpacing = info.remove('txtCellSpace');
    var cellPadding = info.remove('txtCellPad');
    var border = info.remove('txtBorder');
    var width = info.remove('txtWidth');
    var height = info.remove('txtHeight');
    var align = info.remove('cmbAlign');

    dialogDefinition.removeContents('advanced');

    dialogDefinition.addContents( {
        id: 'advanced',
        label: 'Advanced',
        accessKey: 'A',
        elements: [
            {
                type: 'select',
                id: 'selClass',
                label: 'Select the table class',
                items: [ [ 'table' ], [ 'table table-striped'], [ 'table table-bordered'], [ 'table table-hover'], [ 'table table-condensed'] ],
                'default': 'table',
                setup: function(a) {
                    this.setValue(a.getAttribute("class") ||
                    "")
                },
                commit: function(a, d) {
                    this.getValue() ? d.setAttribute("class", this.getValue()) : d.removeAttribute("class")
                }
            }
        ]
    });
  }

});

