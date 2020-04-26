# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Scanner with lex of Patitoplusplus
# Created 04/25/2020
import lex


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

#Build the lexer
lexer = lex.lex()
