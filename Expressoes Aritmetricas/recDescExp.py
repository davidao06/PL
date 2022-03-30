from sys import stdin
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
Comandos -> Comando Comandos {ID,BANG,INTER}
        | empty {END}

Comando -> ATRIB {ID}
        |PRINT {BANG}
        |READ {INTER}
        
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

def parseError(simb):
    print("Erro sintático :", simb)

def recTerminal(simb):
    global prox_SimbTerminal
    if prox_SimbTerminal.type == simb:
        prox_SimbTerminal = lexer.token()
    else:
        parseError(prox_SimbTerminal)

def recTermo2():
    global prox_SimbTerminal
    if prox_SimbTerminal.type == 'MULT':
        recTerminal('MULT')
        recTermo()
    elif prox_SimbTerminal.type == 'DIV':
        recTerminal('DIV')
        recTermo()
    elif prox_SimbTerminal.type in ['PF','BANG','INTER','END','PLUS','MINUS']:
        pass
    else:
        parseError(prox_SimbTerminal)

def recFator():
    global prox_SimbTerminal
    if prox_SimbTerminal.type == 'ID':
        recTerminal('ID')
    elif prox_SimbTerminal.type == 'NUM':
        recTerminal('NUM')
    elif prox_SimbTerminal.type == 'PA':
        recTerminal('PA')
        recExpressao()
        recTerminal('PF')
    else:
        parseError(prox_SimbTerminal)


def recTermo():
    global prox_SimbTerminal
    if prox_SimbTerminal.type in ['ID','NUM','PA']:
        recFator()
        recTermo2()
    else :
        parseError(prox_SimbTerminal)

def recExpressao2():
    global prox_SimbTerminal
    if prox_SimbTerminal.type == 'PLUS':
        recTerminal('PLUS')
        recExpressao()
    elif prox_SimbTerminal.type == 'MINUS':
        recTerminal('MINUS')
        recExpressao()
    elif prox_SimbTerminal.type in ['PF','ID','BANG','INTER','END']:
        pass

def recExpressao():
    global prox_SimbTerminal
    if prox_SimbTerminal.type in ['ID','NUM','PA']:
        recTermo()
        recExpressao2()
    else :
        parseError(prox_SimbTerminal)
        
            
def recATRIB():
    global prox_SimbTerminal
    if prox_SimbTerminal.type == 'ID':
        recTerminal('ID')
        recTerminal('EQ')
        recExpressao()
    else:
        parseError(prox_SimbTerminal)
        
def recPRINT():
    global prox_SimbTerminal
    if prox_SimbTerminal.type == 'BANG':
        recTerminal('BANG')
        recExpressao()
    else :
        parseError(prox_SimbTerminal)
        
def recREAD():
    global prox_SimbTerminal
    if prox_SimbTerminal.type == 'INTER':
        recTerminal('INTER')
        recTerminal('ID')
    else :
        parseError(prox_SimbTerminal)
        
def recComando():
    global prox_SimbTerminal
    if prox_SimbTerminal.type == 'ID':
        recATRIB()
    elif prox_SimbTerminal.type == 'BANG':
        recPRINT()
    elif prox_SimbTerminal.type == 'INTER':
        recREAD()
    else:
        parseError(prox_SimbTerminal)

def recComandos():
    global prox_SimbTerminal
    if prox_SimbTerminal.type in ['ID','BANG','INTER']:
        recComando()
        recComandos()
    elif prox_SimbTerminal.type == 'END':
        pass
    else :
        parseError(prox_SimbTerminal)
        
def recPrograma():
    global prox_SimbTerminal
    if prox_SimbTerminal.type in ['ID','BANG','INTER','END']:
        recComandos()
        recTerminal('END')
    else:
        parseError(prox_SimbTerminal)
    print("Fim do reconhecimento do programa")
        
def recParser(data):
    global prox_SimbTerminal
    lexer.input(data)
    prox_SimbTerminal = lexer.token()
    recPrograma()

recParser(stdin.read())


    





    