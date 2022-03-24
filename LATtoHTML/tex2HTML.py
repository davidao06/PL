import ply.lex as lex
import sys

states = [('SECCAO','inclusive'),
          ('SUBSECCAO','inclusive'),
          ('BOLD','inclusive'),
          ('ITALICO','inclusive'),
          ('UNDERLINE','inclusive'),
          ('LISTASNUM','inclusive'),
          ('LISTASITEM','inclusive'),
          ('ITEM','inclusive')]

tokens = ['BSEC',
          'ESEC',
          'BSUBSEC',
          'ESUBSEC',
          'BOLD',
          'ITALICO',
          'UNDERLINE'
          ]


lexer = lex.lex()

for linha in sys.stdin:
    lexer.input(linha)
    for t in lexer:
        pass