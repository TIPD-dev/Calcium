from compiler.parser import *
from compiler.lexer import *
from compiler.tokens import *
class Calcium:
    def __init__(self, equation : str):
        if type(equation) != str:
            raise Exception("The Equation must be string")
        self.eq = equation
        self.lexer = lex.lex()
        self.parser = yacc.yacc()
        self.result = self.parser.parse(self.eq)
    def __str__(self):
        return str(self.result)
    def solve(self):
        return self.result