#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the CSSLint plugin linter class."""

from SublimeLinter.lint import Linter, util


class CSSLint(Linter):

    """Provides an interface to the csslint executable."""

    syntax = ('css', 'css3', 'html')
    cmd = 'csslint --format=compact'
    version_args = '--version'
    version_re = r'v(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.10'
    regex = r'''(?xi)
        ^.+:\s*   # filename

        # csslint emits errors that pertain to the code as a whole,
        # in which case there is no line/col information, so that
        # part is optional.
        (?:line\ (?P<line>\d+),\ col\ (?P<col>\d+),\ )?
        (?:(?P<error>error)|(?P<warning>warning))\ -\ (?P<message>.*)
    '''
    word_re = r'^([#\.]?[-\w]+)'
    error_stream = util.STREAM_STDOUT
    tempfile_suffix = 'css'
    selectors = {
        'html': 'source.css.embedded.html'
    }
    defaults = {
        '--errors=,': '',
        '--warnings=,': '',
        '--ignore=,': ''
    }
    inline_overrides = ('errors', 'warnings', 'ignore')
    comment_re = r'\s*/\*'

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method so that general errors that do not have
        a line number can be placed at the beginning of the code.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line is None and message:
            line = 0
            col = 0

        return match, line, col, error, warning, message, near
