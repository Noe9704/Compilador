import ply.lex as lex
import ply.yacc as yacc
import sys


success = True

##Declaration of tokens
tokens = [
    'ID',
    'COLON',
    'CTE_STRING',
    'CTE_I',
    'CTE_F',
    'CTE_C',
    'COMA',
    'SEMICOLON',
    'L_BRACKET',
    'R_BRACKET',
    'EQUAL',
    'L_PARENT',
    'R_PARENT',
    'L_KEY',
    'R_KEY',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSEQUALTHAN',
    'GREATEREQUALTHAN',
    'EQUALX2',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'MONEY',
    'EXCLAMATION',
    'QUESTION'    
    ]

##Reserved words
reserverd = {
    'program' : 'PROGRAM',
    'funcion' : 'FUNCION',
    'var' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'void' : 'VOID',
    'print' : 'PRINT',
    'char' : 'CHAR',
    'if' : 'IF',
    'else' : 'ELSE',
    'so' : 'SO',
    'while' : 'WHILE',
    'from' : 'FROM',
    'to' : 'TO',
    'do' : 'DO',
    'and' : 'AND',
    'or' : 'OR',
    'return' : 'RETURN',
    'read' : 'READ',
    'write' : 'WRITE',
    'main' : 'MAIN'
    
}



##tokens symbols
t_ignore = ' \t\n'
t_COLON = r'\:'
t_COMA = r'\,'
t_SEMICOLON = r'\;'
t_L_KEY = r'\{'
t_R_KEY = r'\}'
t_L_BRACKET = r'\[' 
t_R_BRACKET = r'\]'
t_EQUAL = r'\='
t_L_PARENT = r'\('
t_R_PARENT = r'\)'
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_LESSEQUALTHAN = r'\<='
t_GREATEREQUALTHAN = r'\>='
t_EQUALX2 = r'\=='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_MONEY = r'\$'
t_EXCLAMATION = r'\¡' 
t_QUESTION = r'\?'

t_CTE_I = r'[0-9]+'
t_CTE_F = r'[0-9]+\.[0-9]+'
t_CTE_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_CTE_C = r'(\'[^\']*\')'

tokens = tokens + list(reserverd.values())

##declaration for letters with words ex hola93
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserverd.get(t.value,'ID')
    return t

##Lexer error function
def t_error(t):
    global success
    success = False
    print ("Caracter no valido '%s'" % t.value[0])
    t.lexer.skip(1)
 
lex.lex()

##gramatic rules
def p_program(p):
    '''
    program : PROGRAM ID COLON auxVar auxFuncion MAIN bloque
    '''

def p_auxVar(p):
    '''
    auxVar : var auxVar 
            | empty
    '''

def p_var(p):
    '''
    var : VAR tipo COLON lista_ids auxLista_idsVar SEMICOLON
    '''

def p_tipo(p):
    '''
    tipo : INT
        | FLOAT
        | CHAR
    ''' 

def p_auxLista_idsVar(p):
    '''
    auxLista_idsVar : COMA lista_ids auxLista_idsVar
            | empty  
    ''' 

def p_lista_ids(p):
    '''
    lista_ids : ID casilla casilla 
    '''

def p_casilla(p):
    '''
    casilla : L_BRACKET casillaVar R_BRACKET
            | empty
    '''

def p_casillaVar(p):
    '''
    casillaVar : CTE_I
                | ID
                | exp
    '''

def p_auxFuncion(p):
    '''
    auxFuncion : funcion auxFuncion
            | empty
    '''

def p_funcion(p):
    '''
    funcion : FUNCION tipoFuncion ID L_PARENT auxParametro R_PARENT COLON auxVar bloque
            | empty
    '''

def p_tipoFuncion(p):
    '''
    tipoFuncion : tipo
                | VOID
    '''

def p_auxParametro(p):
    '''
    auxParametro : tipo ID
                | tipo ID COMA auxParametro
                | empty
    '''

