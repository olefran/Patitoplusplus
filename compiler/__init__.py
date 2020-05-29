# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# init file de Patitoplusplus
# Created 04/06/2020
from parser import parser, error
from scanner import lexer
from structures import *
from semantics import symbol_table, const_table
import sys
import pprint

# Para buscar y abrir un file con el programa
data = ""

def debugging(result):
    # Debbuging
    print("Errors: ", result)
    print("Operator Stack: ", operator_stack) #Error saves not operators
    print("Operand Stack: ", operand_stack) #Error none
    print("Symbol Table: ")
    pprint.pprint(symbol_table)
    print("Const Table: ")
    pprint.pprint(const_table)
    print("Cuadruples: ")
    i = 0
    for element in quadruples:
       print( i,": ", element)
       i = i + 1


def main():
    if(len(sys.argv) == 2):
        try:
            f = open(sys.argv[1], "r")
        except:
            print("File not found: " + sys.argv[1])
            return -1
        if f.mode == 'r':
            data = f.read()
            f.close()
        else:
            print("Error: File " + sys.argv[1] + " is not redable")
            return -1
    else:
        print("Usage: " + sys.argv[0] + " file")
        return -1

    # Dar el input al lexer
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
    result = parser.parse(data)

    debugging(result)

    if error:
        sys.exit(1)
    else:
        print("Succesful compilation, passing to execution.")
        sys.exit(0)

# Correr el main
if __name__ == "__main__":
    main()
