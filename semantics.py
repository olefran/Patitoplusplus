# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Cubo de semantica y tabla de simbolos de Patitoplusplus
# Created 04/25/2020
from enum import Enum, IntEnum, auto
from collections import defaultdict
from quadruples import operand_stack, operator_stack, jump_stack, quadruples
import ast

# Variables Auxiliares para currents
current_type = None
current_func = 'global' # Scope
current_var = ''

# Directorio de funciones y sus variables
symbol_table = {
        'global' : {
            'vars' : {}
        }
}

# Directorio de constantes
const_table = {}

# Limites de memoria virtual
# Gracias a la siguiente configuración, solo pueden existir un total de 1500 variables de un tipo
# VARIABLES GLOBALES    INT     FLOAT   CHAR    STRINGS  VOID
GLOBAL_LOWER_LIMIT =    [5_000, 6_500, 8_000, 9_500, 11_000]
GLOBAL_UPPER_LIMIT =    [6_499, 7_999, 9_499, 10_999, 12_499]

# VAR DE FUNCIONES      INT     FLOAT   CHAR    STRINGS
VAR_LOWER_LIMIT =       [13_000, 14_500, 16_000, 17_500]
VAR_UPPER_LIMIT =       [14_499, 15_999, 17_499, 18_999]

# CONSTANTES            INT     FLOAT   CHAR    STRINGS
CONST_LOWER_LIMIT =     [19_000, 20_500, 22_000, 23_500]
CONST_UPPER_LIMIT =     [20_499, 21_999, 23_499, 24_999]

# TEMPORALES            INT     FLOAT   CHAR    STRINGS
TEMP_LOWER_LIMIT =      [25_000, 26_500, 28_000, 29_500]
TEMP_UPPER_LIMIT =     [26_499, 27_999, 29_499, 30_999]

#CONSTANT_UPPER_LIMIT = 30_999

# Contadores de memoria virutal
global_dir_count = list(GLOBAL_LOWER_LIMIT)
var_dir_count = list(VAR_LOWER_LIMIT)
temp_dir_count = list(TEMP_LOWER_LIMIT)
const_dir_count = list(CONST_LOWER_LIMIT)

# Enumeracion de tipos de datos
var_types = ('int', 'float', 'char', 'string')
avail_types = ('int', 'float', 'char', 'string', 'void')
func_types = ('int', 'float', 'char', 'string', 'void')

# Diccionario de Operaciones
str_operations = ('unary+','unary-','!','*','/','+','-','<','>','!=','==','<=','>=','||','&&','=','(','%')
Operations = {
  "PLUS_UNARY" : 1,
  "MINUS_UNARY" : 2,
  "NOT" : 3,
  "TIMES" : 4,
  "DIV" : 5,
  "PLUS" : 6,
  "MINUS" : 7,
  "LESS_THAN" : 8,
  "MORE_THAN" : 9,
  "DIFFERENT" : 10,
  "IS_EQUAL" : 11,
  "LESS_EQUAL" : 12,
  "MORE_EQUAL" : 13,
  "OR" : 14,
  "AND" : 15,
  "EQUAL" : 16,
  "LEE" : 17,
  "WRITE" : 18,
  "GOTO" : 19,
  "GOTOF" : 20,
  "GOSUB" : 21,
  "PARAM" : 22,
  "ERA" : 23,
  "RETURN" : 24,
  "ENDPROC" : 25,
  "END" : 26,
  "ENTER_INSTANCE" : 27,
  "EXIT_INSTANCE" : 28,
  "GET_RETURN" : 29,
  "FAKE_BOTTOM" : 30,
  "VER" : 31,
  "SET_FOREIGN" : 32,
  "UNSET_FOREIGN" : 33,
  "MOD" : 34
 }

# Manejo de la dirección digital de variables globales
def get_global_dir(current_type):
    global global_dir_count
    switcher = {
    "int": 0,
    "float": 1,
    "char": 2,
    "string": 3,
    "void": 4,
    }
    e = None
    result = switcher.get(current_type, -1)
    if result < 0:
        e = "Undefined type: " + current_type
        return result, e
    if global_dir_count[result] > GLOBAL_UPPER_LIMIT[result]:
        e = "Too many " + current_type + "vars"
        return result, e
    global_dir_count[result] = global_dir_count[result] + 1
    return global_dir_count[result] - 1, e