def p_bloque(p):
    '''
    bloque : L_KEY auxEstatuto R_KEY
    '''

def p_auxEstatuto(p):
    '''
    auxEstatuto : estatuto auxEstatuto
                | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
            | llamada SEMICOLON
            | retorno
            | lectura
            | escritura
            | decision
            | repeticion
    '''

def p_asignacion(p):
    '''
    asignacion : lista_ids EQUAL exp SEMICOLON
    '''

def p_exp(p):
    '''
    exp : t auxExp
    '''

def p_auxExp(p):
    '''
    auxExp : PLUS exp
            | MINUS exp
            | empty
    '''

def p_t(p):
    '''
    t : f auxT
    '''

def p_auxT(p):
    '''
    auxT : MULT t
        | DIV t
        | MONEY t
        | EXCLAMATION t
        | QUESTION t
        | empty
    '''

def p_f(p):
    '''
    f : m auxF
    '''

def p_auxF(p):
    '''
    auxF : LESSTHAN f
        | GREATERTHAN f
        | LESSEQUALTHAN f
        | GREATEREQUALTHAN f
        | EQUALX2 f
        | empty
    '''

def p_m(p):
    '''
    m : x auxM
    '''

def p_auxM(p):
    '''
    auxM : OR m
        | empty
    '''

def p_x(p):
    '''
    x : z auxX
    '''

def p_auxX(p):
    '''
    auxX : AND z
        | empty
    '''

def p_z(p):
    '''
    z : var_cte
        | L_PARENT exp R_PARENT
        | lista_ids
        | llamada
        | empty
    '''

def p_var_cte(p):
    '''
    var_cte : ID
            | CTE_I
            | CTE_F
    '''

def p_llamada(p):
    '''
    llamada : ID L_PARENT auxLlamada R_PARENT
    '''

def p_auxLlamada(p):
    '''
    auxLlamada : exp
                | exp COMA auxLlamada
    '''

def p_retorno(p):
    '''
    retorno : RETURN L_PARENT exp R_PARENT SEMICOLON
    '''

def p_lectura(p):
    '''
    lectura : READ L_PARENT auxLectura R_PARENT SEMICOLON
    '''

def p_auxLectura(p):
    '''
    auxLectura : lista_ids
            | lista_ids COMA auxLectura
    '''

def p_escritura(p):
    '''
    escritura : WRITE L_PARENT auxEscritura R_PARENT SEMICOLON
    '''

def p_auxEscritura(p):
    '''
    auxEscritura : auxString 
                 | auxExpEscritura
    '''

def p_auxString(p):
    '''
    auxString : CTE_STRING
              | CTE_STRING COMA auxEscritura  
    '''

def p_auxExpEscritura(p):
    '''
    auxExpEscritura : exp
                    | exp COMA auxExpEscritura
    '''

def p_decision(p):
    '''
    decision : IF L_PARENT exp R_PARENT SO bloque auxDecision
    '''

def p_auxDecision(p):
    '''
    auxDecision : ELSE bloque
                | empty
    '''

def p_repeticion(p):
    '''
    repeticion : condicional
                | nocondicional
    '''

def p_condicional(p):
    '''
    condicional : WHILE L_PARENT exp R_PARENT DO bloque
    '''

def p_nocondicional(p):
    '''
    nocondicional : FROM lista_ids EQUAL exp TO exp DO bloque
    '''

def p_empty(p):
    ''' 
    empty : 
    '''

##error function for parser
def p_error(p):
    global success
    success = False
    print("Error de sintaxis en '%s'" % p)

    
parser = yacc.yacc()

##caso de prueba en el que falla
##testFile2.txt

##caso de prueba exitoso
##testFile.txt

data = "testFile.txt"
f = open(data,'r')
s = f.read()

parser.parse(s)

if success == True:
    print("El archivo se ha aceptado")
    sys.exit()
else:
    print("El archivo tiene errores")
    sys.exit()

f.close()