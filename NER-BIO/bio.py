import re
import ply.lex as lex
import sys



states = [('FEATURE','exclusive')]

tokens = ['B',
          'I',
          'O']

def t_INITIAL_B(t):
    r'B-.+'
    conteudo = t.value[2:]
    partes = re.split(r'\s+',conteudo)
    t.lexer.begin('FEATURE')
    t.lexer.tipoFeature = partes[0]
    t.lexer.valorFeature = partes[1]
    
def t_FEATURE_B(t):
    r'B-.+'
    conteudo = t.value[2:]
    partes = re.split(r'\s+',conteudo)
    if t.lexer.tipoFeature in t.lexer.dic.keys():
        t.lexer.dic[t.lexer.tipoFeature].append(t.lexer.valorFeature)
    else:
        t.lexer.dic[t.lexer.tipoFeature] = [t.lexer.valorFeature]
    t.lexer.tipoFeature = partes[0]
    t.lexer.valorFeature = partes[1]
    
    
def t_FEATURE_I(t):
    r'I-.+'
    conteudo = t.value[2:]
    partes = re.split(r'\s+',conteudo)
    t.lexer.valorFeature += ' ' + partes[1]
    
def t_FEATURE_O(t):
    r'O.+'
    if t.lexer.tipoFeature in t.lexer.dic.keys():
        t.lexer.dic[t.lexer.tipoFeature].append(t.lexer.valorFeature)
    else:
        t.lexer.dic[t.lexer.tipoFeature] = [t.lexer.valorFeature]
    t.lexer.tipoFeature = ''
    t.lexer.valueFeature = ''
    t.lexer.begin('INITIAL')
    
def t_O(t):
    r'O.+'

def t_ANY_error(t):
    r'.|\n'
    t.lexer.skip(1)
     
lexer = lex.lex()

lexer.dic = {}
lexer.tipoFeature = ''
lexer.valorFeature = ''

for linha in sys.stdin:
    lexer.input(linha)
    for t in lexer:
        pass

print (lexer.dic)