# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Parser con yacc de Patitoplusplus
# Created 04/25/2020
import yacc
from scanner import tokens
from semantics import *

# String para errores
input_str = ''

# Punto de partida
start = 'PROGRAM'

# Produccion vacía para epsilon
def p_empty(p):
    'empty :'
    pass

# PROGRAMA → programa id ;  VARS FUNCTIONS MAIN
def p_PROGRAM(p):
    'PROGRAM : PROGRAMA r_goto_main ID DOTCOMA VARS r_save_vars  FUNCTIONS MAIN r_print_constants'
    pass

# MAIN → principal ( )  VARS BLOQUE
def p_MAIN(p):
    'MAIN : PRINCIPAL r_save_func LPAREN RPAREN r_register_princ r_save_param_func VARS r_save_vars r_end_princ r_func_set BLOQUE r_func_end '
    pass

# VARS → var VARPRE | empty
def p_VARS(p):
    '''VARS : VAR VAR_AUX
    | empty'''
    pass

# VARPRE → TIPO IDS VARPRE | empty
def p_VAR_AUX(p):
    '''VAR_AUX : TIPO IDS VAR_AUX
    | empty'''
    pass

# TIPO → int | float | char | string
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

# FUNCTIONS → FUNCTION FUNCTIONS | empty
def p_FUNCTIONS(p):
    '''FUNCTIONS : FUNCTION FUNCTIONS
    | empty'''
    pass

# FUNCTION → funcion TIPO id ( PARAM )  VARS BLOQUE | funcion void id ( PARAM )  VARS BLOQUE
def p_FUNCTION(p):
    '''FUNCTION : FUNCION TIPO ID r_save_func r_register_func LPAREN PARAM RPAREN r_save_param_func VARS r_save_vars r_func_set BLOQUE r_func_end
    | FUNCION VOID r_save_type ID r_save_func r_register_func LPAREN PARAM RPAREN r_save_param_func VARS r_save_vars r_func_set BLOQUE r_func_end'''
    pass

# PARAM → TIPO id PARENTESIS PARAMSUB
# Sólo acepta ids ya declaradas, no acepta constantes
def p_PARAM(p):
    '''PARAM : TIPO ID r_register_var PARENTESIS PARAM_AUX'''
    pass

# PARAM_AUX → , PARAM  | empty
def p_PARAM_AUX(p):
    '''PARAM_AUX : COMA PARAM
    | empty'''
    pass

# PARENTESIS → [ ] | [ ] [ ] | empty
def p_PARENTESIS(p):
    '''PARENTESIS : LSTAPLE RSTAPLE
    | LSTAPLE RSTAPLE LSTAPLE RSTAPLE
    | empty'''
    pass

# BLOQUE → { ESTATUTOS }
def p_BLOQUE(p):
    'BLOQUE : LBRACKET ESTATUTOS RBRACKET'
    pass

# ESTATUTOS → ESTATUTO ESTATUTOS | empty
def p_ESTATUTOS(p):
    '''ESTATUTOS : ESTATUTO ESTATUTOS
    | empty'''
    pass

# ESTATUTO → ASIGNACION ; | FUN ; | COND | WRITE ; | REAd ; | RETURN ;
def p_ESTATUTO(p):
    '''ESTATUTO : ASIGNACION DOTCOMA
    | FUN DOTCOMA
    | COND
    | WRITE DOTCOMA
    | READ DOTCOMA
    | RETURN DOTCOMA'''
    pass

# ASIGNACION → id ARRDIM = EXPRESION | id ARRDIM = CTE_ARR
def p_ASIGNACION(p):
    '''ASIGNACION : ID r_seen_operand_id ARRDIM EQUAL r_seen_operator EXPRESION r_seen_equal
    | ID r_seen_operand_id ARRDIM EQUAL r_seen_operator CTE_ARR'''
    pass

# EXPRESION → SUBEXP EXPRESION_AUX
def p_EXPRESION(p):
    'EXPRESION : SUBEXP r_seen_subexp EXPRESION_AUX'
    pass

# EXPRESION_AUX → && EXPRESION | || EXPRESION | empty
def p_EXPRESION_AUX(p):
    '''EXPRESION_AUX : AND r_seen_operator EXPRESION
    | OR r_seen_operator EXPRESION
    | empty'''
    pass

# SUBEXP → EXP SUBEXP_AUX
def p_SUBEXP(p):
    'SUBEXP : EXP r_seen_exp SUBEXP_AUX'
    pass

# SUBEXP → COMPARACION SUBEXP | empty
def p_SUBEXP_AUX(p):
    '''SUBEXP_AUX : COMPARACION SUBEXP
    | empty'''
    pass

