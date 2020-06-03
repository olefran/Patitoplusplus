# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Cubo de semantica y tabla de simbolos de Patitoplusplus
# Created 04/25/2020
from structures import *
import ast

# ========================================================================== #
# Manejo de la dirección digital de variables globales, constantes, temporales
# ========================================================================== #

# Regresa error en caso de superar la dimension límite de globales
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

# Aumento de la dirrecion de memoria de variables temporales con tamaño del arreglo
# Regresa error en caso de superar la dimension límite de variables locales
def set_var_size_arr(current_type, arr_size):
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
            return e
        if var_dir_count[result] + arr_size - 1 > VAR_UPPER_LIMIT[result]:
            e = "Too many " + current_type + " vars"
            return e
        var_dir_count[result] = var_dir_count[result] + arr_size - 1
        return e

# Aumento de la dirrecion de memoria de variables globales con tamaño del arreglo
# Regresa error en caso de superar la dimension límite de globales
def set_global_size_arr(current_type, arr_size):
        global global_dir_count
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
            return e
        if global_dir_count[result] + arr_size - 1 > GLOBAL_UPPER_LIMIT[result]:
            e = "Too many " + current_type + " vars"
            return e
        global_dir_count[result] = global_dir_count[result] + arr_size - 1
        return e

# Aumento de la dirrecion de memoria de variables temporales con tamaño del arreglo
# Regresa error en caso de superar la dimension límite de temporales
def set_temp_size_arr(current_type, arr_size):
        global global_dir_count
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
            return e
        if temp_dir_count[result] + arr_size - 1 > TEMP_UPPER_LIMIT[result]:
            e = "Too many " + current_type + " vars"
            return e
        temp_dir_count[result] = temp_dir_count[result] + arr_size - 1
        return e

#Sacá un operando del operand_stack
def pop_operand():
    o = operand_stack.pop()
    return o

# Manejo de la dirección digital de variables en funciones
# Regresa error encaso de encontrar un typo no especificado
# Regresa error en caso de superar la dimension límite de variables locales
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
# Regresa error encaso de encontrar un typo no especificado
# Regresa error en caso de superar la dimension límite de variables temporales
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
# Regresa error encaso de encontrar un typo no especificado
# Regresa error en caso de superar la dimension límite de constantes
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

# Manejo de la dirección digital de pointers!
# Regresa error en caso de superar la dimension límite de pointers
def get_point_dir():
    global point_dir_count
    e = None
    if point_dir_count[0] > POINT_UPPER_LIMIT[0]:
        e = "Too many " + current_type + " temps"
        return -1, e
    point_dir_count[0] = point_dir_count[0] + 1
    return point_dir_count[0] -1, e

# ========================================================================== #
# Registro de operandos en tablas de variables, tabla de constantes
# ========================================================================== #

# Registrar un operando en el operand_stack, con su tipo
# Regresa error en caso de superar un límite de dimension
def register_operand(raw_operand):
    global operand_stack
    e, operand = create_operand(raw_operand)
    operand_stack.append(operand)
    return e

# ========================================================================== #
# Registrar elementos temporales, variables, y globales
# ========================================================================== #

# Registrar un id en el operand_stack, con su tipo
# Regresa error en caso de superar el límite de direcciones constante
def register_operand_id(raw_operand, current_func):
    global operand_stack
    e = None
    if symbol_table[current_func]['vars'].get(raw_operand) is None:
        if symbol_table['global']['vars'].get(raw_operand) is None:
            e = "Variable not defined: " + raw_operand
        else:
            operand = (symbol_table['global']['vars'][raw_operand]['type'], symbol_table['global']['vars'][raw_operand]['address']) #Return id by address
            # operand = (symbol_table['global']['vars'][raw_operand]['type'], raw_operand) # Return id by name
            operand_stack.append(operand)
    else:
        operand = (symbol_table[current_func]['vars'][raw_operand]['type'], symbol_table[current_func]['vars'][raw_operand]['address']) #Return id by address
        # operand = (symbol_table[current_func]['vars'][raw_operand]['type'], raw_operand) #Return id by name
        operand_stack.append(operand)
    return e

# Función que llena la operand table y registra cualquier unknown const variables
# Regresa error en caso de superar el límite de direcciones constante
def create_operand(raw_operand):
    t = type(raw_operand)
    type_op = ''
    if t == int:
        type_op = 'int'
    elif t == float:
        type_op = 'float'
    elif t == str and raw_operand[0] == '\'' : # ERROR registers wrong 'char' (counts '')
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
    # return e, (type_op, raw_operand)  #Return constant by name
    return e, (type_op, address) # Return constant by address

