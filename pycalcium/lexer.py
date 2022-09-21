#The Lexer
import ply.lex as lex
from tokens import *

t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LSQU = r'\['
t_RSQU = r'\]'
t_LN = r'ln'
t_LOG = r'log'
t_PI = r'\π'
t_EULER = r'e'
t_POWER = r'\^'
t_ignore = ' \t'
t_PILATIN = 'pi'
t_SQRT = r'√'
def t_error(t):
    print("Illegal character: " + t.value[0])
    t.lexer.skip(1)
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_newline(t):
    r'\n+'
    pass