# Manejo de la dirección digital de variables en funciones
def get_var_dir(current_type):
    global var_dir_count
    switcher = {
    "int": 0,
    "float": 1,
    "char": 2,
    "string": 3
    }
    e = None
    result = switcher.get(current_type, -1)
    if result < 0:
        e = "Undefined type: " + current_type
        return result, e
    if var_dir_count[result] > VAR_UPPER_LIMIT[result]:
        e = "Too many " + current_type + " vars"
        return result, e
    var_dir_count[result] = var_dir_count[result] + 1
    return var_dir_count[result] - 1, e

# Manejo de la dirección digital de variables temporales
def get_temp_dir(current_type):
    global temp_dir_count
    switcher = {
    "int": 0,
    "float": 1,
    "char": 2,
    "string": 3
    }
    e = None
    result = switcher.get(current_type, -1)
    if result < 0:
        e = "Undefined type: " + current_type
        return result, e
    if temp_dir_count[result] > TEMP_UPPER_LIMIT[result]:
        e = "Too many " + current_type + " temps"
        return result, e
    temp_dir_count[result] = temp_dir_count[result] + 1
    return temp_dir_count[result] -1, e

# Manejo de la dirección digital de constantes
def get_const_dir(current_type):
    global const_dir_count
    switcher = {
    "int": 0,
    "float": 1,
    "char": 2,
    "string": 3
    }
    e = None
    result = switcher.get(current_type, -1)
    if result < 0:
        e = "Undefined type: " + current_type
        return result, e
    if const_dir_count[result] > CONST_UPPER_LIMIT[result]:
        e = "Too many " + current_type + " consts"
        return result, e
    const_dir_count[result] = const_dir_count[result] + 1
    return const_dir_count[result] -1, e

# Funciones

# Registrar un operando en el operand_stack, con su tipo
# TODO: Modify to use addreses? And IDS
def register_operand(raw_operand):
    global operand_stack
    e, operand = create_operand(raw_operand)
    operand_stack.append(operand)
    return e


def register_operand_id(raw_operand, current_func):
    global operand_stack
    e = None
    if symbol_table[current_func]['vars'].get(raw_operand) is None:
        if symbol_table['global']['vars'].get(raw_operand) is None:
            e = "Variable not defined: " + raw_operand
        else:
            #operand = (symbol_table['global']['vars'][raw_operand]['type'], symbol_table['global']['vars'][raw_operand])
            operand = (symbol_table['global']['vars'][raw_operand]['type'], raw_operand)
            operand_stack.append(operand)
    else:
        #operand = (symbol_table[current_func]['vars'][raw_operand]['type'], symbol_table[current_func]['vars'][raw_operand])
        operand = (symbol_table[current_func]['vars'][raw_operand]['type'], raw_operand)
        operand_stack.append(operand)
    return e

# Esta función llena la operand table y registra cualquier unknown const variables
#It is unkownable by this humble programmer if this is the correct implementation
def create_operand(raw_operand):
    t = type(raw_operand)
    type_op = ''
    if t == int:
        type_op = 'int'
    elif t == float:
        type_op = 'float'
    elif t == str and len(raw_operand) == 1 :
        type_op = 'char'
    elif t == str:
        type_op = 'string'
    e = None
    address = -1
    if type_op == '':
        e = "unknown type used " + raw_operand
        return e, (type_op, address)
    if const_table.get(raw_operand) is None:
        address, e = get_const_dir(type_op)
        const_table[raw_operand] = {
            'address': address,
            'type': type_op
        }
    else:
        address = const_table[raw_operand]['address']
    return e, (type_op, raw_operand)

#Register a operator (raw_symbol) on the operator_stack
def register_operator(raw_operator):
    global operator_stack
    operator_stack.append(raw_operator)


#TODO: Resolve the operation _ gnerate the cuadruple?
# TODO: Realizar los operandos especiales unitarios para matrices


