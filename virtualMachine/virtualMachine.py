#Virtual machine implementation
# Ceasar Buenfil A01207499
# Oscar Lerma A01380817

import pprint
from operations import *
import ast

# ========================================================================== #
# Matrix de operaciones
# ========================================================================== #

operations = {
    "unary+" : plus_unary_solve,
    "unary-" : minus_unary_solve,
    "!" : not_unary_solve,
    "*" : times_solve,
    "/" : divide_solve,
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
    "LEE" : lee_solve, #Lee varias
    "ESCRIBE" : escribe_solve, #Escribe varias
    "GOTO" : goto_solve,
    "GOTOF" : gotof_solve,
    "GOTOV" : gotov_solve,
    "GOSUB" : gosub_solve,
    "PARAM" : param_solve,
    "ERA" : era_solve,
    "RETURN" : return_solve,
    "ENDFunc" : endfunc_solve,
    "END" : end_solve,
    "VER" : verify_solve,
    "+dir" : plus_add_solve,
    "=mat" : equal_mat_solve,
    "$" : det_mat_solve,
    "¡" : trans_mat_solve,
    "?" : inv_mat_solve,
    "+mat" : plus_mat_solve,
    "-mat" : minus_mat_solve,
    "*mat" : times_mat_solve,
    "unary+mat": plus_unary_mat_solve,
    "unary-mat": minus_unary_mat_solve
 }

# Ejecuta los cuadruplos desde  un quad point = 0
def main():
  '''Grab the object code file and run it.'''
  global quad_size, quadruples
  #Executa cuadruplos uno por uno
  quad_pointer = 0
  while quad_pointer < quad_size:
      e = operations[quadruples[quad_pointer][0]](quadruples[quad_pointer][1], quadruples[quad_pointer][2], quadruples[quad_pointer][3])
      # print(quadruples[quad_pointer][0], quadruples[quad_pointer][1], quadruples[quad_pointer][2], quadruples[quad_pointer][3])
      if e == True:
          set_pointer(quad_pointer+1)
      elif e is not None and e is not False:
          print("Error on quad:", quad_pointer, ": ", e)
          break
      quad_pointer = get_pointer()
  #print_structs()

# Correr el main
if __name__ == "__main__":
    main()
