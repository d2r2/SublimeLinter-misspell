from SublimeLinter.lint import util, Linter, WARNING


class Misspell(Linter):
    cmd = 'misspell'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDOUT
    default_type = WARNING
    defaults = {
        'selector': 'source.go, source.c, source.c++, source.js, source.ruby, source.java'
    }
