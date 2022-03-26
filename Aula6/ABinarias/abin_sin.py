import ply.yacc as yacc
from abin_lex import tokens

def p_gramatica(p):
    '''
    ABin : PA PF
         | PA NUM ABin ABin PF
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