# Función que llena la operand table y registra cualquier unknown const variables
# Regresa error en caso de superar el límite de direcciones constante
def create_operand_point(raw_operand, name):
    e = None
    if const_table.get(raw_operand) is None:
        address, e = get_const_dir('int')
        const_table[raw_operand] = {
            'address': address,
            'type': 'pointer',
            'name' : name
        }
    else:
        address = const_table[raw_operand]['address']
    # return e, (type_op, raw_operand)  #Return constant by name
    return e, ('int', address) # Return constant by address

# Register a operator (raw_symbol) on the operator_stack
def register_operator(raw_operator):
    global operator_stack
    operator_stack.append(raw_operator)

#Saca el elemento top de lista y regresa None
def top(l):
  if len(l) > 0:
    return l[-1]
  return None

# Elimina el elemento "(" de operator_stack
# Regresa error en caso de no encontrar '('
def pop_fake_bottom():
  global operator_stack
  operator = operator_stack.pop()
  if operator != '(':
      e = 'Expected: )'

# ========================================================================== #
# Creación de cuadruplos de operaciones
# ========================================================================== #

# Crea los cuadruplos y amenta el quad_pointer
def create_quadruple(operator, left_operand, right_operand, result):
    global quadruples, quad_pointer
    quadruples.append([operator, left_operand, right_operand, result])
    quad_pointer = quad_pointer + 1

# Genera cuadruplos para la siguiento operacion (en caso de que exista) en ops.
# Resulve la siguiente operacion (del operador_stack) si esta incluido en ops.
# Regresa error si la operación no puede ser resulta con los operandos dados
# Regresa error si intenta realizar una operación a una operación void

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

      # Checa si ambos operandos son matrices y genera los cuadruplos
      if const_table.get(right_operand) is not None and const_table.get(left_operand) is not None:
          if const_table[right_operand].get('name') is not None and const_table[left_operand].get('name') is not None:
              result_type, temp, e = check_mat_op(operator, right_operand, const_table[right_operand]['name'], left_operand, const_table[left_operand]['name'], result_type, mark_assigned)
              if e:
                  return e

      elif mark_assigned:
          create_quadruple(operator, right_operand, None, left_operand)
          temp = left_operand
      else:
          temp, e = get_temp_dir(result_type)
          create_quadruple(operator, left_operand, right_operand, temp)
      operand_stack.append( (result_type, temp) ) #Se quedan los results en el stack

    elif operator == ')':
        operator_stack.pop()
        if top(operator) != '(':
            e = "Expected: ')'"
        else:
            operator = operator_stack.pop()
    return e

# Checa operaciones matriciales especiales de operador
# Regresa error en caso de intentar realizar operaciones con dimensiones incorrectas (en caso de matrices)
# Regresa error si se intenta realizar una operación con un tipo incorrecto.
def check_mat_op(operator, right_operand, right_name, left_operand, left_name, result_type, mark_assigned):
    e = None
    size_right = []
    size_left = []

    if symbol_table[current_func]['vars'].get(right_name) is None:
        size_right = right_name
    else:
        for element in symbol_table[current_func]['vars'][right_name]['isArray'].items():
            size_right.append(element[1]['Ls'])
        size_right = tuple(size_right)

    if symbol_table[current_func]['vars'].get(left_name) is None:
        size_left = left_name
    else:
        for element in symbol_table[current_func]['vars'][left_name]['isArray'].items():
            size_left.append(element[1]['Ls'])
        size_left = tuple(size_left)

    if operator != "*":
        if size_right != size_left:
            e = "Matrices (" + str(right_name) + ", " + str(left_name) + ") don't have size (" + str(size_right) + "," + str(size_left) + ") for the op: " + operator
            return result_type, -1, e
    else:
        if len(size_right) != 2:
            e = "Matrix multiplication can only be done in 2 dimentions, recieved" + str(right_name) + ", size :" + str(size_right)
            return result_type, -1, e
        elif size_right[1] != size_left[0]:
            e = "Incorrect Matrix multiplication dimentions, recieved:" + str(size_right[1]) + " != " + str(size_left[0])
            return result_type, -1, e

    operator = operator + "mat"

    if mark_assigned:
      create_quadruple(operator, (right_operand, size_right) , None, ( left_operand, size_left ) )
      temp = left_operand
    else:
        temp, e = get_temp_dir(result_type)
        create_operand_point(temp, size_right)
        set_temp_size_arr(result_type, multiply_tuple(size_right) )
        if operator == "*":
            size_temp = (size_right[0], size_left[1])
            create_quadruple(operator, (left_operand, size_left), (right_operand, size_right) , (temp, size_temp) )
        else:
            create_quadruple(operator, (left_operand, size_left), (right_operand, size_right) , (temp, size_left) )

    return result_type, temp, e

