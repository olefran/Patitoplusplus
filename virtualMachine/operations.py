# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Operaciones para virtualMachine
# Created 04/25/2020
from structures import *
import ast
import numpy as np
# ========================================================================== #
# Operations.py
# ========================================================================== #

# ========================================================================== #
# Funciones miscelánias
# ========================================================================== #

# Regresa el último elemento de una lista, ó en caso de None, regresa None
def top(l):
  if len(l) > 0:
    return l[-1]
  return None

# Regresa el quad_pointer
def get_pointer():
    global quad_pointer
    return quad_pointer

# Regresa quad_pointer
def set_pointer(value):
    global quad_pointer
    quad_pointer = value

# Transforma int hacia booleano
def check_true(input):
    return not input == 0

# Transforma bool hacia intbool
def get_bool_int(input):
    if input == False:
        return 0
    else:
        return 1

# Regresa el tipo de la variable conforme a su dieecion virtual
def check_type(dir):
    if dir < 6500:
        return 'int'
    if dir < 8000:
        return 'float'
    if dir < 9500:
        return 'char'
    if dir < 11000:
        return 'string'
    if dir < 13000:
        return 'void'
    if dir < 14500:
        return 'int'
    if dir < 16000:
        return 'float'
    if dir < 17500:
        return 'char'
    if dir < 19000:
        return 'string'
    if dir < 20500:
        return 'int'
    if dir < 22000:
        return 'float'
    if dir < 23500:
        return 'char'
    if dir < 25000:
        return 'string'
    if dir < 26500:
        return 'int'
    if dir < 28000:
        return 'float'
    if dir < 29500:
        return 'char'
    if dir < 31000:
        return 'string'
    if dir < 50000:
        return 'pointer'


# ========================================================================== #
# Operaciones de Máquina virtual
# ========================================================================== #

# Regresa el valor asocioado con la direción
def get_value(dir):
    if dir > 4999 and dir < 12500:
        if global_memory.get(dir) is None:
            raise Exception("Undefined dir: " + str(dir) )
        else:
            return global_memory[dir]
    elif dir > 18999 and dir < 25000:
        if const_table.get(dir) is None:
            raise Exception("Undefined dir: " + str(dir) )
        else:
            return const_table[dir]['value']
    elif dir > 49999:
        return get_value(get_value_for_address(dir))
    else:
        if top(temp_memory).get(dir) is None:
            raise Exception("Undefined dir: " + str(dir) )
        else:
            return top(temp_memory)[dir]

# Regresa el valor asocioado con la direción (sin busqueda de pointers)
def get_value_for_address(dir):
    if dir > 4999 and dir < 12500:
        if global_memory.get(dir) is None:
            raise Exception("Undefined dir: " + str(dir) )
        else:
            return global_memory[dir]
    elif dir > 18999 and dir < 25000:
        if const_table.get(dir) is None:
            raise Exception("Undefined dir: " + str(dir) )
        else:
            return const_table[dir]['value']
    else:
        if top(temp_memory).get(dir) is None:
            raise Exception("Undefined dir: " + str(dir) )
        else:
            return top(temp_memory)[dir]

# Escribe el valor que se asocia con la direción dir
def set_value(value, dir):
    global temp_memory, global_memory
    e = True
    try:
        if dir > 4999 and dir < 12500:
            global_memory[dir] = value
        elif dir > 49999:
            set_value(value, get_value_for_address(dir))
        else:
            top(temp_memory)[dir] = value
    except:
        e = "Error on assingning value " + str(value) + " to dir " + str(dir)
    return e

# Escribe el valor que se asocia con la direción dir (sin  busqieda de pointers)
def set_value_for_address(value, dir):
    global temp_memory, global_memory
    e = True
    try:
        if dir > 4999 and dir < 12500:
            global_memory[dir] = value
        else:
            top(temp_memory)[dir] = value
    except:
        e = "Error on assingning value " + str(value) + " to dir " + str(dir)
    return e

# Cambia quad_pointer
def goto_solve(first, second, dst):
    global quad_pointer
    quad_pointer = dst
    return False

# Suma unaria
def plus_unary_solve(first, second, dst):
    return set_value(+get_value(first),dst)

# Menos unario
def minus_unary_solve(first, second, dst):
    return set_value(-get_value(first), dst)

# Not lógico unario
def not_unary_solve(first, second, dst):
    temp = None
    if check_true( get_value(first) ):
        temp = 0
    else:
        temp = 1
    return set_value(temp, dst)
    # return set_value( get_bool_int( not check_true(first) ), dst )

