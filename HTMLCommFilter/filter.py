import ply.lex as lex
import sys


states = [('COMMENT','exclusive')]

tokens = ['BCOM',
          'ECOM',
          'IGNORE',
          'CAPTURE']

def t_BCOM(t):
    r'<!--'
    t.lexer.begin('COMMENT')
    
def t_COMMENT_ECOM(t):
    r'-->'
    t.lexer.begin('INITIAL')
    
def t_COMMENT_IGNORE(t):
    r'.|\n'
    
def t_CAPTURE(t):
    r'.|\n'
    print(t.value,end='')

    
    
lexer = lex.lex()

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        pass