# Checa operaciones matriciales especiales de operadores unarios
# Regresa error en caso de intentar realizar operaciones con dimensiones incorrectas (en caso de matrices)
# Regresa error si se intenta realizar una operación con un tipo incorrecto.
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

        #Caso especial para operadores unarios
        if const_table.get(operand_name) is not None:
            if const_table[operand_name].get('name') is not None:
                size = []
                name = const_table[operand_name]['name']
                if symbol_table[current_func]['vars'].get(name) is None:
                    size = name
                else:
                    for element in symbol_table[current_func]['vars'][name]['isArray'].items():
                        size.append(element[1]['Ls'])
                    size = tuple(size)

                if operator == '$':
                    if size[0] != size[1]:
                        return "Incorrect dim for operator " + str(operator) + ": " + str(size[0]) + " =!" + str(size[1])
                    create_quadruple(operator, (operand_name, size), None , temp )

                elif operator == '¡':
                    if len(size) != 2:
                        return "Incorrect dim for operator " + str(operator) + " recieved " + str(len(size)) + " expected 2"
                    temp_size = tuple([size[1], size[0]])
                    create_operand_point(temp, temp_size)
                    set_temp_size_arr(result_type, multiply_tuple(size) )
                    create_quadruple(operator, (operand_name, size), None , (temp, temp_size) )

                elif operator == '?':
                    if len(size) != 2:
                        return "Incorrect dim for operator " + str(operator) + " recieved " + str(len(size)) + " expected 2"
                    create_operand_point(temp, size)
                    set_temp_size_arr(result_type, multiply_tuple(size) )
                    create_quadruple(operator, (operand_name, size), None , (temp, size) )

                else:
                    operator = operator + "mat"
                    create_operand_point(temp, size)
                    set_temp_size_arr(result_type, multiply_tuple(size) )
                    create_quadruple(operator, (operand_name, size), None , (temp, size) )

        elif operator == '$' or operator == '¡' or operator == '?':
            return "Operator " + str(operator) + " not given a Matrix, recieved: " + str(result_type)
        else :
            create_quadruple(operator, operand_name, None, temp)

        operand_stack.append((result_type, temp))

    return e

# ========================================================================== #
# Operaciones de modulos (funciones)
# ========================================================================== #


# Checa el valor de un entero en la expresion
# Regresa error si no existe tal entero.
def check_int():
    global jump_stack
    e = None
    if top(operand_stack)[0] != 'int':
        e = "Expected: 'int' type on expression"
    else:
        type, result = operand_stack.pop()
        create_quadruple('GOTOF', result, None, None)
        jump_stack.append(quad_pointer - 1)

# Llenar un elemento del goto
# Regresa error si no se puede modificar el cuadruplo goto
def fill_quad(end, cont):
    global quadruples
    e = None
    try:
        quadruples[end][3] = cont
    except:
        e = "Unable to modify quadruple: " + end
    return e

# end if OR while statement and fill waiting goto dir
# Termina una expresion while ó un for y genera cuadruplos para la actualizacion de cuadruples
# Regresa un error en caso de superar el límite de direcciones virtuales
def cond_end(type_op):
    e = None
    global jump_stack, for_operand_stack
    end = jump_stack.pop()
    if type_op == "while" or type_op == "for":
        loop_return = jump_stack.pop()
        if type_op == "for":
            operand = for_operand_stack.pop()
            e, (type, address) = create_operand(1)
            temp, e =  get_temp_dir(type)
            create_quadruple('+', operand, address, temp)
            create_quadruple('=', temp, None, operand)
            loop_return = loop_return - 1
        create_quadruple('GOTO', None , None, loop_return)
    e = fill_quad(end, quad_pointer)
    return e