# '''Generates quadruple for next operation if it exists in ops.
# Solves the next operation (from the operation stack) if it is included in ops.
# Returns error if operation cannot be performed on the given operands.
# Returns error if trying to perform an operation on a call to a void function.'''

def solve_op_or_cont(ops: [Operations]):
    global operator_stack, operand_stack
    e = None
    if operator_stack:
        if operator_stack[-1] in ops:
            operator = operator_stack[-1]
            # Checar que al menos haya 2 operandos y nos sea fake bottom
            if len(operand_stack) > 1 and operator_stack[-1] != "(" and operator_stack[-2] != "(":
                operator = operator_stack.pop()
                right_type, right_operand = operand_stack.pop()
                left_type, left_operand = operand_stack.pop()
                # Buscar el tipo del operador
                result_type = semantic_cube[left_type][right_type][operator]
                if not result_type:
                     if left_type == 'void' or right_type == 'void':
                         return f'Expression returns no value.'
                     return f'Type mismatch: Invalid operation \'{operator}\' on given operand \'{right_operand}\' and \'{left_operand}\''
                #temp = solve_expression(result_type, right_operand, left_operand)
                temp, e = get_temp_dir(result_type)
                # if temp.get_error():
                #  return temp.get_error()
                # Generate Cuadruple
                # TODO: Verify OPERATION
                quadruples.append([operator, left_operand, right_operand, temp])
                #print(quadruples)
                operand_stack.append( (result_type, temp) )
    return e

#
def solve_expression(result_type, right_operand, left_operand):
    global current_func
    #TODO: Add adresses to variables and CTEs
    pass

# Semantic cube for Operations
semantic_cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

semantic_cube['int']['int']['&&'] = 'int'
semantic_cube['int']['int']['||'] = 'int'
semantic_cube['int']['int']['<'] = 'int'
semantic_cube['int']['int']['>'] = 'int'
semantic_cube['int']['int']['!='] = 'int'
semantic_cube['int']['int']['=='] = 'int'
semantic_cube['int']['int']['<='] = 'int'
semantic_cube['int']['int']['>='] = 'int'
semantic_cube['int']['int']['+'] = 'int'
semantic_cube['int']['int']['-'] = 'int'
semantic_cube['int']['int']['*'] = 'int'
semantic_cube['int']['int']['/'] = 'int'
semantic_cube['int']['int']['='] = 'int'
semantic_cube['int']['lee']['='] = 'int'
semantic_cube['int']['unary+'] = 'int'
semantic_cube['int']['unary-'] = 'int'
semantic_cube['int']['!'] = 'int'

semantic_cube['float']['float']['&&'] = 'int'
semantic_cube['float']['float']['||'] = 'int'
semantic_cube['float']['float']['<'] = 'int'
semantic_cube['float']['float']['>'] = 'int'
semantic_cube['float']['float']['!='] = 'int'
semantic_cube['float']['float']['=='] = 'int'
semantic_cube['float']['float']['<='] = 'int'
semantic_cube['float']['float']['>='] = 'int'
semantic_cube['float']['float']['+'] = 'float'
semantic_cube['float']['float']['-'] = 'float'
semantic_cube['float']['float']['*'] = 'float'
semantic_cube['float']['float']['/'] = 'float'
semantic_cube['float']['float']['='] = 'float'
semantic_cube['float']['lee']['='] = 'float'
semantic_cube['float']['unary+'] = 'float'
semantic_cube['float']['unary-'] = 'float'
semantic_cube['float']['!'] = 'int'

semantic_cube['char']['char']['&&'] = 'int'
semantic_cube['char']['char']['||'] = 'int'
semantic_cube['char']['char']['<'] = 'int'
semantic_cube['char']['char']['>'] = 'int'
semantic_cube['char']['char']['!='] = 'int'
semantic_cube['char']['char']['=='] = 'int'
semantic_cube['char']['char']['>='] = 'int'
semantic_cube['char']['char']['<='] = 'int'
semantic_cube['char']['char']['+'] = 'char'
semantic_cube['char']['char']['-'] = 'char'
semantic_cube['char']['char']['*'] = 'char'
semantic_cube['char']['char']['/'] = 'char'
semantic_cube['char']['char']['='] = 'char'
semantic_cube['char']['lee']['='] = 'char'
semantic_cube['char']['unary+'] = None
semantic_cube['char']['unary-'] = None
semantic_cube['char']['!'] = 'char'

