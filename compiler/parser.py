# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Parser con yacc de Patitoplusplus
# Created on 04/25/2020
# ========================================================================== #
# Parser.py
# ========================================================================== #
import yacc
from scanner import tokens
from semantics import *
import pprint

# String para errores
input_str = ''

# Punto de partida
start = 'PROGRAM'

# ========================================================================== #
# Gramática Libre de Contexto
# ========================================================================== #

# Produccion vacía para epsilon
def p_empty(p):
    'empty :'# goto_main : Crea cuadruplo principal para salto a MAIN
    pass

# PROGRAMA → programa r_goto_main id ;  VARS r_save_vars FUNCTIONS MAIN r_print_constants
# r_goto_main : Crea cuadruplo principal para salto a MAIN
# r_save_vars : Salva el numero de varaibles de la funcion en la variable func_var_count
# r_print_constants : Crea el archivo objeto para la virtual machine
def p_PROGRAM(p):
    'PROGRAM : PROGRAMA r_goto_main ID DOTCOMA VARS r_save_vars FUNCTIONS MAIN r_print_constants'
    pass

# MAIN → principal r_save_func ( ) r_register_princ r_save_param_func VARS r_save_vars r_end_princ r_func_set BLOQUE r_func_end
# r_save_func : Guarda la funcion en variable current_func
# r_register_princ : Crea el diccionario y la llave de la funcion en el symbol_table
# r_save_param_func : Salva el numero de parametros de la funcion en la variable func_param_counter
# r_save_vars : Salva el numero de varaibles de la funcion en la variable func_var_count
# r_end_princ : Guarda el cuadruplo de salto al final de la operación
# r_func_set : Guarda el instruction pointer en el jump_stack
# r_func_end : Destruye la var table de la funcion, crea el cueadruplo de ERA
def p_MAIN(p):
    'MAIN : PRINCIPAL r_save_func LPAREN RPAREN r_register_princ r_save_param_func VARS r_save_vars r_end_princ r_func_set BLOQUE r_func_end '
    pass

# VARS → var VAR_AUX | empty
def p_VARS(p):
    '''VARS : VAR VAR_AUX
    | empty'''
    pass

# VAR_AUX → TIPO IDS VAR_AUX | empty
def p_VAR_AUX(p):
    '''VAR_AUX : TIPO IDS VAR_AUX
    | empty'''
    pass

# TIPO → int r_save_type | float r_save_type | char r_save_type | string r_save_type
# r_save_type : Salva el tipo en la varable global current_type
def p_TIPO(p):
    '''TIPO : INT r_save_type
    | FLOAT r_save_type
    | CHAR r_save_type
    | STRING r_save_type'''
    pass

# IDS → id r_register_var ARRDIM r_populate_r ; | id r_register_var ARRDIM r_populate_r, IDS
# r_register_var : Salva el nombre de variable en la variable global current_var
# r_populate_r : Genera el size, y los offset de arreglos, en caso de que existan
def p_IDS(p):
    '''IDS : ID r_register_var ARRDIM r_populate_r DOTCOMA
    | ID r_register_var ARRDIM r_populate_r COMA IDS'''
    pass

# ARRDIM → [ CTE_I ARRDIM_AUX ] ARRDIM | empty
# r_register_arr : Salva el nombre de el arreglo, en el symbol_table
# r_register_dim : Salva las dimensiones del arreglo en el symbol_table
def p_ARRDIM(p):
    '''ARRDIM : r_register_arr LSTAPLE CTE_I r_register_dim ARRDIM_AUX RSTAPLE ARRDIM
    | empty'''
    pass

# ARRDIM → , CTE_I ARRDIM_AUX | empty
# r_register_dim : Salva las dimensiones del arreglo en el symbol_table
def p_ARRDIM_AUX(p):
    '''ARRDIM_AUX : COMA CTE_I r_register_dim ARRDIM_AUX
    | empty'''
    pass

