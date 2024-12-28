# Tab Group Salute, a plugin for gedit

Switch between tab groups using Ctrl+\<key above Tab\>  
<https://github.com/jefferyto/gedit-tab-group-salute>  
0.3.0

All bug reports, feature requests, and miscellaneous comments are
welcome at the [project issue tracker].

Be sure to watch the project on GitHub to receive notifications for new
releases.

[project issue tracker]: https://github.com/jefferyto/gedit-tab-group-salute/issues

## Requirements

This plugin requires gedit 3.12 or newer.

## Installation

1.  Download the [latest release] and extract.
2.  Copy the `tab-group-salute` folder and the `tab-group-salute.plugin`
    file into `~/.local/share/gedit/plugins` (create if it does not
    exist).
3.  Restart gedit, then activate the plugin in the **Plugins** tab in
    gedit’s **Preferences** window.

[latest release]: https://github.com/jefferyto/gedit-tab-group-salute/releases/latest

## Usage

This plugin adds keyboard shortcuts that use the key above the
<kbd>Tab</kbd> key, written here as <kbd>\`</kbd> (grave accent /
backquote / backtick):

*   <kbd>Ctrl</kbd>+<kbd>\`</kbd> - Move forward to the next tab group
*   <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>\`</kbd> - Move backward to
    the previous tab group

These shortcuts may override the "invert case" shortcut
(<kbd>Ctrl</kbd>+<kbd>~</kbd>), if the key above the <kbd>Tab</kbd> key
produces the tilde symbol.

## Contributing

The code in `tab-group-salute/utils` comes from [python-gtk-utils];
changes should ideally be contributed to that project, then pulled back
into this one with `git subtree pull`.

[python-gtk-utils]: https://github.com/jefferyto/python-gtk-utils

## Credits

Inspired by:

*   A [request] from [Control Your Tabs]

[request]: https://github.com/jefferyto/gedit-control-your-tabs/issues/11
[Control Your Tabs]: https://github.com/jefferyto/gedit-control-your-tabs

## License

Copyright © 2018 Jeffery To <jeffery.to@gmail.com>

Available under GNU General Public License version 2 or later

## Other plugins you may like

*   [Control Your Tabs]  
    Switch between document tabs using Ctrl+Tab and other common keyboard shortcuts

*   [Ex-Mortis]  
    Reopen closed windows and optionally restore windows between sessions

*   [Python Console]  
    Interactive Python console standing in the bottom panel

[Control Your Tabs]: https://github.com/jefferyto/gedit-control-your-tabs
[Ex-Mortis]: https://github.com/jefferyto/gedit-ex-mortis
[Python Console]: https://github.com/jefferyto/gedit-pythonconsole
