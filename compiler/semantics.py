# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Cubo de semantica y tabla de simbolos de Patitoplusplus
# Created 04/25/2020
from structures import *
import ast

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
            operand = (symbol_table['global']['vars'][raw_operand]['type'], symbol_table['global']['vars'][raw_operand]['address']) #Return id by address
            #operand = (symbol_table['global']['vars'][raw_operand]['type'], raw_operand) # Return id by name
            operand_stack.append(operand)
    else:
        operand = (symbol_table[current_func]['vars'][raw_operand]['type'], symbol_table[current_func]['vars'][raw_operand]['address']) #Return id by address
        #operand = (symbol_table[current_func]['vars'][raw_operand]['type'], raw_operand) #Return id by name
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
    elif t == str and raw_operand[0] == '\'' : #ERROR registers wrong 'char' (counts '')
        raw_operand = raw_operand.replace('\'','')
        type_op = 'char'
    elif t == str:
        raw_operand = raw_operand.replace('\"','')
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
    #return e, (type_op, raw_operand)  #Return constant by name
    return e, (type_op, address) # Return constant by address

#Register a operator (raw_symbol) on the operator_stack
def register_operator(raw_operator):
    global operator_stack
    operator_stack.append(raw_operator)

#Gets top element of stack without popping it and if there is none is doesn't crash
def top(l):
  if len(l) > 0:
    return l[-1]
  return None

#Pops ( aka fake bottom form the operator_stack
def pop_fake_bottom():
  global operator_stack
  operator = operator_stack.pop()
  if operator != '(':
      e = 'Expected: )'

# TODO: Realizar los operandos especiales unitarios para matrices


# Create cuadruples and add to quad_pointer
def create_quadruple(operator, left_operand, right_operand, result):
    global quadruples, quad_pointer
    quadruples.append([operator, left_operand, right_operand, result])
    quad_pointer = quad_pointer + 1


# '''Generates quadruple for next operation if it exists in ops.
# Solves the next operation (from the operation stack) if it is included in ops.
# Returns error if operation cannot be performed on the given operands.
# Returns error if trying to perform an operation on a call to a void function.'''
def solve_op_or_cont(ops: [Operations], mark_assigned):
    global operator_stack, operand_stack
    e = None
    operator = top(operator_stack)
    if operator in ops:
      right_type, right_operand = operand_stack.pop()
      left_type, left_operand = operand_stack.pop()
      operator = operator_stack.pop()
      result_type = semantic_cube[left_type][right_type][operator]
      if not result_type:
        if left_type == 'void' or right_type == 'void':
          return f'Expression returns no value.'
        return f'Type mismatch: Invalid operation \'{operator}\' on given operand \'{right_operand}\' and \'{left_operand}\''
      temp, e = None, None
      if mark_assigned:
          create_quadruple(operator, right_operand, None, left_operand)
          temp = left_operand
      else:
          temp, e = get_temp_dir(result_type)
          create_quadruple(operator, left_operand, right_operand, temp)
      operand_stack.append( (result_type, temp) ) #Se quedan los results en el stack
    elif operator == ')':
        operator_stack.pop()
        print(top(operator))
        if top(operator) != '(':
            e = "Expected: ')'"
        else:
            operator = operator_stack.pop()
    return e

#Generates cuadruples for unary operations
def solve_unary_or_cont(ops: [Operations]):
    global operator_stack, operand_stack
    e = None
    operator = top(operator_stack)
    if operator in ops :
        operand_type, operand_name = operand_stack.pop()
        operator = operator_stack.pop()
        if operator == 'PLUS_UNARY':
            operator = 'unary+'
        elif operator == 'MINUS_UNARY':
            operator = 'unary-'
        result_type = semantic_cube[operand_type][operator]
        if not result_type:
            return f"Type mismatch: Invalid operation \'{operator}\' on given operand \'{operand_name}\'"
        temp, e = get_temp_dir(result_type)
        create_quadruple(operator, operand_name, None, temp)
        operand_stack.append((result_type, temp))

    return e



#
#def solve_expression(result_type, right_operand, left_operand):
#    global current_func
    #TODO: Add adresses to variables and CTEs
#    pass

# check value ("int") for if / while expressions
def check_int():
    global jump_stack
    e = None
    if top(operand_stack)[0] != 'int':
        e = "Expected: 'int' type on expression"
    else:
        type, result = operand_stack.pop()
        create_quadruple('GOTOF', result, None, None)
        jump_stack.append(quad_pointer - 1)

# fill waiting goto staement
def fill_quad(end, cont):
    global quadruples
    e = None
    try:
        quadruples[end][3] = cont
    except:
        e = "Unable to modify quadruple: " + end
    return e

# end if OR while statement and fill waiting goto dir
def cond_end(type_op):
    e = None
    global jump_stack
    end = jump_stack.pop()
    if type_op == "while" or type_op == "for":
        loop_return = jump_stack.pop()
        create_quadruple('GOTO', None , None, loop_return)
    e = fill_quad(end, quad_pointer)
    return e

