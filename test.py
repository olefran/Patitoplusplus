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

# Productions
start = 'PROGRAM'

def p_empty(p):
    'empty :'
    pass

# PROGRAMA → programa id ; VAR_AUX FUNCTIONS MAIN
def p_PROGRAM(p):
    'PROGRAM : PROGRAMA ID DOTCOMA VAR_AUX FUNCTIONS MAIN'
    pass

#MAIN → principal ( ) VAR_AUX BLOQUE
def p_MAIN(p):
    'MAIN : PRINCIPAL LPAREN RPAREN VAR_AUX BLOQUE'
    pass

# VAR_AUX → VARS | empty
def p_VAR_AUX(p):
    '''VAR_AUX : VARS
    | empty'''
    pass

#VARS → var VARPRE
def p_VARS(p):
    'VARS : VAR VARPRE'
    pass

#VARPRE → TIPO IDS ; | TIPO IDS ; VARPRE
def p_VARPRE(p):
    '''VARPRE : TIPO IDS DOTCOMA
    | TIPO IDS DOTCOMA VARPRE'''
    pass

#TIPO → int | float | char | string
def p_TIPO(p):
    '''TIPO : INT
    | FLOAT
    | CHAR
    | STRING'''
    pass

# IDS → id ARRDIM ; | id ARRDIM , IDS
def p_IDS(p):
    '''IDS : ID ARRDIM DOTCOMA
    | ID ARRDIM COMA IDS'''
    pass

# ARRDIM → [ EXPRESION ] | [ EXPRESION ] [ EXPRESION ] | empty
def p_ARRDIM(p):
    '''ARRDIM : LSTAPLE EXPRESION RSTAPLE
    | LSTAPLE EXPRESION RSTAPLE LSTAPLE EXPRESION RSTAPLE
    | empty'''
    pass

#FUNCTIONS → FUNCTION FUNCTIONS | empty
def p_FUNCTIONS(p):
    '''FUNCTIONS : FUNCTION FUNCTIONS
    | empty'''
    pass

#FUNCTION → funcion TIPO id ( PARAM ) VAR_AUX BLOQUE | funcion TIPO void ( PARAM ) VAR_AUX BLOQUE
def p_FUNCTION(p):
    '''FUNCTION : FUNCION TIPO ID LBRACKET PARAM RBRACKET VAR_AUX BLOQUE
    | FUNCION TIPO VOID LBRACKET PARAM RBRACKET VAR_AUX BLOQUE'''
    pass

#PARAM → TIPO id PARENTESIS PARAMSUB
def p_PARAM(p):
    '''PARAM : TIPO ID PARENTESIS PARAMSUB'''
    pass

#PARAMSUB → , PARAM  | empty
def p_PARAMSUB(p):
    '''PARAMSUB : COMA PARAM
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

#ESTATUTO → ASIGNACION ; | FUN ; | COND ; | WRITE ; | REAd ; | RETURN ;
def p_ESTATUTO(p):
    '''ESTATUTO : ASIGNACION DOTCOMA
    | FUN DOTCOMA
    | COND DOTCOMA
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

#EXP → TERMINO | TERMINO + TERMINO | TERMINO - TERMINO
def p_EXP(p):
    '''EXP : TERMINO
    | TERMINO PLUS TERMINO
    | TERMINO MINUS TERMINO'''
    pass

#TERMINO → FACTOR | FACTOR * FACTOR | FACTOR / FACTOR | FACTOR % FACTOR
def p_TERMINO(p):
    '''TERMINO : FACTOR
    | FACTOR MULT FACTOR
    | FACTOR DIV FACTOR
    | FACTOR MOD FACTOR'''
    pass

#FACTOR → ( EXPRESION ) | + CTE | - CTE | NOT CTE | ARROP CTE | CTE
def p_FACTOR(p):
    '''FACTOR : LPAREN EXPRESION RPAREN
    | PLUS CTE
    | MINUS CTE
    | NOT CTE
    | ARROP CTE
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
    'IF : SI LPAREN EXPRESION RPAREN ENTONCES BLOQUE SINO IF_AUX'
    pass

#IFAUX → sino BLOQUE | empty
def p_IF_AUX(p):
    '''IF_AUX : SINO BLOQUE
    | empty'''
    pass

#WHILE → mientras ( EXPRESION ) haz BLOQUE
def p_WHILE(p):
    'WHILE :  MIENTRAS LPAREN EXPRESION RPAREN HAZ BLOQUE'
    pass

#FOR → desde ASIGNACION hasta EXPRESION hacer BLOQUE
def p_FOR(p):
    'FOR :  DESDE ASIGNACION HASTA EXPRESION HACER BLOQUE'
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

#Precedence: Build againts ambiguity
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV', 'MOD'),
    ('right', 'EQUAL'),
    ('left', 'AND', 'OR'),
)

#Build the lexer
lexer = lex.lex()

#Build the parser
parser = yacc.yacc()



# Test it out
aux = int(input("1.Programa que cumple\n2.Programa que no cumple\n3.Documento\n"))

data = ""

if(aux == 1):
    data = '''program Example;
var aux1, aux2: float; aux3: int;
{

}'''

elif(aux == 2):
    data = '''programa ~'''

elif(aux == 3):
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

