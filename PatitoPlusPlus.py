# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Lexer and Sintaxis Verification of Patitoplusplus
# Created 04/06/2020
import lex
import yacc

# Language's reserved keywords.
reserved = {
    'programa': 'PROGRAMA',
    'principal': 'PRINCIPAL',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'funcion': 'FUNCION',
    'lee': 'LEE',
    'escribe': 'ESCRIBE',
    'si': 'SI',
    'entonces': 'ENTONCES',
    'sino': 'SINO',
    'regresa': 'REGRESA',
    'mientras': 'MIENTRAS',
    'haz': 'HAZ',
    'desde': 'DESDE',
    'hasta': 'HASTA',
    'hacer': 'HACER',
    'string': 'STRING',
    'null': 'NULL',
    'void': 'VOID',
}

#Tokens
tokens = [
    'ID', 'DOTCOMA', 'LBRACKET', 'RBRACKET', 'EQUAL', 'MORE', 'LESS',
    'DIFFERENT', 'LPAREN', 'RPAREN', 'COMA', 'CTE_STRING',
    'PLUS', 'MINUS', 'MULT', 'DIV', 'CTE_I', 'CTE_F', 'CTE_CH',
    'NOT', 'AND', 'OR', 'COMPARE', 'MOD', 'TRANS_ARR', 'INV_ARR', 'DET_ARR',
    'COMMENT', 'MOREEQUAL', 'LESSEQUAL', 'LSTAPLE', 'RSTAPLE'
    ] + list(reserved.values())

t_DOTCOMA   = r';'
t_LBRACKET  = r'{'
t_RBRACKET  = r'}'
t_EQUAL     = r'='
t_MORE      = r'>'
t_LESS      = r'<'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COMA      = r'\,'
t_CTE_CH    = r'\'[A-Za-z]\''
t_CTE_STRING= r'".*."'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULT      = r'\*'
t_DIV       = r'/'
t_CTE_I     = r'[0-9][0-9]*'
t_CTE_F     = r'(\+|-)?[0-9]+(\.[0-9]+)?f' #Modified "f" at the end, and '+' on digit part
t_AND       = r'&&'
t_OR        = r'\|\|'
t_COMPARE   = r'=='
t_MOREEQUAL = r'>='
t_LESSEQUAL = r'<='
t_TRANS_ARR = r'¡'
t_DET_ARR   = r'\$'
t_MOD       = r'%'
t_NOT       = r'!'
t_INV_ARR   = r'\?'
t_DIFFERENT = r'!='
t_LSTAPLE   = r'\['
t_RSTAPLE   = r'\]'
t_ignore_COMMENT = r'%%.*'

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  # Check if matched id is a reserved keyword.
  t.type = reserved.get(t.value, 'ID')
  return t

#Current variables and Symbol Table
current_type = ''
current_func = ''
current_var = ''
symbol_table = {}

# Productions
start = 'PROGRAM'

def p_empty(p):
    'empty :'
    pass

# PROGRAMA → programa id ;  VARS FUNCTIONS MAIN
def p_PROGRAM(p):
    'PROGRAM : PROGRAMA ID DOTCOMA VARS FUNCTIONS MAIN'
    print(symbol_table)

#MAIN → principal ( )  VARS BLOQUE
def p_MAIN(p):
    'MAIN : PRINCIPAL r_save_func LPAREN RPAREN VARS r_register_func BLOQUE'
    pass

#VARS → var VARPRE | empty
def p_VARS(p):
    '''VARS : VAR VAR_AUX
    | empty'''
    pass

#empty?
#VARPRE → TIPO IDS VARPRE | empty
def p_VAR_AUX(p):
    '''VAR_AUX : TIPO IDS VAR_AUX
    | empty'''
    pass

#TIPO → int | float | char | string
def p_TIPO(p):
    '''TIPO : INT r_save_type
    | FLOAT r_save_type
    | CHAR r_save_type
    | STRING r_save_type'''
    pass

# IDS → id ARRDIM ; | id ARRDIM , IDS
def p_IDS(p):
    '''IDS : ID r_register_var ARRDIM DOTCOMA
    | ID r_register_var ARRDIM COMA IDS'''
    pass

# ARRDIM → [ EXPRESION ] | [ EXPRESION ] [ EXPRESION ] | [ EXPRESION , EXPRESION ] | empty
def p_ARRDIM(p):
    '''ARRDIM : LSTAPLE EXPRESION RSTAPLE
    | LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE
    | LSTAPLE EXPRESION COMA EXPRESION RSTAPLE
    | empty'''
    pass

#FUNCTIONS → FUNCTION FUNCTIONS | empty
def p_FUNCTIONS(p):
    '''FUNCTIONS : FUNCTION FUNCTIONS
    | empty'''
    pass

