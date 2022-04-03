from lib2to3.pgen2 import token
import ply.lex as lex

tokens = ['Z','O']

t_Z = '0'
t_O = '1'

t_ignore = " \t\n"

def t_error(t):
    print('Carater ilegal: ',t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()