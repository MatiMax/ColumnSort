# ColumnSort
ColumnSort is a plugin package for Sublime Text version 3 which provides a simple means of sorting tab-separated text by column.
## Limitations
* ColumnSort currently only works with tabular text which has its columns separated with a tab character ('\t' or '\x09').
* Currently only ascending sorting is available.

## Usage
1. Install the package either
   * by copyping the package to Sublime's package folder using the menu entry <kbd>Browse Packages…</kbd>, or
   * by using the very convenient [Package Control](https://packagecontrol.io) plugin and choosing the <kbd>Install Package</kbd> command from the command palette.
2. Open a file with tab-separated content, or produce or paste suchlike text in a buffer.
3. Select the lines you want to include to be sorted.
4. Press <kbd>Cmd Ctrl X</kbd> on the Mac, <kbd>Ctrl Meta X</kbd> on Linux or <kbd>Ctrl Alt X</kbd> on Windows. This will produce a popup window which displays the content of the first row as separate entries to choose from. The idea behind this is that often the first row contains header descriptions which makes identifying the data in the columns much easier.
5. Select an entry in the popup window with the up and down arrow keys and press <kbd>Return</kbd> or <kbd>Enter</kbd>, or click on an entry with the mouse.
6. The selected text will be **replaced** with the sorted text.
