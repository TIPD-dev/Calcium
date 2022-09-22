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
def p_golden_ratio(p):
    'factor : GOLDEN'
    p[0] = 1.6180339887498948482
def p_apery_constant(p):
    'factor : Z'
    p[0] = 1.2020569
def p_feigenbaum_alpha(p):
    'factor : ALPHA'
    p[0] = 2.5029
def p_feigenbaum_delta(p):
    'factor : DELTA'
    p[0] = 4.6692
def p_euler_mascheroni_constant(p):
    'factor : GAMMA'
    p[0] = 0.57721
def p_conway_constant(p):
    'factor : LAMBDA'
    p[0] = 1.30357
def p_khinchin_constant(p):
    'factor : K'
    p[0] = 2.6854520010
def p_glaisher_kinkelin_constant(p):
    'factor : A'
    p[0] = 1.2824271291

#Large Numbers
def p_googol(p):
    'factor : GOOGOL'
    p[0] = 10 ** 100
def p_googolplex(p):
    'factor : GOOGOLPLEX'
    p[0] = 10 ** (10 ** 100)

#Calculus
def p_logarithm(p):
    'factor : LOG LPAR expression RPAR'
    from math import log10
    p[0] = log10(p[3])
def p_natural_logarithm(p):
    'factor : LN LPAR expression RPAR'
    from math import log, e
    p[0] = log(p[3], e)