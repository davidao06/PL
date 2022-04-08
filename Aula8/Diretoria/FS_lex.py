import ply.lex as lex

literals = ['[',']','(',')']
tokens = ['texto']

def t_texto(t):
    r'\"[^"]+\"'
    return t
    

t_ignore =" \t\n"

def t_error(t):
    print('Carater ilegal: ',t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()