# Generate quadruples for else staement
# Genera cuadruples para else
# Regresa un error en caso de uperar el límite de direcciones virtuales
def else_start():
    global jump_stack
    e = None
    create_quadruple('GOTO', None, None, None)
    if_false = jump_stack.pop()
    jump_stack.append(quad_pointer - 1)
    e = fill_quad(if_false, quad_pointer)
    return e

# Genera el quad_pointer en la función while
def set_while():
    global jump_stack
    jump_stack.append(quad_pointer)
    return None

# Crea cuadruplo para main
def goto_main(function):
    global jump_stack
    create_quadruple('GOTO', None, None, None)
    jump_stack.append(quad_pointer - 1)

# Crea cuadruplo final para for
# Regresa error en caso de no encontrar una expresion int
def set_for():
    global jump_stack, for_operand_stack
    e = None
    if top(operand_stack)[0] != 'int':
        e = "Expected: 'int' type on expression"
    type, operand = top(operand_stack)
    for_operand_stack.append(operand)

# Guarda el quad pointer para la operación for, appenda la dirección para regresar en el jump_stack
# Regresa error en caso de no encontrar una expresion int
def gen_for():
    global jump_stack, for_operand_stack
    e = None
    if top(operand_stack)[0] != 'int':
        e = "Expected: 'int' type on expression"
    else:
        operator_stack.append("<")
        e = solve_op_or_cont(['<'], mark_assigned = False)
        type, operand = operand_stack.pop()
        create_quadruple('GOTOF', operand, None, None)
        jump_stack.append(quad_pointer - 1)
        jump_stack.append(quad_pointer - 1)
    return e

# Salva el numero de parametros de la funcion en la variable func_param_counter
# Regresa error si no existe la funcion
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

# Agrega a la función dentro del symbol_table su address
# Regresa error en caso de no poder accesa la current func
def func_set(current_func):
    global symbol_table
    e = None
    try:
        symbol_table[current_func]['pos'] = quad_pointer
    except:
        e = "Not able to modify quad pointer on start position on function: " + current_func
    return e

# Termina el contexto de la funcion (reseta contadores temporales y locales)
# Regresa error si la funcion no existe
def func_end(current_func):
    global symbol_table, temp_dir_count, var_dir_count
    e = None
    try:
        symbol_table[current_func]['vars'] = None  #DELETE VAR TABLE
        temp_dir_count = list(TEMP_LOWER_LIMIT) #RESET temp counter
        var_dir_count = list(VAR_LOWER_LIMIT) #RESET temp func_dim_counter
    except:
        e = "Not able to delete var table on function: " + current_func
    create_quadruple("ENDFunc", None, None, None)
    return e
    pass

# Recibe las funciones direcciones virtuales
# Regresa error si sobrepasa el límite superior de variables locales
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

# Crea el cuadruplo de ERA de funcion, con si tamaño
# Regresa un error si la funcion no existe
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

# Crear cuadruples PARAM para current_func
# Regresa error en caso de numeros de parametros incorrecto.
# Regresa error en caso de tipado incorrecto de parametros
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

# Genera cuadruplo gosub, genera operación de igual para valores de retorno
def go_sub(current_func):
    create_quadruple("GOSUB", current_func, None, symbol_table[current_func]['pos'])
    if symbol_table['global']['vars'].get(current_func) is not None:
        temp, e = get_temp_dir(symbol_table['global']['vars'][current_func]['type'])
        operand_stack.append( (symbol_table['global']['vars'][current_func]['type'], temp) )
        create_quadruple('=', symbol_table['global']['vars'][current_func]['address'], None, temp)

# Genera cuadruplos para funciones como lee y escribe
def default_function(func):
    Type, value = operand_stack.pop()
    create_quadruple(func, None, None, value)

# Genera archivo objeto para maquina virtual
def print_constants():
    global symbol_table, const_table, quadruples

    #Modificar constant table para escribir address : value , type
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

# Guarda dirección principal en "goto main" jump
def end_princ():
    global jump_stack, quadruples
    quadruples[jump_stack.pop()][3] = quad_pointer

# Caulcula el  tamaño del arreglo con base en su dimensiones
def size_arr_calc(arr_isArray):
    size = 1
    for element in arr_isArray.items():
        size = size * element[1]['Ls']
    return size

# Multiplicación de elementos de tupla
def multiply_tuple(varr):
    temp = 1
    for elem in varr:
        temp = temp * elem
    return temp
