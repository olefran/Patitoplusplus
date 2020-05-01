# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Parser with yacc of Patitoplusplus
# Created 04/25/2020
import yacc
from scanner import tokens
from semantics import *


#Productions
start = 'PROGRAM'

def p_empty(p):
    'empty :'
    pass

# PROGRAMA → programa id ;  VARS FUNCTIONS MAIN
def p_PROGRAM(p):
    'PROGRAM : PROGRAMA ID DOTCOMA VARS FUNCTIONS MAIN'
    pass

#MAIN → principal ( )  VARS BLOQUE
def p_MAIN(p):
    'MAIN : PRINCIPAL r_save_func LPAREN RPAREN r_register_princ VARS BLOQUE'
    pass

#VARS → var VARPRE | empty
def p_VARS(p):
    '''VARS : VAR VAR_AUX
    | empty'''
    pass

#VARPRE → TIPO IDS VARPRE | empty
def p_VAR_AUX(p):
    '''VAR_AUX : TIPO IDS VAR_AUX
    | empty'''
    pass

#TIPO → int | float | char | string
def p_TIPO(p):
    '''TIPO : INT r_save_type
    | FLOAT r_save_type
    | CHAR r_save_type
    | STRING r_save_type'''
    pass

# IDS → id ARRDIM ; | id ARRDIM , IDS
def p_IDS(p):
    '''IDS : ID r_register_var ARRDIM DOTCOMA
    | ID r_register_var ARRDIM COMA IDS'''
    pass

# ARRDIM → [ EXPRESION ] | [ EXPRESION ] [ EXPRESION ] | [ EXPRESION , EXPRESION ] | empty
def p_ARRDIM(p):
    '''ARRDIM : LSTAPLE EXPRESION RSTAPLE
    | LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE
    | LSTAPLE EXPRESION COMA EXPRESION RSTAPLE
    | empty'''
    pass

#FUNCTIONS → FUNCTION FUNCTIONS | empty
def p_FUNCTIONS(p):
    '''FUNCTIONS : FUNCTION FUNCTIONS
    | empty'''
    pass

#FUNCTION → funcion TIPO id ( PARAM )  VARS BLOQUE | funcion void id ( PARAM )  VARS BLOQUE
def p_FUNCTION(p):
    '''FUNCTION : FUNCION TIPO ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUE
    | FUNCION VOID r_save_type ID r_save_func r_register_func LPAREN PARAM RPAREN VARS BLOQUE'''
    pass

#PARAM → TIPO id PARENTESIS PARAMSUB
def p_PARAM(p):
    '''PARAM : TIPO ID r_register_var PARENTESIS PARAM_AUX'''
    pass

#PARAM_AUX → , PARAM  | empty
def p_PARAM_AUX(p):
    '''PARAM_AUX : COMA PARAM
    | empty'''
    pass

#PARENTESIS → [ ] | [ ] [ ] | empty
def p_PARENTESIS(p):
    '''PARENTESIS : LSTAPLE RSTAPLE
    | LSTAPLE RSTAPLE LSTAPLE RSTAPLE
    | empty'''
    pass

#BLOQUE → { ESTATUTOS }
def p_BLOQUE(p):
    'BLOQUE : LBRACKET ESTATUTOS RBRACKET'
    pass

#ESTATUTOS → ESTATUTO ESTATUTOS | empty
def p_ESTATUTOS(p):
    '''ESTATUTOS : ESTATUTO ESTATUTOS
    | empty'''
    pass

#ESTATUTO → ASIGNACION ; | FUN ; | COND | WRITE ; | REAd ; | RETURN ;
def p_ESTATUTO(p):
    '''ESTATUTO : ASIGNACION DOTCOMA
    | FUN DOTCOMA
    | COND
    | WRITE DOTCOMA
    | READ DOTCOMA
    | RETURN DOTCOMA'''
    pass

#ASIGNACION → id ARRDIM = EXPRESION | id ARRDIM = CTE_ARR
def p_ASIGNACION(p):
    '''ASIGNACION : ID ARRDIM EQUAL EXPRESION
    | ID ARRDIM EQUAL CTE_ARR'''
    pass