# FUNCTIONS → FUNCTION FUNCTIONS | empty
def p_FUNCTIONS(p):
    '''FUNCTIONS : FUNCTION FUNCTIONS
    | empty'''
    pass

# FUNCTION → funcion TIPO id ( PARAM )  VARS BLOQUE | funcion void id ( PARAM )  VARS BLOQUE
# r_save_type : Salva el tipo en la varable global current_type
# r_save_func : Guarda la funcion en variable current_func
# r_register_func : Guarda el diccionario y la llave en el symbol_table
# r_save_param_func : Salva el numero de parametros de la funcion en la variable func_param_counter
# r_save_vars : Salva el numero de varaibles de la funcion en la variable func_var_count
# r_func_set : Guarda el instruction pointer en el jump_stack
# r_func_end : Destruye la var table de la funcion, crea el cueadruplo de ERA
def p_FUNCTION(p):
    '''FUNCTION : FUNCION TIPO ID r_save_func r_register_func LPAREN PARAM RPAREN r_save_param_func VARS r_save_vars r_func_set BLOQUE r_func_end
    | FUNCION VOID r_save_type ID r_save_func r_register_func LPAREN PARAM RPAREN r_save_param_func VARS r_save_vars r_func_set BLOQUE r_func_end'''
    pass

# PARAM → TIPO id PARAM_AUX
# Sólo acepta ids ya declaradas, no acepta constantes
# r_register_var : Salva el nombre de variable en la variable global current_var
def p_PARAM(p):
    '''PARAM : TIPO ID r_register_var PARAM_AUX
    | empty'''
    pass