# multiplicar
def times_solve(first, second, dst):
    return set_value( get_value(first) * get_value(second), dst)

# dividir
def divide_solve(first, second, dst):
    return set_value( get_value(first) / get_value(second), dst)

# Modulo
def mod_solve(first, second, dst):
    return set_value( get_value(first) % get_value(second), dst)

# Suma
def plus_solve(first, second, dst):
    return set_value( get_value(first) + get_value(second), dst)

# Resta
def minus_solve(first, second, dst):
    return set_value( get_value(first) - get_value(second), dst)

# Menor que
def less_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) < get_value(second) ), dst )

# Mayor que
def more_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) > get_value(second) ), dst )

# Differente a
def different_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) != get_value(second) ), dst )

# Es igual a
def comparison_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) == get_value(second) ), dst )

# Menor o igual
def less_than_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) <= get_value(second) ), dst )

#Mayor o igual
def more_than_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) >= get_value(second) ), dst )

# Ó
def or_solve(first, second, dst):
    temp = check_true( get_value(first) ) or check_true( get_value(second) )
    return set_value( get_bool_int( temp ), dst )

# Y
def and_solve(first, second, dst):
    temp = check_true( get_value(first) ) and check_true( get_value(second) )
    return set_value( get_bool_int( temp ), dst )

# Igual a
def equal_solve(first, second, dst):
    return set_value(get_value(first), dst)

#Igual a matrix
def equal_mat_solve(first, second, dst):
    size = 1
    temp = 0
    for dim in first[1]:
        size = size * dim
    for x in range(size):
        temp = set_value(get_value(first[0] + x), dst[0] + x )
        if temp is not True:
            return temp
    return temp


# Suma unaria matrix
def plus_unary_mat_solve(first, second, dst):
    size = 1
    temp = 0
    for dim in first[1]:
        size = size * dim
    for x in range(size):
        temp = set_value(+get_value(first[0] + x), dst[0] + x )
        if temp is not True:
            return temp
    return temp

# Resta unaria matriz
def minus_unary_mat_solve(first, second, dst):
    size = 1
    temp = 0
    for dim in first[1]:
        size = size * dim
    for x in range(size):
        temp = set_value(-get_value(first[0] + x), dst[0] + x )
        if temp is not True:
            return temp
    return temp

#Get cofactor for determinant calculation [DEPRECATED FOR NUMPY]
def get_cofactor(first):
    i = j = 0
    for row in range(first[1][0]):
        for col in range(first[1][0]):
            pass

#Determinante de matrices
def det_mat_solve(first, second, dst):
    temp = None
    mat = []
    arr_temp = []
    for x in range(first[1][0]):
        for y in range(first[1][1]):
            arr_temp.append(get_value(first[0] + x*first[1][0] + y ) )
        mat.append(arr_temp)
        arr_temp = []
    answer = np.linalg.det(mat)
    return set_value(answer, dst)

#Matriz transpuesta
def trans_mat_solve(first, second, dst):
    temp = None
    mat = []
    arr_temp = []
    aux = 0
    for x in range(first[1][0]):
        for y in range(first[1][1]):
            arr_temp.append(get_value(first[0] + aux))
            aux = aux + 1
        mat.append(arr_temp)
        arr_temp = []
    matrix = np.array(mat)
    matrix = matrix.transpose()
    for x in range(dst[1][0]):
        for y in range(dst[1][1]):
            temp = set_value(matrix[x][y], dst[0]+x*dst[1][1]+y )
            if temp is not True:
                return temp
    return temp

# Matriz inversa
def inv_mat_solve(first, second, dst):
    temp = None
    mat = []
    arr_temp = []
    for x in range(first[1][0]):
        for y in range(first[1][1]):
            arr_temp.append(get_value(first[0] + x*first[1][0] + y ) )
        mat.append(arr_temp)
        arr_temp = []
    matrix = np.linalg.inv(mat)
    for x in range(first[1][1]):
        for y in range(first[1][0]):
            temp = set_value(matrix[y][x], dst[0]+y*first[1][1]+x )
            if temp is not True:
                return temp
    return temp

# Suma de matrices
def plus_mat_solve(first, second, dst):
    size = 1
    temp = None
    for dim in first[1]:
        size = size * dim
    for x in range(size):

        temp = set_value(get_value(first[0] + x) + get_value(second[0] + x), dst[0] + x )
        if temp is not True:
            return temp
    return temp

