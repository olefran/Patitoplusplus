
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMleftPLUSMINUSleftMULTDIVMODrightEQUALleftANDORAND CHAR COMA COMMENT COMPARE CTE_CH CTE_F CTE_I CTE_STRING DESDE DET_ARR DIFFERENT DIV DOTCOMA ENTONCES EQUAL ESCRIBE FLOAT FUNCION HACER HASTA HAZ ID INT INV_ARR LBRACKET LEE LESS LESSEQUAL LPAREN LSTAPLE MIENTRAS MINUS MOD MORE MOREEQUAL MULT NOT NULL OR PLUS PRINCIPAL PROGRAMA RBRACKET REGRESA RPAREN RSTAPLE SI SINO STRING TRANS_ARR VAR VOIDempty :PROGRAM : PROGRAMA ID DOTCOMA VARS FUNCTIONS MAINMAIN : PRINCIPAL r_save_func LPAREN RPAREN r_register_princ VARS BLOQUEVARS : VAR VAR_AUX\n    | emptyVAR_AUX : TIPO IDS VAR_AUX\n    | emptyTIPO : INT r_save_type\n    | FLOAT r_save_type\n    | CHAR r_save_type\n    | STRING r_save_typeIDS : ID r_register_var ARRDIM DOTCOMA\n    | ID r_register_var ARRDIM COMA IDSARRDIM : LSTAPLE EXPRESION RSTAPLE\n    | LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE\n    | LSTAPLE EXPRESION COMA EXPRESION RSTAPLE\n    | emptyFUNCTIONS : FUNCTION FUNCTIONS\n    | emptyFUNCTION : FUNCION TIPO ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUE\n    | FUNCION VOID r_save_type ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUEPARAM : TIPO ID r_register_var PARENTESIS PARAM_AUXPARAM_AUX : COMA PARAM\n    | emptyPARENTESIS : LSTAPLE RSTAPLE\n    | LSTAPLE RSTAPLE LSTAPLE RSTAPLE\n    | emptyBLOQUE : LBRACKET ESTATUTOS RBRACKETESTATUTOS : ESTATUTO ESTATUTOS\n    | emptyESTATUTO : ASIGNACION DOTCOMA\n    | FUN DOTCOMA\n    | COND\n    | WRITE DOTCOMA\n    | READ DOTCOMA\n    | RETURN DOTCOMAASIGNACION : ID r_seen_operand_id ARRDIM EQUAL r_seen_operator EXPRESION r_seen_equal\n    | ID r_seen_operand_id ARRDIM EQUAL r_seen_operator CTE_ARREXPRESION : SUBEXP r_seen_subexp EXPRESION_AUXEXPRESION_AUX : AND r_seen_operator EXPRESION\n    | OR r_seen_operator EXPRESION\n    | emptySUBEXP : EXP r_seen_exp SUBEXP_AUXSUBEXP_AUX : COMPARACION SUBEXP\n    | emptyCOMPARACION : MORE r_seen_operator\n    | LESS r_seen_operator\n    | COMPARE r_seen_operator\n    | DIFFERENT r_seen_operator\n    | MOREEQUAL r_seen_operator\n    | LESSEQUAL r_seen_operatorEXP : TERMINO r_seen_term EXP_AUXEXP_AUX : PLUS r_seen_operator EXP\n    | MINUS r_seen_operator EXP\n    | emptyTERMINO : FACTOR r_seen_factor TERMINO_AUXTERMINO_AUX : MULT r_seen_operator TERMINO\n    | DIV r_seen_operator TERMINO r_seen_term\n    | MOD r_seen_operator TERMINO r_seen_term\n    | emptyFACTOR : LPAREN r_seen_operator EXPRESION RPAREN r_seen_operator\n    | PLUS r_seen_unary_operator CTE\n    | MINUS r_seen_unary_operator CTE\n    | NOT r_seen_unary_operator CTE\n    | CTE ARROP\n    | CTECTE : CTE_I r_seen_operand\n    | CTE_F r_seen_operand\n    | CTE_CH r_seen_operand\n    | CTE_STRING r_seen_operand\n    | FUN\n    | ID r_seen_operand_id ARRDIM ARROP : DET_ARR\n    | TRANS_ARR\n    | INV_ARRFUN : ID LPAREN FUN_AUX RPARENFUN_AUX : EXPRESION COMA FUN_AUX\n    | EXPRESION\n    | emptyCOND : IF\n    | FOR\n    | WHILEIF : SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE IF_AUX\n    | SI LPAREN EXPRESION RPAREN ENTONCES COND IF_AUX : SINO BLOQUE\n    | emptyWHILE :  MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX BLOQUE\n    | MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX CONDWHILE_AUX : HAZ\n    | empty FOR :  DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE\n    | DESDE ASIGNACION HASTA EXPRESION HACER CONDWRITE : ESCRIBE LPAREN WRITE_AUX RPARENWRITE_AUX : EXPRESION WRITE_AUXSUBWRITE_AUXSUB : COMA WRITE_AUX\n    | emptyREAD : LEE LPAREN READ_AUX RPARENREAD_AUX : ID ARRDIM READ_AUXSUBREAD_AUXSUB : COMA READ_AUX\n    | emptyRETURN : REGRESA LPAREN EXPRESION RPAREN\n    | REGRESA LPAREN NULL RPARENCTE_ARR : LBRACKET CTE_ARR_AUX RBRACKET\n    | LBRACKET CTE_ARR_AUX2 RBRACKET CTE_ARR_AUX : CTE\n    | CTE_ARR_AUXSUB CTE_ARR_AUXSUB : COMA CTE_ARR_AUX\n    | empty CTE_ARR_AUX2 : LBRACKET CTE_ARR_AUX RBRACKET  CTE_ARR_AUX2SUBCTE_ARR_AUX2SUB : COMA CTE_ARR_AUX2\n    | empty r_save_type : r_save_func : r_register_func : r_register_var : r_register_princ : r_seen_operand : r_seen_operand_id :r_seen_operator : r_seen_equal : r_seen_subexp : r_seen_exp : r_seen_term : r_seen_factor : r_seen_unary_operator : '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,19,122,178,],[0,-2,-3,-28,]),'ID':([2,13,15,16,17,18,22,23,26,27,28,29,32,39,45,51,52,54,55,67,72,73,78,79,85,87,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,123,129,130,132,133,134,135,136,137,138,139,140,141,142,145,147,151,156,157,158,163,178,180,181,182,183,184,186,187,188,189,192,208,215,218,229,232,242,244,245,246,247,248,249,251,256,258,260,265,],[3,25,-112,-112,-112,-112,31,-112,-8,-9,-10,-11,37,61,25,-119,-125,-125,-125,61,61,61,61,61,61,124,61,-119,-119,61,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,155,61,61,-46,-47,-48,-49,-50,-51,61,61,61,61,61,61,155,-33,-80,-81,-82,191,-28,-31,-32,-34,-35,-36,61,204,61,61,61,61,-119,61,61,204,61,-1,-84,-91,-92,-87,-88,61,61,-83,-86,-85,]),'DOTCOMA':([3,25,34,38,40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,92,95,96,98,105,108,109,113,115,116,117,118,128,131,143,144,149,150,152,153,154,168,169,170,171,172,173,174,175,176,198,199,216,220,222,223,240,241,250,262,263,],[4,-115,-1,44,-17,-121,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,-72,-16,-44,-119,-76,180,181,182,183,184,-15,-40,-41,-53,-54,-57,-123,-123,-61,-58,-59,-93,-97,-101,-102,-120,-38,-37,-103,-104,]),'VAR':([4,41,62,125,167,],[6,-116,6,6,6,]),'FUNCION':([4,5,6,7,9,12,14,24,33,44,65,178,196,214,],[-1,11,-1,-5,11,-4,-7,-1,-6,-12,-13,-28,-20,-21,]),'PRINCIPAL':([4,5,6,7,8,9,10,12,14,21,24,33,44,65,178,196,214,],[-1,-1,-1,-5,20,-1,-19,-4,-7,-18,-1,-6,-12,-13,-28,-20,-21,]),'INT':([6,11,24,44,63,65,89,211,],[15,15,15,-12,15,-13,15,15,]),'FLOAT':([6,11,24,44,63,65,89,211,],[16,16,16,-12,16,-13,16,16,]),'CHAR':([6,11,24,44,63,65,89,211,],[17,17,17,-12,17,-13,17,17,]),'STRING':([6,11,24,44,63,65,89,211,],[18,18,18,-12,18,-13,18,18,]),'LBRACKET':([6,7,12,14,24,33,41,44,62,65,86,125,166,167,197,215,226,229,234,235,236,237,238,242,259,268,],[-1,-5,-4,-7,-1,-6,-116,-12,-1,-13,123,-1,123,-1,123,-119,-1,242,123,123,123,-89,-90,251,123,251,]),'VOID':([11,],[23,]),'LPAREN':([20,30,31,36,37,39,42,43,51,61,64,67,72,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,129,130,132,133,134,135,136,137,138,139,140,141,142,145,155,159,160,161,162,164,186,188,189,192,208,215,218,229,],[-113,35,-113,-114,-113,51,63,-114,-119,85,89,51,51,51,51,-119,-119,51,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,51,51,-46,-47,-48,-49,-50,-51,51,51,51,51,51,51,85,186,187,188,189,192,51,51,51,51,51,-119,51,51,]),'LSTAPLE':([25,34,61,66,84,124,155,165,185,191,204,213,],[-115,39,-118,90,39,-115,-118,194,39,-118,39,228,]),'COMA':([25,34,38,40,46,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,92,95,96,98,105,108,109,113,115,116,117,118,120,124,128,131,143,144,165,168,169,170,171,172,173,174,175,176,193,195,198,199,202,204,213,221,239,242,251,256,266,],[-115,-1,45,-17,67,-121,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,-72,145,-115,-16,-44,-119,-76,-1,-15,-40,-41,-53,-54,-57,-123,-123,-61,211,-27,-58,-59,218,-1,-25,232,-26,256,256,256,268,]),'RPAREN':([35,40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,85,88,92,95,96,98,105,108,109,113,114,115,116,117,118,119,120,121,124,126,128,131,143,144,145,165,168,169,170,171,172,173,174,175,176,177,193,195,198,199,201,202,203,204,205,206,207,209,210,212,213,217,219,221,227,230,231,233,239,243,],[41,-17,-121,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-1,125,-39,-42,-43,-45,-52,-55,-56,-60,143,-62,-63,-64,-72,144,-78,-79,-115,167,-16,-44,-119,-76,-1,-1,-15,-40,-41,-53,-54,-57,-123,-123,-61,-77,-1,-27,-58,-59,216,-1,220,-1,222,223,224,226,-22,-24,-25,-94,-96,-1,-23,-95,-98,-100,-26,-99,]),'PLUS':([39,40,49,50,51,53,56,57,58,59,60,61,66,67,70,71,72,74,75,76,77,80,81,82,83,84,85,90,93,94,97,99,100,101,102,103,104,106,107,109,110,111,112,113,115,116,117,118,128,129,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,168,173,174,175,176,186,188,189,192,198,199,208,215,218,229,],[52,-17,-123,-124,-119,-66,-117,-117,-117,-117,-71,-118,-14,52,106,-1,52,-65,-73,-74,-75,-67,-68,-69,-70,-1,52,52,-119,-119,52,-119,-119,-119,-119,-119,-119,-119,-119,-56,-119,-119,-119,-60,-62,-63,-64,-72,-16,52,52,-46,-47,-48,-49,-50,-51,52,52,52,52,52,-119,-76,52,-15,-57,-123,-123,-61,52,52,52,52,-58,-59,52,-119,52,52,]),'MINUS':([39,40,49,50,51,53,56,57,58,59,60,61,66,67,70,71,72,74,75,76,77,80,81,82,83,84,85,90,93,94,97,99,100,101,102,103,104,106,107,109,110,111,112,113,115,116,117,118,128,129,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,168,173,174,175,176,186,188,189,192,198,199,208,215,218,229,],[54,-17,-123,-124,-119,-66,-117,-117,-117,-117,-71,-118,-14,54,107,-1,54,-65,-73,-74,-75,-67,-68,-69,-70,-1,54,54,-119,-119,54,-119,-119,-119,-119,-119,-119,-119,-119,-56,-119,-119,-119,-60,-62,-63,-64,-72,-16,54,54,-46,-47,-48,-49,-50,-51,54,54,54,54,54,-119,-76,54,-15,-57,-123,-123,-61,54,54,54,54,-58,-59,54,-119,54,54,]),'NOT':([39,51,67,72,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,129,130,132,133,134,135,136,137,138,139,140,141,142,145,186,188,189,192,208,215,218,229,],[55,-119,55,55,55,55,-119,-119,55,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,55,55,-46,-47,-48,-49,-50,-51,55,55,55,55,55,55,55,55,55,55,55,-119,55,55,]),'CTE_I':([39,51,52,54,55,67,72,73,78,79,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,129,130,132,133,134,135,136,137,138,139,140,141,142,145,186,188,189,192,208,215,218,229,242,251,256,],[56,-119,-125,-125,-125,56,56,56,56,56,56,56,-119,-119,56,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,56,56,-46,-47,-48,-49,-50,-51,56,56,56,56,56,56,56,56,56,56,56,-119,56,56,56,56,56,]),'CTE_F':([39,51,52,54,55,67,72,73,78,79,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,129,130,132,133,134,135,136,137,138,139,140,141,142,145,186,188,189,192,208,215,218,229,242,251,256,],[57,-119,-125,-125,-125,57,57,57,57,57,57,57,-119,-119,57,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,57,57,-46,-47,-48,-49,-50,-51,57,57,57,57,57,57,57,57,57,57,57,-119,57,57,57,57,57,]),'CTE_CH':([39,51,52,54,55,67,72,73,78,79,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,129,130,132,133,134,135,136,137,138,139,140,141,142,145,186,188,189,192,208,215,218,229,242,251,256,],[58,-119,-125,-125,-125,58,58,58,58,58,58,58,-119,-119,58,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,58,58,-46,-47,-48,-49,-50,-51,58,58,58,58,58,58,58,58,58,58,58,-119,58,58,58,58,58,]),'CTE_STRING':([39,51,52,54,55,67,72,73,78,79,85,90,93,94,97,99,100,101,102,103,104,106,107,110,111,112,129,130,132,133,134,135,136,137,138,139,140,141,142,145,186,188,189,192,208,215,218,229,242,251,256,],[59,-119,-125,-125,-125,59,59,59,59,59,59,59,-119,-119,59,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,-119,59,59,-46,-47,-48,-49,-50,-51,59,59,59,59,59,59,59,59,59,59,59,-119,59,59,59,59,59,]),'DET_ARR':([40,53,56,57,58,59,60,61,66,80,81,82,83,84,118,128,144,168,],[-17,75,-117,-117,-117,-117,-71,-118,-14,-67,-68,-69,-70,-1,-72,-16,-76,-15,]),'TRANS_ARR':([40,53,56,57,58,59,60,61,66,80,81,82,83,84,118,128,144,168,],[-17,76,-117,-117,-117,-117,-71,-118,-14,-67,-68,-69,-70,-1,-72,-16,-76,-15,]),'INV_ARR':([40,53,56,57,58,59,60,61,66,80,81,82,83,84,118,128,144,168,],[-17,77,-117,-117,-117,-117,-71,-118,-14,-67,-68,-69,-70,-1,-72,-16,-76,-15,]),'MULT':([40,50,53,56,57,58,59,60,61,66,71,74,75,76,77,80,81,82,83,84,115,116,117,118,128,143,144,168,176,],[-17,-124,-66,-117,-117,-117,-117,-71,-118,-14,110,-65,-73,-74,-75,-67,-68,-69,-70,-1,-62,-63,-64,-72,-16,-119,-76,-15,-61,]),'DIV':([40,50,53,56,57,58,59,60,61,66,71,74,75,76,77,80,81,82,83,84,115,116,117,118,128,143,144,168,176,],[-17,-124,-66,-117,-117,-117,-117,-71,-118,-14,111,-65,-73,-74,-75,-67,-68,-69,-70,-1,-62,-63,-64,-72,-16,-119,-76,-15,-61,]),'MOD':([40,50,53,56,57,58,59,60,61,66,71,74,75,76,77,80,81,82,83,84,115,116,117,118,128,143,144,168,176,],[-17,-124,-66,-117,-117,-117,-117,-71,-118,-14,112,-65,-73,-74,-75,-67,-68,-69,-70,-1,-62,-63,-64,-72,-16,-119,-76,-15,-61,]),'MORE':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,118,128,143,144,168,171,172,173,174,175,176,198,199,],[-17,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,99,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-52,-55,-56,-60,-62,-63,-64,-72,-16,-119,-76,-15,-53,-54,-57,-123,-123,-61,-58,-59,]),'LESS':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,118,128,143,144,168,171,172,173,174,175,176,198,199,],[-17,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,100,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-52,-55,-56,-60,-62,-63,-64,-72,-16,-119,-76,-15,-53,-54,-57,-123,-123,-61,-58,-59,]),'COMPARE':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,118,128,143,144,168,171,172,173,174,175,176,198,199,],[-17,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,101,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-52,-55,-56,-60,-62,-63,-64,-72,-16,-119,-76,-15,-53,-54,-57,-123,-123,-61,-58,-59,]),'DIFFERENT':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,118,128,143,144,168,171,172,173,174,175,176,198,199,],[-17,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,102,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-52,-55,-56,-60,-62,-63,-64,-72,-16,-119,-76,-15,-53,-54,-57,-123,-123,-61,-58,-59,]),'MOREEQUAL':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,118,128,143,144,168,171,172,173,174,175,176,198,199,],[-17,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,103,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-52,-55,-56,-60,-62,-63,-64,-72,-16,-119,-76,-15,-53,-54,-57,-123,-123,-61,-58,-59,]),'LESSEQUAL':([40,48,49,50,53,56,57,58,59,60,61,66,69,70,71,74,75,76,77,80,81,82,83,84,105,108,109,113,115,116,117,118,128,143,144,168,171,172,173,174,175,176,198,199,],[-17,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,104,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-52,-55,-56,-60,-62,-63,-64,-72,-16,-119,-76,-15,-53,-54,-57,-123,-123,-61,-58,-59,]),'AND':([40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,96,98,105,108,109,113,115,116,117,118,128,131,143,144,168,171,172,173,174,175,176,198,199,],[-17,-121,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,93,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-43,-45,-52,-55,-56,-60,-62,-63,-64,-72,-16,-44,-119,-76,-15,-53,-54,-57,-123,-123,-61,-58,-59,]),'OR':([40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,96,98,105,108,109,113,115,116,117,118,128,131,143,144,168,171,172,173,174,175,176,198,199,],[-17,-121,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,94,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-43,-45,-52,-55,-56,-60,-62,-63,-64,-72,-16,-44,-119,-76,-15,-53,-54,-57,-123,-123,-61,-58,-59,]),'RSTAPLE':([40,46,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,91,92,95,96,98,105,108,109,113,115,116,117,118,127,128,131,143,144,168,169,170,171,172,173,174,175,176,194,198,199,228,],[-17,66,-121,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,128,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,-72,168,-16,-44,-119,-76,-15,-40,-41,-53,-54,-57,-123,-123,-61,213,-58,-59,239,]),'HACER':([40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,92,95,96,98,105,108,109,113,115,116,117,118,128,131,143,144,168,169,170,171,172,173,174,175,176,198,199,225,],[-17,-121,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,-72,-16,-44,-119,-76,-15,-40,-41,-53,-54,-57,-123,-123,-61,-58,-59,235,]),'HASTA':([40,47,48,49,50,53,56,57,58,59,60,61,66,68,69,70,71,74,75,76,77,80,81,82,83,84,92,95,96,98,105,108,109,113,115,116,117,118,128,131,143,144,168,169,170,171,172,173,174,175,176,190,198,199,240,241,250,262,263,],[-17,-121,-122,-123,-124,-66,-117,-117,-117,-117,-71,-118,-14,-1,-1,-1,-1,-65,-73,-74,-75,-67,-68,-69,-70,-1,-39,-42,-43,-45,-52,-55,-56,-60,-62,-63,-64,-72,-16,-44,-119,-76,-15,-40,-41,-53,-54,-57,-123,-123,-61,208,-58,-59,-120,-38,-37,-103,-104,]),'RBRACKET':([40,56,57,58,59,60,61,66,80,81,82,83,84,118,123,128,144,146,147,148,151,156,157,158,168,178,179,180,181,182,183,184,242,244,245,246,247,248,249,251,252,253,254,255,256,257,258,260,261,264,265,266,267,269,270,],[-17,-117,-117,-117,-117,-71,-118,-14,-67,-68,-69,-70,-1,-72,-1,-16,-76,178,-1,-30,-33,-80,-81,-82,-15,-28,-29,-31,-32,-34,-35,-36,-1,-1,-84,-91,-92,-87,-88,-1,262,263,-105,-106,-1,-108,-83,-86,266,-107,-85,-1,-109,-111,-110,]),'EQUAL':([40,66,128,155,168,185,191,200,],[-17,-14,-16,-118,-15,-1,-118,215,]),'ESCRIBE':([123,147,151,156,157,158,178,180,181,182,183,184,244,245,246,247,248,249,258,260,265,],[159,159,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'LEE':([123,147,151,156,157,158,178,180,181,182,183,184,244,245,246,247,248,249,258,260,265,],[160,160,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'REGRESA':([123,147,151,156,157,158,178,180,181,182,183,184,244,245,246,247,248,249,258,260,265,],[161,161,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'SI':([123,147,151,156,157,158,178,180,181,182,183,184,226,234,235,236,237,238,244,245,246,247,248,249,258,260,265,],[162,162,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,162,162,162,-89,-90,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'DESDE':([123,147,151,156,157,158,178,180,181,182,183,184,226,234,235,236,237,238,244,245,246,247,248,249,258,260,265,],[163,163,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,163,163,163,-89,-90,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'MIENTRAS':([123,147,151,156,157,158,178,180,181,182,183,184,226,234,235,236,237,238,244,245,246,247,248,249,258,260,265,],[164,164,-33,-80,-81,-82,-28,-31,-32,-34,-35,-36,-1,164,164,164,-89,-90,-1,-84,-91,-92,-87,-88,-83,-86,-85,]),'SINO':([178,244,],[-28,259,]),'NULL':([188,],[206,]),'ENTONCES':([224,],[234,]),'HAZ':([226,],[237,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'VARS':([4,62,125,167,],[5,86,166,197,]),'empty':([4,5,6,9,24,34,62,68,69,70,71,84,85,123,125,145,147,165,167,185,193,202,204,221,226,242,244,251,256,266,],[7,10,14,10,14,40,7,95,98,108,113,40,121,148,7,121,148,195,7,40,212,219,40,233,238,257,260,257,257,269,]),'FUNCTIONS':([5,9,],[8,21,]),'FUNCTION':([5,9,],[9,9,]),'VAR_AUX':([6,24,],[12,33,]),'TIPO':([6,11,24,63,89,211,],[13,22,13,87,87,87,]),'MAIN':([8,],[19,]),'IDS':([13,45,],[24,65,]),'r_save_type':([15,16,17,18,23,],[26,27,28,29,32,]),'r_save_func':([20,31,37,],[30,36,43,]),'r_register_var':([25,124,],[34,165,]),'ARRDIM':([34,84,185,204,],[38,118,200,221,]),'r_register_func':([36,43,],[42,64,]),'EXPRESION':([39,67,72,85,90,129,130,145,186,188,189,192,208,218,229,],[46,91,114,120,127,169,170,120,202,205,207,209,225,202,240,]),'SUBEXP':([39,67,72,85,90,97,129,130,145,186,188,189,192,208,218,229,],[47,47,47,47,47,131,47,47,47,47,47,47,47,47,47,47,]),'EXP':([39,67,72,85,90,97,129,130,138,139,145,186,188,189,192,208,218,229,],[48,48,48,48,48,48,48,48,171,172,48,48,48,48,48,48,48,48,]),'TERMINO':([39,67,72,85,90,97,129,130,138,139,140,141,142,145,186,188,189,192,208,218,229,],[49,49,49,49,49,49,49,49,49,49,173,174,175,49,49,49,49,49,49,49,49,]),'FACTOR':([39,67,72,85,90,97,129,130,138,139,140,141,142,145,186,188,189,192,208,218,229,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'CTE':([39,67,72,73,78,79,85,90,97,129,130,138,139,140,141,142,145,186,188,189,192,208,218,229,242,251,256,],[53,53,53,115,116,117,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,254,254,254,]),'FUN':([39,67,72,73,78,79,85,90,97,123,129,130,138,139,140,141,142,145,147,186,188,189,192,208,218,229,242,251,256,],[60,60,60,60,60,60,60,60,60,150,60,60,60,60,60,60,60,60,150,60,60,60,60,60,60,60,60,60,60,]),'r_register_princ':([41,],[62,]),'r_seen_subexp':([47,],[68,]),'r_seen_exp':([48,],[69,]),'r_seen_term':([49,174,175,],[70,198,199,]),'r_seen_factor':([50,],[71,]),'r_seen_operator':([51,93,94,99,100,101,102,103,104,106,107,110,111,112,143,215,],[72,129,130,132,133,134,135,136,137,138,139,140,141,142,176,229,]),'r_seen_unary_operator':([52,54,55,],[73,78,79,]),'ARROP':([53,],[74,]),'r_seen_operand':([56,57,58,59,],[80,81,82,83,]),'r_seen_operand_id':([61,155,191,],[84,185,185,]),'PARAM':([63,89,211,],[88,126,227,]),'EXPRESION_AUX':([68,],[92,]),'SUBEXP_AUX':([69,],[96,]),'COMPARACION':([69,],[97,]),'EXP_AUX':([70,],[105,]),'TERMINO_AUX':([71,],[109,]),'FUN_AUX':([85,145,],[119,177,]),'BLOQUE':([86,166,197,234,235,236,259,],[122,196,214,244,246,248,265,]),'ESTATUTOS':([123,147,],[146,179,]),'ESTATUTO':([123,147,],[147,147,]),'ASIGNACION':([123,147,163,],[149,149,190,]),'COND':([123,147,234,235,236,],[151,151,245,247,249,]),'WRITE':([123,147,],[152,152,]),'READ':([123,147,],[153,153,]),'RETURN':([123,147,],[154,154,]),'IF':([123,147,234,235,236,],[156,156,156,156,156,]),'FOR':([123,147,234,235,236,],[157,157,157,157,157,]),'WHILE':([123,147,234,235,236,],[158,158,158,158,158,]),'PARENTESIS':([165,],[193,]),'WRITE_AUX':([186,218,],[201,230,]),'READ_AUX':([187,232,],[203,243,]),'PARAM_AUX':([193,],[210,]),'WRITE_AUXSUB':([202,],[217,]),'READ_AUXSUB':([221,],[231,]),'WHILE_AUX':([226,],[236,]),'CTE_ARR':([229,],[241,]),'r_seen_equal':([240,],[250,]),'CTE_ARR_AUX':([242,251,256,],[252,261,264,]),'CTE_ARR_AUX2':([242,268,],[253,270,]),'CTE_ARR_AUXSUB':([242,251,256,],[255,255,255,]),'IF_AUX':([244,],[258,]),'CTE_ARR_AUX2SUB':([266,],[267,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',17),
  ('PROGRAM -> PROGRAMA ID DOTCOMA VARS FUNCTIONS MAIN','PROGRAM',6,'p_PROGRAM','parser.py',22),
  ('MAIN -> PRINCIPAL r_save_func LPAREN RPAREN r_register_princ VARS BLOQUE','MAIN',7,'p_MAIN','parser.py',27),
  ('VARS -> VAR VAR_AUX','VARS',2,'p_VARS','parser.py',32),
  ('VARS -> empty','VARS',1,'p_VARS','parser.py',33),
  ('VAR_AUX -> TIPO IDS VAR_AUX','VAR_AUX',3,'p_VAR_AUX','parser.py',38),
  ('VAR_AUX -> empty','VAR_AUX',1,'p_VAR_AUX','parser.py',39),
  ('TIPO -> INT r_save_type','TIPO',2,'p_TIPO','parser.py',44),
  ('TIPO -> FLOAT r_save_type','TIPO',2,'p_TIPO','parser.py',45),
  ('TIPO -> CHAR r_save_type','TIPO',2,'p_TIPO','parser.py',46),
  ('TIPO -> STRING r_save_type','TIPO',2,'p_TIPO','parser.py',47),
  ('IDS -> ID r_register_var ARRDIM DOTCOMA','IDS',4,'p_IDS','parser.py',52),
  ('IDS -> ID r_register_var ARRDIM COMA IDS','IDS',5,'p_IDS','parser.py',53),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE','ARRDIM',3,'p_ARRDIM','parser.py',58),
  ('ARRDIM -> LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE','ARRDIM',6,'p_ARRDIM','parser.py',59),
  ('ARRDIM -> LSTAPLE EXPRESION COMA EXPRESION RSTAPLE','ARRDIM',5,'p_ARRDIM','parser.py',60),
  ('ARRDIM -> empty','ARRDIM',1,'p_ARRDIM','parser.py',61),
  ('FUNCTIONS -> FUNCTION FUNCTIONS','FUNCTIONS',2,'p_FUNCTIONS','parser.py',66),
  ('FUNCTIONS -> empty','FUNCTIONS',1,'p_FUNCTIONS','parser.py',67),
  ('FUNCTION -> FUNCION TIPO ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUE','FUNCTION',10,'p_FUNCTION','parser.py',72),
  ('FUNCTION -> FUNCION VOID r_save_type ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUE','FUNCTION',11,'p_FUNCTION','parser.py',73),
  ('PARAM -> TIPO ID r_register_var PARENTESIS PARAM_AUX','PARAM',5,'p_PARAM','parser.py',79),
  ('PARAM_AUX -> COMA PARAM','PARAM_AUX',2,'p_PARAM_AUX','parser.py',84),
  ('PARAM_AUX -> empty','PARAM_AUX',1,'p_PARAM_AUX','parser.py',85),
  ('PARENTESIS -> LSTAPLE RSTAPLE','PARENTESIS',2,'p_PARENTESIS','parser.py',90),
  ('PARENTESIS -> LSTAPLE RSTAPLE LSTAPLE RSTAPLE','PARENTESIS',4,'p_PARENTESIS','parser.py',91),
  ('PARENTESIS -> empty','PARENTESIS',1,'p_PARENTESIS','parser.py',92),
  ('BLOQUE -> LBRACKET ESTATUTOS RBRACKET','BLOQUE',3,'p_BLOQUE','parser.py',97),
  ('ESTATUTOS -> ESTATUTO ESTATUTOS','ESTATUTOS',2,'p_ESTATUTOS','parser.py',102),
  ('ESTATUTOS -> empty','ESTATUTOS',1,'p_ESTATUTOS','parser.py',103),
  ('ESTATUTO -> ASIGNACION DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',108),
  ('ESTATUTO -> FUN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',109),
  ('ESTATUTO -> COND','ESTATUTO',1,'p_ESTATUTO','parser.py',110),
  ('ESTATUTO -> WRITE DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',111),
  ('ESTATUTO -> READ DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',112),
  ('ESTATUTO -> RETURN DOTCOMA','ESTATUTO',2,'p_ESTATUTO','parser.py',113),
  ('ASIGNACION -> ID r_seen_operand_id ARRDIM EQUAL r_seen_operator EXPRESION r_seen_equal','ASIGNACION',7,'p_ASIGNACION','parser.py',118),
  ('ASIGNACION -> ID r_seen_operand_id ARRDIM EQUAL r_seen_operator CTE_ARR','ASIGNACION',6,'p_ASIGNACION','parser.py',119),
  ('EXPRESION -> SUBEXP r_seen_subexp EXPRESION_AUX','EXPRESION',3,'p_EXPRESION','parser.py',124),
  ('EXPRESION_AUX -> AND r_seen_operator EXPRESION','EXPRESION_AUX',3,'p_EXPRESION_AUX','parser.py',129),
  ('EXPRESION_AUX -> OR r_seen_operator EXPRESION','EXPRESION_AUX',3,'p_EXPRESION_AUX','parser.py',130),
  ('EXPRESION_AUX -> empty','EXPRESION_AUX',1,'p_EXPRESION_AUX','parser.py',131),
  ('SUBEXP -> EXP r_seen_exp SUBEXP_AUX','SUBEXP',3,'p_SUBEXP','parser.py',136),
  ('SUBEXP_AUX -> COMPARACION SUBEXP','SUBEXP_AUX',2,'p_SUBEXP_AUX','parser.py',141),
  ('SUBEXP_AUX -> empty','SUBEXP_AUX',1,'p_SUBEXP_AUX','parser.py',142),
  ('COMPARACION -> MORE r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',147),
  ('COMPARACION -> LESS r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',148),
  ('COMPARACION -> COMPARE r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',149),
  ('COMPARACION -> DIFFERENT r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',150),
  ('COMPARACION -> MOREEQUAL r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',151),
  ('COMPARACION -> LESSEQUAL r_seen_operator','COMPARACION',2,'p_COMPARACION','parser.py',152),
  ('EXP -> TERMINO r_seen_term EXP_AUX','EXP',3,'p_EXP','parser.py',157),
  ('EXP_AUX -> PLUS r_seen_operator EXP','EXP_AUX',3,'p_EXP_AUX','parser.py',162),
  ('EXP_AUX -> MINUS r_seen_operator EXP','EXP_AUX',3,'p_EXP_AUX','parser.py',163),
  ('EXP_AUX -> empty','EXP_AUX',1,'p_EXP_AUX','parser.py',164),
  ('TERMINO -> FACTOR r_seen_factor TERMINO_AUX','TERMINO',3,'p_TERMINO','parser.py',169),
  ('TERMINO_AUX -> MULT r_seen_operator TERMINO','TERMINO_AUX',3,'p_TERMINO_AUX','parser.py',174),
  ('TERMINO_AUX -> DIV r_seen_operator TERMINO r_seen_term','TERMINO_AUX',4,'p_TERMINO_AUX','parser.py',175),
  ('TERMINO_AUX -> MOD r_seen_operator TERMINO r_seen_term','TERMINO_AUX',4,'p_TERMINO_AUX','parser.py',176),
  ('TERMINO_AUX -> empty','TERMINO_AUX',1,'p_TERMINO_AUX','parser.py',177),
  ('FACTOR -> LPAREN r_seen_operator EXPRESION RPAREN r_seen_operator','FACTOR',5,'p_FACTOR','parser.py',182),
  ('FACTOR -> PLUS r_seen_unary_operator CTE','FACTOR',3,'p_FACTOR','parser.py',183),
  ('FACTOR -> MINUS r_seen_unary_operator CTE','FACTOR',3,'p_FACTOR','parser.py',184),
  ('FACTOR -> NOT r_seen_unary_operator CTE','FACTOR',3,'p_FACTOR','parser.py',185),
  ('FACTOR -> CTE ARROP','FACTOR',2,'p_FACTOR','parser.py',186),
  ('FACTOR -> CTE','FACTOR',1,'p_FACTOR','parser.py',187),
  ('CTE -> CTE_I r_seen_operand','CTE',2,'p_CTE','parser.py',192),
  ('CTE -> CTE_F r_seen_operand','CTE',2,'p_CTE','parser.py',193),
  ('CTE -> CTE_CH r_seen_operand','CTE',2,'p_CTE','parser.py',194),
  ('CTE -> CTE_STRING r_seen_operand','CTE',2,'p_CTE','parser.py',195),
  ('CTE -> FUN','CTE',1,'p_CTE','parser.py',196),
  ('CTE -> ID r_seen_operand_id ARRDIM','CTE',3,'p_CTE','parser.py',197),
  ('ARROP -> DET_ARR','ARROP',1,'p_ARROP','parser.py',202),
  ('ARROP -> TRANS_ARR','ARROP',1,'p_ARROP','parser.py',203),
  ('ARROP -> INV_ARR','ARROP',1,'p_ARROP','parser.py',204),
  ('FUN -> ID LPAREN FUN_AUX RPAREN','FUN',4,'p_FUN','parser.py',209),
  ('FUN_AUX -> EXPRESION COMA FUN_AUX','FUN_AUX',3,'p_FUN_AUX','parser.py',214),
  ('FUN_AUX -> EXPRESION','FUN_AUX',1,'p_FUN_AUX','parser.py',215),
  ('FUN_AUX -> empty','FUN_AUX',1,'p_FUN_AUX','parser.py',216),
  ('COND -> IF','COND',1,'p_COND','parser.py',221),
  ('COND -> FOR','COND',1,'p_COND','parser.py',222),
  ('COND -> WHILE','COND',1,'p_COND','parser.py',223),
  ('IF -> SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE IF_AUX','IF',7,'p_IF','parser.py',228),
  ('IF -> SI LPAREN EXPRESION RPAREN ENTONCES COND','IF',6,'p_IF','parser.py',229),
  ('IF_AUX -> SINO BLOQUE','IF_AUX',2,'p_IF_AUX','parser.py',234),
  ('IF_AUX -> empty','IF_AUX',1,'p_IF_AUX','parser.py',235),
  ('WHILE -> MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX BLOQUE','WHILE',6,'p_WHILE','parser.py',240),
  ('WHILE -> MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX COND','WHILE',6,'p_WHILE','parser.py',241),
  ('WHILE_AUX -> HAZ','WHILE_AUX',1,'p_WHILE_AUX','parser.py',246),
  ('WHILE_AUX -> empty','WHILE_AUX',1,'p_WHILE_AUX','parser.py',247),
  ('FOR -> DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE','FOR',6,'p_FOR','parser.py',252),
  ('FOR -> DESDE ASIGNACION HASTA EXPRESION HACER COND','FOR',6,'p_FOR','parser.py',253),
  ('WRITE -> ESCRIBE LPAREN WRITE_AUX RPAREN','WRITE',4,'p_WRITE','parser.py',258),
  ('WRITE_AUX -> EXPRESION WRITE_AUXSUB','WRITE_AUX',2,'p_WRITE_AUX','parser.py',263),
  ('WRITE_AUXSUB -> COMA WRITE_AUX','WRITE_AUXSUB',2,'p_WRITE_AUXSUB','parser.py',268),
  ('WRITE_AUXSUB -> empty','WRITE_AUXSUB',1,'p_WRITE_AUXSUB','parser.py',269),
  ('READ -> LEE LPAREN READ_AUX RPAREN','READ',4,'p_READ','parser.py',274),
  ('READ_AUX -> ID ARRDIM READ_AUXSUB','READ_AUX',3,'p_READ_AUX','parser.py',279),
  ('READ_AUXSUB -> COMA READ_AUX','READ_AUXSUB',2,'p_READ_AUXSUB','parser.py',284),
  ('READ_AUXSUB -> empty','READ_AUXSUB',1,'p_READ_AUXSUB','parser.py',285),
  ('RETURN -> REGRESA LPAREN EXPRESION RPAREN','RETURN',4,'p_RETURN','parser.py',290),
  ('RETURN -> REGRESA LPAREN NULL RPAREN','RETURN',4,'p_RETURN','parser.py',291),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX RBRACKET','CTE_ARR',3,'p_CTE_ARR','parser.py',296),
  ('CTE_ARR -> LBRACKET CTE_ARR_AUX2 RBRACKET','CTE_ARR',3,'p_CTE_ARR','parser.py',297),
  ('CTE_ARR_AUX -> CTE','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','parser.py',302),
  ('CTE_ARR_AUX -> CTE_ARR_AUXSUB','CTE_ARR_AUX',1,'p_CTE_ARR_AUX','parser.py',303),
  ('CTE_ARR_AUXSUB -> COMA CTE_ARR_AUX','CTE_ARR_AUXSUB',2,'p_CTE_ARR_AUXSUB','parser.py',308),
  ('CTE_ARR_AUXSUB -> empty','CTE_ARR_AUXSUB',1,'p_CTE_ARR_AUXSUB','parser.py',309),
  ('CTE_ARR_AUX2 -> LBRACKET CTE_ARR_AUX RBRACKET CTE_ARR_AUX2SUB','CTE_ARR_AUX2',4,'p_CTE_ARR_AUX2','parser.py',314),
  ('CTE_ARR_AUX2SUB -> COMA CTE_ARR_AUX2','CTE_ARR_AUX2SUB',2,'p_CTE_ARR_AUX2SUB','parser.py',319),
  ('CTE_ARR_AUX2SUB -> empty','CTE_ARR_AUX2SUB',1,'p_CTE_ARR_AUX2SUB','parser.py',320),
  ('r_save_type -> <empty>','r_save_type',0,'p_r_save_type','parser.py',333),
  ('r_save_func -> <empty>','r_save_func',0,'p_r_save_func','parser.py',338),
  ('r_register_func -> <empty>','r_register_func',0,'p_r_register_func','parser.py',343),
  ('r_register_var -> <empty>','r_register_var',0,'p_r_register_var','parser.py',354),
  ('r_register_princ -> <empty>','r_register_princ',0,'p_r_register_princ','parser.py',374),
  ('r_seen_operand -> <empty>','r_seen_operand',0,'p_r_seen_operand','parser.py',382),
  ('r_seen_operand_id -> <empty>','r_seen_operand_id',0,'p_r_seen_operand_id','parser.py',388),
  ('r_seen_operator -> <empty>','r_seen_operator',0,'p_r_seen_operator','parser.py',394),
  ('r_seen_equal -> <empty>','r_seen_equal',0,'p_r_seen_equal','parser.py',400),
  ('r_seen_subexp -> <empty>','r_seen_subexp',0,'p_r_seen_subexp','parser.py',406),
  ('r_seen_exp -> <empty>','r_seen_exp',0,'p_r_seen_exp','parser.py',412),
  ('r_seen_term -> <empty>','r_seen_term',0,'p_r_seen_term','parser.py',418),
  ('r_seen_factor -> <empty>','r_seen_factor',0,'p_r_seen_factor','parser.py',424),
  ('r_seen_unary_operator -> <empty>','r_seen_unary_operator',0,'p_r_seen_unary_operator','parser.py',430),
]
