# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Cubo de semantica y tabla de simbolos de Patitoplusplus
# Created 04/25/2020
from enum import Enum, IntEnum, auto
from collections import defaultdict
from quadruples import operand_stack, operator_stack, type_stack, jump_stack, quadruples
import ast

current_type = None
current_func = 'global' # Scope
current_var = ''

symbol_table = {
        'global' : {
            'vars' : {}
        }
}

# Limites de memoria virtual
# Gracias a la siguiente configuración, solo pueden existir un total de 1500 variables de un tipo

VAR_LOWER_LIMIT = [13_000, 14_500, 16_000, 17_500]
VAR_UPPER_LIMIT = [14_499, 15_999, 17_499, 18_999]

TEMP_LOWER_LIMIT = [19_000, 20_500, 22_000, 23_500]
TEMP_UPPER_LIMIT = [20_499, 21_999, 23_499, 24_999]

CONST_LOWER_LIMIT = [25_000, 26_500, 28_000, 29_500]
CONST_UPPER_LIMIT = [26_499, 27_999, 29_499, 30_999]

#CONSTANT_UPPER_LIMIT = 30_999

# Contadores de memoria virutal
var_dir_count = list(VAR_LOWER_LIMIT)

temp_dir_count = list(TEMP_LOWER_LIMIT)

const_dir_count = list(CONST_LOWER_LIMIT)


# Enumeracion de tipos de datos
class Types(Enum):
  INT = 'int'
  FLOAT = 'float'
  CHAR = 'char'
  STRING = 'string'
  VOID = 'void'
  LEE = 'lee'

var_types = ('int', 'float', 'char', 'string')
avail_types = ('int', 'float', 'char', 'string', 'void')
func_types = ('int', 'float', 'char', 'string', 'void')

class Operations(IntEnum):
  PLUS_UNARY = 1
  MINUS_UNARY = 2
  NOT = 3
  TIMES = 4
  DIV = 5
  PLUS = 6
  MINUS = 7
  LESS_THAN = 8
  MORE_THAN = 9
  DIFFERENT = 10
  IS_EQUAL = 11
  LESS_EQUAL = 12
  MORE_EQUAL = 13
  OR = 14
  AND = 15
  EQUAL = 16
  LEE = 17
  WRITE = 18
  GOTO = 19
  GOTOF = 20
  GOSUB = 21
  PARAM = 22
  ERA = 23
  RETURN = 24
  ENDPROC = 25
  END = 26
  ENTER_INSTANCE = 27
  EXIT_INSTANCE = 28
  GET_RETURN = 29
  FAKE_BOTTOM = 30
  VER = 31
  SET_FOREIGN = 32
  UNSET_FOREIGN = 33
  MOD = 34

str_operations = {
    'unary+': 'unary+',
    'unary-': 'unary-',
    '!': '!',
    '*': '*',
    '/': '/',
    '+': '+',
    '-': '-',
    '<': '<',
    '>': '>',
    '!=': '!=',
    '==': '==',
    '<=': '<=',
    '>=': '>=',
    '||': '||',
    '&&': '&&',
    '=': '=',
    '(': '(',
    '%': '%'
}

#Manage Virtual address

def get_var_dir(current_type):
    global var_dir_count, VAR_UPPER_LIMIT
    switcher = {
    1: "int"
    2: "float"
    3: "char"
    4: "string"
    }
    result = switcher.get(current_type, -1)
    assert(result > 0), "Error!: Undefined type."
    if (var_dir_count[result] + 1 > VAR_UPPER_LIMIT[result]):
        




#Functions

# Register an operand on the operand_stack, with its type
def register_operand(raw_operand):
    global operand_stack
    try:
        operand = create_operand(raw_operand)
    except:
        print('Error al registrar operando')


    operand_stack.append(operand)

def create_operand(raw_operand):
    t = type(raw_operand)
    type_op = ''
    if t == int:
        type_op = 'int'
    if t == float:
        type_op = 'float'

    if t == str and len(raw_operand) == 1 :
        type_op = 'char'
    elif t == str:
        type_op = 'string'

    return (type_op, raw_operand)

#Register a function on the operator_stack
def register_operator(raw_operator):
    global operator_stack
    operator_stack.append(raw_operator)

#TODO: Resolve the operation _ gnerate the cuadruple?
# '''Generates quadruple for next operation if it exists in ops.
# Solves the next operation (from the operation stack) if it is included in ops.
# Returns error if operation cannot be performed on the given operands.
# Returns error if trying to perform an operation on a call to a void function.'''
def solve_op_or_cont(ops: [Operations]):
    global operator_stack, operand_stack, type_stack
    if operator_stack:
        if operator_stack[-1] in ops:
            #print(ops)
            # print(operator_stack)
            # print(operand_stack)
            operator = operator_stack[-1]
            # print(operator)

            # We need to verify if the stack has at leat two operands and they are not a fake bottom
            if len(operand_stack) > 1 and operator_stack[-1] is not "(" and operator_stack[-2] is not "(":
                operator = operator_stack.pop()
                right_type, right_operand = operand_stack.pop()
                left_type, left_operand = operand_stack.pop()

                #Search for Operator Type
                result_type = semantic_cube[left_type][right_type][operator]


                if not result_type:
                     if left_type == 'void' or right_type == 'void':
                         return f'Expression returns no value.'
                     return f'Type mismatch: Invalid operation \'{operator}\' on given operand \'{right_operand}\' and \'{left_operand}\''

                #placeholder
                #temp = solve_expression(result_type, right_operand, left_operand)
                temp = (result_type, "0")
                #if temp.get_error():
                #  return temp.get_error()
                # Generate Cuadruple
                # TODO: Verfy OPERATION
                quadruples.append([operator, left_operand, right_operand, temp])
                operand_stack.append(temp)

# Declaracion de cubo sematico, todo que no sea declarado se considera NULO
# TODO: Realizar los operandos especiales unitarios para matrices
    pass


def solve_expression(result_type, right_operand, left_operand):
    global current_func
    #TODO: Add adresses to variables and CTEs

    address = temp


semantic_cube = defaultdict(
    lambda: defaultdict(lambda: defaultdict(lambda: None)))

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
