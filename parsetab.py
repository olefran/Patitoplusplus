
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMleftPLUSMINUSleftMULTDIVMODrightEQUALleftANDORAND CHAR COMA COMMENT COMPARE CTE_CH CTE_F CTE_I CTE_STRING DESDE DET_ARR DIFFERENT DIV DOTCOMA ENTONCES EQUAL ESCRIBE FLOAT FUNCION HACER HASTA HAZ ID INT INV_ARR LBRACKET LEE LESS LESSEQUAL LPAREN LSTAPLE MIENTRAS MINUS MOD MORE MOREEQUAL MULT NOT NULL OR PLUS PRINCIPAL PROGRAMA RBRACKET REGRESA RPAREN RSTAPLE SI SINO STRING TRANS_ARR VAR VOIDempty :PROGRAM : PROGRAMA ID DOTCOMA VARS FUNCTIONS MAINMAIN : PRINCIPAL r_save_func LPAREN RPAREN r_register_princ VARS BLOQUEVARS : VAR VAR_AUX\n    | emptyVAR_AUX : TIPO IDS VAR_AUX\n    | emptyTIPO : INT r_save_type\n    | FLOAT r_save_type\n    | CHAR r_save_type\n    | STRING r_save_typeIDS : ID r_register_var ARRDIM DOTCOMA\n    | ID r_register_var ARRDIM COMA IDSARRDIM : LSTAPLE EXPRESION RSTAPLE\n    | LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE\n    | LSTAPLE EXPRESION COMA EXPRESION RSTAPLE\n    | emptyFUNCTIONS : FUNCTION FUNCTIONS\n    | emptyFUNCTION : FUNCION TIPO ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUE\n    | FUNCION VOID r_save_type ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUEPARAM : TIPO ID r_register_var PARENTESIS PARAM_AUXPARAM_AUX : COMA PARAM\n    | emptyPARENTESIS : LSTAPLE RSTAPLE\n    | LSTAPLE RSTAPLE LSTAPLE RSTAPLE\n    | emptyBLOQUE : LBRACKET ESTATUTOS RBRACKETESTATUTOS : ESTATUTO ESTATUTOS\n    | emptyESTATUTO : ASIGNACION DOTCOMA\n    | FUN DOTCOMA\n    | COND\n    | WRITE DOTCOMA\n    | READ DOTCOMA\n    | RETURN DOTCOMAASIGNACION : ID ARRDIM EQUAL r_seen_operator EXPRESION\n    | ID ARRDIM EQUAL r_seen_operator CTE_ARREXPRESION : SUBEXP r_seen_subexp EXPRESION_AUXEXPRESION_AUX : AND r_seen_operator EXPRESION\n    | OR r_seen_operator EXPRESION\n    | emptySUBEXP : EXP r_seen_exp SUBEXP_AUXSUBEXP_AUX : COMPARACION SUBEXP\n    | emptyCOMPARACION : MORE r_seen_operator\n    | LESS r_seen_operator\n    | COMPARE r_seen_operator\n    | DIFFERENT r_seen_operator\n    | MOREEQUAL r_seen_operator\n    | LESSEQUAL r_seen_operatorEXP : TERMINO r_seen_term EXP_AUXEXP_AUX : PLUS r_seen_operator EXP\n    | MINUS r_seen_operator EXP\n    | emptyTERMINO : FACTOR r_seen_factor TERMINO_AUXTERMINO_AUX : MULT r_seen_operator TERMINO\n    | DIV r_seen_operator TERMINO r_seen_term\n    | MOD r_seen_operator TERMINO r_seen_term\n    | emptyFACTOR : LPAREN r_seen_operator EXPRESION RPAREN r_seen_operator\n    | PLUS r_seen_unary_operator CTE\n    | MINUS r_seen_unary_operator CTE\n    | NOT r_seen_unary_operator CTE\n    | CTE ARROP\n    | CTECTE : CTE_I r_seen_operand\n    | CTE_F r_seen_operand\n    | CTE_CH r_seen_operand\n    | CTE_STRING r_seen_operand\n    | FUN\n    | ID ARRDIM ARROP : DET_ARR\n    | TRANS_ARR\n    | INV_ARRFUN : ID LPAREN FUN_AUX RPARENFUN_AUX : EXPRESION COMA FUN_AUX\n    | EXPRESION\n    | emptyCOND : IF\n    | FOR\n    | WHILEIF : SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE IF_AUX\n    | SI LPAREN EXPRESION RPAREN ENTONCES COND IF_AUX : SINO BLOQUE\n    | emptyWHILE :  MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX BLOQUE\n    | MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX CONDWHILE_AUX : HAZ\n    | empty FOR :  DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE\n    | DESDE ASIGNACION HASTA EXPRESION HACER CONDWRITE : ESCRIBE LPAREN WRITE_AUX RPARENWRITE_AUX : EXPRESION WRITE_AUXSUBWRITE_AUXSUB : COMA WRITE_AUX\n    | emptyREAD : LEE LPAREN READ_AUX RPARENREAD_AUX : ID ARRDIM READ_AUXSUBREAD_AUXSUB : COMA READ_AUX\n    | emptyRETURN : REGRESA LPAREN EXPRESION RPAREN\n    | REGRESA LPAREN NULL RPARENCTE_ARR : LBRACKET CTE_ARR_AUX RBRACKET\n    | LBRACKET CTE_ARR_AUX2 RBRACKET CTE_ARR_AUX : CTE\n    | CTE_ARR_AUXSUB CTE_ARR_AUXSUB : COMA CTE_ARR_AUX\n    | empty CTE_ARR_AUX2 : LBRACKET CTE_ARR_AUX RBRACKET  CTE_ARR_AUX2SUBCTE_ARR_AUX2SUB : COMA CTE_ARR_AUX2\n    | empty r_save_type : r_save_func : r_register_func : r_register_var : r_register_princ : r_seen_operand : r_seen_operator : r_seen_subexp : r_seen_exp : r_seen_term : r_seen_factor : r_seen_unary_operator : '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,19,121,177,],[0,-2,-3,-28,]),'ID':([2,13,15,16,17,18,22,23,26,27,28,29,32,39,45,51,52,54,55,67,72,73,78,79,85,87,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,122,128,129,131,132,133,134,135,136,137,138,139,140,141,144,146,150,155,156,157,162,177,179,180,181,182,183,185,186,187,188,191,199,207,214,217,230,233,241,246,249,250,251,252,253,254,259,261,263,],[3,25,-112,-112,-112,-112,31,-112,-8,-9,-10,-11,37,61,25,-118,-123,-123,-123,61,61,61,61,61,61,123,61,-118,-118,61,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,154,61,61,-46,-47,-48,-49,-50,-51,61,61,61,61,61,61,154,-33,-80,-81,-82,190,-28,-31,-32,-34,-35,-36,61,203,61,61,61,-118,61,61,61,61,203,61,61,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'DOTCOMA':([3,25,34,38,40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,92,95,96,98,105,108,109,113,115,116,117,127,130,142,143,148,149,151,152,153,167,168,169,170,171,172,173,174,175,197,198,215,219,221,222,228,229,256,257,],[4,-115,-1,44,-17,-119,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,-16,-44,-118,-76,179,180,181,182,183,-15,-40,-41,-53,-54,-57,-121,-121,-61,-58,-59,-93,-97,-101,-102,-37,-38,-103,-104,]),'VAR':([4,41,62,124,166,],[6,-116,6,6,6,]),'FUNCION':([4,5,6,7,9,12,14,24,33,44,65,177,195,213,],[-1,11,-1,-5,11,-4,-7,-1,-6,-12,-13,-28,-20,-21,]),'PRINCIPAL':([4,5,6,7,8,9,10,12,14,21,24,33,44,65,177,195,213,],[-1,-1,-1,-5,20,-1,-19,-4,-7,-18,-1,-6,-12,-13,-28,-20,-21,]),'INT':([6,11,24,44,63,65,89,210,],[15,15,15,-12,15,-13,15,15,]),'FLOAT':([6,11,24,44,63,65,89,210,],[16,16,16,-12,16,-13,16,16,]),'CHAR':([6,11,24,44,63,65,89,210,],[17,17,17,-12,17,-13,17,17,]),'STRING':([6,11,24,44,63,65,89,210,],[18,18,18,-12,18,-13,18,18,]),'LBRACKET':([6,7,12,14,24,33,41,44,62,65,86,124,165,166,196,199,214,225,230,235,236,237,238,239,260,265,],[-1,-5,-4,-7,-1,-6,-116,-12,-1,-13,122,-1,122,-1,122,-118,230,-1,241,122,122,122,-89,-90,122,241,]),'VOID':([11,],[23,]),'LPAREN':([20,30,31,36,37,39,42,43,51,61,64,67,72,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,128,129,131,132,133,134,135,136,137,138,139,140,141,144,154,158,159,160,161,163,185,187,188,191,199,207,214,217,],[-113,35,-113,-114,-113,51,63,-114,-118,85,89,51,51,51,51,-118,-118,51,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,51,51,-46,-47,-48,-49,-50,-51,51,51,51,51,51,51,85,185,186,187,188,191,51,51,51,51,-118,51,51,51,]),'LSTAPLE':([25,34,61,66,123,154,164,190,203,212,],[-115,39,39,90,-115,39,193,39,39,227,]),'COMA':([25,34,38,40,46,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,92,95,96,98,105,108,109,113,115,116,117,119,123,127,130,142,143,164,167,168,169,170,171,172,173,174,175,192,194,197,198,201,203,212,220,230,240,241,246,262,],[-115,-1,45,-17,67,-119,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,144,-115,-16,-44,-118,-76,-1,-15,-40,-41,-53,-54,-57,-121,-121,-61,210,-27,-58,-59,217,-1,-25,233,246,-26,246,246,265,]),'RPAREN':([35,40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,85,88,92,95,96,98,105,108,109,113,114,115,116,117,118,119,120,123,125,127,130,142,143,144,164,167,168,169,170,171,172,173,174,175,176,192,194,197,198,200,201,202,203,204,205,206,208,209,211,212,216,218,220,226,231,232,234,240,248,],[41,-17,-119,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-1,124,-39,-42,-43,-45,-52,-55,-56,-60,142,-62,-63,-64,143,-78,-79,-115,166,-16,-44,-118,-76,-1,-1,-15,-40,-41,-53,-54,-57,-121,-121,-61,-77,-1,-27,-58,-59,215,-1,219,-1,221,222,223,225,-22,-24,-25,-94,-96,-1,-23,-95,-98,-100,-26,-99,]),'PLUS':([39,40,49,50,51,53,56,57,58,59,60,61,66,67,70,71,72,74,75,76,77,80,81,82,83,84,85,90,93,94,97,99,100,101,102,103,104,106,107,109,110,111,112,113,115,116,117,127,128,129,131,132,133,134,135,136,137,138,139,140,141,142,143,144,167,172,173,174,175,185,187,188,191,197,198,199,207,214,217,],[52,-17,-121,-122,-118,-66,-117,-117,-117,-117,-71,-1,-14,52,106,-1,52,-65,-73,-74,-75,-67,-68,-69,-70,-72,52,52,-118,-118,52,-118,-118,-118,-118,-118,-118,-118,-118,-56,-118,-118,-118,-60,-62,-63,-64,-16,52,52,-46,-47,-48,-49,-50,-51,52,52,52,52,52,-118,-76,52,-15,-57,-121,-121,-61,52,52,52,52,-58,-59,-118,52,52,52,]),'MINUS':([39,40,49,50,51,53,56,57,58,59,60,61,66,67,70,71,72,74,75,76,77,80,81,82,83,84,85,90,93,94,97,99,100,101,102,103,104,106,107,109,110,111,112,113,115,116,117,127,128,129,131,132,133,134,135,136,137,138,139,140,141,142,143,144,167,172,173,174,175,185,187,188,191,197,198,199,207,214,217,],[54,-17,-121,-122,-118,-66,-117,-117,-117,-117,-71,-1,-14,54,107,-1,54,-65,-73,-74,-75,-67,-68,-69,-70,-72,54,54,-118,-118,54,-118,-118,-118,-118,-118,-118,-118,-118,-56,-118,-118,-118,-60,-62,-63,-64,-16,54,54,-46,-47,-48,-49,-50,-51,54,54,54,54,54,-118,-76,54,-15,-57,-121,-121,-61,54,54,54,54,-58,-59,-118,54,54,54,]),'NOT':([39,51,67,72,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,128,129,131,132,133,134,135,136,137,138,139,140,141,144,185,187,188,191,199,207,214,217,],[55,-118,55,55,55,55,-118,-118,55,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,55,55,-46,-47,-48,-49,-50,-51,55,55,55,55,55,55,55,55,55,55,-118,55,55,55,]),'CTE_I':([39,51,52,54,55,67,72,73,78,79,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,128,129,131,132,133,134,135,136,137,138,139,140,141,144,185,187,188,191,199,207,214,217,230,241,246,],[56,-118,-123,-123,-123,56,56,56,56,56,56,56,-118,-118,56,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,56,56,-46,-47,-48,-49,-50,-51,56,56,56,56,56,56,56,56,56,56,-118,56,56,56,56,56,56,]),'CTE_F':([39,51,52,54,55,67,72,73,78,79,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,128,129,131,132,133,134,135,136,137,138,139,140,141,144,185,187,188,191,199,207,214,217,230,241,246,],[57,-118,-123,-123,-123,57,57,57,57,57,57,57,-118,-118,57,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,57,57,-46,-47,-48,-49,-50,-51,57,57,57,57,57,57,57,57,57,57,-118,57,57,57,57,57,57,]),'CTE_CH':([39,51,52,54,55,67,72,73,78,79,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,128,129,131,132,133,134,135,136,137,138,139,140,141,144,185,187,188,191,199,207,214,217,230,241,246,],[58,-118,-123,-123,-123,58,58,58,58,58,58,58,-118,-118,58,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,58,58,-46,-47,-48,-49,-50,-51,58,58,58,58,58,58,58,58,58,58,-118,58,58,58,58,58,58,]),'CTE_STRING':([39,51,52,54,55,67,72,73,78,79,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,128,129,131,132,133,134,135,136,137,138,139,140,141,144,185,187,188,191,199,207,214,217,230,241,246,],[59,-118,-123,-123,-123,59,59,59,59,59,59,59,-118,-118,59,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,-118,59,59,-46,-47,-48,-49,-50,-51,59,59,59,59,59,59,59,59,59,59,-118,59,59,59,59,59,59,]),'DET_ARR':([40,53,56,57,58,59,60,61,66,80,81,82,83,84,127,143,167,],[-17,75,-117,-117,-117,-117,-71,-1,-14,-67,-68,-69,-70,-72,-16,-76,-15,]),'TRANS_ARR':([40,53,56,57,58,59,60,61,66,80,81,82,83,84,127,143,167,],[-17,76,-117,-117,-117,-117,-71,-1,-14,-67,-68,-69,-70,-72,-16,-76,-15,]),'INV_ARR':([40,53,56,57,58,59,60,61,66,80,81,82,83,84,127,143,167,],[-17,77,-117,-117,-117,-117,-71,-1,-14,-67,-68,-69,-70,-72,-16,-76,-15,]),'MULT':([40,50,53,56,57,58,59,60,61,66,71,74,75,76,77,80,81,82,83,84,115,116,117,127,142,143,167,175,],[-17,-122,-66,-117,-117,-117,-117,-71,-1,-14,110,-65,-73,-74,-75,-67,-68,-69,-70,-72,-62,-63,-64,-16,-118,-76,-15,-61,]),'DIV':([40,50,53,56,57,58,59,60,61,66,71,74,75,76,77,80,81,82,83,84,115,116,117,127,142,143,167,175,],[-17,-122,-66,-117,-117,-117,-117,-71,-1,-14,111,-65,-73,-74,-75,-67,-68,-69,-70,-72,-62,-63,-64,-16,-118,-76,-15,-61,]),'MOD':([40,50,53,56,57,58,59,60,61,66,71,74,75,76,77,80,81,82,83,84,115,116,117,127,142,143,167,175,],[-17,-122,-66,-117,-117,-117,-117,-71,-1,-14,112,-65,-73,-74,-75,-67,-68,-69,-70,-72,-62,-63,-64,-16,-118,-76,-15,-61,]),'MORE':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,127,142,143,167,170,171,172,173,174,175,197,198,],[-17,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,99,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-52,-55,-56,-60,-62,-63,-64,-16,-118,-76,-15,-53,-54,-57,-121,-121,-61,-58,-59,]),'LESS':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,127,142,143,167,170,171,172,173,174,175,197,198,],[-17,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,100,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-52,-55,-56,-60,-62,-63,-64,-16,-118,-76,-15,-53,-54,-57,-121,-121,-61,-58,-59,]),'COMPARE':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,127,142,143,167,170,171,172,173,174,175,197,198,],[-17,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,101,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-52,-55,-56,-60,-62,-63,-64,-16,-118,-76,-15,-53,-54,-57,-121,-121,-61,-58,-59,]),'DIFFERENT':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,127,142,143,167,170,171,172,173,174,175,197,198,],[-17,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,102,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-52,-55,-56,-60,-62,-63,-64,-16,-118,-76,-15,-53,-54,-57,-121,-121,-61,-58,-59,]),'MOREEQUAL':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,127,142,143,167,170,171,172,173,174,175,197,198,],[-17,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,103,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-52,-55,-56,-60,-62,-63,-64,-16,-118,-76,-15,-53,-54,-57,-121,-121,-61,-58,-59,]),'LESSEQUAL':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,127,142,143,167,170,171,172,173,174,175,197,198,],[-17,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,104,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-52,-55,-56,-60,-62,-63,-64,-16,-118,-76,-15,-53,-54,-57,-121,-121,-61,-58,-59,]),'AND':([40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,96,98,105,108,109,113,115,116,117,127,130,142,143,167,170,171,172,173,174,175,197,198,],[-17,-119,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,93,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-43,-45,-52,-55,-56,-60,-62,-63,-64,-16,-44,-118,-76,-15,-53,-54,-57,-121,-121,-61,-58,-59,]),'OR':([40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,96,98,105,108,109,113,115,116,117,127,130,142,143,167,170,171,172,173,174,175,197,198,],[-17,-119,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,94,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-43,-45,-52,-55,-56,-60,-62,-63,-64,-16,-44,-118,-76,-15,-53,-54,-57,-121,-121,-61,-58,-59,]),'RSTAPLE':([40,46,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,91,92,95,96,98,105,108,109,113,115,116,117,126,127,130,142,143,167,168,169,170,171,172,173,174,175,193,197,198,227,],[-17,66,-119,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,127,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,167,-16,-44,-118,-76,-15,-40,-41,-53,-54,-57,-121,-121,-61,212,-58,-59,240,]),'HACER':([40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,92,95,96,98,105,108,109,113,115,116,117,127,130,142,143,167,168,169,170,171,172,173,174,175,197,198,224,],[-17,-119,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,-16,-44,-118,-76,-15,-40,-41,-53,-54,-57,-121,-121,-61,-58,-59,236,]),'HASTA':([40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,92,95,96,98,105,108,109,113,115,116,117,127,130,142,143,167,168,169,170,171,172,173,174,175,189,197,198,228,229,256,257,],[-17,-119,-120,-121,-122,-66,-117,-117,-117,-117,-71,-1,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-72,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,-16,-44,-118,-76,-15,-40,-41,-53,-54,-57,-121,-121,-61,207,-58,-59,-37,-38,-103,-104,]),'RBRACKET':([40,56,57,58,59,60,61,66,80,81,82,83,84,122,127,143,145,146,147,150,155,156,157,167,177,178,179,180,181,182,183,230,241,242,243,244,245,246,247,249,250,251,252,253,254,255,258,259,261,262,263,264,266,267,],[-17,-117,-117,-117,-117,-71,-1,-14,-67,-68,-69,-70,-72,-1,-16,-76,177,-1,-30,-33,-80,-81,-82,-15,-28,-29,-31,-32,-34,-35,-36,-1,-1,256,257,-105,-106,-1,-108,-1,-84,-91,-92,-87,-88,262,-107,-83,-86,-1,-85,-109,-111,-110,]),'EQUAL':([40,66,127,154,167,184,190,],[-17,-14,-16,-1,-15,199,-1,]),'ESCRIBE':([122,146,150,155,156,157,177,179,180,181,182,183,249,250,251,252,253,254,259,261,263,],[158,158,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'LEE':([122,146,150,155,156,157,177,179,180,181,182,183,249,250,251,252,253,254,259,261,263,],[159,159,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'REGRESA':([122,146,150,155,156,157,177,179,180,181,182,183,249,250,251,252,253,254,259,261,263,],[160,160,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'SI':([122,146,150,155,156,157,177,179,180,181,182,183,225,235,236,237,238,239,249,250,251,252,253,254,259,261,263,],[161,161,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,161,161,161,-89,-90,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'DESDE':([122,146,150,155,156,157,177,179,180,181,182,183,225,235,236,237,238,239,249,250,251,252,253,254,259,261,263,],[162,162,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,162,162,162,-89,-90,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'MIENTRAS':([122,146,150,155,156,157,177,179,180,181,182,183,225,235,236,237,238,239,249,250,251,252,253,254,259,261,263,],[163,163,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,163,163,163,-89,-90,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'SINO':([177,249,],[-28,260,]),'NULL':([187,],[205,]),'ENTONCES':([223,],[235,]),'HAZ':([225,],[238,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'VARS':([4,62,124,166,],[5,86,165,196,]),'empty':([4,5,6,9,24,34,61,62,68,69,70,71,85,122,124,144,146,154,164,166,190,192,201,203,220,225,230,241,246,249,262,],[7,10,14,10,14,40,40,7,95,98,108,113,120,147,7,120,147,40,194,7,40,211,218,40,234,239,247,247,247,261,266,]),'FUNCTIONS':([5,9,],[8,21,]),'FUNCTION':([5,9,],[9,9,]),'VAR_AUX':([6,24,],[12,33,]),'TIPO':([6,11,24,63,89,210,],[13,22,13,87,87,87,]),'MAIN':([8,],[19,]),'IDS':([13,45,],[24,65,]),'r_save_type':([15,16,17,18,23,],[26,27,28,29,32,]),'r_save_func':([20,31,37,],[30,36,43,]),'r_register_var':([25,123,],[34,164,]),'ARRDIM':([34,61,154,190,203,],[38,84,184,184,220,]),'r_register_func':([36,43,],[42,64,]),'EXPRESION':([39,67,72,85,90,128,129,144,185,187,188,191,207,214,217,],[46,91,114,119,126,168,169,119,201,204,206,208,224,228,201,]),'SUBEXP':([39,67,72,85,90,97,128,129,144,185,187,188,191,207,214,217,],[47,47,47,47,47,130,47,47,47,47,47,47,47,47,47,47,]),'EXP':([39,67,72,85,90,97,128,129,137,138,144,185,187,188,191,207,214,217,],[48,48,48,48,48,48,48,48,170,171,48,48,48,48,48,48,48,48,]),'TERMINO':([39,67,72,85,90,97,128,129,137,138,139,140,141,144,185,187,188,191,207,214,217,],[49,49,49,49,49,49,49,49,49,49,172,173,174,49,49,49,49,49,49,49,49,]),'FACTOR':([39,67,72,85,90,97,128,129,137,138,139,140,141,144,185,187,188,191,207,214,217,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'CTE':([39,67,72,73,78,79,85,90,97,128,129,137,138,139,140,141,144,185,187,188,191,207,214,217,230,241,246,],[53,53,53,115,116,117,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,244,244,244,]),'FUN':([39,67,72,73,78,79,85,90,97,122,128,129,137,138,139,140,141,144,146,185,187,188,191,207,214,217,230,241,246,],[60,60,60,60,60,60,60,60,60,149,60,60,60,60,60,60,60,60,149,60,60,60,60,60,60,60,60,60,60,]),'r_register_princ':([41,],[62,]),'r_seen_subexp':([47,],[68,]),'r_seen_exp':([48,],[69,]),'r_seen_term':([49,173,174,],[70,197,198,]),'r_seen_factor':([50,],[71,]),'r_seen_operator':([51,93,94,99,100,101,102,103,104,106,107,110,111,112,142,199,],[72,128,129,131,132,133,134,135,136,137,138,139,140,141,175,214,]),'r_seen_unary_operator':([52,54,55,],[73,78,79,]),'ARROP':([53,],[74,]),'r_seen_operand':([56,57,58,59,],[80,81,82,83,]),'PARAM':([63,89,210,],[88,125,226,]),'EXPRESION_AUX':([68,],[92,]),'SUBEXP_AUX':([69,],[96,]),'COMPARACION':([69,],[97,]),'EXP_AUX':([70,],[105,]),'TERMINO_AUX':([71,],[109,]),'FUN_AUX':([85,144,],[118,176,]),'BLOQUE':([86,165,196,235,236,237,260,],[121,195,213,249,251,253,263,]),'ESTATUTOS':([122,146,],[145,178,]),'ESTATUTO':([122,146,],[146,146,]),'ASIGNACION':([122,146,162,],[148,148,189,]),'COND':([122,146,235,236,237,],[150,150,250,252,254,]),'WRITE':([122,146,],[151,151,]),'READ':([122,146,],[152,152,]),'RETURN':([122,146,],[153,153,]),'IF':([122,146,235,236,237,],[155,155,155,155,155,]),'FOR':([122,146,235,236,237,],[156,156,156,156,156,]),'WHILE':([122,146,235,236,237,],[157,157,157,157,157,]),'PARENTESIS':([164,],[192,]),'WRITE_AUX':([185,217,],[200,231,]),'READ_AUX':([186,233,],[202,248,]),'PARAM_AUX':([192,],[209,]),'WRITE_AUXSUB':([201,],[216,]),'CTE_ARR':([214,],[229,]),'READ_AUXSUB':([220,],[232,]),'WHILE_AUX':([225,],[237,]),'CTE_ARR_AUX':([230,241,246,],[242,255,258,]),'CTE_ARR_AUX2':([230,265,],[243,267,]),'CTE_ARR_AUXSUB':([230,241,246,],[245,245,245,]),'IF_AUX':([249,],[259,]),'CTE_ARR_AUX2SUB':([262,],[264,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',14),
  ('PROGRAM -> PROGRAMA ID DOTCOMA VARS FUNCTIONS MAIN','PROGRAM',6,'p_PROGRAM','parser.py',19),
  ('MAIN -> PRINCIPAL r_save_func LPAREN RPAREN r_register_princ VARS BLOQUE','MAIN',7,'p_MAIN','parser.py',24),
  ('VARS -> VAR VAR_AUX','VARS',2,'p_VARS','parser.py',29),
  ('VARS -> empty','VARS',1,'p_VARS','parser.py',30),
  ('VAR_AUX -> TIPO IDS VAR_AUX','VAR_AUX',3,'p_VAR_AUX','parser.py',35),
  ('VAR_AUX -> empty','VAR_AUX',1,'p_VAR_AUX','parser.py',36),
  ('TIPO -> INT r_save_type','TIPO',2,'p_TIPO','parser.py',41),
  ('TIPO -> FLOAT r_save_type','TIPO',2,'p_TIPO','parser.py',42),
  ('TIPO -> CHAR r_save_type','TIPO',2,'p_TIPO','parser.py',43),
  ('TIPO -> STRING r_save_type','TIPO',2,'p_TIPO','parser.py',44),
  ('IDS -> ID r_register_var ARRDIM DOTCOMA','IDS',4,'p_IDS','parser.py',49),
  ('IDS -> ID r_register_var ARRDIM COMA IDS','IDS',5,'p_IDS','parser.py',50),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE','ARRDIM',3,'p_ARRDIM','parser.py',55),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE','ARRDIM',6,'p_ARRDIM','parser.py',56),
  ('ARRDIM -> LSTAPLE EXPRESION COMA EXPRESION RSTAPLE','ARRDIM',5,'p_ARRDIM','parser.py',57),
  ('ARRDIM -> empty','ARRDIM',1,'p_ARRDIM','parser.py',58),
  ('FUNCTIONS -> FUNCTION FUNCTIONS','FUNCTIONS',2,'p_FUNCTIONS','parser.py',63),
  ('FUNCTIONS -> empty','FUNCTIONS',1,'p_FUNCTIONS','parser.py',64),
  ('FUNCTION -> FUNCION TIPO ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUE','FUNCTION',10,'p_FUNCTION','parser.py',69),
  ('FUNCTION -> FUNCION VOID r_save_type ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUE','FUNCTION',11,'p_FUNCTION','parser.py',70),
  ('PARAM -> TIPO ID r_register_var PARENTESIS PARAM_AUX','PARAM',5,'p_PARAM','parser.py',75),
  ('PARAM_AUX -> COMA PARAM','PARAM_AUX',2,'p_PARAM_AUX','parser.py',80),
  ('PARAM_AUX -> empty','PARAM_AUX',1,'p_PARAM_AUX','parser.py',81),
  ('PARENTESIS -> LSTAPLE RSTAPLE','PARENTESIS',2,'p_PARENTESIS','parser.py',86),
  ('PARENTESIS -> LSTAPLE RSTAPLE LSTAPLE RSTAPLE','PARENTESIS',4,'p_PARENTESIS','parser.py',87),
  ('PARENTESIS -> empty','PARENTESIS',1,'p_PARENTESIS','parser.py',88),
  ('BLOQUE -> LBRACKET ESTATUTOS RBRACKET','BLOQUE',3,'p_BLOQUE','parser.py',93),
  ('ESTATUTOS -> ESTATUTO ESTATUTOS','ESTATUTOS',2,'p_ESTATUTOS','parser.py',98),
  ('ESTATUTOS -> empty','ESTATUTOS',1,'p_ESTATUTOS','parser.py',99),
  ('ESTATUTO -> ASIGNACION DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',104),
  ('ESTATUTO -> FUN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',105),
  ('ESTATUTO -> COND','ESTATUTO',1,'p_ESTATUTO','parser.py',106),
  ('ESTATUTO -> WRITE DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',107),
  ('ESTATUTO -> READ DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',108),
  ('ESTATUTO -> RETURN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',109),
  ('ASIGNACION -> ID ARRDIM EQUAL r_seen_operator EXPRESION','ASIGNACION',5,'p_ASIGNACION','parser.py',114),
  ('ASIGNACION -> ID ARRDIM EQUAL r_seen_operator CTE_ARR','ASIGNACION',5,'p_ASIGNACION','parser.py',115),
  ('EXPRESION -> SUBEXP r_seen_subexp EXPRESION_AUX','EXPRESION',3,'p_EXPRESION','parser.py',120),
  ('EXPRESION_AUX -> AND r_seen_operator EXPRESION','EXPRESION_AUX',3,'p_EXPRESION_AUX','parser.py',125),
  ('EXPRESION_AUX -> OR r_seen_operator EXPRESION','EXPRESION_AUX',3,'p_EXPRESION_AUX','parser.py',126),
  ('EXPRESION_AUX -> empty','EXPRESION_AUX',1,'p_EXPRESION_AUX','parser.py',127),
  ('SUBEXP -> EXP r_seen_exp SUBEXP_AUX','SUBEXP',3,'p_SUBEXP','parser.py',132),
  ('SUBEXP_AUX -> COMPARACION SUBEXP','SUBEXP_AUX',2,'p_SUBEXP_AUX','parser.py',137),
  ('SUBEXP_AUX -> empty','SUBEXP_AUX',1,'p_SUBEXP_AUX','parser.py',138),
  ('COMPARACION -> MORE r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',143),
  ('COMPARACION -> LESS r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',144),
  ('COMPARACION -> COMPARE r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',145),
  ('COMPARACION -> DIFFERENT r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',146),
  ('COMPARACION -> MOREEQUAL r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',147),
  ('COMPARACION -> LESSEQUAL r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',148),
  ('EXP -> TERMINO r_seen_term EXP_AUX','EXP',3,'p_EXP','parser.py',153),
  ('EXP_AUX -> PLUS r_seen_operator EXP','EXP_AUX',3,'p_EXP_AUX','parser.py',158),
  ('EXP_AUX -> MINUS r_seen_operator EXP','EXP_AUX',3,'p_EXP_AUX','parser.py',159),
  ('EXP_AUX -> empty','EXP_AUX',1,'p_EXP_AUX','parser.py',160),
  ('TERMINO -> FACTOR r_seen_factor TERMINO_AUX','TERMINO',3,'p_TERMINO','parser.py',165),
  ('TERMINO_AUX -> MULT r_seen_operator TERMINO','TERMINO_AUX',3,'p_TERMINO_AUX','parser.py',170),
  ('TERMINO_AUX -> DIV r_seen_operator TERMINO r_seen_term','TERMINO_AUX',4,'p_TERMINO_AUX','parser.py',171),
  ('TERMINO_AUX -> MOD r_seen_operator TERMINO r_seen_term','TERMINO_AUX',4,'p_TERMINO_AUX','parser.py',172),
  ('TERMINO_AUX -> empty','TERMINO_AUX',1,'p_TERMINO_AUX','parser.py',173),
  ('FACTOR -> LPAREN r_seen_operator EXPRESION RPAREN r_seen_operator','FACTOR',5,'p_FACTOR','parser.py',179),
  ('FACTOR -> PLUS r_seen_unary_operator CTE','FACTOR',3,'p_FACTOR','parser.py',180),
  ('FACTOR -> MINUS r_seen_unary_operator CTE','FACTOR',3,'p_FACTOR','parser.py',181),
  ('FACTOR -> NOT r_seen_unary_operator CTE','FACTOR',3,'p_FACTOR','parser.py',182),
  ('FACTOR -> CTE ARROP','FACTOR',2,'p_FACTOR','parser.py',183),
  ('FACTOR -> CTE','FACTOR',1,'p_FACTOR','parser.py',184),
  ('CTE -> CTE_I r_seen_operand','CTE',2,'p_CTE','parser.py',189),
  ('CTE -> CTE_F r_seen_operand','CTE',2,'p_CTE','parser.py',190),
  ('CTE -> CTE_CH r_seen_operand','CTE',2,'p_CTE','parser.py',191),
  ('CTE -> CTE_STRING r_seen_operand','CTE',2,'p_CTE','parser.py',192),
  ('CTE -> FUN','CTE',1,'p_CTE','parser.py',193),
  ('CTE -> ID ARRDIM','CTE',2,'p_CTE','parser.py',194),
  ('ARROP -> DET_ARR','ARROP',1,'p_ARROP','parser.py',199),
  ('ARROP -> TRANS_ARR','ARROP',1,'p_ARROP','parser.py',200),
  ('ARROP -> INV_ARR','ARROP',1,'p_ARROP','parser.py',201),
  ('FUN -> ID LPAREN FUN_AUX RPAREN','FUN',4,'p_FUN','parser.py',206),
  ('FUN_AUX -> EXPRESION COMA FUN_AUX','FUN_AUX',3,'p_FUN_AUX','parser.py',211),
  ('FUN_AUX -> EXPRESION','FUN_AUX',1,'p_FUN_AUX','parser.py',212),
  ('FUN_AUX -> empty','FUN_AUX',1,'p_FUN_AUX','parser.py',213),
  ('COND -> IF','COND',1,'p_COND','parser.py',218),
  ('COND -> FOR','COND',1,'p_COND','parser.py',219),
  ('COND -> WHILE','COND',1,'p_COND','parser.py',220),
  ('IF -> SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE IF_AUX','IF',7,'p_IF','parser.py',225),
  ('IF -> SI LPAREN EXPRESION RPAREN ENTONCES COND','IF',6,'p_IF','parser.py',226),
  ('IF_AUX -> SINO BLOQUE','IF_AUX',2,'p_IF_AUX','parser.py',231),
  ('IF_AUX -> empty','IF_AUX',1,'p_IF_AUX','parser.py',232),
  ('WHILE -> MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX BLOQUE','WHILE',6,'p_WHILE','parser.py',237),
  ('WHILE -> MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX COND','WHILE',6,'p_WHILE','parser.py',238),
  ('WHILE_AUX -> HAZ','WHILE_AUX',1,'p_WHILE_AUX','parser.py',243),
  ('WHILE_AUX -> empty','WHILE_AUX',1,'p_WHILE_AUX','parser.py',244),
  ('FOR -> DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE','FOR',6,'p_FOR','parser.py',249),
  ('FOR -> DESDE ASIGNACION HASTA EXPRESION HACER COND','FOR',6,'p_FOR','parser.py',250),
  ('WRITE -> ESCRIBE LPAREN WRITE_AUX RPAREN','WRITE',4,'p_WRITE','parser.py',255),
  ('WRITE_AUX -> EXPRESION WRITE_AUXSUB','WRITE_AUX',2,'p_WRITE_AUX','parser.py',260),
  ('WRITE_AUXSUB -> COMA WRITE_AUX','WRITE_AUXSUB',2,'p_WRITE_AUXSUB','parser.py',265),
  ('WRITE_AUXSUB -> empty','WRITE_AUXSUB',1,'p_WRITE_AUXSUB','parser.py',266),
  ('READ -> LEE LPAREN READ_AUX RPAREN','READ',4,'p_READ','parser.py',271),
  ('READ_AUX -> ID ARRDIM READ_AUXSUB','READ_AUX',3,'p_READ_AUX','parser.py',276),
  ('READ_AUXSUB -> COMA READ_AUX','READ_AUXSUB',2,'p_READ_AUXSUB','parser.py',281),
  ('READ_AUXSUB -> empty','READ_AUXSUB',1,'p_READ_AUXSUB','parser.py',282),
  ('RETURN -> REGRESA LPAREN EXPRESION RPAREN','RETURN',4,'p_RETURN','parser.py',287),
  ('RETURN -> REGRESA LPAREN NULL RPAREN','RETURN',4,'p_RETURN','parser.py',288),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX RBRACKET','CTE_ARR',3,'p_CTE_ARR','parser.py',293),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX2 RBRACKET','CTE_ARR',3,'p_CTE_ARR','parser.py',294),
  ('CTE_ARR_AUX -> CTE','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','parser.py',299),
  ('CTE_ARR_AUX -> CTE_ARR_AUXSUB','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','parser.py',300),
  ('CTE_ARR_AUXSUB -> COMA CTE_ARR_AUX','CTE_ARR_AUXSUB',2,'p_CTE_ARR_AUXSUB','parser.py',305),
  ('CTE_ARR_AUXSUB -> empty','CTE_ARR_AUXSUB',1,'p_CTE_ARR_AUXSUB','parser.py',306),
  ('CTE_ARR_AUX2 -> LBRACKET CTE_ARR_AUX RBRACKET CTE_ARR_AUX2SUB','CTE_ARR_AUX2',4,'p_CTE_ARR_AUX2','parser.py',311),
  ('CTE_ARR_AUX2SUB -> COMA CTE_ARR_AUX2','CTE_ARR_AUX2SUB',2,'p_CTE_ARR_AUX2SUB','parser.py',316),
  ('CTE_ARR_AUX2SUB -> empty','CTE_ARR_AUX2SUB',1,'p_CTE_ARR_AUX2SUB','parser.py',317),
  ('r_save_type -> <empty>','r_save_type',0,'p_r_save_type','parser.py',338),
  ('r_save_func -> <empty>','r_save_func',0,'p_r_save_func','parser.py',343),
  ('r_register_func -> <empty>','r_register_func',0,'p_r_register_func','parser.py',348),
  ('r_register_var -> <empty>','r_register_var',0,'p_r_register_var','parser.py',356),
  ('r_register_princ -> <empty>','r_register_princ',0,'p_r_register_princ','parser.py',365),
  ('r_seen_operand -> <empty>','r_seen_operand',0,'p_r_seen_operand','parser.py',372),
  ('r_seen_operator -> <empty>','r_seen_operator',0,'p_r_seen_operator','parser.py',378),
  ('r_seen_subexp -> <empty>','r_seen_subexp',0,'p_r_seen_subexp','parser.py',385),
  ('r_seen_exp -> <empty>','r_seen_exp',0,'p_r_seen_exp','parser.py',391),
  ('r_seen_term -> <empty>','r_seen_term',0,'p_r_seen_term','parser.py',397),
  ('r_seen_factor -> <empty>','r_seen_factor',0,'p_r_seen_factor','parser.py',403),
  ('r_seen_unary_operator -> <empty>','r_seen_unary_operator',0,'p_r_seen_unary_operator','parser.py',409),
]