# COMPARACION → > | < | == | != | >= | <=
def p_COMPARACION(p):
    '''COMPARACION : MORE r_seen_operator
    | LESS r_seen_operator
    | COMPARE r_seen_operator
    | DIFFERENT r_seen_operator
    | MOREEQUAL r_seen_operator
    | LESSEQUAL r_seen_operator'''
    pass

# EXP → TERMINO EXP_AUX
def p_EXP(p):
    'EXP : TERMINO r_seen_term EXP_AUX'
    pass

# + EXP | - EXP | empty
def p_EXP_AUX(p):
    '''EXP_AUX : PLUS r_seen_operator EXP
    | MINUS r_seen_operator EXP
    | empty'''
    pass

# TERMINO → FACTOR TERMINO_AUX
def p_TERMINO(p):
    'TERMINO : FACTOR r_seen_factor TERMINO_AUX'
    pass

# TERMINO_AUX → * TERMINO | / TERMINO | % TERMINO | empty
def p_TERMINO_AUX(p):
    '''TERMINO_AUX : MULT r_seen_operator TERMINO
    | DIV r_seen_operator TERMINO r_seen_term
    | MOD r_seen_operator TERMINO r_seen_term
    | empty'''
    pass

# FACTOR → ! FACTOR_AUX | FACTOR_AUX
def p_FACTOR(p):
    '''FACTOR : NOT r_seen_unary_operator FACTOR_AUX
    | FACTOR_AUX'''
    e = solve_unary_or_cont(["MINUS_UNARY", "PLUS_UNARY", "!"])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# FACTOR → ( EXPRESION ) | SIGN ( EXPRESION ) | SIGN CTE | CTE ARROP | CTE
def p_FACTOR_AUX(p):
    '''FACTOR_AUX : SIGN LPAREN r_seen_operator EXPRESION RPAREN r_pop_fake_bottom
    | SIGN CTE ARROP'''
    e = solve_unary_or_cont(["MINUS_UNARY", "PLUS_UNARY", "!"])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# SIGN → + CTE | - CTE
def p_SIGN(p):
    '''SIGN : PLUS r_seen_unary_operator
    | MINUS r_seen_unary_operator
    | empty'''

# CTE → cte_i | cte_f | ct_ch | cte_string | FUN | ID ARRDIM
def p_CTE(p):
    '''CTE : CTE_I r_seen_operand
    | CTE_F r_seen_operand
    | CTE_CH r_seen_operand
    | CTE_STRING r_seen_operand
    | FUN
    | ID r_seen_operand_id ARRDIM '''
    pass

# ARROP→ $ | ! | ?
# TODO: Have an seen operator to use this kinds of matrix operations
def p_ARROP(p):
    '''ARROP : DET_ARR r_seen_operator_mat
    | TRANS_ARR r_seen_operator_mat
    | INV_ARR r_seen_operator_mat
    | empty'''
    pass

# FUN → id ( FUN_AUX )
def p_FUN(p):
    'FUN : ID r_check_func LPAREN FUN_AUX RPAREN r_go_sub'
    pass

# FUN_AUX → CTE , FUN_AUX | CTE
def p_FUN_AUX(p):
    '''FUN_AUX : EXPRESION r_check_param COMA FUN_AUX
    | EXPRESION r_check_param
    | empty'''
    pass

# COND → IF | FOR | WHILE
def p_COND(p):
    '''COND : IF
    | FOR
    | WHILE'''
    pass

# IF → si ( EXPRESION ) entonces IF2
def p_IF(p):
    'IF : SI LPAREN EXPRESION r_check_int RPAREN ENTONCES IF2 r_if_end'
    pass

# IF2 → BLOQUE IF_AUX | COND
def p_IF2(p):
    '''IF2 : BLOQUE IF_AUX
    | COND'''
    pass

# IFAUX → sino BLOQUE | empty
def p_IF_AUX(p):
    '''IF_AUX : SINO r_else_start BLOQUE
    | empty'''
    pass

# WHILE → mientras ( EXPRESION ) WHILE_AUX WHILE2
def p_WHILE(p):
    'WHILE :  MIENTRAS r_set_while LPAREN EXPRESION r_check_int RPAREN WHILE_AUX WHILE2 r_while_end'
    pass

# WHILE2 → BLOQUE | COND
def p_WHILE2(p):
    '''WHILE2 :  BLOQUE
    | COND'''
    pass

# WHILE_AUX → haz | empty
def p_WHILE_AUX(p):
    '''WHILE_AUX : HAZ
    | empty '''
    pass

# FOR → desde ASIGNACION hasta EXPRESION hacer FOR2
def p_FOR(p):
    'FOR : DESDE ASIGNACION HASTA EXPRESION r_for_gen HACER FOR2 r_for_end'
    pass

