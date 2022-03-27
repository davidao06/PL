import ply.lex as lex
import re

tokens = ['PLUS','MINUS','MULT','DIV','NUM','PA','PF']

def t_NUM(t):
    r'\d+'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'\-'
    return t
    
def t_DIV (t):
    r'\/'
    return t
    
def t_MULT(t):
    r'\*'
    return t    
    
def t_PA(t):
    r'\('
    return t
    
def t_PF(t):
    r'\)'
    return t

t_ignore = " \t\n"

def t_error(t):
    print('Carater ilegal: ',t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
