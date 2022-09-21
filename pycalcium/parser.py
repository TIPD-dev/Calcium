import ply.yacc as yacc

#Error Handler
def p_error(p):
    print("Syntax Error!")

#Basic Arithmetic
def p_expression_add(p):
    'expression : expression ADD term'
    p[0] = p[1] + p[3]
def p_expression_sub(p):
    'expression : expression SUB term'
    p[0] = p[1] - p[3]
def p_term_mul(p):
    'term : term MUL factor'
    p[0] = p[1] * p[3]
def p_term_div(p):
    'term : term DIV factor'
    p[0] = p[1] / p[3]
def p_factor_int(p):
    'factor : INT'
    p[0] = p[1]
def p_factor_float(p):
    'factor : FLOAT'
    p[0] = p[1]
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

#Brackets
def p_factor_expression(p):
    'factor : LPAR expression RPAR'
    p[0] = p[2]
def p_factor_expression_square(p):
    'factor : LSQU expression RSQU'
    p[0] = p[2]

#Advanced Arithmetic
def p_power(p):
    'term : factor POWER factor'
    p[0] = p[1] ** p[3]
def p_sqrt(p):
    'term : SQRT factor'
    from math import sqrt
    p[0] = sqrt(p[2])

#Constants
def p_pi(p):
    'factor : PI'
    from math import pi
    p[0] = pi
def p_pi_latin(p): #Pi Latin is just 'pi'
    'factor : PILATIN'
    from math import pi
    p[0] = pi
def p_euler(p):
    'factor : EULER'
    from math import e
    p[0] = e

#Calculus
def p_logarithm(p):
    'factor : LOG LPAR expression RPAR'
    from math import log10
    p[0] = log10(p[3])
def p_natural_logarithm(p):
    'factor : LN LPAR expression RPAR'
    from math import log, e
    p[0] = log(p[3], e)