# FOR2 → BLOQUE | COND
def p_FOR2(p):
    '''FOR2 : BLOQUE
    | COND'''
    pass

# WRITE → escribe ( WRITE_AUX )
def p_WRITE(p):
    'WRITE : ESCRIBE LPAREN WRITE_AUX RPAREN r_escribe'
    pass

# WRITE_AUX → EXPRESION WRITE_AUXSUB
def p_WRITE_AUX(p):
    'WRITE_AUX : EXPRESION WRITE_AUXSUB'
    pass

# WRITE_AUXSUB → , WRITE_AUX | empty
def p_WRITE_AUXSUB(p):
    '''WRITE_AUXSUB : COMA WRITE_AUX
    | empty'''
    pass

# READ → lee ( READ_AUX )
def p_READ(p):
    'READ : LEE LPAREN READ_AUX RPAREN r_lee'
    pass

# READ_AUX → id ARRDIM READ_AUXSUB
def p_READ_AUX(p):
    'READ_AUX : ID ARRDIM READ_AUXSUB'
    pass

# READ_AUXSUB →, READ_AUX | empty
def p_READ_AUXSUB(p):
    '''READ_AUXSUB : COMA READ_AUX
    | empty'''
    pass

# RETURN → regresa ( EXPRESION ) | regresa ( NULL )
def p_RETURN(p):
    '''RETURN : REGRESA LPAREN EXPRESION RPAREN r_regresa
    | REGRESA LPAREN NULL RPAREN'''
    pass

# CTE_ARR → { CTE_ARR_AUX } | { CTE_ARR_AUX2 }
def p_CTE_ARR(p):
    '''CTE_ARR : LBRACKET CTE_ARR_AUX RBRACKET
    | LBRACKET CTE_ARR_AUX2 RBRACKET '''
    pass

# CTE_ARR_AUX → CTE | CTE_ARR_AUXSUB
def p_CTE_ARR_AUX(p):
    '''CTE_ARR_AUX : CTE
    | CTE_ARR_AUXSUB '''
    pass

# CTE_ARR_AUXSUB →, CTE_ARR_AUX | empty
def p_CTE_ARR_AUXSUB(p):
    '''CTE_ARR_AUXSUB : COMA CTE_ARR_AUX
    | empty '''
    pass

# CTE_ARR_AUX2 → { CTE_ARR_AUX } CTE_ARR_AUX2SUB
def p_CTE_ARR_AUX2(p):
    'CTE_ARR_AUX2 : LBRACKET CTE_ARR_AUX RBRACKET  CTE_ARR_AUX2SUB'
    pass

# CTE_ARR_AUX2SUB → , CTE_ARR_AUX2  | empty
def p_CTE_ARR_AUX2SUB(p):
    '''CTE_ARR_AUX2SUB : COMA CTE_ARR_AUX2
    | empty '''
    pass

# Precedencia: Para ambigüedades en la Operaciones
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV', 'MOD'),
    ('right', 'EQUAL'),
    ('left', 'AND', 'OR'),
)

# Funciones para guardar en symbol_table
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
    if symbol_table.get(current_func) is None:
        e = None
        current_dir = None
        symbol_table[current_func] = {
            'type': current_type,
            'vars': {}
            }
        if current_type != "void": #Discriminate void for saving functions on globar var table
            current_dir, e = get_global_dir(current_type)
            symbol_table['global']['vars'][current_func] = {
                'type' : current_type,
                'address' : current_dir
                }
    else:
        handle_error(p.lineno(-1), p.lexpos(-1), "multiple function name declaration: " + current_func)

def p_r_register_var(p):
    'r_register_var : '
    global current_var, func_var_count
    current_var = p[-1]
    e = None
    if symbol_table[current_func]['vars'].get(current_var) is None:
        if current_func == 'global':
            current_dir, e = get_global_dir(current_type) #Get direction or launch error
        else:
            current_dir, e = get_var_dir(current_type) #Get direction or launch error

        if e:
            handle_error(p.lineno(-1), p.lexpos(-1), e)

        e = get_func_count(current_type, current_var) #Add the counter to variable / param counter

        if e:
            handle_error(p.lineno(-1), p.lexpos(-1), e)


        symbol_table[current_func]['vars'][current_var] = {
            'type': current_type, 'address': current_dir,
        }
    else:
        handle_error(p.lineno(-1), p.lexpos(-1), "multiple var name declaration: " + current_var )

def p_r_register_princ(p):
    'r_register_princ : '
    global symbol_table
    symbol_table[current_func] = {
        'vars': {}
    }

