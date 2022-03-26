import ply.yacc as yacc
from listas_lex import tokens

def p_gramatica(p):
    '''
    Lista : PA Lista2
    Lista2 : Conteudo PF
           | PF
    Conteudo : Elem VIRGULA Conteudo
             | Elem
    Elem : NUM
         | Lista
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
