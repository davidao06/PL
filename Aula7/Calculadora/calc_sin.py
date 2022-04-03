import ply.yacc as yacc
from calc_lex import tokens,literals

def p_Calc(p):
    "Calc : Comandos"
    
def p_Comandos_Lista(p):
    'Comandos : Comandos Comando'
    
def p_Comandos_Simples(p):
    'Comandos : Comando'
    
def p_Comando_Atrib(p):
    "Comando : id '=' Exp"
    p.parser.registos[p[1]] = p[3]
    
def p_Comando_Print(p):
    "Comando : '!' Exp"
    print(p[2])
    
def p_Comando_Read(p):
    "Comando : '?' id"
    linha = input("Insira o valor da variavel:")
    valor = int(linha)
    p.parser.registos[p[2]] = valor
    
def p_Comando_DUMP(p):
    "Comando : DUMP"
    print(p.parser.registos)

def p_Exp_Soma(p):
    "Exp : Exp '+' Termo"
    p[0] = p[1] + p[3]
    
def p_Exp_Sub(p):
    "Exp : Exp '-' Termo"
    p[0] = p[1] - p[3]
    
def p_Exp_Termo(p):
    "Exp : Termo"
    p[0] = p[1]
    
def p_Termo_Mult(p):
    "Termo : Termo '*' Fator"
    p[0] = p[1] * p[3]
    
def p_Termo_Div(p):
    "Termo : Termo '/' Fator"
    if p[3] != 0:
        p[0] = p[1] / p[3]
    
def p_Termo_Fator(p):
    "Termo : Fator"
    p[0] = p[1]
    
def p_Fator_ID(p):
    "Fator : id"
    if p[1] in p.parser.registos.keys():
        p[0] = p.parser.registos[p[1]]
    else:
        print("Variavel nao existe")
        p[0] = 0
    
def p_Fator_NUM(p):
    "Fator : num"
    p[0] = p[1]
    
def p_Fator_Parenteses(p):
    "Fator : '(' Exp ')'"
    p[0] = p[2]
    

def p_error(p):
    print("Erro sintático: ",p)
    p.parser.sucess = False
    
    

parser = yacc.yacc()

parser.registos = {}
parser.sucess = True

import sys
for linha in sys.stdin:
    parser.sucess = True
    parser.parse(linha)