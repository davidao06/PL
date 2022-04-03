from sys import stdin
from numpy import std
import ply.lex as lex

# Analizador léxico

tokens = ['PA','PF','ID','NUM','PLUS','MINUS','MULT','DIV','EQ','BANG','INTER','END']

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_PA(t):
    r'\('
    return t

def t_PF(t):
    r'\)'
    return t

def t_ID(t):
    r'[a-z][A-Za-z]*'
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_MULT(t):
    r'\*'
    return t

def t_DIV(t):
    r'\/'
    return t

def t_EQ(t):
    r'='
    return t

def t_END(t):
    r'!!'
    return t

def t_BANG(t):
    r'!'
    return t

def t_INTER(t):
    r'\?'
    return t

t_ignore = " \t"

def t_error(t):
    print("Erro léxico :",t.value[0])
    t.lexer.skip(1)
    return t

lexer = lex.lex()
    
#FIM DO ANALIZADOR LÉXICO
#--------------------------------------------------

# Parser recursivo descendente
# Gramática abstracta a ser implementada neste parser
'''
Programa -> Comandos {ID,BANG,INTER,END}
Comandos -> Comando Comandos {ID,BANG,INTER,END}

Comando -> ATRIB {ID}
        |PRINT {BANG}
        |READ {INTER}
        |END {END}
        
ATRIB -> ID EQ EXP {ID}
PRINT -> BANG EXP {BANG}
READ -> INTER ID  {INTER}

EXP -> TERMO EXP2 {ID,NUM,PA}
EXP2 -> PLUS EXP {PLUS}
    | MINUS EXP {MINUS}
    | EMPTY {PF,ID,BANG,INTER,END}
    
TERMO -> FATOR TERMO2 {ID,NUM,PA}
TERMO2 -> MULT TERMO {MULT}
    | DIV TERMO {DIV}
    | EMPTY {PF,ID,BANG,INTER,END,PLUS,MINUS}
    
FATOR -> ID {ID}
    |NUM {NUM}
    |PA EXP PF {PA}
'''

prox_SimbTerminal = ('Erro','',0,0)
fim = False
dicRegistos = {}

def parseError(simb):
    print("Erro sintático :", simb)

def recTerminal(simb):
    global prox_SimbTerminal
    if prox_SimbTerminal.type == simb:
        valor = prox_SimbTerminal.value
        prox_SimbTerminal = lexer.token()
        return valor
    else:
        parseError(prox_SimbTerminal)

def recTermo2(parcela1):
    global prox_SimbTerminal
    if prox_SimbTerminal is None:
        return parcela1
    elif prox_SimbTerminal.type == 'MULT':
        recTerminal('MULT')
        valor = recTermo()
        return parcela1 * valor
    elif prox_SimbTerminal.type == 'DIV':
        recTerminal('DIV')
        valor = recTermo()
        return parcela1 / valor
    elif prox_SimbTerminal.type in ['PF','BANG','INTER','END','PLUS','MINUS']:
        return parcela1
    else:
        parseError(prox_SimbTerminal)

def recFator():
    global prox_SimbTerminal
    global dicRegistos
    if prox_SimbTerminal.type == 'ID':
        id = recTerminal('ID')
        if id in dicRegistos.keys():
            valor = dicRegistos[id]
            return valor
        else :
            print("Variavel ",id,' nao está nos registos')
            return 0
    elif prox_SimbTerminal.type == 'NUM':
        return recTerminal('NUM')
    elif prox_SimbTerminal.type == 'PA':
        recTerminal('PA')
        valor = recExpressao()
        recTerminal('PF')
        return valor
    else:
        parseError(prox_SimbTerminal)


def recTermo():
    global prox_SimbTerminal
    if prox_SimbTerminal.type in ['ID','NUM','PA']:
        parcela1 = recFator()
        return recTermo2(parcela1)
    else :
        parseError(prox_SimbTerminal)

def recExpressao2(parcela1):
    global prox_SimbTerminal
    if prox_SimbTerminal is None:
        return parcela1
    elif prox_SimbTerminal.type == 'PLUS':
        recTerminal('PLUS')
        valor = recExpressao()
        return parcela1 + valor
    elif prox_SimbTerminal.type == 'MINUS':
        recTerminal('MINUS')
        valor = recExpressao()
        return parcela1 - valor
    elif prox_SimbTerminal.type in ['PF','ID','BANG','INTER','END']:
        return parcela1

def recExpressao():
    global prox_SimbTerminal
    if prox_SimbTerminal.type in ['ID','NUM','PA']:
        parcela1 = recTermo()
        return recExpressao2(parcela1)
    else :
        parseError(prox_SimbTerminal)
        
            
def recATRIB():
    global prox_SimbTerminal
    global dicRegistos
    if prox_SimbTerminal.type == 'ID':
        id = recTerminal('ID')
        recTerminal('EQ')
        valor = recExpressao()
        dicRegistos[id] = valor
    else:
        parseError(prox_SimbTerminal)
        
def recPRINT():
    global prox_SimbTerminal
    if prox_SimbTerminal.type == 'BANG':
        recTerminal('BANG')
        valor = recExpressao()
        print(valor)
    else :
        parseError(prox_SimbTerminal)
        
def recREAD():
    global prox_SimbTerminal
    global dicRegistos
    if prox_SimbTerminal.type == 'INTER':
        recTerminal('INTER')
        id = recTerminal('ID')
        linha = input("Introduza o valor para a variavel: ")
        lexer.input(linha)
        prox_SimbTerminal = lexer.token()
        valor = recExpressao()
        dicRegistos[id] = valor
    else :
        parseError(prox_SimbTerminal)
        
def recComando():
    global prox_SimbTerminal
    global fim
    if prox_SimbTerminal.type == 'ID':
        recATRIB()
    elif prox_SimbTerminal.type == 'BANG':
        recPRINT()
    elif prox_SimbTerminal.type == 'INTER':
        recREAD()
    elif prox_SimbTerminal.type == 'END':
        recTerminal('END')
        fim = True
    else:
        parseError(prox_SimbTerminal)

def recComandos():
    global prox_SimbTerminal
    if prox_SimbTerminal.type in ['ID','BANG','INTER','END']:
        recComando()
        recComandos()
    else :
        parseError(prox_SimbTerminal)
        
def recPrograma():
    global prox_SimbTerminal
    if prox_SimbTerminal.type in ['ID','BANG','INTER','END']:
        recComandos()
    else:
        parseError(prox_SimbTerminal)
    print("Fim do reconhecimento do programa")
        
def recParser(data):
    global prox_SimbTerminal
    lexer.input(data)
    prox_SimbTerminal = lexer.token()
    recPrograma()

for linha in stdin:
    lexer.input(linha)
    prox_SimbTerminal = lexer.token()
    recComando()
    if fim:
        break

print(dicRegistos)
    