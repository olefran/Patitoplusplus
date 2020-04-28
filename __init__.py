# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# init file of Patitoplusplus
# Created 04/06/2020
from parser import parser
from scanner import lexer
from quadruples import operand_stack, operator_stack
import sys

# Open file or fail at it, but try to look profesional
data = ""
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


    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)

    result = parser.parse(data)
    print("Errors: ", result)
    print("Operator Stack: ", operator_stack)
    #print("Operand Stack: ", operand_stack)
    return 0

if __name__ == "__main__":
    main()