semantic_cube['int']['float']['&&'] = semantic_cube['float']['int']['&&'] = 'int'
semantic_cube['int']['float']['||'] = semantic_cube['float']['int']['||'] = 'int'
semantic_cube['int']['float']['<'] = semantic_cube['float']['int']['<'] = 'int'
semantic_cube['int']['float']['>'] = semantic_cube['float']['int']['>'] = 'int'
semantic_cube['int']['float']['!='] = semantic_cube['float']['int']['!='] = 'int'
semantic_cube['int']['float']['=='] = semantic_cube['float']['int']['=='] = 'int'
semantic_cube['int']['float']['<='] = semantic_cube['float']['int']['<='] = 'int'
semantic_cube['int']['float']['>='] = semantic_cube['float']['int']['>='] = 'int'
semantic_cube['int']['float']['+'] = semantic_cube['float']['int']['+'] = 'float'
semantic_cube['int']['float']['-'] = semantic_cube['float']['int']['-'] = 'float'
semantic_cube['int']['float']['*'] = semantic_cube['float']['int']['*'] = 'float'
semantic_cube['int']['float']['/'] = semantic_cube['float']['int']['/'] = 'float'
semantic_cube['int']['float']['='] = 'int'
semantic_cube['float']['int']['='] = 'float'

semantic_cube['int']['char']['&&'] = semantic_cube['char']['int']['&&'] = 'int'
semantic_cube['int']['char']['||'] = semantic_cube['char']['int']['||'] = 'int'
semantic_cube['int']['char']['<'] = semantic_cube['char']['int']['<'] = 'int'
semantic_cube['int']['char']['>'] = semantic_cube['char']['int']['>'] = 'int'
semantic_cube['int']['char']['!='] = semantic_cube['char']['int']['!='] = 'int'
semantic_cube['int']['char']['=='] = semantic_cube['char']['int']['=='] = 'int'
semantic_cube['int']['char']['<='] = semantic_cube['char']['int']['<='] = 'int'
semantic_cube['int']['char']['>='] = semantic_cube['char']['int']['>='] = 'int'
semantic_cube['int']['char']['+'] = semantic_cube['char']['int']['+'] = 'int'
semantic_cube['int']['char']['-'] = semantic_cube['char']['int']['-'] = 'int'
semantic_cube['int']['char']['*'] = semantic_cube['char']['int']['*'] = 'int'
semantic_cube['int']['char']['/'] = semantic_cube['char']['int']['/'] = 'int'
semantic_cube['int']['char']['='] = 'int'
semantic_cube['char']['int']['='] = 'char'

semantic_cube['float']['char']['&&'] = semantic_cube['char']['float']['&&'] = 'int'
semantic_cube['float']['char']['||'] = semantic_cube['char']['float']['||'] = 'int'
semantic_cube['float']['char']['<'] = semantic_cube['char']['float']['<'] = 'int'
semantic_cube['float']['char']['>'] = semantic_cube['char']['float']['>'] = 'int'
semantic_cube['float']['char']['!='] = semantic_cube['char']['float']['!='] = 'int'
semantic_cube['float']['char']['=='] = semantic_cube['char']['float']['=='] = 'int'
semantic_cube['float']['char']['<='] = semantic_cube['char']['float']['<='] = 'int'
semantic_cube['float']['char']['>='] = semantic_cube['char']['float']['>='] = 'int'
semantic_cube['float']['char']['+'] = semantic_cube['char']['float']['+'] = 'float'
semantic_cube['float']['char']['-'] = semantic_cube['char']['float']['-'] = 'float'
semantic_cube['float']['char']['*'] = semantic_cube['char']['float']['*'] = 'float'
semantic_cube['float']['char']['/'] = semantic_cube['char']['float']['/'] = 'float'
semantic_cube['float']['char']['='] = 'float'
semantic_cube['char']['float']['='] = 'char'
semantic_cube['char']['lee']['='] = 'char'
