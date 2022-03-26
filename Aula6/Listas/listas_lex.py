import ply.lex as lex

tokens = ['PA','PF','NUM','VIRGULA']

t_PA = r'\['
t_PF = r'\]'
t_NUM = r'\d+'
t_VIRGULA = r','

t_ignore = " \t\n"

def t_error(t):
    print('Carater ilegal: ',t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()