SublimeLinter-csslint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-csslint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-csslint)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [csslint](https://github.com/stubbornella/csslint/wiki). It will be used with files that have the “CSS” syntax, or within `<style>` tags in HTML files.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `csslint` is installed on your system. To install `csslint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `csslint` by typing the following in a terminal:
   ```
   npm install -g csslint
   ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

**Note:** This plugin requires `csslint` 0.10.0 or later.

### Linter configuration
In order for `csslint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `csslint` is installed and configured, you can proceed to install the SublimeLinter-csslint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `csslint`. Among the entries you should see `SublimeLinter-csslint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

In addition to the standard SublimeLinter settings, SublimeLinter-csslint provides its own settings which correspond to the command line options of the same name. All of them may be used as [inline overrides](http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-overrides).

|Setting|Description|
|:------|:----------|
|errors|A comma-separated list of rules to include as errors|
|warnings|A comma-separated list of rules to include as warnings|
|ignore|A comma-separated list of rules to ignore|

To get a list of the available rule names, execute `csslint --list-rules` from a terminal.

You may also use any of the `csslint` configuration options, including `.csslintrc` files and embedded rules. Please see the [csslint documentation](https://github.com/stubbornella/csslint/wiki/Command-line-interface#configuration-files) for more information.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass csslint and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
