# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Scanner with lex of Patitoplusplus
# Created on 04/25/2020
# ========================================================================== #
# Scanner.py
# ========================================================================== #
import lex
import math

# Palabras reservadas
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

# Tokens
tokens = [
    'ID', 'DOTCOMA', 'LBRACKET', 'RBRACKET', 'EQUAL', 'MORE', 'LESS',
    'DIFFERENT', 'LPAREN', 'RPAREN', 'COMA', 'CTE_STRING',
    'PLUS', 'MINUS', 'MULT', 'DIV', 'CTE_I', 'CTE_F', 'CTE_CH',
    'NOT', 'AND', 'OR', 'COMPARE', 'MOD', 'TRANS_ARR', 'INV_ARR', 'DET_ARR',
    'COMMENT', 'MOREEQUAL', 'LESSEQUAL', 'LSTAPLE', 'RSTAPLE'
    ] + list(reserved.values())

# Definición de Tokens
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

# Función para comentarios
def t_COMMENT(t):
     r'\%%.*'
     pass

# Función que diferencia tokens de constantes de int y float
def t_CTE_F(t):
  r'([0-9]*[.])?[0-9]+'
  if int(math.floor(float(t.value))) == float(t.value):
    t.value = int(t.value)
    t.type = 'CTE_I'
  else:
    t.value = float(t.value)
  return t

# Función para tokens de id
def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  # Checar si es una palabra reservada
  t.type = reserved.get(t.value, 'ID')
  return t

# Función de contador de nuevas líneas
def t_newline(t):
    r'[\n]+'
    t.lexer.lineno += t.value.count("\n")


# Ignorar los tabs
t_ignore = ' \t'

# Función para errores en el lexer
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el Lexer
lexer = lex.lex()
