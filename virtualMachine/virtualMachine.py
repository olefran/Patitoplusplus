#Virtual machine implementation
# Ceasar Buenfil A0120
# Oscar Lerma A01380817

import pprint
from operations import *

operations = {
    "+unary" : plus_unary_solve,
    "-unary" : minus_unary_solve,
    "!" : not_unary_solve,
    "*" : times_solve,
    "%" : mod_solve,
    "+" : plus_solve,
    "-" : minus_solve,
    "<" : less_solve,
    ">" : more_solve,
    "!=" : different_solve,
    "==" : comparison_solve,
    "<=" : less_than_solve,
    ">=" : more_than_solve,
    "||" : or_solve,
    "&&" : and_solve,
    "=" : equal_solve,
    "LEE" : lee_solve,
    "ESCRIBE" : escribe_solve,
    "GOTO" : goto_solve,
    "GOTOF" : gotof_solve,
    "GOSUB" : gosub_solve,
    "PARAM" : param_solve,
    "ERA" : era_solve,
    "RETURN" : return_solve,
    "ENDFunc" : endfunc_solve,
    "END" : end_solve,
    "FAKE_BOTTOM" : fake_bottom_solve,
    "VER" : verify_solve
 } #TODO: Implement functions, AND implement matrix based operations

def main():
  '''Grab the object code file and run it.'''
  global quad_pointer, quad_size, quadruples

  print_structs()

  #Execute the quadruples one by one
  while quad_pointer < quad_size:
      e = operations[quadruples[quad_pointer][0]](quadruples[quad_pointer][1], quadruples[quad_pointer][2], quadruples[quad_pointer][3])
      if e == True:
          quad_pointer = quad_pointer + 1
      elif e is not None and e is not False:
          print("Error on quad:", quad_pointer, ": ", e)
          break

# Correr el main
if __name__ == "__main__":
    main()
