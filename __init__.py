# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# init file of Patitoplusplus
# Created 04/06/2020
from parser import parser
from scanner import lexer
import sys

# Test it out
#aux = int(input("1.Ingrese Programa\n2.Documento Prueba\n"))

data = ""
def main():
    if(len(sys.argv) == 2):
        f = open(sys.argv[1], "r")
        if f.mode == 'r':
            data = f.read()
            f.close()
        else:
            print("Error: File" + sys.argv[1] + "not found or redable")
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
    return 0

if __name__ == "__main__":
    main()
