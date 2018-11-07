# Tab Group Salute, a plugin for gedit

Switch between tab groups using Ctrl+\` / Ctrl+Shift+\` (backquote /
backtick)  
<https://github.com/jefferyto/gedit-tab-group-salute>  
0.1.0

All bug reports, feature requests and miscellaneous comments are welcome
at the [project issue tracker][].

## Requirements

This plugin requires gedit 3.12 or newer.

## Installation

1.  Download the source code (as [zip][] or [tar.gz][]) and extract.
2.  Copy the `tab-group-salute` folder and the `tab-group-salute.plugin`
    file into `~/.local/share/gedit/plugins` (create if it does not
    exist).
3.  Restart gedit, then activate the plugin in the **Plugins** tab in
    gedit's **Preferences** window.

## Usage

*   <kbd>Ctrl</kbd>+<kbd>\`</kbd> - Move forward to the next tab group
*   <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>\`</kbd> - Move backward to
    the previous tab group

Note that <kbd>Ctrl</kbd>+<kbd>~</kbd> (equivalent to
<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>\`</kbd>) is originally assigned
in gedit to toggle (invert) case of selected text. This plugin will
override this assignment.

## Credits

Inspired by:

*   A [request for help][] with [Control Your Tabs][]

## License

Copyright &copy; 2018 Jeffery To <jeffery.to@gmail.com>

Available under GNU General Public License version 3


[project issue tracker]: https://github.com/jefferyto/gedit-tab-group-salute/issues
[zip]: https://github.com/jefferyto/gedit-tab-group-salute/archive/master.zip
[tar.gz]: https://github.com/jefferyto/gedit-tab-group-salute/archive/master.tar.gz
[request for help]: https://github.com/jefferyto/gedit-control-your-tabs/issues/11
[Control Your Tabs]: https://github.com/jefferyto/gedit-control-your-tabs