# Registra la direción para el salto inicial de programa "goto main"
def p_r_end_princ(p):
    'r_end_princ : '
    e = end_princ()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# Funciones para guardar Operandos y Operadores para hacer Cuádruplos y Operaciones
def p_r_seen_operand(p):
    'r_seen_operand : '
    e = register_operand(p[-1])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_operand_id(p):
    'r_seen_operand_id :'
    e = register_operand_id(p[-1], current_func)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_operator(p):
    'r_seen_operator : '
    e = register_operator(p[-1])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_unary_operator(p):
    'r_seen_unary_operator : '
    raw_operator = p[-1]
    if raw_operator == '+':
        operator = "PLUS_UNARY"
    elif raw_operator == '-':
        operator = "MINUS_UNARY"
    else:
        operator = "!"
    e = register_operator(operator)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)


def p_r_seen_equal(p):
    'r_seen_equal : '
    e = solve_op_or_cont(['='], mark_assigned=True)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_subexp(p):
    'r_seen_subexp : '
    e = solve_op_or_cont(['&&', '||'], mark_assigned=False)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_exp(p):
    'r_seen_exp : '
    e = solve_op_or_cont(['>', '<', '==','!=', '<=', '>='], mark_assigned=False)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_term(p):
    'r_seen_term : '
    e = solve_op_or_cont(['+', '-'], mark_assigned=False)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_factor(p):
    'r_seen_factor : '
    e = solve_op_or_cont(['*', '/', '%'], mark_assigned=False)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_seen_operator_mat(p):
    'r_seen_operator_mat : '
    pass #TODO operator with matrices

def p_r_pop_fake_bottom(p):
  'r_pop_fake_bottom : '
  e = pop_fake_bottom()
  if e:
      handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_check_int(p):
    'r_check_int : '
    e = check_int()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_if_end(p):
    'r_if_end : '
    e = cond_end("if")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_else_start(p):
    'r_else_start : '
    e = else_start()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_set_while(p):
    'r_set_while : '
    e = set_while()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_while_end(p):
    'r_while_end : '
    e = cond_end("while")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_for_gen(p):
    'r_for_gen : '
    e = gen_for()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_for_end(p):
    'r_for_end : '
    e = cond_end("for")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_save_param_func(p):
    'r_save_param_func : '
    e = populate_func("numparam", current_func) #Save the number of parameters
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_save_vars(p):
    'r_save_vars : '
    e = populate_func("numvar", current_func) #save the number of variables
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_func_set(p):
    'r_func_set : '
    e = func_set(current_func) #Set the quad-pointer to start the function
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_func_end(p):
    'r_func_end : '
    e = func_end(current_func) #End var table, create_quadruple ENDFunc
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_check_func(p):
    'r_check_func : '
    e = func_check(p[-1]) #Checa que exista la funcion en el symbol_table
    global call_func
    call_func = p[-1]
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_check_param(p):
    'r_check_param : '
    global call_func, current_func
    e = check_param(call_func)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_go_sub(p):
    'r_go_sub : '
    global call_func
    e = go_sub(call_func)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_goto_main(p):
    'r_goto_main : '
    e = goto_main(p[-1])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_regresa(p):
    'r_regresa : '
    e = default_function("REGRESA")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_escribe(p):
    'r_escribe : '
    e = default_function("ESCRIBE")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_lee(p):
    'r_lee : '
    e = default_function("LEE")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

def p_r_print_constants(p):
    'r_print_constants : '
    e = print_constants()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# Para controlar errores
def handle_error(line, lexpos, mssg):
  '''Print error message and set error state to true'''
  global error
  error = True
  error_prefix(line, lexpos, input_str)
  print(mssg)

def error_prefix(line, lexpos, input_str):
  '''Prints the line and column where an error ocurred.'''

  print(f'Error at {line}:{find_column(lexpos, input_str)} - ', end='')
  global error
  error = True

def find_column(lexpos, input_str: str):
  '''Finds the column where an error ocurred.
  This is used to display error messages.
  '''

  line_start = input_str.rfind('\n', 0, lexpos) + 1
  return (lexpos - line_start) + 1

def p_error(p):
  global error
  error = True
  error_prefix(p.lineno, p.lexpos, input_str)
  print(f'Unexpected token {p.value}.')
  recover_parser(parser)

def recover_parser(parser):
  '''Recovers parser on error to keep finding errors.'''

  opened = 0
  tokName = None
  while True:
    tok = parser.token()
    if not tok:
      break
    tokName = tok.type
    if tokName == 'SC' and opened == 0:
      break
    elif tokName == 'LEFT_B':
      opened += 1
    elif tokName == 'RIGHT_B':
      opened -= 1
      if opened == 0:
        break
  parser.restart()
  return tokName

# Construir el Parser
parser = yacc.yacc()
