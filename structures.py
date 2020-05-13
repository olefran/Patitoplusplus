# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Estructuras de datos de Patitoplusplus
# Created 04/06/2020
from enum import Enum, IntEnum, auto
from collections import defaultdict

#Stack de Operaciones
operator_stack = []

# Stack para operandos
# Pila0
# Guarda typo y nombre
operand_stack = []

#Stack de salto durante ejecucion
jump_stack = []

# Generated quadruples
quadruples = []
quad_pointer = 0

# Variables Auxiliares para currents
current_type = None
current_func = 'global' # Scope
current_var = ''

# Directorio de funciones y sus variables
symbol_table = {
        'global' : {
            'vars' : {}
        }
}

# Directorio de constantes
const_table = {}

# Operador Temporal de for
temp_for_op = None

# Limites de memoria virtual
# Gracias a la siguiente configuración, solo pueden existir un total de 1500 variables de un tipo
# VARIABLES GLOBALES    INT     FLOAT   CHAR    STRINGS  VOID
GLOBAL_LOWER_LIMIT =    [5_000, 6_500, 8_000, 9_500, 11_000]
GLOBAL_UPPER_LIMIT =    [6_499, 7_999, 9_499, 10_999, 12_499]

# VAR DE FUNCIONES      INT     FLOAT   CHAR    STRINGS
VAR_LOWER_LIMIT =       [13_000, 14_500, 16_000, 17_500]
VAR_UPPER_LIMIT =       [14_499, 15_999, 17_499, 18_999]

# CONSTANTES            INT     FLOAT   CHAR    STRINGS
CONST_LOWER_LIMIT =     [19_000, 20_500, 22_000, 23_500]
CONST_UPPER_LIMIT =     [20_499, 21_999, 23_499, 24_999]

# TEMPORALES            INT     FLOAT   CHAR    STRINGS
TEMP_LOWER_LIMIT =      [25_000, 26_500, 28_000, 29_500]
TEMP_UPPER_LIMIT =     [26_499, 27_999, 29_499, 30_999]

#CONSTANT_UPPER_LIMIT = 30_999

# Contadores de memoria virutal
global_dir_count = list(GLOBAL_LOWER_LIMIT)
var_dir_count = list(VAR_LOWER_LIMIT)
temp_dir_count = list(TEMP_LOWER_LIMIT)
const_dir_count = list(CONST_LOWER_LIMIT)

# Enumeracion de tipos de datos
var_types = ('int', 'float', 'char', 'string')
avail_types = ('int', 'float', 'char', 'string', 'void')
func_types = ('int', 'float', 'char', 'string', 'void')

# Diccionario de Operaciones
str_operations = ('unary+','unary-','!','*','/','+','-','<','>','!=','==','<=','>=','||','&&','=','(','%')
Operations = {
  "PLUS_UNARY" : 1,
  "MINUS_UNARY" : 2,
  "NOT" : 3,
  "TIMES" : 4,
  "DIV" : 5,
  "PLUS" : 6,
  "MINUS" : 7,
  "LESS_THAN" : 8,
  "MORE_THAN" : 9,
  "DIFFERENT" : 10,
  "IS_EQUAL" : 11,
  "LESS_EQUAL" : 12,
  "MORE_EQUAL" : 13,
  "OR" : 14,
  "AND" : 15,
  "EQUAL" : 16,
  "LEE" : 17,
  "WRITE" : 18,
  "GOTO" : 19,
  "GOTOF" : 20,
  "GOSUB" : 21,
  "PARAM" : 22,
  "ERA" : 23,
  "RETURN" : 24,
  "ENDPROC" : 25,
  "END" : 26,
  "ENTER_INSTANCE" : 27,
  "EXIT_INSTANCE" : 28,
  "GET_RETURN" : 29,
  "FAKE_BOTTOM" : 30,
  "VER" : 31,
  "SET_FOREIGN" : 32,
  "UNSET_FOREIGN" : 33,
  "MOD" : 34
 }

# Semantic cube for Operations
semantic_cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

semantic_cube['int']['int']['&&'] = 'int'
semantic_cube['int']['int']['||'] = 'int'
semantic_cube['int']['int']['<'] = 'int'
semantic_cube['int']['int']['>'] = 'int'
semantic_cube['int']['int']['!='] = 'int'
semantic_cube['int']['int']['=='] = 'int'
semantic_cube['int']['int']['<='] = 'int'
semantic_cube['int']['int']['>='] = 'int'
semantic_cube['int']['int']['+'] = 'int'
semantic_cube['int']['int']['-'] = 'int'
semantic_cube['int']['int']['*'] = 'int'
semantic_cube['int']['int']['/'] = 'int'
semantic_cube['int']['int']['='] = 'int'
semantic_cube['int']['lee']['='] = 'int'
semantic_cube['int']['unary+'] = 'int'
semantic_cube['int']['unary-'] = 'int'
semantic_cube['int']['!'] = 'int'