# PARAM_AUX → , PARAM  | empty
def p_PARAM_AUX(p):
    '''PARAM_AUX : COMA PARAM
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

# ESTATUTO → ASIGNACION ; | FUN ; | COND | WRITE ; | READ ; | RETURN ;
def p_ESTATUTO(p):
    '''ESTATUTO : ASIGNACION DOTCOMA
    | FUN DOTCOMA
    | COND
    | WRITE DOTCOMA
    | READ DOTCOMA
    | RETURN DOTCOMA'''
    pass

# ASIGNACION → id ARRDIM = EXPRESION | id ARRDIM = CTE_ARR
# r_seen_operand_id : Salva el id en el operand stack, ademas de darle una dirrecion virtual
# r_seen_operator : Salva la operación en el operator_stack
# r_seen_equal : Salva la operacion "=" en el operator_stack, busca solucionar la operacion
def p_ASIGNACION(p):
    'ASIGNACION : ID r_seen_operand_id ARRACC EQUAL r_seen_operator EXPRESION r_seen_equal'
    pass

# ARRACC → [ EXPRESION ARRACC_AUX ] | empty
# r_check_dim : Guarda las dimensiones de un arreglo declarado
# r_create_quad : Genera los cuadruplos de VER y de sumas de pointer
# r_close_arracc : Destruye las variables temporales de declaracion de arreglo
def p_ARRACC(p):
    '''ARRACC : LSTAPLE r_check_dim EXPRESION r_create_quad ARRACC_AUX RSTAPLE r_close_arracc
    | empty'''
    pass

# ARRACC_AUX → , CTE_I ARRACC_AUX | empty
# r_add_dim : Aumenta el contador de dimensiones (r_dim)
# r_create_quad : Genera los cuadruplos de VER y de sumas de pointer
def p_ARRACC_AUX(p):
    '''ARRACC_AUX : COMA r_add_dim EXPRESION r_create_quad ARRACC_AUX
    | empty'''
    pass

# EXPRESION → SUBEXP EXPRESION_AUX
# r_seen_subexp : Trata de buscar operaciones del nivel subexpresion (AND, OR)
def p_EXPRESION(p):
    'EXPRESION : SUBEXP r_seen_subexp EXPRESION_AUX'
    pass

# EXPRESION_AUX → && r_seen_operator EXPRESION | || r_seen_operator EXPRESION | empty
# r_seen_operator : Salva la constante en el operator_stack
def p_EXPRESION_AUX(p):
    '''EXPRESION_AUX : AND r_seen_operator EXPRESION
    | OR r_seen_operator EXPRESION
    | empty'''
    pass

# SUBEXP → EXP SUBEXP_AUX
# r_seen_exp : Trata de buscar operaciones del nivel expresion de comparación
def p_SUBEXP(p):
    'SUBEXP : EXP r_seen_exp SUBEXP_AUX'
    pass

# SUBEXP → COMPARACION SUBEXP | empty
def p_SUBEXP_AUX(p):
    '''SUBEXP_AUX : COMPARACION SUBEXP
    | empty'''
    pass

# COMPARACION → > | < | == | != | >= | <=
# r_seen_operator : Salva la operacion en el operator_stack
def p_COMPARACION(p):
    '''COMPARACION : MORE r_seen_operator
    | LESS r_seen_operator
    | COMPARE r_seen_operator
    | DIFFERENT r_seen_operator
    | MOREEQUAL r_seen_operator
    | LESSEQUAL r_seen_operator'''
    pass

# EXP → TERMINO EXP_AUX
# r_seen_term : Trata de buscar operaciones del nivel termino ( + / - )
def p_EXP(p):
    'EXP : TERMINO r_seen_term EXP_AUX'
    pass

# + EXP | - EXP | empty
# r_seen_operator : Salva la operacion en el operator_stack
def p_EXP_AUX(p):
    '''EXP_AUX : PLUS r_seen_operator EXP
    | MINUS r_seen_operator EXP
    | empty'''
    pass

# TERMINO → FACTOR TERMINO_AUX
# r_seen_factor : Trata de buscar operaciones del nivel factor ( * / % )
def p_TERMINO(p):
    'TERMINO : FACTOR r_seen_factor TERMINO_AUX'
    pass

# TERMINO_AUX → * TERMINO | / TERMINO | % TERMINO | empty
# r_seen_operator : Salva la operacion en el operator_stack
# r_seen_term : Trata de buscar operaciones del nivel termino ( comparacion )
def p_TERMINO_AUX(p):
    '''TERMINO_AUX : MULT r_seen_operator TERMINO r_seen_term
    | DIV r_seen_operator TERMINO r_seen_term
    | MOD r_seen_operator TERMINO r_seen_term
    | empty'''
    pass

# FACTOR → ! FACTOR_AUX | FACTOR_AUX
# r_seen_unary_operator : Salva la operacion en el operator_stack
# solve_unary_or_cont(ops[]) : Trata de resolver operaciones unarias ( +unary, -unary, !, $, ¡, ? )
def p_FACTOR(p):
    '''FACTOR : NOT r_seen_unary_operator FACTOR_AUX
    | FACTOR_AUX'''
    e = solve_unary_or_cont(["MINUS_UNARY", "PLUS_UNARY", "!", "$", "¡", "?"])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# FACTOR_AUX → ( EXPRESION ) | SIGN ( EXPRESION ) | SIGN CTE | CTE ARROP | CTE
# r_seen_operator : Salva la operacion en el operator_stack
# r_pop_fake_bottom : Elimina el elemento "(" del operator_stack
# solve_unary_or_cont(ops[]) : Trata de resolver operaciones unarias ( +unary, -unary, !, $, ¡, ? )
def p_FACTOR_AUX(p):
    '''FACTOR_AUX : SIGN LPAREN r_seen_operator EXPRESION RPAREN r_pop_fake_bottom
    | SIGN CTE ARROP'''
    e = solve_unary_or_cont(["MINUS_UNARY", "PLUS_UNARY", "!", "$", "¡", "?"])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# SIGN → + CTE | - CTE
# r_seen_unary_operator : Salva la operacion en el operator_stack
def p_SIGN(p):
    '''SIGN : PLUS r_seen_unary_operator
    | MINUS r_seen_unary_operator
    | empty'''

# CTE → cte_i | cte_f | ct_ch | cte_string | FUN | ID ARRACC
# r_seen_operand : Salva la operand en el operand_stack, ADEMÁS de asignarle la dirreción temporal
# r_seen_operand_id : Salva la operarnd en el operand_stack, ADEMÁS de asignarle la dirreción temporal
def p_CTE(p):
    '''CTE : CTE_I r_seen_operand
    | CTE_F r_seen_operand
    | CTE_CH r_seen_operand
    | CTE_STRING r_seen_operand
    | FUN
    | ID r_seen_operand_id ARRACC '''
    pass

# ARROP→ $ | ! | ? | empty
# r_seen_operator_mat : Salva la operand en el operand_stack, ADEMÁS de asignarle la dirreción temporal
def p_ARROP(p):
    '''ARROP : DET_ARR r_seen_operator_mat
    | TRANS_ARR r_seen_operator_mat
    | INV_ARR r_seen_operator_mat
    | empty'''
    pass

# FUN → id ( FUN_AUX )
# r_check_func : Checa de exista la funcion exista en el symbol table
# r_go_sub : Genera el goto hacia la dirreción de la función
def p_FUN(p):
    'FUN : ID r_check_func LPAREN FUN_AUX RPAREN r_go_sub'
    pass

# FUN_AUX → EXPRESION , FUN_AUX | EXPRESION | empty
# r_check_param : Create cuadruples PARAM
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
# r_check_int : Revisa si la expresion es un entero, guarda la dirreción en el jump_stack
# r_if_end : Crea el goto con el elemento top del jump_stack
def p_IF(p):
    'IF : SI LPAREN EXPRESION r_check_int RPAREN ENTONCES IF2 r_if_end'
    pass

# IF2 → BLOQUE IF_AUX | COND
def p_IF2(p):
    '''IF2 : BLOQUE IF_AUX
    | COND'''
    pass

# IFAUX → sino BLOQUE | empty
# r_else_start : Crea el goto false, y el goto con el elemento top del jump_stack
def p_IF_AUX(p):
    '''IF_AUX : SINO r_else_start BLOQUE
    | empty'''
    pass

# WHILE → mientras ( EXPRESION ) WHILE_AUX WHILE2
# r_set_while : Guarda el point instruction en el jump_stack
# r_check_int : Revisa si la expresion es un entero, guarda la dirreción en el jump_stack
# r_while_end : Genera el goto con el elemento top del jump_stack
def p_WHILE(p):
    'WHILE : MIENTRAS r_set_while LPAREN EXPRESION r_check_int RPAREN WHILE_AUX WHILE2 r_while_end'
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
# r_set_for : Guarda el point instruction en el jump_stack
# r_for_gen : Guarda el elemento en el for_operand_stack
# r_for_end : Genera el goto con el elemento top del jump_stack
def p_FOR(p):
    'FOR : DESDE ASIGNACION r_set_for HASTA EXPRESION r_for_gen HACER FOR2 r_for_end'
    pass

# FOR2 → BLOQUE | COND
def p_FOR2(p):
    '''FOR2 : BLOQUE
    | COND'''
    pass

# WRITE → escribe ( WRITE_AUX )
def p_WRITE(p):
    'WRITE : ESCRIBE LPAREN WRITE_AUX RPAREN'
    pass

# WRITE_AUX → EXPRESION WRITE_AUXSUB
# r_escribe : Genera el cuadruplo de escribe
def p_WRITE_AUX(p):
    'WRITE_AUX : EXPRESION r_escribe WRITE_AUXSUB'
    pass

# WRITE_AUXSUB → , WRITE_AUX | empty
def p_WRITE_AUXSUB(p):
    '''WRITE_AUXSUB : COMA WRITE_AUX
    | empty'''
    pass

# READ → lee ( READ_AUX )
def p_READ(p):
    'READ : LEE LPAREN READ_AUX RPAREN'
    pass

# READ_AUX → id ARRDIM READ_AUXSUB
# r_seen_operand_id : Salva la operand en el operand_stack, ADEMÁS de asignarle la dirreción temporal.
# r_lee : Genera el cuadruplo de lectura
def p_READ_AUX(p):
    'READ_AUX : ID r_seen_operand_id ARRDIM r_lee READ_AUXSUB'
    pass

# READ_AUXSUB →, READ_AUX | empty
def p_READ_AUXSUB(p):
    '''READ_AUXSUB : COMA READ_AUX
    | empty'''
    pass

# RETURN → regresa ( EXPRESION ) | regresa ( NULL )
# r_regresa : Genera el cuadruplo de regreso
def p_RETURN(p):
    '''RETURN : REGRESA LPAREN EXPRESION RPAREN r_regresa
    | REGRESA LPAREN NULL RPAREN'''
    pass

# Precedencia: Para ambigüedades en la Operaciones
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV', 'MOD'),
    ('right', 'EQUAL'),
    ('left', 'AND', 'OR'),
)

# ========================================================================== #
# Funciones para guardar en symbol_table
# ========================================================================== #

# r_save_type : Salva el tipo en la varable global current_type
def p_r_save_type(p):
    'r_save_type : '
    global current_type
    current_type = p[-1]

# Guarda la funcion en variable current_func
def p_r_save_func(p):
    'r_save_func : '
    global current_func
    current_func = p[-1]

# Guarda el diccionario y la llave en el symbol_table
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

# Salva el nombre de variable en la variable global current_var
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

        e = get_func_count(current_type, current_dir) #Add the counter to variable / param counter

        if e:
            handle_error(p.lineno(-1), p.lexpos(-1), e)


        symbol_table[current_func]['vars'][current_var] = {
            'type': current_type, 'address': current_dir, 'isArray': False
        }
    else:
        handle_error(p.lineno(-1), p.lexpos(-1), "multiple var name declaration: " + current_var )

# Salva el nombre de el arreglo, en el symbol_table
def p_r_register_arr(p):
    'r_register_arr : '
    global symbol_table, current_var
    if current_var is not None:
        if symbol_table[current_func]['vars'][current_var].get('isArray') is False:
            symbol_table[current_func]['vars'][current_var]['isArray'] = {}
        e, (virtualAddress_type, virtualAddress) = create_operand_point(symbol_table[current_func]['vars'][current_var]['address'], current_var)
        if e:
            handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_register_dim : Salva las dimensiones del arreglo en el symbol_table
def p_r_register_dim(p):
    'r_register_dim : '
    global symbol_table, current_var, func_dim_counter, current_var_aux, r_dim
    if current_var_aux == current_var:
        func_dim_counter = func_dim_counter + 1

    else:
        current_var_aux = current_var
        func_dim_counter = 0
        r_dim = 1

    if symbol_table[current_func]['vars'][current_var]['isArray'] is not False:
        r_dim = (p[-1] - 0 + 1) * r_dim
        symbol_table[current_func]['vars'][current_var]['isArray'][func_dim_counter] = {
        'Li' : 0,
        'Ls' : p[-1],
        'R' : r_dim
        }

# r_populate_r : Genera el size, y los offset de arreglos, en caso de que existan
def p_r_populate_r(p):
    'r_populate_r : '
    global symbol_table, current_var, func_dim_counter, current_var_aux, r_dim, glo
    func_dim_counter = 0
    last_node = 0
    offset = 0
    arr_size = 0
    m_dim = 0
    k = 0
    if symbol_table[current_func]['vars'][current_var]['isArray'] is not False:
        for key in symbol_table[current_func]['vars'][current_var]['isArray'].items():
            m_dim = r_dim / ( key[1]['Ls'] - key[1]['Li'] + 1)
            symbol_table[current_func]['vars'][current_var]['isArray'][key[0]]['m_dim'] = m_dim
            r_dim = m_dim
            offset = offset + key[1]['Li'] * m_dim
            last_node = key[0]
        k = offset
        symbol_table[current_func]['vars'][current_var]['isArray'][last_node]['m_dim'] = -k
        arr_size = size_arr_calc(symbol_table[current_func]['vars'][current_var]['isArray'])
        e = None
        if current_func == 'global':
            e = set_global_size_arr(symbol_table[current_func]['vars'][current_var]['type'],arr_size)
        else:
            e = set_var_size_arr(symbol_table[current_func]['vars'][current_var]['type'],arr_size)
        if e:
            handle_error(p.lineno(-1), p.lexpos(-1), e)

#Checa las dimensiones de un arreglo declarado
def p_r_check_dim(p):
    'r_check_dim : '
    global symbol_table, r_dim, operator_stack, pila_dim
    temp_current = current_func
    if symbol_table[temp_current]['vars'].get(p[-3]) is None:
        temp_current = 'global'

    if symbol_table[temp_current]['vars'][p[-3]]['isArray'] is not False:
        r_dim = 1
        operand_stack.pop()
        pila_dim.append( (p[-3], r_dim) )
        register_operator("(")

# r_create_quad : Genera los cuadruplos de VER y de sumas de pointer
def p_r_create_quad(p):
    'r_create_quad : '
    global operand_stack
    e = None
    temp_current = current_func
    if top(operand_stack)[0] != 'int':
        e = "Expected int on array: " + str(current_var) + " but recieved + " + top(operand_stack)[0]
    if symbol_table[temp_current]['vars'].get(top(pila_dim)[0]) is None:
        if symbol_table['global']['vars'].get(top(pila_dim)[0]) is None:
            e = "Undefined Arr " + top(pila_dim)[[0]]
        else:
            temp_current = 'global'
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

    if symbol_table[temp_current]['vars'][top(pila_dim)[0]]['isArray'].get(r_dim-1) is not None:
        e, (inferior_type, inferior_address) = create_operand(symbol_table[temp_current]['vars'][top(pila_dim)[0]]['isArray'][r_dim-1]['Li'])
        if e:
            handle_error(p.lineno(-1), p.lexpos(-1), e)
        e, (superior_type, superior_address) = create_operand(symbol_table[temp_current]['vars'][top(pila_dim)[0]]['isArray'][r_dim-1]['Ls'])
        if e:
            handle_error(p.lineno(-1), p.lexpos(-1), e)

        create_quadruple("VER", top(operand_stack)[1], inferior_address, superior_address)

    if symbol_table[temp_current]['vars'][top(pila_dim)[0]]['isArray'].get(r_dim) is not None:
        aux_type, aux = operand_stack.pop()
        temp, e = get_temp_dir(aux_type)
        e, (m_dim_type, m_dim_address) = create_operand( symbol_table[temp_current]['vars'][top(pila_dim)[0]]['isArray'][r_dim-1]['m_dim']-1)
        if e:
            handle_error(p.lineno(-1), p.lexpos(-1), e)
        create_quadruple("*", aux, m_dim_address, temp)
        operand_stack.append((aux_type, temp))

    if r_dim > 1:
        aux_type2, aux2 = operand_stack.pop()
        aux_type, aux = operand_stack.pop()
        temp, e = get_temp_dir(aux_type)
        create_quadruple("+", aux, aux2, temp)
        operand_stack.append((aux_type, temp))


# r_add_dim : Aumenta el contador de dimensiones (r_dim)
def p_r_add_dim(p):
    'r_add_dim : '
    global r_dim, pila_dim
    r_dim = r_dim + 1
    temp, temp_dim  = pila_dim.pop()
    pila_dim.append( (temp, r_dim) )

# r_close_arracc : Destruye las variables temporales de declaracion de arreglo
def p_r_close_arracc(p):
    'r_close_arracc : '
    global operand_stack
    aux_type, aux = operand_stack.pop()
    temp_current = current_func
    e = None
    if symbol_table[temp_current]['vars'].get(top(pila_dim)[0]) is None:
        temp_current = 'global'
        if symbol_table[temp_current]['vars'].get(top(pila_dim)[0]) is None:
            e = "Undefined Arr " + top(pila_dim)[0]
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

    temp, e = get_temp_dir(aux_type)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)
        #temp 2 is a pointer array!
    temp2, e = get_point_dir()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

    e, (m_dim_type, m_dim_address) = create_operand( symbol_table[temp_current]['vars'][top(pila_dim)[0]]['isArray'][r_dim-1]['m_dim'])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

    create_quadruple("+", aux, m_dim_address, temp)

    #Create a new operand with the virtual address of the array, AS a value of a new const
    e, (virtualAddress_type, virtualAddress) = create_operand_point(symbol_table[temp_current]['vars'][top(pila_dim)[0]]['address'], top(pila_dim)[0])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

    # ( + temp virtualAddress(arr) newtemp)
    # temp2 = offset + base(dir)
    create_quadruple("+dir", temp, virtualAddress, temp2)
    operand_stack.append( (aux_type, temp2) )
    pop_fake_bottom()


# r_register_princ : Crea el diccionario y la llave de la funcion en el symbol_table
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

# r_seen_operand_id : Salva el id en el operand stack, ademas de darle una dirrecion virtual.
def p_r_seen_operand_id(p):
    'r_seen_operand_id :'
    e = register_operand_id(p[-1], current_func)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_seen_operator : Salva la constante en el operand_stack, ademas de darle una dirrecion virtual.
def p_r_seen_operator(p):
    'r_seen_operator : '
    e = register_operator(p[-1])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_seen_unary_operator : Salva la operacion en el operator_stack
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

# r_seen_operator_mat : Salva la operarnd en el operand_stack, ADEMAS de asignarle la dirreción temporal.
def p_r_seen_operator_mat(p):
    'r_seen_operator_mat : '
    raw_operator = p[-1]
    e = register_operator(raw_operator)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_seen_equal : Salva la operacion "=" en el operand_stack, busca solucionar la operacion
def p_r_seen_equal(p):
    'r_seen_equal : '
    e = solve_op_or_cont(['='], mark_assigned=True)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_seen_subexp : Trata de buscar operaciones del nivel subexpresion (AND, OR)
def p_r_seen_subexp(p):
    'r_seen_subexp : '
    e = solve_op_or_cont(['&&', '||'], mark_assigned=False)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_seen_exp : Trata de buscar operaciones del nivel subexpresion  (AND, OR)
def p_r_seen_exp(p):
    'r_seen_exp : '
    e = solve_op_or_cont(['>', '<', '==','!=', '<=', '>='], mark_assigned=False)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_seen_term : Trata de buscar operaciones del nivel termino ( comparacion )
def p_r_seen_term(p):
    'r_seen_term : '
    e = solve_op_or_cont(['+', '-'], mark_assigned=False)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_seen_factor : Trata de buscar operaciones del nivel factor ( * / % )
def p_r_seen_factor(p):
    'r_seen_factor : '
    e = solve_op_or_cont(['*', '/', '%'], mark_assigned=False)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_pop_fake_bottom : Elimina el elemento "(" del operator_stack
def p_r_pop_fake_bottom(p):
  'r_pop_fake_bottom : '
  e = pop_fake_bottom()
  if e:
      handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_check_int : Revisa si la expresion es un entero, guarda la dirreción en el jump_stack
def p_r_check_int(p):
    'r_check_int : '
    e = check_int()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_if_end : Crea el goto con el elemento top del jump_stack
def p_r_if_end(p):
    'r_if_end : '
    e = cond_end("if")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_else_start : crea el goto false, y el goto con el elemento top del jump_stack
def p_r_else_start(p):
    'r_else_start : '
    e = else_start()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_set_while : Guarda el point instruction en el jump_stack
def p_r_set_while(p):
    'r_set_while : '
    e = set_while()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_while_end : Genera el goto con el elemnto top del jump_stack
def p_r_while_end(p):
    'r_while_end : '
    e = cond_end("while")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_set_for : Guarda el point instruction en el jump_stack
def p_r_set_for(p):
    'r_set_for : '
    e = set_for()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_for_gen : Guarda el elemento en el for_operand_stack
def p_r_for_gen(p):
    'r_for_gen : '
    e = gen_for()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_for_end : Genera el goto con el elemnto top del jump_stack
def p_r_for_end(p):
    'r_for_end : '
    e = cond_end("for")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_save_param_func : Salva el numero de parametros de la funcion en la variable func_param_counter
def p_r_save_param_func(p):
    'r_save_param_func : '
    e = populate_func("numparam", current_func) #Save the number of parameters
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

#Save the number of variables
def p_r_save_vars(p):
    'r_save_vars : '
    e = populate_func("numvar", current_func)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

#Set the quad-pointer to start the function
def p_r_func_set(p):
    'r_func_set : '
    e = func_set(current_func)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

#End var table, create_quadruple ENDFunc
def p_r_func_end(p):
    'r_func_end : '
    e = func_end(current_func)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

#Checa que exista la funcion en el symbol_table
def p_r_check_func(p):
    'r_check_func : '
    e = func_check(p[-1])
    global call_func
    call_func = p[-1]
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_check_param : Crea cuadruplos PARAM
def p_r_check_param(p):
    'r_check_param : '
    global call_func, current_func
    e = check_param(call_func)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_go_sub : Genera el goto hacia la dirreción de la función
def p_r_go_sub(p):
    'r_go_sub : '
    global call_func
    e = go_sub(call_func)
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_goto_main : Crea cuadruplo principal para salto a MAIN
def p_r_goto_main(p):
    'r_goto_main : '
    e = goto_main(p[-1])
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_regresa : Genera el cuadruplo de regreso
def p_r_regresa(p):
    'r_regresa : '
    e = default_function("RETURN")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_escribe : Genera el cuadruplo de escribe
def p_r_escribe(p):
    'r_escribe : '
    e = default_function("ESCRIBE")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_lee : Genera el cuadruplo de lectura
def p_r_lee(p):
    'r_lee : '
    e = default_function("LEE")
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# r_print_constants : Crea el archivo objeto para la virtual machine
def p_r_print_constants(p):
    'r_print_constants : '
    e = print_constants()
    if e:
        handle_error(p.lineno(-1), p.lexpos(-1), e)

# ========================================================================== #
# Manejo de Errores
# ========================================================================== #

# Función para controlar errores
def handle_error(line, lexpos, mssg):
  '''Print error message and set error state to true'''
  global p_error
  p_error = True
  error_prefix(line, lexpos, input_str)
  print(mssg)

# Función para impirmir errores a pantalla
def error_prefix(line, lexpos, input_str):
  '''Prints the line and column where an error ocurred.'''

  print(f'Error at line = {line} - ', end='')
  global p_error
  p_error = True

#Funcion para imprimir errores a pantalla.
def p_error(p):
  global p_error
  p_error = True
  error_prefix(p.lineno, p.lexpos, input_str)
  print(f'Unexpected token {p.value}.')
  recover_parser(parser)

# Funcion para recuperar la continiudad de parser en caso de error
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
  parser.lineno = 1
  parser.restart()
  return tokName

# Construir el Parser
parser = yacc.yacc()
