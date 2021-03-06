# Oscar Lerma A01380817
# Cesar Buenfil Vazquez A01207499
# Estructuras de datos de Patitoplusplus
# Created 04/06/2020
from enum import Enum, IntEnum, auto
from collections import defaultdict
# ========================================================================== #
# Structures.py
# ========================================================================== #

# ========================================================================== #
# Estructuras de Semanticas
# ========================================================================== #
#Valor booleano de error just incase
p_error = False

#Stack de Operaciones
operator_stack = []

# Stack para operandos
# Guarda typo y nombre
operand_stack = []

#Stack de salto durante ejecucion
jump_stack = []

# Almacenamiento de cuadruplos
quadruples = []
quad_pointer = 0

# Cuenta de parametros y variables para creación de functiones
#                INT, FLOAT, CHAR , STRING
func_var_count = [0,    0,      0,      0]

# Cuenta de temporales para creación de funciones
#                 INT   FLOAT  CHAR  STRING
func_temp_count = [0,     0,    0,    0]

#Guarda parametros en orden de su declaración
func_param_order = []

# Guarda el conteo de parametros
func_param_counter = 0

#Array auxiliar variables
func_dim_counter = 0
current_var_aux = None
r_dim = 1

# Estructuras de arreglos y variables
pila_dim = []


# Contador de operandos para for
for_operand_stack = []

# Variables Auxiliares para currents
current_type = None
current_func = 'global' # Scope
current_var = ''
call_func = 'global'

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

# ========================================================================== #
# Limites de memoria virtual
# ========================================================================== #
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

#POINTERS                  INT
POINT_LOWER_LIMIT =     [50_000]
POINT_UPPER_LIMIT =     [51_499]


# Contadores de memoria virutal
global_dir_count = list(GLOBAL_LOWER_LIMIT)
var_dir_count = list(VAR_LOWER_LIMIT)
temp_dir_count = list(TEMP_LOWER_LIMIT)
const_dir_count = list(CONST_LOWER_LIMIT)
point_dir_count = list(POINT_LOWER_LIMIT)
# Enumeracion de tipos de datos
var_types = ('int', 'float', 'char', 'string')
avail_types = ('int', 'float', 'char', 'string', 'void')
func_types = ('int', 'float', 'char', 'string', 'void')

# Diccionario de Operaciones
Operations = {
    "PLUS_UNARY" : 1,
    "MINUS_UNARY" : 2,
    "!" : 3,
    "*" : 4,
    "%" : 5,
    "+" : 6,
    "-" : 7,
    "<" : 8,
    ">" : 9,
    "!=" : 10,
    "==" : 11,
    "<=" : 12,
    ">=" : 13,
    "||" : 14,
    "&&" : 15,
    "=" : 16,
    "LEE" : 17,
    "ESCRIBE" : 18,
    "GOTO" : 19,
    "GOTOF" : 20,
    "GOSUB" : 21,
    "PARAM" : 22,
    "ERA" : 23,
    "RETURN" : 24,
    "ENDFunc" : 25,
    "END" : 26,
    "FAKE_BOTTOM" : 27,
    "VER" : 28
 }

# ========================================================================== #
# Cubo Semantico
# ========================================================================== #

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
semantic_cube['int']['int']['%'] = 'int'
semantic_cube['int']['int']['='] = 'int'
semantic_cube['int']['lee']['='] = 'int'
semantic_cube['int']['unary+'] = 'int'
semantic_cube['int']['unary-'] = 'int'
semantic_cube['int']['!'] = 'int'
semantic_cube['int']['$'] = 'int'
semantic_cube['int']['¡'] = 'int'
semantic_cube['int']['?'] = 'int'

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
semantic_cube['int']['$'] = 'float'
semantic_cube['int']['¡'] = 'float'
semantic_cube['int']['?'] = 'float'

# semantic_cube['char']['char']['&&'] = 'int'
# semantic_cube['char']['char']['||'] = 'int'
semantic_cube['char']['char']['!='] = 'int'
semantic_cube['char']['char']['=='] = 'int'
semantic_cube['char']['char']['+'] = 'str'
semantic_cube['char']['char']['='] = 'char'
semantic_cube['char']['lee']['='] = 'char'
# semantic_cube['int']['char']['='] = 'int'
# semantic_cube['char']['int']['='] = 'char'
# semantic_cube['float']['char']['='] = 'float'
# semantic_cube['char']['float']['='] = 'char'

# semantic_cube['string']['string']['&&'] = 'int'
# semantic_cube['string']['string']['||'] = 'int'
semantic_cube['string']['string']['!='] = 'int'
semantic_cube['string']['string']['=='] = 'int'
semantic_cube['string']['string']['+'] = 'str'
semantic_cube['string']['string']['='] = 'string'
semantic_cube['string']['lee']['='] = 'string'
# semantic_cube['int']['string']['='] = 'int'
# semantic_cube['string']['int']['='] = 'string'
# semantic_cube['float']['string']['='] = 'float'
# semantic_cube['string']['float']['='] = 'string'

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
