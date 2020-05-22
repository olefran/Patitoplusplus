#Virtual machine implementation
# Ceasar Buenfil A0120
# Oscar Lerma A01380817

import pprint
from solvers import *

Operations = {
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
 } #TODO: Implement solvers, AND implement matrix based operations

with open("virtualMachine/Output.txt",'r', newline = '\n') as file:
    input = eval(file.read())

# Save elements, nice and easy
const_table = input['const_table']
symbol_table = input['symbol_table']
quadruples = input['quadruples']
print("Symbol Table: ")
pprint.pprint(symbol_table)
print("Const Table: ")
pprint.pprint(const_table)
print("Cuadruples: ")
i = 0
for element in quadruples:
   print( i,": ", element)
   i = i + 1

#Super switch for quad execution
def execute_quad(quadruple):
    result = Operations.get(quadruple[0], -1)
    #Error
    if result == -1:
        e = "Cuadruple instruction not found " + quadruple[0]
    # PLUS_UNARY
    if result == 1:
        pass # TODO Implement unary plus and minus operation
    if result == 2:
        pass #COULD this be implemented as lambda functions?
    pass

def run(input):
  '''Grab the object code file and run it.'''

  quadruples = input['quadruples']
  set_input(input)

  cont = 100
  while not should_end():
    quadruple = quadruples[get_q()]
    print(get_q(), '-', operations[quadruple[0]].__name__, quadruple)
    e = operations[quadruple[0]](quadruple[1], quadruple[2], quadruple[3])
    if e:
      print(e)
      break
    cont -= 1
