# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Operaciones para virtualMachine
# Created 04/25/2020\
import pprint

# ========================================================================== #
# Estructuras de Máquina Virtual
# ========================================================================== #

# Arreglo de dicionarios
temp_memory = [{}]

current_temp_memory = {} #Dictionary for ERA declaration

global_memory = {}

execution_stack = ['main']

jump_stack = [] #Used for jumps in era

const_table = None

symbol_table = None

quadruples = None

quad_size = 0

quad_pointer = 0

# Llenado del archibo obj "Output.txt"
with open("virtualMachine/Output.txt",'r', newline = '\n') as file:
    text_file = eval(file.read())

const_table = text_file['const_table']
symbol_table = text_file['symbol_table']
quadruples = text_file['quadruples']
quad_size = len(quadruples)

def print_structs():
    print("Temp Memory: ")
    pprint.pprint(temp_memory)
    print("Global Memory: ")
    pprint.pprint(global_memory)

    print("Symbol Table: ")
    pprint.pprint(symbol_table)
    print("Const Table: ")
    pprint.pprint(const_table)
    print("Quadruples: ")
    i = 0
    for element in quadruples:
       print( i,": ", element)
       i = i + 1
