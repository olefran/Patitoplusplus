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

# print("Symbol Table: ")
# pprint.pprint(symbol_table)
# print("Const Table: ")
# pprint.pprint(const_table)
# pprint.pprint(quadruples)
# i = 0
# for element in quadruples:
#    print( i,": ", element)
#    i = i + 1


def main():
  '''Grab the object code file and run it.'''
  global const_table, symbol_table, quadruples, quad_size, quad_pointer
  with open("virtualMachine/Output.txt",'r', newline = '\n') as file:
      input = eval(file.read())

  const_table = input['const_table']
  symbol_table = input['symbol_table']
  quadruples = input['quadruples']
  quad_size = len(quadruples)

  pprint.pprint(const_table)

  #Execute the quadruples one by one
  while quad_pointer < quad_size:
    e = operations[quadruple[quad_pointer][0]](quadruple[quad_pointer][1], quadruple[quad_pointer][2], quadruple[quad_pointer][3])

    if e == True:
      quad_pointer = quad_pointer + 1
    elif e == False:
        pass #DO NOT ADD TO QUAD POINTER
    elif e:
        print("Error on quad:" + quad_pointer + ": " + e)
        break

# Correr el main
if __name__ == "__main__":
    main()
