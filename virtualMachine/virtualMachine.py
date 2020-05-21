#Virtual machine implementation
# Ceasar Buenfil A0120
# Oscar Lerma A01380817

from structures import Operations

with open("Output.txt",'r', newline = '\n') as file:
    input = eval(file.read())

# Save elements, nice and easy
const_table = input['const_table']
symbol_table = input['symbol_table']
quadruples = input['quadruples']

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

def run():
    for quadruple in quadruples:
        e = execute_quad(quadruple)
        if e:
            print("Error:", quadruple,e)
