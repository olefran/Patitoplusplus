
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMAND CHAR COMA COMMENT COMPARE CTE_CH CTE_F CTE_I CTE_STRING DESDE DET_ARR DIFFERENT DIV DOTCOMA ENTONCES EQUAL ESCRIBE FLOAT FUNCION HACER HASTA HAZ ID INT INV_ARR LBRACKET LEE LESS LESSEQUAL LPAREN LSTAPLE MIENTRAS MINUS MOD MORE MOREEQUAL MULT NOT NULL OR PLUS PRINCIPAL PROGRAMA RBRACKET REGRESA RPAREN RSTAPLE SI SINO STRING TRANS_ARR VAR VOIDempty :PROGRAM : PROGRAMA ID DOTCOMA VAR_AUX FUNCTIONS MAINMAIN : PRINCIPAL LPAREN RPAREN VAR_AUX BLOQUEVAR_AUX : VARS\n    | emptyVARS : VAR VARPREVARPRE : TIPO IDS DOTCOMA\n    | TIPO IDS DOTCOMA VARPRETIPO : INT\n    | FLOAT\n    | CHAR\n    | STRINGIDS : ID ARRDIM DOTCOMA\n    | ID ARRDIM COMA IDSARRDIM : LSTAPLE EXPRESION RSTAPLE\n    | LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE\n    | emptyFUNCTIONS : FUNCTION FUNCTIONS\n    | emptyFUNCTION : FUNCION TIPO ID LBRACKET PARAM RBRACKET VAR_AUX BLOQUE\n    | FUNCION TIPO VOID LBRACKET PARAM RBRACKET VAR_AUX BLOQUE\n    | emptyPARAM : TIPO ID PARENTESIS PARAMSUBPARAMSUB : COMA PARAM\n    | emptyPARENTESIS : LSTAPLE RSTAPLE\n    | LSTAPLE RSTAPLE LSTAPLE RSTAPLE\n    | emptyBLOQUE : LBRACKET ESTATUTOS RBRACKETESTATUTOS : ESTATUTO ESTATUTOS\n    | emptyESTATUTO : ASIGNACION DOTCOMA\n    | FUN DOTCOMA\n    | COND DOTCOMA\n    | WRITE DOTCOMA\n    | READ DOTCOMA\n    | RETURN DOTCOMAASIGNACION : ID ARRDIM EQUAL EXPRESION\n    | ID ARRDIM EQUAL CTE_ARREXPRESION : SUBEXP AND SUBEXP\n    | SUBEXP OR SUBEXP\n    | SUBEXPSUBEXP : EXP\n    | EXP COMPARACION EXPCOMPARACION : MORE\n    | LESS\n    | COMPARE\n    | DIFFERENT\n    | MOREEQUAL\n    | LESSEQUALEXP : TERMINO\n    | TERMINO PLUS TERMINO\n    | TERMINO MINUS TERMINOTERMINO : FACTOR\n    | FACTOR MULT FACTOR\n    | FACTOR DIV FACTOR\n    | FACTOR MOD FACTORFACTOR : LPAREN EXPRESION RPAREN\n    | PLUS CTE\n    | MINUS CTE\n    | NOT CTE\n    | CTECTE : CTE_I\n    | CTE_F\n    | CTE_CH\n    | ARROP ID ARRDIM\n    | CTE_STRINGARROP : DET_ARR\n    | TRANS_ARR\n    | INV_ARR\n    | emptyFUN : ID LPAREN FUN_AUX RPARENFUN_AUX : CTE COMA FUN_AUX\n    | CTE COND : IF\n    | FOR\n    | WHILEIF : SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE SINO IF_AUXIF_AUX : SINO BLOQUE\n    | emptyWHILE :  MIENTRAS LPAREN EXPRESION RPAREN HAZ BLOQUEFOR :  DESDE ASIGNACION HASTA EXPRESION HACER BLOQUEWRITE : ESCRIBE LPAREN WRITE_AUX RPARENWRITE_AUX : WRITE_AUX2 WRITE_AUXSUBWRITE_AUXSUB : COMA WRITE_AUX\n    | emptyWRITE_AUX2 : EXPRESION\n    | CTE_STRINGREAD : LEE LPAREN READ_AUX RPARENREAD_AUX : ID ARRDIM READ_AUXSUBREAD_AUXSUB : COMA READ_AUX\n    | emptyRETURN : REGRESA EXPRESION\n    | REGRESA FUN\n    | REGRESA NULLCTE_ARR : LBRACKET CTE_ARR_AUX RBRACKET\n    | LBRACKET CTE_ARR_AUX2 RBRACKET CTE_ARR_AUX : CTE\n    | CTE_ARR_AUXSUB CTE_ARR_AUXSUB : COMA CTE_ARR_AUX\n    | empty CTE_ARR_AUX2 : LBRACKET CTE_ARR_AUX RBRACKET  CTE_ARR_AUX2SUBCTE_ARR_AUX2SUB : COMA CTE_ARR_AUX2\n    | empty '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,19,82,123,],[0,-2,-3,-29,]),'ID':([2,14,15,16,17,18,22,30,37,42,43,45,47,51,53,54,55,56,58,63,64,65,66,67,68,69,70,71,72,73,76,77,78,83,87,99,113,115,125,126,127,128,129,130,132,133,134,139,142,150,160,166,168,171,179,184,185,189,],[3,24,-9,-10,-11,-12,26,-1,24,-1,-1,-1,-1,81,-68,-69,-70,-71,84,-1,-1,-1,-45,-46,-47,-48,-49,-50,-1,-1,-1,-1,-1,107,-1,107,138,141,-32,-33,-34,-35,-36,-37,-1,-1,158,-1,-1,-1,-1,-1,-1,-1,-1,-1,-71,158,]),'DOTCOMA':([3,23,24,29,31,36,39,40,41,44,46,48,49,50,52,61,62,74,75,80,81,88,89,90,91,92,93,94,95,96,97,101,102,103,104,105,106,108,109,110,123,135,136,137,149,164,165,167,169,173,195,196,200,201,203,208,209,211,],[4,28,-1,36,-17,-13,-42,-43,-51,-54,-62,-63,-64,-65,-67,-14,-15,-59,-60,-61,-1,-40,-41,-44,-52,-53,-55,-56,-57,-58,-66,125,126,127,128,129,130,-75,-76,-77,-29,-93,-94,-95,-16,-38,-39,-72,-83,-89,-96,-97,-82,-81,-1,-78,-80,-79,]),'VAR':([4,32,85,86,],[8,8,8,8,]),'FUNCION':([4,5,6,7,10,11,13,28,35,123,147,148,],[-1,12,-4,-5,12,-22,-6,-7,-8,-29,-20,-21,]),'PRINCIPAL':([4,5,6,7,9,10,11,13,21,28,35,123,147,148,],[-1,-1,-4,-5,20,-1,-19,-6,-18,-7,-8,-29,-20,-21,]),'LBRACKET':([6,7,13,26,27,28,32,35,57,85,86,120,121,150,166,191,192,193,205,207,],[-4,-5,-6,33,34,-7,-1,-8,83,-1,-1,83,83,166,179,83,83,83,179,83,]),'INT':([8,12,28,33,34,144,],[15,15,15,15,15,15,]),'FLOAT':([8,12,28,33,34,144,],[16,16,16,16,16,16,]),'CHAR':([8,12,28,33,34,144,],[17,17,17,17,17,17,]),'STRING':([8,12,28,33,34,144,],[18,18,18,18,18,18,]),'VOID':([15,16,17,18,22,],[-9,-10,-11,-12,27,]),'LPAREN':([20,30,45,63,64,65,66,67,68,69,70,71,72,73,76,77,78,87,107,111,112,113,114,116,133,138,139,142,150,160,171,],[25,45,45,45,45,45,-45,-46,-47,-48,-49,-50,45,45,45,45,45,45,132,133,134,45,139,142,45,132,45,45,45,45,45,]),'LSTAPLE':([24,62,81,84,107,141,146,158,],[30,87,30,118,30,30,163,30,]),'COMA':([24,29,31,39,40,41,44,46,48,49,50,52,62,74,75,80,81,84,88,89,90,91,92,93,94,95,96,97,117,119,146,149,152,154,155,156,158,166,174,178,179,184,202,],[-1,37,-17,-42,-43,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-1,-40,-41,-44,-52,-53,-55,-56,-57,-58,-66,144,-28,-26,-16,168,171,-87,-67,-1,184,189,-27,184,184,205,]),'RPAREN':([25,31,39,40,41,44,46,48,49,50,52,62,74,75,79,80,81,88,89,90,91,92,93,94,95,96,97,149,151,152,153,154,155,156,157,158,159,161,170,172,174,186,187,188,190,198,],[32,-17,-42,-43,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,96,-61,-1,-40,-41,-44,-52,-53,-55,-56,-57,-58,-66,-16,167,-74,169,-1,-87,-67,173,-1,175,177,-84,-86,-1,-73,-85,-90,-92,-91,]),'PLUS':([30,31,41,44,45,46,48,49,50,52,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,87,93,94,95,96,97,113,133,139,142,149,150,156,160,171,],[42,-17,72,-54,42,-62,-63,-64,-65,-67,-15,42,42,42,-45,-46,-47,-48,-49,-50,42,42,-59,-60,42,42,42,-61,-1,42,-55,-56,-57,-58,-66,42,42,42,42,-16,42,-67,42,42,]),'MINUS':([30,31,41,44,45,46,48,49,50,52,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,87,93,94,95,96,97,113,133,139,142,149,150,156,160,171,],[43,-17,73,-54,43,-62,-63,-64,-65,-67,-15,43,43,43,-45,-46,-47,-48,-49,-50,43,43,-59,-60,43,43,43,-61,-1,43,-55,-56,-57,-58,-66,43,43,43,43,-16,43,-67,43,43,]),'NOT':([30,45,63,64,65,66,67,68,69,70,71,72,73,76,77,78,87,113,133,139,142,150,160,171,],[47,47,47,47,47,-45,-46,-47,-48,-49,-50,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'CTE_I':([30,42,43,45,47,63,64,65,66,67,68,69,70,71,72,73,76,77,78,87,113,132,133,139,142,150,160,166,168,171,179,184,],[48,48,48,48,48,48,48,48,-45,-46,-47,-48,-49,-50,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'CTE_F':([30,42,43,45,47,63,64,65,66,67,68,69,70,71,72,73,76,77,78,87,113,132,133,139,142,150,160,166,168,171,179,184,],[49,49,49,49,49,49,49,49,-45,-46,-47,-48,-49,-50,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'CTE_CH':([30,42,43,45,47,63,64,65,66,67,68,69,70,71,72,73,76,77,78,87,113,132,133,139,142,150,160,166,168,171,179,184,],[50,50,50,50,50,50,50,50,-45,-46,-47,-48,-49,-50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'CTE_STRING':([30,42,43,45,47,63,64,65,66,67,68,69,70,71,72,73,76,77,78,87,113,132,133,139,142,150,160,166,168,171,179,184,],[52,52,52,52,52,52,52,52,-45,-46,-47,-48,-49,-50,52,52,52,52,52,52,52,52,156,52,52,52,52,52,52,156,52,52,]),'DET_ARR':([30,42,43,45,47,63,64,65,66,67,68,69,70,71,72,73,76,77,78,87,113,132,133,139,142,150,160,166,168,171,179,184,],[53,53,53,53,53,53,53,53,-45,-46,-47,-48,-49,-50,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'TRANS_ARR':([30,42,43,45,47,63,64,65,66,67,68,69,70,71,72,73,76,77,78,87,113,132,133,139,142,150,160,166,168,171,179,184,],[54,54,54,54,54,54,54,54,-45,-46,-47,-48,-49,-50,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'INV_ARR':([30,42,43,45,47,63,64,65,66,67,68,69,70,71,72,73,76,77,78,87,113,132,133,139,142,150,160,166,168,171,179,184,],[55,55,55,55,55,55,55,55,-45,-46,-47,-48,-49,-50,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'MULT':([31,44,46,48,49,50,52,62,74,75,80,81,96,97,149,156,],[-17,76,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-58,-66,-16,-67,]),'DIV':([31,44,46,48,49,50,52,62,74,75,80,81,96,97,149,156,],[-17,77,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-58,-66,-16,-67,]),'MOD':([31,44,46,48,49,50,52,62,74,75,80,81,96,97,149,156,],[-17,78,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-58,-66,-16,-67,]),'MORE':([31,40,41,44,46,48,49,50,52,62,74,75,80,81,91,92,93,94,95,96,97,149,156,],[-17,66,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-52,-53,-55,-56,-57,-58,-66,-16,-67,]),'LESS':([31,40,41,44,46,48,49,50,52,62,74,75,80,81,91,92,93,94,95,96,97,149,156,],[-17,67,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-52,-53,-55,-56,-57,-58,-66,-16,-67,]),'COMPARE':([31,40,41,44,46,48,49,50,52,62,74,75,80,81,91,92,93,94,95,96,97,149,156,],[-17,68,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-52,-53,-55,-56,-57,-58,-66,-16,-67,]),'DIFFERENT':([31,40,41,44,46,48,49,50,52,62,74,75,80,81,91,92,93,94,95,96,97,149,156,],[-17,69,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-52,-53,-55,-56,-57,-58,-66,-16,-67,]),'MOREEQUAL':([31,40,41,44,46,48,49,50,52,62,74,75,80,81,91,92,93,94,95,96,97,149,156,],[-17,70,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-52,-53,-55,-56,-57,-58,-66,-16,-67,]),'LESSEQUAL':([31,40,41,44,46,48,49,50,52,62,74,75,80,81,91,92,93,94,95,96,97,149,156,],[-17,71,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-52,-53,-55,-56,-57,-58,-66,-16,-67,]),'AND':([31,39,40,41,44,46,48,49,50,52,62,74,75,80,81,90,91,92,93,94,95,96,97,149,156,],[-17,63,-43,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-44,-52,-53,-55,-56,-57,-58,-66,-16,-67,]),'OR':([31,39,40,41,44,46,48,49,50,52,62,74,75,80,81,90,91,92,93,94,95,96,97,149,156,],[-17,64,-43,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-44,-52,-53,-55,-56,-57,-58,-66,-16,-67,]),'RSTAPLE':([31,38,39,40,41,44,46,48,49,50,52,62,74,75,80,81,88,89,90,91,92,93,94,95,96,97,118,122,149,163,],[-17,62,-42,-43,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-40,-41,-44,-52,-53,-55,-56,-57,-58,-66,146,149,-16,178,]),'HASTA':([31,39,40,41,44,46,48,49,50,52,62,74,75,80,81,88,89,90,91,92,93,94,95,96,97,140,149,164,165,195,196,],[-17,-42,-43,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-40,-41,-44,-52,-53,-55,-56,-57,-58,-66,160,-16,-38,-39,-96,-97,]),'HACER':([31,39,40,41,44,46,48,49,50,52,62,74,75,80,81,88,89,90,91,92,93,94,95,96,97,149,176,],[-17,-42,-43,-51,-54,-62,-63,-64,-65,-67,-15,-59,-60,-61,-1,-40,-41,-44,-52,-53,-55,-56,-57,-58,-66,-16,192,]),'RBRACKET':([31,48,49,50,52,59,60,62,81,83,84,97,98,99,100,117,119,124,125,126,127,128,129,130,143,145,146,149,162,166,178,179,180,181,182,183,184,185,194,197,202,204,206,210,],[-17,-63,-64,-65,-67,85,86,-15,-1,-1,-1,-66,123,-1,-31,-1,-28,-30,-32,-33,-34,-35,-36,-37,-23,-25,-26,-16,-24,-1,-27,-1,195,196,-98,-99,-1,-101,202,-100,-1,-102,-104,-103,]),'EQUAL':([31,62,107,131,141,149,],[-17,-15,-1,150,-1,-16,]),'ESCRIBE':([83,99,125,126,127,128,129,130,],[111,111,-32,-33,-34,-35,-36,-37,]),'LEE':([83,99,125,126,127,128,129,130,],[112,112,-32,-33,-34,-35,-36,-37,]),'REGRESA':([83,99,125,126,127,128,129,130,],[113,113,-32,-33,-34,-35,-36,-37,]),'SI':([83,99,125,126,127,128,129,130,],[114,114,-32,-33,-34,-35,-36,-37,]),'DESDE':([83,99,125,126,127,128,129,130,],[115,115,-32,-33,-34,-35,-36,-37,]),'MIENTRAS':([83,99,125,126,127,128,129,130,],[116,116,-32,-33,-34,-35,-36,-37,]),'NULL':([113,],[137,]),'SINO':([123,199,203,],[-29,203,207,]),'ENTONCES':([175,],[191,]),'HAZ':([177,],[193,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'VAR_AUX':([4,32,85,86,],[5,57,120,121,]),'VARS':([4,32,85,86,],[6,6,6,6,]),'empty':([4,5,10,24,30,32,42,43,45,47,63,64,65,72,73,76,77,78,81,83,84,85,86,87,99,107,113,117,132,133,139,141,142,150,154,158,160,166,168,171,174,179,184,202,203,],[7,11,11,31,56,7,56,56,56,56,56,56,56,56,56,56,56,56,31,100,119,7,7,56,100,31,56,145,56,56,56,31,56,56,172,31,56,185,56,56,190,185,185,206,209,]),'FUNCTIONS':([5,10,],[9,21,]),'FUNCTION':([5,10,],[10,10,]),'VARPRE':([8,28,],[13,35,]),'TIPO':([8,12,28,33,34,144,],[14,22,14,58,58,58,]),'MAIN':([9,],[19,]),'IDS':([14,37,],[23,61,]),'ARRDIM':([24,81,107,141,158,],[29,97,131,131,174,]),'EXPRESION':([30,45,87,113,133,139,142,150,160,171,],[38,79,122,135,155,159,161,164,176,155,]),'SUBEXP':([30,45,63,64,87,113,133,139,142,150,160,171,],[39,39,88,89,39,39,39,39,39,39,39,39,]),'EXP':([30,45,63,64,65,87,113,133,139,142,150,160,171,],[40,40,40,40,90,40,40,40,40,40,40,40,40,]),'TERMINO':([30,45,63,64,65,72,73,87,113,133,139,142,150,160,171,],[41,41,41,41,41,91,92,41,41,41,41,41,41,41,41,]),'FACTOR':([30,45,63,64,65,72,73,76,77,78,87,113,133,139,142,150,160,171,],[44,44,44,44,44,44,44,93,94,95,44,44,44,44,44,44,44,44,]),'CTE':([30,42,43,45,47,63,64,65,72,73,76,77,78,87,113,132,133,139,142,150,160,166,168,171,179,184,],[46,74,75,46,80,46,46,46,46,46,46,46,46,46,46,152,46,46,46,46,46,182,152,46,182,182,]),'ARROP':([30,42,43,45,47,63,64,65,72,73,76,77,78,87,113,132,133,139,142,150,160,166,168,171,179,184,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'PARAM':([33,34,144,],[59,60,162,]),'COMPARACION':([40,],[65,]),'BLOQUE':([57,120,121,191,192,193,207,],[82,147,148,199,200,201,211,]),'ESTATUTOS':([83,99,],[98,124,]),'ESTATUTO':([83,99,],[99,99,]),'ASIGNACION':([83,99,115,],[101,101,140,]),'FUN':([83,99,113,],[102,102,136,]),'COND':([83,99,],[103,103,]),'WRITE':([83,99,],[104,104,]),'READ':([83,99,],[105,105,]),'RETURN':([83,99,],[106,106,]),'IF':([83,99,],[108,108,]),'FOR':([83,99,],[109,109,]),'WHILE':([83,99,],[110,110,]),'PARENTESIS':([84,],[117,]),'PARAMSUB':([117,],[143,]),'FUN_AUX':([132,168,],[151,186,]),'WRITE_AUX':([133,171,],[153,187,]),'WRITE_AUX2':([133,171,],[154,154,]),'READ_AUX':([134,189,],[157,198,]),'CTE_ARR':([150,],[165,]),'WRITE_AUXSUB':([154,],[170,]),'CTE_ARR_AUX':([166,179,184,],[180,194,197,]),'CTE_ARR_AUX2':([166,205,],[181,210,]),'CTE_ARR_AUXSUB':([166,179,184,],[183,183,183,]),'READ_AUXSUB':([174,],[188,]),'CTE_ARR_AUX2SUB':([202,],[204,]),'IF_AUX':([203,],[208,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','PatitoPlusPlus.py',90),
  ('PROGRAM -> PROGRAMA ID DOTCOMA VAR_AUX FUNCTIONS MAIN','PROGRAM',6,'p_PROGRAM','PatitoPlusPlus.py',95),
  ('MAIN -> PRINCIPAL LPAREN RPAREN VAR_AUX BLOQUE','MAIN',5,'p_MAIN','PatitoPlusPlus.py',100),
  ('VAR_AUX -> VARS','VAR_AUX',1,'p_VAR_AUX','PatitoPlusPlus.py',105),
  ('VAR_AUX -> empty','VAR_AUX',1,'p_VAR_AUX','PatitoPlusPlus.py',106),
  ('VARS -> VAR VARPRE','VARS',2,'p_VARS','PatitoPlusPlus.py',111),
  ('VARPRE -> TIPO IDS DOTCOMA','VARPRE',3,'p_VARPRE','PatitoPlusPlus.py',116),
  ('VARPRE -> TIPO IDS DOTCOMA VARPRE','VARPRE',4,'p_VARPRE','PatitoPlusPlus.py',117),
  ('TIPO -> INT','TIPO',1,'p_TIPO','PatitoPlusPlus.py',122),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','PatitoPlusPlus.py',123),
  ('TIPO -> CHAR','TIPO',1,'p_TIPO','PatitoPlusPlus.py',124),
  ('TIPO -> STRING','TIPO',1,'p_TIPO','PatitoPlusPlus.py',125),
  ('IDS -> ID ARRDIM DOTCOMA','IDS',3,'p_IDS','PatitoPlusPlus.py',130),
  ('IDS -> ID ARRDIM COMA IDS','IDS',4,'p_IDS','PatitoPlusPlus.py',131),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE','ARRDIM',3,'p_ARRDIM','PatitoPlusPlus.py',136),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE','ARRDIM',6,'p_ARRDIM','PatitoPlusPlus.py',137),
  ('ARRDIM -> empty','ARRDIM',1,'p_ARRDIM','PatitoPlusPlus.py',138),
  ('FUNCTIONS -> FUNCTION FUNCTIONS','FUNCTIONS',2,'p_FUNCTIONS','PatitoPlusPlus.py',143),
  ('FUNCTIONS -> empty','FUNCTIONS',1,'p_FUNCTIONS','PatitoPlusPlus.py',144),
  ('FUNCTION -> FUNCION TIPO ID LBRACKET PARAM RBRACKET VAR_AUX BLOQUE','FUNCTION',8,'p_FUNCTION','PatitoPlusPlus.py',149),
  ('FUNCTION -> FUNCION TIPO VOID LBRACKET PARAM RBRACKET VAR_AUX BLOQUE','FUNCTION',8,'p_FUNCTION','PatitoPlusPlus.py',150),
  ('FUNCTION -> empty','FUNCTION',1,'p_FUNCTION','PatitoPlusPlus.py',151),
  ('PARAM -> TIPO ID PARENTESIS PARAMSUB','PARAM',4,'p_PARAM','PatitoPlusPlus.py',156),
  ('PARAMSUB -> COMA PARAM','PARAMSUB',2,'p_PARAMSUB','PatitoPlusPlus.py',161),
  ('PARAMSUB -> empty','PARAMSUB',1,'p_PARAMSUB','PatitoPlusPlus.py',162),
  ('PARENTESIS -> LSTAPLE RSTAPLE','PARENTESIS',2,'p_PARENTESIS','PatitoPlusPlus.py',167),
  ('PARENTESIS -> LSTAPLE RSTAPLE LSTAPLE RSTAPLE','PARENTESIS',4,'p_PARENTESIS','PatitoPlusPlus.py',168),
  ('PARENTESIS -> empty','PARENTESIS',1,'p_PARENTESIS','PatitoPlusPlus.py',169),
  ('BLOQUE -> LBRACKET ESTATUTOS RBRACKET','BLOQUE',3,'p_BLOQUE','PatitoPlusPlus.py',174),
  ('ESTATUTOS -> ESTATUTO ESTATUTOS','ESTATUTOS',2,'p_ESTATUTOS','PatitoPlusPlus.py',179),
  ('ESTATUTOS -> empty','ESTATUTOS',1,'p_ESTATUTOS','PatitoPlusPlus.py',180),
  ('ESTATUTO -> ASIGNACION DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',185),
  ('ESTATUTO -> FUN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',186),
  ('ESTATUTO -> COND DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',187),
  ('ESTATUTO -> WRITE DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',188),
  ('ESTATUTO -> READ DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',189),
  ('ESTATUTO -> RETURN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','PatitoPlusPlus.py',190),
  ('ASIGNACION -> ID ARRDIM EQUAL EXPRESION','ASIGNACION',4,'p_ASIGNACION','PatitoPlusPlus.py',195),
  ('ASIGNACION -> ID ARRDIM EQUAL CTE_ARR','ASIGNACION',4,'p_ASIGNACION','PatitoPlusPlus.py',196),
  ('EXPRESION -> SUBEXP AND SUBEXP','EXPRESION',3,'p_EXPRESION','PatitoPlusPlus.py',201),
  ('EXPRESION -> SUBEXP OR SUBEXP','EXPRESION',3,'p_EXPRESION','PatitoPlusPlus.py',202),
  ('EXPRESION -> SUBEXP','EXPRESION',1,'p_EXPRESION','PatitoPlusPlus.py',203),
  ('SUBEXP -> EXP','SUBEXP',1,'p_SUBEXP','PatitoPlusPlus.py',208),
  ('SUBEXP -> EXP COMPARACION EXP','SUBEXP',3,'p_SUBEXP','PatitoPlusPlus.py',209),
  ('COMPARACION -> MORE','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',214),
  ('COMPARACION -> LESS','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',215),
  ('COMPARACION -> COMPARE','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',216),
  ('COMPARACION -> DIFFERENT','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',217),
  ('COMPARACION -> MOREEQUAL','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',218),
  ('COMPARACION -> LESSEQUAL','COMPARACION',1,'p_COMPARACION','PatitoPlusPlus.py',219),
  ('EXP -> TERMINO','EXP',1,'p_EXP','PatitoPlusPlus.py',224),
  ('EXP -> TERMINO PLUS TERMINO','EXP',3,'p_EXP','PatitoPlusPlus.py',225),
  ('EXP -> TERMINO MINUS TERMINO','EXP',3,'p_EXP','PatitoPlusPlus.py',226),
  ('TERMINO -> FACTOR','TERMINO',1,'p_TERMINO','PatitoPlusPlus.py',231),
  ('TERMINO -> FACTOR MULT FACTOR','TERMINO',3,'p_TERMINO','PatitoPlusPlus.py',232),
  ('TERMINO -> FACTOR DIV FACTOR','TERMINO',3,'p_TERMINO','PatitoPlusPlus.py',233),
  ('TERMINO -> FACTOR MOD FACTOR','TERMINO',3,'p_TERMINO','PatitoPlusPlus.py',234),
  ('FACTOR -> LPAREN EXPRESION RPAREN','FACTOR',3,'p_FACTOR','PatitoPlusPlus.py',239),
  ('FACTOR -> PLUS CTE','FACTOR',2,'p_FACTOR','PatitoPlusPlus.py',240),
  ('FACTOR -> MINUS CTE','FACTOR',2,'p_FACTOR','PatitoPlusPlus.py',241),
  ('FACTOR -> NOT CTE','FACTOR',2,'p_FACTOR','PatitoPlusPlus.py',242),
  ('FACTOR -> CTE','FACTOR',1,'p_FACTOR','PatitoPlusPlus.py',243),
  ('CTE -> CTE_I','CTE',1,'p_CTE','PatitoPlusPlus.py',248),
  ('CTE -> CTE_F','CTE',1,'p_CTE','PatitoPlusPlus.py',249),
  ('CTE -> CTE_CH','CTE',1,'p_CTE','PatitoPlusPlus.py',250),
  ('CTE -> ARROP ID ARRDIM','CTE',3,'p_CTE','PatitoPlusPlus.py',251),
  ('CTE -> CTE_STRING','CTE',1,'p_CTE','PatitoPlusPlus.py',252),
  ('ARROP -> DET_ARR','ARROP',1,'p_ARROP','PatitoPlusPlus.py',257),
  ('ARROP -> TRANS_ARR','ARROP',1,'p_ARROP','PatitoPlusPlus.py',258),
  ('ARROP -> INV_ARR','ARROP',1,'p_ARROP','PatitoPlusPlus.py',259),
  ('ARROP -> empty','ARROP',1,'p_ARROP','PatitoPlusPlus.py',260),
  ('FUN -> ID LPAREN FUN_AUX RPAREN','FUN',4,'p_FUN','PatitoPlusPlus.py',265),
  ('FUN_AUX -> CTE COMA FUN_AUX','FUN_AUX',3,'p_FUN_AUX','PatitoPlusPlus.py',270),
  ('FUN_AUX -> CTE','FUN_AUX',1,'p_FUN_AUX','PatitoPlusPlus.py',271),
  ('COND -> IF','COND',1,'p_COND','PatitoPlusPlus.py',276),
  ('COND -> FOR','COND',1,'p_COND','PatitoPlusPlus.py',277),
  ('COND -> WHILE','COND',1,'p_COND','PatitoPlusPlus.py',278),
  ('IF -> SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE SINO IF_AUX','IF',8,'p_IF','PatitoPlusPlus.py',283),
  ('IF_AUX -> SINO BLOQUE','IF_AUX',2,'p_IF_AUX','PatitoPlusPlus.py',288),
  ('IF_AUX -> empty','IF_AUX',1,'p_IF_AUX','PatitoPlusPlus.py',289),
  ('WHILE -> MIENTRAS LPAREN EXPRESION RPAREN HAZ BLOQUE','WHILE',6,'p_WHILE','PatitoPlusPlus.py',294),
  ('FOR -> DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE','FOR',6,'p_FOR','PatitoPlusPlus.py',299),
  ('WRITE -> ESCRIBE LPAREN WRITE_AUX RPAREN','WRITE',4,'p_WRITE','PatitoPlusPlus.py',304),
  ('WRITE_AUX -> WRITE_AUX2 WRITE_AUXSUB','WRITE_AUX',2,'p_WRITE_AUX','PatitoPlusPlus.py',309),
  ('WRITE_AUXSUB -> COMA WRITE_AUX','WRITE_AUXSUB',2,'p_WRITE_AUXSUB','PatitoPlusPlus.py',314),
  ('WRITE_AUXSUB -> empty','WRITE_AUXSUB',1,'p_WRITE_AUXSUB','PatitoPlusPlus.py',315),
  ('WRITE_AUX2 -> EXPRESION','WRITE_AUX2',1,'p_WRITE_AUX2','PatitoPlusPlus.py',320),
  ('WRITE_AUX2 -> CTE_STRING','WRITE_AUX2',1,'p_WRITE_AUX2','PatitoPlusPlus.py',321),
  ('READ -> LEE LPAREN READ_AUX RPAREN','READ',4,'p_READ','PatitoPlusPlus.py',326),
  ('READ_AUX -> ID ARRDIM READ_AUXSUB','READ_AUX',3,'p_READ_AUX','PatitoPlusPlus.py',331),
  ('READ_AUXSUB -> COMA READ_AUX','READ_AUXSUB',2,'p_READ_AUXSUB','PatitoPlusPlus.py',336),
  ('READ_AUXSUB -> empty','READ_AUXSUB',1,'p_READ_AUXSUB','PatitoPlusPlus.py',337),
  ('RETURN -> REGRESA EXPRESION','RETURN',2,'p_RETURN','PatitoPlusPlus.py',342),
  ('RETURN -> REGRESA FUN','RETURN',2,'p_RETURN','PatitoPlusPlus.py',343),
  ('RETURN -> REGRESA NULL','RETURN',2,'p_RETURN','PatitoPlusPlus.py',344),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX RBRACKET','CTE_ARR',3,'p_CTE_ARR','PatitoPlusPlus.py',349),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX2 RBRACKET','CTE_ARR',3,'p_CTE_ARR','PatitoPlusPlus.py',350),
  ('CTE_ARR_AUX -> CTE','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','PatitoPlusPlus.py',355),
  ('CTE_ARR_AUX -> CTE_ARR_AUXSUB','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','PatitoPlusPlus.py',356),
  ('CTE_ARR_AUXSUB -> COMA CTE_ARR_AUX','CTE_ARR_AUXSUB',2,'p_CTE_ARR_AUXSUB','PatitoPlusPlus.py',361),
  ('CTE_ARR_AUXSUB -> empty','CTE_ARR_AUXSUB',1,'p_CTE_ARR_AUXSUB','PatitoPlusPlus.py',362),
  ('CTE_ARR_AUX2 -> LBRACKET CTE_ARR_AUX RBRACKET CTE_ARR_AUX2SUB','CTE_ARR_AUX2',4,'p_CTE_ARR_AUX2','PatitoPlusPlus.py',367),
  ('CTE_ARR_AUX2SUB -> COMA CTE_ARR_AUX2','CTE_ARR_AUX2SUB',2,'p_CTE_ARR_AUX2SUB','PatitoPlusPlus.py',372),
  ('CTE_ARR_AUX2SUB -> empty','CTE_ARR_AUX2SUB',1,'p_CTE_ARR_AUX2SUB','PatitoPlusPlus.py',373),
]
