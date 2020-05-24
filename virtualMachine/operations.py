# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Operaciones para virtualMachine
# Created 04/25/2020
from structures import *

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
        else:
            top(temp_memory)[dir] = value
    except:
        e = "Error on assingning value " + value + " to dir " + dir
    return e

def goto_solve(first, second, dst):
    global quad_pointer
    quad_pointer = dst
    return False

def plus_unary_solve(first, second, dst):
    return set_value(+get_value(first),dst)

def minus_unary_solve(first, second, dst):
    return set_value(-get_value(first), dst)

def not_unary_solve(fist, second, dst):
    temp = None
    if check_true( get_value(first) ):
        temp = 0
    else:
        temp = 1
    return set_value(temp, dst)
    # return set_value( get_bool_int( not check_true(first) ), dst )

def times_solve(first, second, dst):
    return set_value( get_value(first) * get_value(second), dst)

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

def lee_solve(first, second, dst):
    temp = input() #NEED TO CHECK TYPE!!!!!
    return set_value(temp, dst)

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

def gosub_solve(first, second, dst):
    global quad_pointer, jump_stack
    jump_stack.append(quad_pointer + 1) #Set for return of exectuion
    quad_pointer = dst
    return False

def param_solve(first, second, dst):
    return

def era_solve(first, second, dst):
    global temp_memory, execution_stack
    temp_memory.append({}) # Not naming these could get confusing for debugging (memory context for functions)
    execution_stack.append(first)
    return

def return_solve(first, second, dst):
    return

def endfunc_solve(first, second, dst):
    global temp_memory, jump_stack
    #temp_memory.pop() #destroy context
    if top(jump_stack):
        quad_pointer = jump_stack.pop() #Return to previuos pointer
        execution_stack.pop() #Return context to previous function
        return False
    return True

def end_solve(first, second, dst):
    return

def fake_bottom_solve(first, second, dst):
    return

def verify_solve(first, second, dst):
    return
