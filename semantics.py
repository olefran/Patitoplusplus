    # Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# semantincs cube and symbol table of Patitoplusplus
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

#Funcion para consultar un simbolo dad una llave
# Input: dirreción del simbolo
# Output: Symbolo
def consult_type():
    return NULL

# Limites de memoria virtual
ATTRIBUTE_LOWER_LIMIT = 7_000
ATTRIBUTE_UPPER_LIMIT = 12_999
VAR_LOWER_LIMIT = 13_000
VAR_UPPER_LIMIT = 18_999
TEMP_LOWER_LIMIT = 19_000
TEMP_UPPER_LIMIT = 24_999
GLOBAL_ADJUSTMENT = 12_000
ATTRIBUTES_ADJUSTMENT = 6_000
CONSTANT_LOWER_LIMIT = 25_000
CONSTANT_UPPER_LIMIT = 30_999


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
            print(operator)

            # We need to verify if the stack has at leat two operands and is not a fake bottom
            if len(operand_stack) > 1 and operator_stack[-1] is not "(":
                operator = operator_stack.pop()
                right_type, right_operand = operand_stack.pop()
                print(right_type, right_operand)
                left_type, left_operand = operand_stack.pop()
                print(left_type, left_operand)
            #
            # result_type = semantic_cube[left_type][right_type][operator]
            #
            # print(right_operand, left_operand, result_type)
            #
            # if not result_type:
            #     if left_type == 'void' or right_type == 'void':
            #         return f'Expression returns no value.'
            #     return f'Type mismatch: Invalid operation \'{operator}\' on given operand'

            #temp = build_temp_operand(result_type)
            #if temp.get_error():
            #  return temp.get_error()
            # Generate Cuadruple
            # TODO: Verfy OPERATION
            #quadruples.append([operator, left_operand, right_operand, temp])
            #operand_stack.append(temp_type, temp)

# Declaracion de cubo sematico, todo que no sea declarado se considera NULO
# TODO: Realizar los operandos especiales unitarios para matrices
    pass

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
