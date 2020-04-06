from arpeggio import ZeroOrMore, OneOrMore, Optional, ParserPython, RegExMatch, Terminal, NonTerminal
import sys

def id():           return RegExMatch(r'[a-zA-Z]\w*')
def cte_i():        return RegExMatch(r'\d*')
def cte_f():        return RegExMatch(r'\d*\.\d*')
def cte_string():   return RegExMatch(r"'.*'")
def TIPO():         return ['int', 'float']
def VARS():         return 'var', OneOrMore(id, ZeroOrMore(',', id), ':', TIPO, ';')
def VAR_CTE():      return [id, cte_f, cte_i]
def EXP():          return TERMINO, ZeroOrMore(['+', '-'], TERMINO)
def EXPRESION():    return EXP, Optional(['>', '<', '<>'], EXP)
def FACTOR():       return [('{', EXPRESION, '}'), (Optional(['+', '-']), VAR_CTE)]
def TERMINO():      return FACTOR, ZeroOrMore(['*', '/'], FACTOR)
def ASIGNACION():   return id, '=', EXPRESION, ';'
def CONDICION():    return 'if(', EXPRESION, ')', BLOQUE, Optional('else', BLOQUE), ';'
def ESCRITURA():    return 'print(', [EXPRESION, cte_string], ZeroOrMore(',', [EXPRESION, 'cte_string']), ');'
def ESTATUTO():     return [ASIGNACION, CONDICION, ESCRITURA]
def BLOQUE():       return '{', ZeroOrMore(ESTATUTO), '}'
def PROGRAMA():     return 'program', id, ':', Optional(VARS), BLOQUE

def get_parser():
    return ParserPython(PROGRAMA)


def print_result(result, tabs=1):
    spacing = '| '.join(['' for i in range(tabs)])
    for r in result:
        if isinstance(r, NonTerminal):
            print(f"{spacing}{r.rule_name}:")
            print_result(r, tabs + 1)
        else:
            print(f"{spacing}{r.rule_name if r.rule_name else 'String'} - {r.value}")


if __name__=='__main__':
    if len(sys.argv) < 2:
        print('Manda un archivo')
    else:
        print_result(get_parser().parse(open(sys.argv[1], 'r').read()))
