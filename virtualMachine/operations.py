# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Operaciones para virtualMachine
# Created 04/25/2020
from structures import *
import ast

def top(l):
  if len(l) > 0:
    return l[-1]
  return None

def get_pointer():
    global quad_pointer
    return quad_pointer

def set_pointer(value):
    global quad_pointer
    quad_pointer = value

def check_true(input):
    return not input == 0

def get_bool_int(input):
    if input == False:
        return 0
    else:
        return 1

#This is an ugly function, made by an ugly guy,
#i blame not one but myself for the idea, jesus i hate this function
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

def goto_solve(first, second, dst):
    global quad_pointer
    quad_pointer = dst
    return False

def plus_unary_solve(first, second, dst):
    return set_value(+get_value(first),dst)

def minus_unary_solve(first, second, dst):
    return set_value(-get_value(first), dst)

def not_unary_solve(first, second, dst):
    temp = None
    if check_true( get_value(first) ):
        temp = 0
    else:
        temp = 1
    return set_value(temp, dst)
    # return set_value( get_bool_int( not check_true(first) ), dst )

def times_solve(first, second, dst):
    return set_value( get_value(first) * get_value(second), dst)

def divide_solve(first, second, dst):
    return set_value( get_value(first) / get_value(second), dst)

def mod_solve(first, second, dst):
    return set_value( get_value(first) % get_value(second), dst)

def plus_solve(first, second, dst):
    return set_value( get_value(first) + get_value(second), dst)

def minus_solve(first, second, dst):
    return set_value( get_value(first) - get_value(second), dst)

def less_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) < get_value(second) ), dst )

def more_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) > get_value(second) ), dst )

def different_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) != get_value(second) ), dst )

def comparison_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) == get_value(second) ), dst )

def less_than_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) <= get_value(second) ), dst )

def more_than_solve(first, second, dst):
    return set_value( get_bool_int( get_value(first) >= get_value(second) ), dst )

def or_solve(first, second, dst):
    temp = check_true( get_value(first) ) or check_true( get_value(second) )
    return set_value( get_bool_int( temp ), dst )

def and_solve(first, second, dst):
    temp = check_true( get_value(first) ) and check_true( get_value(second) )
    return set_value( get_bool_int( temp ), dst )

def equal_solve(first, second, dst):
    return set_value(get_value(first), dst)

def equal_mat_solve(first, second, dst):
    for x in range(first[1]):
        temp = set_value(get_value(first[0] + x), dst[0] + x )
        if temp is not True:
            return temp
    return temp
    #Aqui hay que hacer lo de igualar matrices

def det_mat_solve(first, second, dst):
    #Aqui hay que hacer lo de igualar matrices
    return set_value(get_value(first), dst)

def trans_mat_solve(first, second, dst):
    #Aqui hay que hacer lo de igualar matrices
    return set_value(get_value(first), dst)

def inv_mat_solve(first, second, dst):
    #Aqui hay que hacer lo de igualar matrices
    return set_value(get_value(first), dst)

def plus_mat_solve(first, second, dst):
    #Aqui hay que hacer lo de igualar matrices
    for x in range(first[1]):
        temp = set_value(get_value(first[0] + x) + get_value(second[0] + x), dst[0] + x )
        if temp is not True:
            return temp
    return temp

def minus_mat_solve(first, second, dst):
    #Aqui hay que hacer lo de igualar matrices
    for x in range(first[1]):
        temp = set_value(get_value(first[0] + x) - get_value(second[0] + x), dst[0] + x )
        if temp is not True:
            return temp
    return temp

#Does not distingish between a char and a string
#Also this is a dumb way to check types, jesus
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

def escribe_solve(first, second, dst):
    print(get_value(dst))
    return True

def gotof_solve(first, second, dst):
    global quad_pointer
    if check_true( get_value(first) ):
        return True
    else:
        quad_pointer = dst
        return False

def gotov_solve(first, second, dst):
    global quad_pointer
    if not check_true( get_value(first) ):
        return True
    else:
        quad_pointer = dst
        return False

def gosub_solve(first, second, dst):
    global quad_pointer, jump_stack, current_temp_memory
    temp_memory.append(current_temp_memory)
    current_temp_memory = {}  #Created / delete temporal dictionary for param copying
    jump_stack.append(quad_pointer + 1) #Set for return of exectuion
    quad_pointer = dst
    return False

#TODO: Save the real parameter values
def param_solve(first, second, dst):
    global temp_memory, current_temp_memory
    e = True
    current_temp_memory[ symbol_table[top(execution_stack)]['param'][dst-1][1] ] = get_value(first)
    return e

#TODO: Use the size of the function somewhere
def era_solve(first, second, dst):
    global execution_stack
    execution_stack.append(first)
    return True


def return_solve(first, second, dst):
    global global_memory
    e = True
    #Ago trampa aquí no se si sea válido
    global_memory[ symbol_table['global']['vars'][top(execution_stack)]['address'] ] = get_value(dst)
    return e

def endfunc_solve(first, second, dst):
    global temp_memory, jump_stack, quad_pointer
    #temp_memory.pop() #destroy context
    execution_stack.pop() #Return context to previous function
    if top(jump_stack):
        quad_pointer = jump_stack.pop() #Return to previuos pointer (not nesesary if in main)
        return False
    return True

#What is this function?!
def end_solve(first, second, dst):
    return True

def plus_add_solve(first, second, dst):
    return set_value_for_address( (int) (get_value(first) + get_value(second)), dst)


def verify_solve(first, second, dst):
    temp = get_value(dst)
    first_val = get_value(first)
    second_val = get_value(second)
    if (temp >= first_val and temp > second_val ):
        return True
    return "Index out of bounds: " + str(temp) + " on (" + str(first_val) + ", " + str(second_val) + ")"