# Resta de matrices
def minus_mat_solve(first, second, dst):
    size = 1
    temp = None
    for dim in first[1]:
        size = size * dim
    for x in range(size):
        temp = set_value(get_value(first[0] + x) - get_value(second[0] + x), dst[0] + x )
        if temp is not True:
            return temp
    return temp

# Multiplicacion de matrices
def times_mat_solve(first, second, dst):
    #Aqui hay que hacer lo de multiplicar matrices (solo de 2 dimensiones ó 1 dimensiones)
    result = 0
    temp = None
    for i in range( first[1][0] ):
        for j in range ( second[1][1] ):
            for k in range( first[1][1] ):
                # result += X[i][k] + Y[k][j]
                result = result + get_value(first[0] + i * first[1][0] + k) * get_value(second[0] + k * second[1][0] + j)
            temp = set_value(result, dst[0] + i * first[1][0] + j)
            if temp is not True:
                return temp
    return temp


# Lectura (checar el tipo y lanza error en caso de discrepancias)
def lee_solve(first, second, dst):
    temp = input('patito>')
    var_user = None
    type_var_user = None
    try:
        var_user = ast.literal_eval(temp)
        type_var_user = str(type(var_user))
    except:
        var_user = temp
        if len(temp) == 1:
            type_var_user = "<class \'char\'>"
        else:
            type_var_user = str(type(var_user))

    real_type = "<class \'" + check_type(dst) +"\'>"

    if (type_var_user == "<class \'int\'>" and real_type == "<class \'float\'>"):
        var_user = float(var_user)
        return set_value(var_user, dst)
    elif (type_var_user == "<class \'float\'>" and real_type == "<class \'int\'>"):
        var_user = int(var_user)
        return set_value(var_user, dst)
    elif (type_var_user == "<class \'char\'>" and real_type == "<class \'string\'>"):
        return set_value(var_user, dst)
    elif (type_var_user == real_type):
        return set_value(var_user, dst)
    else:
        return "Error of input type, Expected : " + real_type + " recieved: " + str(type(var_user))

#Escritura a standart ouput
def escribe_solve(first, second, dst):
    print(get_value(dst))
    return True

#Resuelve GOTOF
def gotof_solve(first, second, dst):
    global quad_pointer
    if check_true( get_value(first) ):
        return True
    else:
        quad_pointer = dst
        return False

#Resuelve GOTOV
def gotov_solve(first, second, dst):
    global quad_pointer
    if not check_true( get_value(first) ):
        return True
    else:
        quad_pointer = dst
        return False

# Resuleve GOSUB (Guarda el quad_pointer en jump_stack)
def gosub_solve(first, second, dst):
    global quad_pointer, jump_stack, current_temp_memory
    temp_memory.append(current_temp_memory)
    current_temp_memory = {}  #Created / delete temporal dictionary for param copying
    jump_stack.append(quad_pointer + 1) #Set for return of exectuion
    quad_pointer = dst
    return False

# Mapea el valor de los parametros con el nombre del symbol_table
def param_solve(first, second, dst):
    global temp_memory, current_temp_memory
    e = True
    current_temp_memory[ symbol_table[top(execution_stack)]['param'][dst-1][1] ] = get_value(first)
    return e

# Crea un nuevo ambiente de ejecucion
def era_solve(first, second, dst):
    global execution_stack
    execution_stack.append(first)
    return True

# Regresa el address de la funcion
def return_solve(first, second, dst):
    global global_memory
    e = True
    #Ago trampa aquí no se si sea válido
    global_memory[ symbol_table['global']['vars'][top(execution_stack)]['address'] ] = get_value(dst)
    return e

#Termina la funcion y destruye su memoria de contexto
def endfunc_solve(first, second, dst):
    global temp_memory, jump_stack, quad_pointer
    temp_memory.pop() #destroy context
    execution_stack.pop() #Return context to previous function
    if top(jump_stack):
        quad_pointer = jump_stack.pop() #Return to previuos pointer (not nesesary if in main)
        return False
    return True

#Suma de direcion de matrices
def plus_add_solve(first, second, dst):
    return set_value_for_address( (int) (get_value(first) + get_value(second)), dst)

# Verificación de indices de matrices
def verify_solve(first, second, dst):
    second_val = get_value(dst)
    temp = get_value(first)
    first_val = get_value(second)
    if (temp >= first_val and temp < second_val ):
        return True
    return "Index out of bounds: " + str(temp) + " on (" + str(first_val) + ", " + str(second_val) + ")"
