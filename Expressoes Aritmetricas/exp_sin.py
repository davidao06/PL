import ply.yacc as yacc
from exp_lex import tokens

def p_gramatica(p):
    '''
    EXP : EXP PLUS MULTDIV
        | EXP MINUS MULTDIV
        | MULTDIV
    MULTDIV : MULTDIV DIV PARENTESES
        | MULTDIV MULT PARENTESES
        | PARENTESES
    PARENTESES : NUM
               | PA EXP PF
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
