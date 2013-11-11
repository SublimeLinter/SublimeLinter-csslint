#
# css.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-css
# License: MIT
#

from SublimeLinter.lint import Linter


class CSS(Linter):
    language = 'css'
    cmd = ('csslint', '--format=compact')
    regex = (
        r'(?i)^.+: (?:line (?P<line>\d+), col (?P<col>\d+), )?'
        r'(?P<type>(?:error|warning)) - (?P<error>.*)$'
    )
    tempfile_suffix = '.css'

    def split_match(self, match):
        match, row, col, error_type, error, near = super().split_match(match)

        # csslint can give general errors that apply to the document as a whole.
        # In that case we pin them to the beginning of the document.
        if row is None and error:
            row = 0
            col = 0

        return match, row, col, error_type, error, near
