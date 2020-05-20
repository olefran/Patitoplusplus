#Virtual machine implementation
# Ceasar Buenfil A0120
# Oscar Lerma A01380817

from .. import structures

with open("Output.txt",'r', newline = '\n') as file:
    input = eval(file.read())

# Save elements, nice and easy
const_table = input['const_table']
symbol_table = input['symbol_table']
quadruples = input['quadruples']

#Super switch for quad execution
def execute_quad(quadruple):
    return None

for quadruple in quadruples:
    e = execute_quad(quadruple)
    if e:
        print("Error:", quadruple,e)
