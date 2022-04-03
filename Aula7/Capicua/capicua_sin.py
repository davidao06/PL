import ply.yacc as yacc
from capicua_lex import tokens

def p_gramatica(p):
    '''
    Capicua : Z Capicua Z
            | O Capicua O
            | Z
            | O
            |
    '''
    
def p_error(p):
    print("Erro sintatico: ",p)
    parser.sucess = False
    
parser = yacc.yacc()

import sys
for linha in sys.stdin:
    parser.sucess = True
    parser.parse(linha)
    if parser.sucess:
        print("Frase valida: ",linha)
    else:
        print("Frase invalida: ",linha)
