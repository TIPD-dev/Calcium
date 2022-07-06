
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD DIV FLOAT INT LPAR MUL RPAR SUBexpression : expression ADD termexpression : expression SUB termexpression : termterm : term MUL factorterm : term DIV factorterm : factorfactor : INTfactor : FLOATfactor : LPAR expression RPAR'
    
_lr_action_items = {'INT':([0,6,7,8,9,10,],[4,4,4,4,4,4,]),'FLOAT':([0,6,7,8,9,10,],[5,5,5,5,5,5,]),'LPAR':([0,6,7,8,9,10,],[6,6,6,6,6,6,]),'$end':([1,2,3,4,5,12,13,14,15,16,],[0,-3,-6,-7,-8,-1,-2,-4,-5,-9,]),'ADD':([1,2,3,4,5,11,12,13,14,15,16,],[7,-3,-6,-7,-8,7,-1,-2,-4,-5,-9,]),'SUB':([1,2,3,4,5,11,12,13,14,15,16,],[8,-3,-6,-7,-8,8,-1,-2,-4,-5,-9,]),'RPAR':([2,3,4,5,11,12,13,14,15,16,],[-3,-6,-7,-8,16,-1,-2,-4,-5,-9,]),'MUL':([2,3,4,5,12,13,14,15,16,],[9,-6,-7,-8,9,9,-4,-5,-9,]),'DIV':([2,3,4,5,12,13,14,15,16,],[10,-6,-7,-8,10,10,-4,-5,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,6,],[1,11,]),'term':([0,6,7,8,],[2,2,12,13,]),'factor':([0,6,7,8,9,10,],[3,3,3,3,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression ADD term','expression',3,'p_expression_add','parser.py',5),
  ('expression -> expression SUB term','expression',3,'p_expression_sub','parser.py',8),
  ('expression -> term','expression',1,'p_expression_term','parser.py',11),
  ('term -> term MUL factor','term',3,'p_term_mul','parser.py',14),
  ('term -> term DIV factor','term',3,'p_term_div','parser.py',17),
  ('term -> factor','term',1,'p_term_factor','parser.py',20),
  ('factor -> INT','factor',1,'p_factor_int','parser.py',23),
  ('factor -> FLOAT','factor',1,'p_factor_float','parser.py',26),
  ('factor -> LPAR expression RPAR','factor',3,'p_factor_expression','parser.py',29),
]