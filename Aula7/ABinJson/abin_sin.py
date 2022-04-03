import ply.yacc as yacc
from abin_lex import tokens
    
def p_Final(p):
    "Final : ABin"
    print(p[1])
    
def p_ABin_Vazia(p):
    "ABin : PA PF"
    p[0] = "null"
    
def p_ABin_Nodo(p):
    "ABin : PA NUM ABin ABin PF"
    p[0] = "{\n" + "\t\"root\": " + p[2] + ",\n" +  "\t\"left\": " + p[3] +",\n" + "\t\"right\": " + p[4] +",\n" + "}\n"
    
    
def p_error(p):
    print("Erro sintatico: ",p)
    
parser = yacc.yacc()

import sys
for linha in sys.stdin:
    parser.parse(linha)
