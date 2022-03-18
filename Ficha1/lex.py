'''
1 + ( 2 * a )

NUM OP PA NUM OP ID PF

((2 * 3) + 5) * x 

PA PA NUM OP NUM PF OP NUM PF OP ID
'''

import ply.lex as lex

tokens = [
    "NUM",
    "PA",
    'PF',
    'ID',
    'OP',
    'SKIP'
]

t_PA = r'\('
t_NUM = r'\d+'
t_PF = r'\)'
t_ID = r'[a-zA-Z]\w*'
t_OP = r'[\-+*/]'

def t_SKIP(t):
    r'[ \n\t]'
    return t

def t_error(t):
    print('Erro')
    t.lexer.skip(1)

lexer = lex.lex()

import sys

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)