import re

matriculasPattern = r'(\d\d)(:|-|...)(\d\d)\2(\d\d)\2(\d\d)'

patternCompiled = re.compile(matriculasPattern)

matriculas = [
    '25:26:27:28',
    '25-25-25-25',
    '24:24-23-21',
    '1:24:54:65',
]

for s in matriculas:
    m = patternCompiled.search(s)
    if m:
        print('Match: ',s)
    else:
        print('No match: ',s)