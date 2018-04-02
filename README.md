SublimeLinter-csslint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-csslint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-csslint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [csslint](https://github.com/stubbornella/csslint/wiki).
It will be used with files that have the "CSS" syntax, or within `<style>` tags in HTML files.

## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, ensure that `csslint` (version 0.10.0 or later) is installed on your system.
To install `csslint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `csslint` by typing the following in a terminal:
   ```
   npm install -g csslint
   ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

Please make sure that the path to `csslint` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

Additional SublimeLinter-csslint settings: 

|Setting|Description|
|:------|:----------|
|errors|A comma-separated list of rules to include as errors|
|warnings|A comma-separated list of rules to include as warnings|
|ignore|A comma-separated list of rules to ignore|

To get a list of the available rule names, execute `csslint --list-rules` from a terminal.

You may also use any of the `csslint` configuration options, including `.csslintrc` files and embedded rules. Please see the [csslint documentation](https://github.com/stubbornella/csslint/wiki/Command-line-interface#configuration-files) for more information.