semantic_cube['float']['float']['&&'] = 'int'
semantic_cube['float']['float']['||'] = 'int'
semantic_cube['float']['float']['<'] = 'int'
semantic_cube['float']['float']['>'] = 'int'
semantic_cube['float']['float']['!='] = 'int'
semantic_cube['float']['float']['=='] = 'int'
semantic_cube['float']['float']['<='] = 'int'
semantic_cube['float']['float']['>='] = 'int'
semantic_cube['float']['float']['+'] = 'float'
semantic_cube['float']['float']['-'] = 'float'
semantic_cube['float']['float']['*'] = 'float'
semantic_cube['float']['float']['/'] = 'float'
semantic_cube['float']['float']['='] = 'float'
semantic_cube['float']['lee']['='] = 'float'
semantic_cube['float']['unary+'] = 'float'
semantic_cube['float']['unary-'] = 'float'
semantic_cube['float']['!'] = 'int'

semantic_cube['char']['char']['&&'] = 'int'
semantic_cube['char']['char']['||'] = 'int'
semantic_cube['char']['char']['<'] = 'int'
semantic_cube['char']['char']['>'] = 'int'
semantic_cube['char']['char']['!='] = 'int'
semantic_cube['char']['char']['=='] = 'int'
semantic_cube['char']['char']['>='] = 'int'
semantic_cube['char']['char']['<='] = 'int'
semantic_cube['char']['char']['+'] = 'char'
semantic_cube['char']['char']['-'] = 'char'
semantic_cube['char']['char']['*'] = 'char'
semantic_cube['char']['char']['/'] = 'char'
semantic_cube['char']['char']['='] = 'char'
semantic_cube['char']['lee']['='] = 'char'
semantic_cube['char']['unary+'] = None
semantic_cube['char']['unary-'] = None
semantic_cube['char']['!'] = 'char'

semantic_cube['int']['float']['&&'] = semantic_cube['float']['int']['&&'] = 'int'
semantic_cube['int']['float']['||'] = semantic_cube['float']['int']['||'] = 'int'
semantic_cube['int']['float']['<'] = semantic_cube['float']['int']['<'] = 'int'
semantic_cube['int']['float']['>'] = semantic_cube['float']['int']['>'] = 'int'
semantic_cube['int']['float']['!='] = semantic_cube['float']['int']['!='] = 'int'
semantic_cube['int']['float']['=='] = semantic_cube['float']['int']['=='] = 'int'
semantic_cube['int']['float']['<='] = semantic_cube['float']['int']['<='] = 'int'
semantic_cube['int']['float']['>='] = semantic_cube['float']['int']['>='] = 'int'
semantic_cube['int']['float']['+'] = semantic_cube['float']['int']['+'] = 'float'
semantic_cube['int']['float']['-'] = semantic_cube['float']['int']['-'] = 'float'
semantic_cube['int']['float']['*'] = semantic_cube['float']['int']['*'] = 'float'
semantic_cube['int']['float']['/'] = semantic_cube['float']['int']['/'] = 'float'
semantic_cube['int']['float']['='] = 'int'
semantic_cube['float']['int']['='] = 'float'

semantic_cube['int']['char']['&&'] = semantic_cube['char']['int']['&&'] = 'int'
semantic_cube['int']['char']['||'] = semantic_cube['char']['int']['||'] = 'int'
semantic_cube['int']['char']['<'] = semantic_cube['char']['int']['<'] = 'int'
semantic_cube['int']['char']['>'] = semantic_cube['char']['int']['>'] = 'int'
semantic_cube['int']['char']['!='] = semantic_cube['char']['int']['!='] = 'int'
semantic_cube['int']['char']['=='] = semantic_cube['char']['int']['=='] = 'int'
semantic_cube['int']['char']['<='] = semantic_cube['char']['int']['<='] = 'int'
semantic_cube['int']['char']['>='] = semantic_cube['char']['int']['>='] = 'int'
semantic_cube['int']['char']['+'] = semantic_cube['char']['int']['+'] = 'int'
semantic_cube['int']['char']['-'] = semantic_cube['char']['int']['-'] = 'int'
semantic_cube['int']['char']['*'] = semantic_cube['char']['int']['*'] = 'int'
semantic_cube['int']['char']['/'] = semantic_cube['char']['int']['/'] = 'int'
semantic_cube['int']['char']['='] = 'int'
semantic_cube['char']['int']['='] = 'char'

semantic_cube['float']['char']['&&'] = semantic_cube['char']['float']['&&'] = 'int'
semantic_cube['float']['char']['||'] = semantic_cube['char']['float']['||'] = 'int'
semantic_cube['float']['char']['<'] = semantic_cube['char']['float']['<'] = 'int'
semantic_cube['float']['char']['>'] = semantic_cube['char']['float']['>'] = 'int'
semantic_cube['float']['char']['!='] = semantic_cube['char']['float']['!='] = 'int'
semantic_cube['float']['char']['=='] = semantic_cube['char']['float']['=='] = 'int'
semantic_cube['float']['char']['<='] = semantic_cube['char']['float']['<='] = 'int'
semantic_cube['float']['char']['>='] = semantic_cube['char']['float']['>='] = 'int'
semantic_cube['float']['char']['+'] = semantic_cube['char']['float']['+'] = 'float'
semantic_cube['float']['char']['-'] = semantic_cube['char']['float']['-'] = 'float'
semantic_cube['float']['char']['*'] = semantic_cube['char']['float']['*'] = 'float'
semantic_cube['float']['char']['/'] = semantic_cube['char']['float']['/'] = 'float'
semantic_cube['float']['char']['='] = 'float'
semantic_cube['char']['float']['='] = 'char'
semantic_cube['char']['lee']['='] = 'char'
