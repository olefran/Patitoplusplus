# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Operaciones para virtualMachine
# Created 04/25/2020\
from enum import Enum, IntEnum, auto
from collections import defaultdict
import ast
import pprint

temp_memory = {} # Can temp memory be used as a execution_stack?

global_memory = {}

execution_stack = []

const_table = None

symbol_table = None

quadruples = None

quad_size = 0

quad_pointer = 0

with open("virtualMachine/Output.txt",'r', newline = '\n') as file:
    input = eval(file.read())

const_table = input['const_table']
symbol_table = input['symbol_table']
quadruples = input['quadruples']
quad_size = len(quadruples)

def print_structs():
    print(quad_size)
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