#FUNCTION → funcion TIPO id ( PARAM )  VARS BLOQUE | funcion void id ( PARAM )  VARS BLOQUE
def p_FUNCTION(p):
    '''FUNCTION : FUNCION TIPO ID r_save_func LPAREN PARAM RPAREN VARS r_register_func BLOQUE
    | FUNCION VOID r_save_type ID r_save_func LPAREN PARAM RPAREN VARS r_register_func BLOQUE'''
    pass

#PARAM → TIPO id PARENTESIS PARAMSUB
def p_PARAM(p):
    '''PARAM : TIPO ID r_register_var PARENTESIS PARAM_AUX'''
    pass

#PARAM_AUX → , PARAM  | empty
def p_PARAM_AUX(p):
    '''PARAM_AUX : COMA PARAM
    | empty'''
    pass

#PARENTESIS → [ ] | [ ] [ ] | empty
def p_PARENTESIS(p):
    '''PARENTESIS : LSTAPLE RSTAPLE
    | LSTAPLE RSTAPLE LSTAPLE RSTAPLE
    | empty'''
    pass

#BLOQUE → { ESTATUTOS }
def p_BLOQUE(p):
    'BLOQUE : LBRACKET ESTATUTOS RBRACKET'
    pass

#ESTATUTOS → ESTATUTO ESTATUTOS | empty
def p_ESTATUTOS(p):
    '''ESTATUTOS : ESTATUTO ESTATUTOS
    | empty'''
    pass

#ESTATUTO → ASIGNACION ; | FUN ; | COND | WRITE ; | REAd ; | RETURN ;
def p_ESTATUTO(p):
    '''ESTATUTO : ASIGNACION DOTCOMA
    | FUN DOTCOMA
    | COND
    | WRITE DOTCOMA
    | READ DOTCOMA
    | RETURN DOTCOMA'''
    pass

#ASIGNACION → id ARRDIM = EXPRESION | id ARRDIM = CTE_ARR
def p_ASIGNACION(p):
    '''ASIGNACION : ID ARRDIM EQUAL EXPRESION
    | ID ARRDIM EQUAL CTE_ARR'''
    pass

#EXPRESION → SUBEXP && SUBEXP | SUBEXP || SUBEXP | SUBEXP
def p_EXPRESION(p):
    '''EXPRESION : SUBEXP AND SUBEXP
    | SUBEXP OR SUBEXP
    | SUBEXP'''
    pass

#SUBEXP → EXP | EXP COMPARACION EXP
def p_SUBEXP(p):
    '''SUBEXP : EXP
    | EXP COMPARACION EXP'''
    pass

#COMPARACION → > | < | == | != | >= | <=
def p_COMPARACION(p):
    '''COMPARACION : MORE
    | LESS
    | COMPARE
    | DIFFERENT
    | MOREEQUAL
    | LESSEQUAL'''
    pass

#EXP → TERMINO | TERMINO + EXP | TERMINO - EXP
def p_EXP(p):
    '''EXP : TERMINO
    | TERMINO PLUS EXP
    | TERMINO MINUS EXP'''
    pass

#TERMINO → FACTOR | FACTOR * TERMINO | FACTOR / TERMINO | FACTOR % TERMINO
def p_TERMINO(p):
    '''TERMINO : FACTOR
    | FACTOR MULT TERMINO
    | FACTOR DIV TERMINO
    | FACTOR MOD TERMINO'''
    pass

#FACTOR → ( EXPRESION ) | + CTE | - CTE | NOT CTE | CTE ARROP | CTE
def p_FACTOR(p):
    '''FACTOR : LPAREN EXPRESION RPAREN
    | PLUS CTE
    | MINUS CTE
    | NOT CTE
    | CTE ARROP
    | CTE'''
    pass

#CTE → cte_i | cte_f | ct_ch | cte_string | FUN | ID ARRDIM
def p_CTE(p):
    '''CTE : CTE_I
    | CTE_F
    | CTE_CH
    | CTE_STRING
    | FUN
    | ID ARRDIM'''
    pass

#ARROP→ $ | ! | ?
def p_ARROP(p):
    '''ARROP : DET_ARR
    | TRANS_ARR
    | INV_ARR'''
    pass

#FUN → id ( FUN_AUX )
def p_FUN(p):
    'FUN : ID LPAREN FUN_AUX RPAREN'
    pass

#FUN_AUX → CTE , FUN_AUX | CTE
def p_FUN_AUX(p):
    '''FUN_AUX : EXPRESION COMA FUN_AUX
    | EXPRESION
    | empty'''
    pass

#COND → IF | FOR | WHILE
def p_COND(p):
    '''COND : IF
    | FOR
    | WHILE'''
    pass

#IF → si ( EXPRESION ) entonces BLOQUE IF_AUX
def p_IF(p):
    '''IF : SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE IF_AUX
    | SI LPAREN EXPRESION RPAREN ENTONCES COND '''
    pass

