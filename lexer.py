import ply.lex as lex
import ply.yacc as yacc
errors = False

tokens = (
    'IF',
    'END',
    'WHILE',
    'FOR',
    'LPAREN',
    'RPAREN',
    'ID',
    'COMPARISON',
    'NUMBER',
    'EQUALS',
    'COLON',
    'PRINT',
    'STRUCT',
    'FUNCTION',
    'COMMA'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMPARISON = r'<=|>=|<|>|==|!='
t_EQUALS = r'='
t_COLON = r':'
t_COMMA = r','


def t_FUNCTION(t):
    r'function'
    return t


def t_STRUCT(t):
    r'struct'
    return t


def t_PRINT(t):
    r'print'
    return t

def t_IF(t):
    r'if'
    return t

def t_END(t):
    r'end'
    return t


def t_FOR(t):
    r'for'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_ignore = ' \t'

def t_error(t):
    print(f'Illegal character at {t.value[0]}')
    t.lexer.skip(1)


lexer = lex.lex()

def p_start(p):
    '''
    start : if_condition
          | for_loop
          | while_loop
          | struct
          | function
    '''
    pass


def p_function(p):
    '''
    function : FUNCTION ID LPAREN id_list_function RPAREN statement END
    '''
    pass

def p_id_list_function(p):
    '''
    id_list_function : ID
                     | ID COMMA id_list_function
    '''
    pass

def p_struct(p):
    '''
    struct : STRUCT ID id_list END
    '''
    pass

def p_id_list(p):
    '''
    id_list : ID
            | ID id_list
    '''
    pass


def p_if_condition(p):
    '''
    if_condition : IF LPAREN condition RPAREN statement END
                 | IF condition statement END 
    '''
    pass


def p_while_loop(p):
    '''
    while_loop : WHILE LPAREN condition RPAREN statement END
               | WHILE condition statement END
    '''
    pass

def p_for_loop(p):
    '''
    for_loop : FOR LPAREN ID EQUALS NUMBER COLON NUMBER RPAREN statement END
             | FOR ID EQUALS NUMBER COLON NUMBER statement END
    '''
    pass


def p_condition(p):
    '''
    condition : ID COMPARISON ID
              | ID COMPARISON NUMBER
              | NUMBER COMPARISON ID
              | NUMBER COMPARISON NUMBER
    '''
    pass

def p_statement(p):
    '''
    statement : ID EQUALS NUMBER
              | ID EQUALS ID
              | PRINT LPAREN ID RPAREN
              | PRINT ID
    '''

def p_error(p):
    global errors
    errors = True
    if(errors):
        print(f'Syntax error at {p.value}')
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

samples = [
    "if(x > 10) y=10 end",
    "if(x = 10) y=20 end",

    "while(x >= 10) print(x) end",
    "while(x == 10) print(x end",

    "for(i = 1:100) print(y) end",
    "for(i = i:2) print(y) end",

    "struct foo x y end",
    "struc foo x y end",

    "function f(x,y) x=y end",
    "function f(x,) x=y end"
]

def parseInput(code):
    parser.parse(code)
    if(errors):
        print("Invalid")
        print("\n")
    else:
        print("Valid")
        print("\n")


for code in samples:
    errors = False
    print("Code: ", code)
    print("Tokens:")
    lexer.input(code)
    for tokens in lexer:
        print(tokens)
    print("Parsing Result: ", end="")
    parseInput(code)
