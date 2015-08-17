# ColumnSort
ColumnSort is a plugin package for Sublime Text version 3 which provides a simple means of sorting tab-separated text by column.
## Limitations
* ColumnSort allows to either specify the column (field) separation character, or let ColumnSort try to auto-detect the separator via the settings.
* Either ascending or descending sorting is available via the settings.

## Usage
1. Install the package either
   * by copyping the package to Sublime's package folder using the menu entry <kbd>Browse Packages…</kbd>, or
   * by using the very convenient [Package Control](https://packagecontrol.io) plugin and choosing the <kbd>Install Package</kbd> command from the command palette.
2. Open a file with column-separated content, or produce or paste suchlike text in a buffer.
3. Select the lines you want to include to be sorted.
4. Press <kbd>Cmd Ctrl X</kbd> on the Mac, <kbd>Ctrl Meta X</kbd> on Linux or <kbd>Ctrl Alt X</kbd> on Windows. This will produce a popup window which displays the content of the first row as separate entries to choose from. The idea behind this is that often the first row contains header descriptions which makes identifying the data in the columns much easier.
5. Select an entry in the popup window with the up and down arrow keys and press <kbd>Return</kbd> or <kbd>Enter</kbd>, or click on an entry with the mouse.
6. The selected text will be **replaced** with the sorted text.

## Settings
The settings file currently has the following options to tinkle with:

### columnsort\_field\_separator (default: <kbd>"auto"</kbd>)

Field separation character, or "auto" if ColumnSort should try to detect columns separated by
one of the following characters:
* Tabulator (\t)
* Comma (,)
* Semicolon (;)
* Colon (:)
* Vertical Bar (|)
* Forward Slash (/)
* Hash (#)

NOTE 1: The order of the field separation characters listed here is also defining their priority in
        which they will be detected and processed. As a consequence, a file which contains more than
        one field separation character will be split into columns by the first occurrence of those
        characters in top to bottom order.

NOTE 2: Currently "string escaping" using single or double quotes is not supported by the splitting
        method used. It is therefore highly recommended to stick with tab-separation for a hasslefree
        and reliable operation.

### columnsort\_skip\_header (default: <kbd>true</kbd>)
ColumnSort cannot predict if the selected text contains a header line or not. Set this property to
either true or false to indicate if you want to force a default.

If the property is set to true the first row of the selection will be only used for	column heading
display purposes and left alone during sorting which will then begin with the second line of the
selection.

### columnsort\_sort\_direction (default: <kbd>"ascending"</kbd>)
The sorting can be defined to be <kbd>"ascending"</kbd> or <kbd>"descending"</kbd> by default.
