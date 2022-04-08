import ply.yacc as yacc
from FS_lex import tokens,literals



def p_Axioma(p):
    "Axioma : Dir"
    print(p[1])
    return p

def p_Dir_Conteudo(p):
    "Dir : '(' texto Conteudo ')'"
    p[0] = ['mkdir '+ p[2]] + [f'cd {p[2]}'] + p[3] + ["cd .."]
    return p

def p_Dir_Ficheiro(p):
    "Dir : Ficheiro"
    p[0] = [p[1]]
    return p

def p_Conteudo_Recursivo(p):
    "Conteudo : Conteudo Dir"
    p[0] = p[1] + p[2]
    return p

def p_Conteudo_Paragem(p):
    "Conteudo : "
    p[0] = []
    return p

def p_Ficheiro(p):
    "Ficheiro : '[' texto texto ']'"
    p[0] = f'cp {p[3]} {p[2]}'
    return p


def p_error(p):
    print("Erro sintático: ",p)
    
    

parser = yacc.yacc()

import sys
linha = sys.stdin.read()
parser.parse(linha)