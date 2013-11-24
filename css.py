#
# css.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-css
# License: MIT
#

import re

from SublimeLinter.lint import Linter


class CSS(Linter):
    language = ('css', 'html')
    cmd = 'csslint --format=compact'
    regex = r'''
        ^.+:\s*   # filename

        # csslint emits errors that pertain to the code as a whole,
        # in which case there is no line/col information, so that
        # part is optional.
        (?:line\ (?P<line>\d+),\ col\ (?P<col>\d+),\ )?
        (?:(?P<error>error)|(?P<warning>warning))\ -\ (?P<message>.*)$
    '''
    re_flags = re.VERBOSE | re.IGNORECASE
    word_re = r'^(#?[-\w]+)'
    tempfile_suffix = 'css'
    selectors = {
        'html': 'source.css.embedded.html'
    }

    def split_match(self, match):
        match, row, col, error, warning, message, near = super().split_match(match)

        # csslint can give general errors that apply to the document as a whole.
        # In that case we pin them to the beginning of the document.
        if row is None and message:
            row = 0
            col = 0

        return match, row, col, error, warning, message, near
