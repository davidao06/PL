
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUM PA PFFinal : ABinABin : PA PFABin : PA NUM ABin ABin PF'
    
_lr_action_items = {'PA':([0,4,5,6,8,],[3,-2,3,3,-3,]),'$end':([1,2,4,8,],[0,-1,-2,-3,]),'PF':([3,4,7,8,],[4,-2,8,-3,]),'NUM':([3,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Final':([0,],[1,]),'ABin':([0,5,6,],[2,6,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Final","S'",1,None,None,None),
  ('Final -> ABin','Final',1,'p_Final','abin_sin.py',5),
  ('ABin -> PA PF','ABin',2,'p_ABin_Vazia','abin_sin.py',9),
  ('ABin -> PA NUM ABin ABin PF','ABin',5,'p_ABin_Nodo','abin_sin.py',13),
]
