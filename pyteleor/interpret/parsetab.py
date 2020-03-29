
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL COLON COMMA COMMENT E FLOAT GT GTE IMPLY INT LPAREN LT LTE NAME NEWLINE RPAREN STR program : program NEWLINE line  program : line  line : plan\n             | plan COMMENT\n             | rule\n             | rule COMMENT plan : statement COLON  line : COMMENT\n             | empty rule : conditions IMPLY actions  conditions : empty  conditions : condition  conditions : condition COMMA conditions  actions : empty  actions : action  actions : action COMMA actions  action :  NAME LPAREN args RPAREN  condition : statement  condition : NAME statement : NAME LPAREN args RPAREN condition : arg operator arg  operator : LT \n                 | GT \n                 | LTE\n                 | GTE \n                 | E empty :  args : empty args : arg  args : arg COMMA args  arg : STR\n            | FLOAT\n            | INT \n            | BOOL\n    arg : statement arg : NAME '
    
_lr_action_items = {'COMMENT':([0,3,5,16,19,20,30,31,32,44,48,51,],[4,17,18,4,-7,-27,-10,-14,-15,-27,-16,-17,]),'NEWLINE':([0,1,2,3,4,5,6,16,17,18,19,20,29,30,31,32,44,48,51,],[-27,16,-2,-3,-8,-5,-9,-27,-4,-6,-7,-27,-1,-10,-14,-15,-27,-16,-17,]),'$end':([0,1,2,3,4,5,6,16,17,18,19,20,29,30,31,32,44,48,51,],[-27,0,-2,-3,-8,-5,-9,-27,-4,-6,-7,-27,-1,-10,-14,-15,-27,-16,-17,]),'IMPLY':([0,6,7,8,9,10,12,13,14,15,16,22,34,38,39,40,41,42,43,46,],[-27,-11,-18,20,-19,-12,-31,-32,-33,-34,-27,-27,-36,-35,-13,-11,-18,-19,-21,-20,]),'NAME':([0,16,20,21,22,23,24,25,26,27,28,44,45,47,],[9,9,33,34,42,34,-22,-23,-24,-25,-26,33,34,34,]),'STR':([0,16,21,22,23,24,25,26,27,28,45,47,],[12,12,12,12,12,-22,-23,-24,-25,-26,12,12,]),'FLOAT':([0,16,21,22,23,24,25,26,27,28,45,47,],[13,13,13,13,13,-22,-23,-24,-25,-26,13,13,]),'INT':([0,16,21,22,23,24,25,26,27,28,45,47,],[14,14,14,14,14,-22,-23,-24,-25,-26,14,14,]),'BOOL':([0,16,21,22,23,24,25,26,27,28,45,47,],[15,15,15,15,15,-22,-23,-24,-25,-26,15,15,]),'COLON':([7,46,],[19,-20,]),'COMMA':([7,9,10,12,13,14,15,32,34,37,38,41,42,43,46,51,],[-18,-19,22,-31,-32,-33,-34,44,-36,47,-35,-18,-19,-21,-20,-17,]),'LT':([7,9,11,12,13,14,15,41,42,46,],[-35,-36,24,-31,-32,-33,-34,-35,-36,-20,]),'GT':([7,9,11,12,13,14,15,41,42,46,],[-35,-36,25,-31,-32,-33,-34,-35,-36,-20,]),'LTE':([7,9,11,12,13,14,15,41,42,46,],[-35,-36,26,-31,-32,-33,-34,-35,-36,-20,]),'GTE':([7,9,11,12,13,14,15,41,42,46,],[-35,-36,27,-31,-32,-33,-34,-35,-36,-20,]),'E':([7,9,11,12,13,14,15,41,42,46,],[-35,-36,28,-31,-32,-33,-34,-35,-36,-20,]),'LPAREN':([9,33,34,42,],[21,45,21,21,]),'RPAREN':([12,13,14,15,21,34,35,36,37,38,45,46,47,49,50,],[-31,-32,-33,-34,-27,-36,46,-28,-29,-35,-27,-20,-27,51,-30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'line':([0,16,],[2,29,]),'plan':([0,16,],[3,3,]),'rule':([0,16,],[5,5,]),'empty':([0,16,20,21,22,44,45,47,],[6,6,31,36,40,31,36,36,]),'statement':([0,16,21,22,23,45,47,],[7,7,38,41,38,38,38,]),'conditions':([0,16,22,],[8,8,39,]),'condition':([0,16,22,],[10,10,10,]),'arg':([0,16,21,22,23,45,47,],[11,11,37,11,43,37,37,]),'operator':([11,],[23,]),'actions':([20,44,],[30,48,]),'action':([20,44,],[32,32,]),'args':([21,45,47,],[35,49,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program NEWLINE line','program',3,'p_program_n','__init__.py',71),
  ('program -> line','program',1,'p_program_1','__init__.py',75),
  ('line -> plan','line',1,'p_line','__init__.py',79),
  ('line -> plan COMMENT','line',2,'p_line','__init__.py',80),
  ('line -> rule','line',1,'p_line','__init__.py',81),
  ('line -> rule COMMENT','line',2,'p_line','__init__.py',82),
  ('plan -> statement COLON','plan',2,'p_plan','__init__.py',87),
  ('line -> COMMENT','line',1,'p_line_empty','__init__.py',91),
  ('line -> empty','line',1,'p_line_empty','__init__.py',92),
  ('rule -> conditions IMPLY actions','rule',3,'p_rule','__init__.py',97),
  ('conditions -> empty','conditions',1,'p_conditions0','__init__.py',102),
  ('conditions -> condition','conditions',1,'p_conditions1','__init__.py',106),
  ('conditions -> condition COMMA conditions','conditions',3,'p_conditionsn','__init__.py',110),
  ('actions -> empty','actions',1,'p_actions0','__init__.py',115),
  ('actions -> action','actions',1,'p_actions1','__init__.py',119),
  ('actions -> action COMMA actions','actions',3,'p_actionsn','__init__.py',123),
  ('action -> NAME LPAREN args RPAREN','action',4,'p_action','__init__.py',127),
  ('condition -> statement','condition',1,'p_condition','__init__.py',131),
  ('condition -> NAME','condition',1,'p_condition1','__init__.py',135),
  ('statement -> NAME LPAREN args RPAREN','statement',4,'p_statement','__init__.py',139),
  ('condition -> arg operator arg','condition',3,'p_compare','__init__.py',144),
  ('operator -> LT','operator',1,'p_coperator','__init__.py',148),
  ('operator -> GT','operator',1,'p_coperator','__init__.py',149),
  ('operator -> LTE','operator',1,'p_coperator','__init__.py',150),
  ('operator -> GTE','operator',1,'p_coperator','__init__.py',151),
  ('operator -> E','operator',1,'p_coperator','__init__.py',152),
  ('empty -> <empty>','empty',0,'p_empty','__init__.py',156),
  ('args -> empty','args',1,'p_args0','__init__.py',160),
  ('args -> arg','args',1,'p_args1','__init__.py',164),
  ('args -> arg COMMA args','args',3,'p_argsn','__init__.py',168),
  ('arg -> STR','arg',1,'p_literal','__init__.py',172),
  ('arg -> FLOAT','arg',1,'p_literal','__init__.py',173),
  ('arg -> INT','arg',1,'p_literal','__init__.py',174),
  ('arg -> BOOL','arg',1,'p_literal','__init__.py',175),
  ('arg -> statement','arg',1,'p_arg_statement','__init__.py',180),
  ('arg -> NAME','arg',1,'p_arg','__init__.py',184),
]
