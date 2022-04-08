import ply.yacc as yacc
from Sexp_lex import tokens,literals

def produtorio(lista):
    total = 1
    for num in lista:
        total = total * num
    return total


def somatorio(lista):
    total = 0
    for num in lista:
        total = total + num
    return total

def p_Axioma(p):
    "Axioma : Sexp"
    p[0] = p[1]
    print(p[0])
    return p

def p_Sexp_MULT(p):
    "Sexp : '(' '*' Lista ')'"
    p[0] = produtorio(p[3])
    return p

def p_Sexp_SUM(p):
    "Sexp : '(' '+' Lista ')'"
    p[0] = somatorio(p[3])
    return p

def p_Sexp_NUM(p):
    "Sexp : num"
    p[0] = p[1]
    return p

def p_Lista_Recursivo(p):
    "Lista : Lista Sexp"
    p[1].append(p[2])
    p[0] = p[1]
    return p

def p_Lista_Paragem(p):
    "Lista : Sexp Sexp"
    p[0] = []
    p[0].append(p[1])
    p[0].append(p[2])
    return p


def p_error(p):
    print("Erro sintático: ",p)
    p.parser.sucess = False
    
    

parser = yacc.yacc()

import sys
for linha in sys.stdin:
    parser.sucess = True
    parser.parse(linha)