# Generate quadruples for else staement
def else_start():
    global jump_stack
    e = None
    create_quadruple('GOTO', None, None, None)
    if_false = jump_stack.pop()
    jump_stack.append(quad_pointer - 1)
    e = fill_quad(if_false, quad_pointer)
    return e

#Set quad_pointer to while function
def set_while():
    global jump_stack
    jump_stack.append(quad_pointer)
    return None

# Creates quadruple for main
def goto_main(function):
    global jump_stack
    create_quadruple('GOTO', None, None, None)
    jump_stack.append(quad_pointer - 1)

#set quad_pointer
def gen_for():
    global jump_stack
    e = None
    if top(operand_stack)[0] != 'int':
        e = "Expected: 'int' type on expression"
    else:
        operator_stack.append(">")
        e = solve_op_or_cont(['>'], mark_assigned = False)
        type, operand = operand_stack.pop()
        create_quadruple('GOTOF', operand, None, None)
        jump_stack.append(quad_pointer - 1)
        jump_stack.append(quad_pointer - 1)
    return e

def populate_func(type_op, current_func):
    global symbol_table, func_var_count, func_param_order
    e = None
    if symbol_table[current_func].get(type_op) is not None:
        e = "Trying to define a new param/var number for function: " + current_func

    if type_op == "numparam":
        symbol_table[current_func]['param'] = func_param_order # Save parameter order

    symbol_table[current_func][type_op] = func_var_count
    func_var_count = [0, 0, 0, 0]
    func_param_order = []
    return e

def func_set(current_func):
    global symbol_table
    e = None
    try:
        symbol_table[current_func]['pos'] = quad_pointer
    except:
        e = "Not able to modify quad pointer on start position on function: " + current_func
    return e

def func_end(current_func):
    global symbol_table, temp_dir_count, var_dir_count
    e = None
    try:
        #symbol_table[current_func]['vars'] = None    #DELETE THE VAR TABLE
        temp_dir_count = list(TEMP_LOWER_LIMIT) #RESET the temp counter
        var_dir_count = list(VAR_LOWER_LIMIT) #RESET the temp countre
    except:
        e = "Not able to delete var table on function: " + current_func
    create_quadruple("ENDFunc", None, None, None)
    return e
    pass

def get_func_count(current_type, current_var):
    global func_var_count, func_param_order
    switcher = {
    "int": 0,
    "float": 1,
    "char": 2,
    "string": 3
    }
    e = None
    result = switcher.get(current_type, -1)
    if result < 0:
        e = "Invalid type on counter addition on: " + current_var
    func_var_count[result] = func_var_count[result] + 1
    func_param_order.append( (current_type, current_var) )
    return e

def func_check(current_func):
    global symbol_table, func_param_counter
    e = None
    size = []
    func_param_counter = 0
    if symbol_table.get(current_func) is None:
        e = "Function not found: " + current_func
    else:
        for element in range(len(symbol_table[current_func]['numvar'])):
            size.append(symbol_table[current_func]['numvar'][element] + symbol_table[current_func]['numparam'][element])
        create_quadruple("ERA", current_func, None, size)
    return e

def check_param(current_func):
    global func_param_counter
    e = None
    argumentType, value = operand_stack.pop()
    paramsize = len(symbol_table[current_func]['param'])
    tempParam = func_param_counter + 1
    if func_param_counter >= paramsize:
        e = "Too many parameters on: " + current_func
        return e
    if argumentType == symbol_table[current_func]['param'][func_param_counter][0]:
        create_quadruple("PARAM", value, None, tempParam)
        func_param_counter = func_param_counter + 1
    else:
        e = "Type error on " + current_func + " parameter " + str(func_param_counter + 1) + " erronuos type of " + argumentType
    return e

def go_sub(current_func):
    create_quadruple("GOSUB", current_func, None, symbol_table[current_func]['pos'])
    if symbol_table['global']['vars'].get(current_func) is not None:
        temp, e = get_temp_dir(symbol_table['global']['vars'][current_func]['type'])
        operand_stack.append( (symbol_table['global']['vars'][current_func]['type'], temp) )
        create_quadruple('=', symbol_table['global']['vars'][current_func]['address'], None, temp)

def default_function(func):
    Type, value = operand_stack.pop()
    create_quadruple(func, None, None, value)

# Save elements for virtual machine on Ouput.txt
def print_constants():
    global symbol_table, const_table, quadruples

    #Modificar constant table to write address : value , type
    constant_dir = {}

    for element in const_table:
        constant_dir[ const_table[element]['address'] ] = {
            'value' : element,
            'type' : const_table[element]['type']
        }

    text_file = open("virtualMachine/Output.txt", "w")
    text_file.write('{\n')
    text_file.write('\'symbol_table\': ' + str(symbol_table) + ',\n')
    text_file.write('\'const_table\': ' + str(constant_dir) + ',\n')
    text_file.write('\'quadruples\': ' + str(quadruples) + '\n')
    text_file.write('}')
    text_file.close()

#Save principal address on "goto main" jump
def end_princ():
    global jump_stack, quadruples
    quadruples[jump_stack.pop()][3] = quad_pointer
