import re
from collections import namedtuple

Token = namedtuple('Token',
            ['type', 'value', 'lineno', 'columno'])

def tokens(source, definitions, ignore_case=True):
    """Yield a token if part of the source matched one
    of the token definitions."""
    re_definitions = [ (re.compile(t_def[0], re.I),
                        t_def[1]) for t_def in definitions ]

    # Break sources into lines
    lines = source.split("\n")
    for lineno, line in enumerate(lines):
        columno = 0
        while columno < len(line):
            match = None
            for t_def, t_type in re_definitions:
                match = t_def.match(line, columno)
                if match:
                    yield Token(type=t_type, value=match.group(0),
                        lineno=lineno, columno=columno)
                    columno = match.end()
                    break
            if not match:
                yield Token(type="UNKNOWN_TOKEN", value=line[columno],
                    lineno=lineno, columno=columno)
                columno += 1


#definitions = [
#    (r'hello', 'HELLO'),
#    (r'\d+', 'NUMBER'),
#    (r'\w+', 'WORD')
#]

#for x in tokens("123 hello what? \nhello123 hello what", definitions):
#    print x