#EXPRESION → SUBEXP && SUBEXP | SUBEXP || SUBEXP | SUBEXP
# r_seen_andor -> save
def p_EXPRESION(p):
    '''EXPRESION : SUBEXP r_seen_subexp AND r_seen_operator SUBEXP r_seen_subexp
    | SUBEXP r_seen_subexp OR r_seen_operator SUBEXP r_seen_subexp
    | SUBEXP r_seen_subexp'''
    pass

#SUBEXP → EXP | EXP COMPARACION EXP
def p_SUBEXP(p):
    '''SUBEXP : EXP r_seen_exp
    | EXP r_seen_exp COMPARACION r_seen_operator EXP r_seen_exp'''
    pass

#COMPARACION → > | < | == | != | >= | <=
def p_COMPARACION(p):
    '''COMPARACION : MORE
    | LESS
    | COMPARE
    | DIFFERENT
    | MOREEQUAL
    | LESSEQUAL'''
    pass

#EXP → TERMINO | TERMINO + EXP | TERMINO - EXP
def p_EXP(p):
    '''EXP : TERMINO r_seen_term
    | TERMINO r_seen_term PLUS r_seen_operator EXP r_seen_exp
    | TERMINO r_seen_term MINUS r_seen_operator EXP r_seen_exp'''
    pass

#TERMINO → FACTOR | FACTOR * TERMINO | FACTOR / TERMINO | FACTOR % TERMINO
def p_TERMINO(p):
    '''TERMINO : FACTOR r_seen_factor
    | FACTOR r_seen_factor MULT r_seen_operator TERMINO r_seen_term
    | FACTOR r_seen_factor DIV r_seen_operator TERMINO r_seen_term
    | FACTOR r_seen_factor MOD r_seen_operator TERMINO r_seen_term'''
    pass

#FACTOR → ( EXPRESION ) | + CTE | - CTE | NOT CTE | CTE ARROP | CTE
def p_FACTOR(p):
    '''FACTOR : LPAREN r_seen_operator EXPRESION RPAREN r_seen_operator
    | PLUS r_seen_unary_operator CTE
    | MINUS r_seen_unary_operator CTE
    | NOT r_seen_unary_operator CTE
    | CTE ARROP
    | CTE'''
    pass

#CTE → cte_i | cte_f | ct_ch | cte_string | FUN | ID ARRDIM
def p_CTE(p):
    '''CTE : CTE_I r_seen_operand
    | CTE_F r_seen_operand
    | CTE_CH r_seen_operand
    | CTE_STRING r_seen_operand
    | FUN
    | ID ARRDIM '''
    pass

#ARROP→ $ | ! | ?
def p_ARROP(p):
    '''ARROP : DET_ARR
    | TRANS_ARR
    | INV_ARR'''
    pass

#FUN → id ( FUN_AUX )
def p_FUN(p):
    'FUN : ID LPAREN FUN_AUX RPAREN'
    pass

#FUN_AUX → CTE , FUN_AUX | CTE
def p_FUN_AUX(p):
    '''FUN_AUX : EXPRESION COMA FUN_AUX
    | EXPRESION
    | empty'''
    pass

#COND → IF | FOR | WHILE
def p_COND(p):
    '''COND : IF
    | FOR
    | WHILE'''
    pass

#IF → si ( EXPRESION ) entonces BLOQUE IF_AUX
def p_IF(p):
    '''IF : SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE IF_AUX
    | SI LPAREN EXPRESION RPAREN ENTONCES COND '''
    pass

#IFAUX → sino BLOQUE | empty
def p_IF_AUX(p):
    '''IF_AUX : SINO BLOQUE
    | empty'''
    pass

#WHILE → mientras ( EXPRESION ) WHILE_AUX BLOQUE
def p_WHILE(p):
    '''WHILE :  MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX BLOQUE
    | MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX COND'''
    pass

#WHILE_AUX → haz | empty
def p_WHILE_AUX(p):
    '''WHILE_AUX :  HAZ
    | empty '''
    pass

#FOR → desde ASIGNACION hasta EXPRESION hacer BLOQUE
def p_FOR(p):
    '''FOR :  DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE
    | DESDE ASIGNACION HASTA EXPRESION HACER COND'''
    pass

#WRITE → escribe ( WRITE_AUX )
def p_WRITE(p):
    'WRITE : ESCRIBE LPAREN WRITE_AUX RPAREN'
    pass

#WRITE_AUX → EXPRESION WRITE_AUXSUB
def p_WRITE_AUX(p):
    'WRITE_AUX : EXPRESION WRITE_AUXSUB'
    pass