#IFAUX → sino BLOQUE | empty
def p_IF_AUX(p):
    '''IF_AUX : SINO BLOQUE
    | empty'''
    pass

#WHILE → mientras ( EXPRESION ) WHILE_AUX BLOQUE
def p_WHILE(p):
    '''WHILE :  MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX BLOQUE
    | MIENTRAS LPAREN EXPRESION RPAREN WHILE_AUX COND'''
    pass

#WHILE_AUX → haz | empty
def p_WHILE_AUX(p):
    '''WHILE_AUX :  HAZ
    | empty '''
    pass

#FOR → desde ASIGNACION hasta EXPRESION hacer BLOQUE
def p_FOR(p):
    '''FOR :  DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE
    | DESDE ASIGNACION HASTA EXPRESION HACER COND'''
    pass

#WRITE → escribe ( WRITE_AUX )
def p_WRITE(p):
    'WRITE : ESCRIBE LPAREN WRITE_AUX RPAREN'
    pass

#WRITE_AUX → EXPRESION WRITE_AUXSUB
def p_WRITE_AUX(p):
    'WRITE_AUX : EXPRESION WRITE_AUXSUB'
    pass

#WRITE_AUXSUB → , WRITE_AUX | empty
def p_WRITE_AUXSUB(p):
    '''WRITE_AUXSUB : COMA WRITE_AUX
    | empty'''
    pass

#READ → lee ( READ_AUX )
def p_READ(p):
    'READ : LEE LPAREN READ_AUX RPAREN'
    pass

#READ_AUX → id ARRDIM READ_AUXSUB
def p_READ_AUX(p):
    'READ_AUX : ID ARRDIM READ_AUXSUB'
    pass

#READ_AUXSUB →, READ_AUX | empty
def p_READ_AUXSUB(p):
    '''READ_AUXSUB : COMA READ_AUX
    | empty'''
    pass

#RETURN → regresa ( EXPRESION ) regresa ( NULL )
def p_RETURN(p):
    '''RETURN : REGRESA LPAREN EXPRESION RPAREN
    | REGRESA LPAREN NULL RPAREN'''
    pass

#CTE_ARR → { CTE_ARR_AUX } | { CTE_ARR_AUX2 }
def p_CTE_ARR(p):
    '''CTE_ARR : LBRACKET CTE_ARR_AUX RBRACKET
    | LBRACKET CTE_ARR_AUX2 RBRACKET '''
    pass

#CTE_ARR_AUX → CTE | CTE_ARR_AUXSUB
def p_CTE_ARR_AUX(p):
    '''CTE_ARR_AUX : CTE
    | CTE_ARR_AUXSUB '''
    pass

#CTE_ARR_AUXSUB →, CTE_ARR_AUX | empty
def p_CTE_ARR_AUXSUB(p):
    '''CTE_ARR_AUXSUB : COMA CTE_ARR_AUX
    | empty '''
    pass

#CTE_ARR_AUX2 → { CTE_ARR_AUX } CTE_ARR_AUX2SUB
def p_CTE_ARR_AUX2(p):
    'CTE_ARR_AUX2 : LBRACKET CTE_ARR_AUX RBRACKET  CTE_ARR_AUX2SUB'
    pass

#CTE_ARR_AUX2SUB → , CTE_ARR_AUX2  | empty
def p_CTE_ARR_AUX2SUB(p):
    '''CTE_ARR_AUX2SUB : COMA CTE_ARR_AUX2
    | empty '''
    pass


#Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#A string containing ignored characters
t_ignore = ' \t'

#Error handling rule for lexer
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")

#Precedence: Build againts ambiguity
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV', 'MOD'),
    ('right', 'EQUAL'),
    ('left', 'AND', 'OR'),
)

#DirFunctions
def p_r_save_type(p):
    'r_save_type : '
    global current_type
    current_type = p[-1]

def p_r_save_func(p):
    'r_save_func : '
    global current_func
    current_func = p[-1]

def p_r_register_func(p):
    'r_register_func : '
    global symbol_table
    symbol_table[current_func] = {
        'type': current_type,
        'vars': {}
    }

def p_r_register_var(p):
    'r_register_var : '
    global current_var
    current_var = p[-1]
    global symbol_table
    symbol_table[current_func]['vars'][current_var] = {
        'type': current_type,
    }



#Build the lexer
lexer = lex.lex()

#Build the parser
parser = yacc.yacc()



# Test it out
aux = int(input("1.Ingrese Programa\n2.Documento Prueba\n"))

data = ""

if(aux == 1):
    f = open(input("Ingrese el nombre del programa: "), "r")
    if f.mode == 'r':
        data = f.read()
        f.close()
    else:
        print("Error: input File not found or redable")

elif(aux == 2):
    f = open("example.duckpp", "r")
    if f.mode == 'r':
        data = f.read()
        f.close()
    else:
        print("Error: input File not found or redable")


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