#WRITE_AUXSUB → , WRITE_AUX | empty
def p_WRITE_AUXSUB(p):
    '''WRITE_AUXSUB : COMA WRITE_AUX
    | empty'''
    pass

#READ → lee ( READ_AUX )
def p_READ(p):
    'READ : LEE LPAREN READ_AUX RPAREN'
    pass

#READ_AUX → id ARRDIM READ_AUXSUB
def p_READ_AUX(p):
    'READ_AUX : ID ARRDIM READ_AUXSUB'
    pass

#READ_AUXSUB →, READ_AUX | empty
def p_READ_AUXSUB(p):
    '''READ_AUXSUB : COMA READ_AUX
    | empty'''
    pass

#RETURN → regresa ( EXPRESION ) regresa ( NULL )
def p_RETURN(p):
    '''RETURN : REGRESA LPAREN EXPRESION RPAREN
    | REGRESA LPAREN NULL RPAREN'''
    pass

#CTE_ARR → { CTE_ARR_AUX } | { CTE_ARR_AUX2 }
def p_CTE_ARR(p):
    '''CTE_ARR : LBRACKET CTE_ARR_AUX RBRACKET
    | LBRACKET CTE_ARR_AUX2 RBRACKET '''
    pass

#CTE_ARR_AUX → CTE | CTE_ARR_AUXSUB
def p_CTE_ARR_AUX(p):
    '''CTE_ARR_AUX : CTE
    | CTE_ARR_AUXSUB '''
    pass

#CTE_ARR_AUXSUB →, CTE_ARR_AUX | empty
def p_CTE_ARR_AUXSUB(p):
    '''CTE_ARR_AUXSUB : COMA CTE_ARR_AUX
    | empty '''
    pass

#CTE_ARR_AUX2 → { CTE_ARR_AUX } CTE_ARR_AUX2SUB
def p_CTE_ARR_AUX2(p):
    'CTE_ARR_AUX2 : LBRACKET CTE_ARR_AUX RBRACKET  CTE_ARR_AUX2SUB'
    pass

#CTE_ARR_AUX2SUB → , CTE_ARR_AUX2  | empty
def p_CTE_ARR_AUX2SUB(p):
    '''CTE_ARR_AUX2SUB : COMA CTE_ARR_AUX2
    | empty '''
    pass

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")

#Precedence: Build againts ambiguity TODO: More Operations
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV', 'MOD'),
    ('right', 'EQUAL'),
    ('left', 'AND', 'OR'),
)

#DirFunctions
def p_r_save_type(p):
    'r_save_type : '
    global current_type
    current_type = p[-1]

def p_r_save_func(p):
    'r_save_func : '
    global current_func
    current_func = p[-1]

def p_r_register_func(p):
    'r_register_func : '
    global symbol_table
    symbol_table[current_func] = {
        'type': current_type,
        'vars': {}
    }

def p_r_register_var(p):
    'r_register_var : '
    global current_var
    current_var = p[-1]
    global symbol_table
    symbol_table[current_func]['vars'][current_var] = {
        'type': current_type,
    }

def p_r_register_princ(p):
    'r_register_princ : '
    global symbol_table
    symbol_table[current_func] = {
        'vars': {}
    }

def p_r_seen_operand(p):
    'r_seen_operand : '
    e = register_operand(p[-1])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_operator(p):
    'r_seen_operator : '
    e = register_operator(p[-1])
    print(p[-1])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_subexp(p):
    'r_seen_subexp : '
    e = solve_op_or_cont([Operations.AND, Operations.OR])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_exp(p):
    'r_seen_exp : '
    e = solve_op_or_cont([Operations.MORE_THAN, Operations.LESS_THAN, Operations.IS_EQUAL,
                        Operations.DIFFERENT, Operations.LESS_EQUAL, Operations.MORE_EQUAL])
    if e:
        andle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_term(p):
    'r_seen_term : '
    e = solve_op_or_cont([Operations.PLUS, Operations.MINUS])
    if e:
        andle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_factor(p):
    'r_seen_factor : '
    e = solve_op_or_cont([Operations.TIMES, Operations.DIV, Operations.MOD])
    if e:
        andle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_unary_operator(p):
    'r_seen_unary_operator : '
    pass #TODO Unary operation

#Build the parser
parser = yacc.yacc()
