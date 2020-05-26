# Grámatica

import ply.lex as lex
import ply.yacc as yacc
import sys
import cuboSemantico
import pprint

symbols = {
    'name': '',
    'global': {
        'vars': {}
    }
}

constants = {
    'global' :{
        
    }
}

    


contParametros = 0
currentERA = ""

##declaracion de variables para abrir simbolos
current_tipo = ''
current_func = 'global'
current_variable =''
current_param = ''

# Tipos de bases para guardar direcciones
INT_BASE = 0
FLOAT_BASE = 1000
CHAR_BASE = 2000
BOOL_BASE = 3000

##Cantidad total de direcciones por tipo
ADDRESS_SPACE = 1000


# direcciones locales y globales
GLOBAL_BASE = 0
LOCAL_BASE = 10000
CTE_BASE = 20000
MAX_BASE = 30000

global_next_int = GLOBAL_BASE + INT_BASE
global_next_float = GLOBAL_BASE + FLOAT_BASE
global_next_char = GLOBAL_BASE + CHAR_BASE
global_bool_base = GLOBAL_BASE + BOOL_BASE
global_next_bool = GLOBAL_BASE + BOOL_BASE


constant_next_int = CTE_BASE + INT_BASE
constant_next_float = CTE_BASE + FLOAT_BASE
constant_next_char = CTE_BASE + CHAR_BASE
constant_bool_base = CTE_BASE + BOOL_BASE
constant_next_bool = CTE_BASE + BOOL_BASE

#contador inicial de apuntador a direccion actual
next_int = LOCAL_BASE + INT_BASE
next_float = LOCAL_BASE + FLOAT_BASE
next_char = LOCAL_BASE + CHAR_BASE
bool_base = LOCAL_BASE + BOOL_BASE
next_bool = LOCAL_BASE + BOOL_BASE

##funcion para reiniciar al contador de direcciones
def newFunction():
    global next_int, next_float, next_char, next_bool
    next_int = LOCAL_BASE + INT_BASE
    next_float = LOCAL_BASE + FLOAT_BASE
    next_char = LOCAL_BASE + CHAR_BASE
    bool_base = LOCAL_BASE + BOOL_BASE
    next_bool = LOCAL_BASE + BOOL_BASE
"""
def getAddressAux():
    pass
"""    
## Funcion para asignar direcciones de memoria
def getAddress(tipo, force_global=False):
    ## Asignar direcciones a variables globales y a funciones
    if current_func == 'global' or force_global:
        ## Asignar direcciones a variables o funciones enteras
        if tipo == 'int':
            global global_next_int ## Contador de la direccion actual
            aux = global_next_int  ## Auxiliar para no modificar contador original
            if aux >= FLOAT_BASE: ### checar que no se pase del limite de las enteras
                print("Error, espacio de memoria insuficiente para variables globales enteras")
                sys.exit()
            global_next_int += 1 ## Actualiza la direccion 
            return aux ## Se retorna la direccion actual
        elif tipo == 'float': ## Asignar direcciones a variables o funciones flotantes
            global global_next_float ## Contador de la direccion actual
            aux = global_next_float   ## Auxiliar para no modificar contador original
            if aux >= CHAR_BASE: ### checar que no se pase del limite de las flotantes               
                print("Error, espacio de memoria insuficiente para flotantes")
                sys.exit()
            global_next_float += 1 ## Actualiza la direccion 
            return aux ## Se retorna la direccion actual
        elif tipo == 'char': ## Asignar direcciones a variables o funciones de caracter
            global global_next_char ## Contador de la direccion actual
            aux = global_next_char  ## Auxiliar para no modificar contador original
            if aux >= BOOL_BASE: ### checar que no se pase del limite de las caracteres             
                print("Error, espacio de memoria insuficiente para caracteres")
                sys.exit()
            global_next_char += 1 ## Actualiza la direccion 
            return aux ## Se retorna la direccion actual
        elif tipo == 'bool':  ## Asignar direcciones a variables o funciones booleanas
            global global_next_bool ## Contador de la direccion actual
            aux = global_next_bool  ## Auxiliar para no modificar contador original
            if aux >= BOOL_BASE + ADDRESS_SPACE: ### checar que no se pase del limite de las booleanas            
                print("Error, espacio de memoria insuficiente para booleanos")
                sys.exit()
            global_next_bool += 1 ## Actualiza la direccion 
            return aux  ## Se retorna la direccion actual
        
    else: 
        if tipo == 'int':   ## Asignar direcciones a variables locales de tipo entero
            global next_int ## Contador de la direccion actual
            aux = next_int  ## Auxiliar para no modificar contador original
            if aux >= LOCAL_BASE + FLOAT_BASE: ### checar que no se pase del limite de las enteras
                print("Locales,Error, espacio de memoria insuficiente para enteros")
                sys.exit()   
            next_int += 1 ## Actualiza la direccion 
            return aux ## Se retorna la direccion actual
        elif tipo == 'float': ## Asignar direcciones a variables locales de tipo flotante
            global next_float ## Contador de la direccion actual
            aux = next_float  ## Auxiliar para no modificar contador original
            if aux >= LOCAL_BASE + CHAR_BASE: ### checar que no se pase del limite de las flotantes
                # ERROR: Too many variables 
                print("Error, espacio de memoria insuficiente para flotantes")
                sys.exit()
            ##print('Aqui esta aux')            
            next_float += 1 ## Actualiza la direccion 
            return aux ## Se retorna la direccion actual
        elif tipo == 'char': ## Asignar direcciones a variables locales de tipo char
            global next_char ## Contador de la direccion actual
            aux = next_char ## Auxiliar para no modificar contador original
            if aux >= LOCAL_BASE + BOOL_BASE: ### checar que no se pase del limite de las char
                # ERROR: Too many variables 
                print("Error, espacio de memoria insuficiente para char")
                sys.exit()
            next_char += 1 ## Actualiza la direccion 
            return aux ## Se retorna la direccion actual
        elif tipo == 'bool': ## Asignar direcciones a variables locales de tipo bool
            global next_bool ## Contador de la direccion actual
            aux = next_bool  ## Auxiliar para no modificar contador original
            if aux >= LOCAL_BASE + BOOL_BASE + ADDRESS_SPACE or aux >= CTE_BASE: ### checar que no se pase del limite de las bool
                print("Error, espacio de memoria insuficiente para booleanos")
                sys.exit()
            next_bool += 1 ## Actualiza la direccion 
            return aux  ## Se retorna la direccion actual


quadruples = []

##Pilas cuadruplos
Pila_Names = []
Pila_Types = []
Pila_Oper = [] 
pila_Variables_Globales = []
pila_Variables_Generales = []
pila_Variables_Funciones = []
Pila_Saltos = []


## Ejemplo de la estructura de la tabla de simbolos
'''symbols[current_func]['vars'][p[-1]] = {
    'tipo': current_tipo,
    'address': get_address()
}'''
'''symbols = {
    'global': {
        'vars1': {
            'type': 'string'
        },
        'vars2': {
            'type': 'int'
        }
    }
    'main': {
        'tipo': 'void',
        'param': {
            'aux2': {
                'tipo': 'int',
                'address': 1000
            }
        },
        'vars': {
            'aux': {
                'tipo': 'int',
                'address': 1001
            }
        }
    }
    'doSomething: {
        'tipo': 'void',
        'param': {
            'aux2': {
                'tipo': 'int',
                'address': 1000
            }
        },
        'vars': {
            'aux': {
                'tipo': 'int',
                'address': 1001
            }
        }
    }
}'''

## Variable para comprobar si el archivo se acepto correctamente
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
    'AND',
    'OR',
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
t_AND = r'\&'
t_OR = r'\|'
t_MONEY = r'\$'
t_EXCLAMATION = r'\¡' 
t_QUESTION = r'\?'

t_CTE_I = r'[0-9]+'
t_CTE_F = r'[0-9]+\.[0-9]+'
t_CTE_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_CTE_C = r'(\'[^\']*\')'

tokens = tokens + list(reserverd.values())


## Funcion para declarar ID con expresiones regulares
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserverd.get(t.value,'ID')
    return t


## Funcion para detectar simbolos no validos
def t_error(t):
    global success
    success = False
    print ("Caracter no valido '%s'" % t.value[0])
    t.lexer.skip(1)
 
lex.lex()

## Regla gramatical 
def p_program(p):
    '''
    program : PROGRAM ID r_registrar_programa COLON auxVar auxFuncion MAIN r_registrar_main L_PARENT R_PARENT auxVar bloque r_EndProgram
    '''
    
    #stuff.insert(0, stuff[:])
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(stuff)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(symbols)
    pp.pprint(pila_Variables_Funciones)
    # print(symbols)
    # quadruples.insert(0,quadruples[:])
    cont = 0
    for x in quadruples :
        print(cont,end="\t")
        cont = cont + 1
        pp.pprint(x)
        
    ##pp.pprint(Pila_Names)
    print("Constantes")
    pp.pprint(constants)
    #print(quadruples)
    ##print(Pila_Names)
    #print(Pila_Oper)

def p_r_EndProgram(p):
    '''
    r_EndProgram : 
    '''
    cuad = ["END",None,None,None]
    quadruples.append(cuad)

def p_auxVar(p):
    '''
    auxVar : VAR var auxVar 
            | empty
    '''

def p_var(p):
    '''
    var : tipo COLON lista_ids_asignacion auxLista_idsVar_asignacion SEMICOLON
        | tipo COLON lista_ids_asignacion auxLista_idsVar_asignacion SEMICOLON var
    '''

def p_tipo(p):
    '''
    tipo : INT r_registrar_tipo
        | FLOAT r_registrar_tipo
        | CHAR r_registrar_tipo
    ''' 

def p_lista_ids(p):
    '''
    lista_ids : ID r_push_Name casilla casilla 
    '''

def p_auxLista_idsVar_asignacion(p):
    '''
    auxLista_idsVar_asignacion : COMA lista_ids_asignacion auxLista_idsVar_asignacion
            | empty  
    ''' 

def p_lista_ids_asignacion(p):
    '''
    lista_ids_asignacion : ID r_registrar_variable casilla casilla 
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
    funcion : FUNCION tipoFuncion ID r_registrar_func_name L_PARENT auxParametro R_PARENT COLON auxVar bloque r_SaveTemporalVarsFunction
    '''


def p_r_SaveTemporalVarsFunction(p):
    '''
    r_SaveTemporalVarsFunction : 
    '''
    global next_int, LOCAL_BASE
    symbols[current_func]['Temporales'] = {'int': next_int-LOCAL_BASE - INT_BASE - len(symbols[current_func]['params']),
                                           'float': next_float - LOCAL_BASE - FLOAT_BASE,
                                           'char': next_char - LOCAL_BASE - CHAR_BASE,
                                           'bool': next_bool - LOCAL_BASE - BOOL_BASE}
    cuad = ["ENDPROC",None,None,None]
    quadruples.append(cuad)


def p_r_funcionERA(p):
    '''
    r_funcionERA : 
    '''
    global currentERA
    funcName = p[-1]
    currentERA = funcName
    cuad = ["Era",None,None,funcName]
    quadruples.append(cuad)


def p_r_reiniciaContadorParametrosLlamadas(p):
    '''
    r_reiniciaContadorParametrosLlamadas : 
    '''
    global contParametros
    contParametros = 0


def p_r_funcionParametros(p):
    '''
    r_funcionParametros : 
    '''
    global contParametros
    contParametros +=1 
    functionName = Pila_Names.pop()
    Pila_Types.pop()
    paramsFunction = symbols[currentERA]['params'].items()
    if len(list((symbols[currentERA]['params'].items()))) >= contParametros :
        cuad = ["Param",functionName ,None,"par" + str(contParametros)]
        quadruples.append(cuad)

    else :
        print("Error, no  se han mandado la cantidad de argumentos que tiene la firma original de la funcion")
        sys.exit()


def p_r_funcionGOSUB(p):
    '''
    r_funcionGOSUB : 
    '''
    global currentERA
    cuad = ["GoSub",None,None,currentERA]
    currentERA = ""
    quadruples.append(cuad)



def p_tipoFuncion(p):
    '''
    tipoFuncion : tipo
                | VOID r_registrar_tipo
    '''

def p_auxParametro(p):
    '''
    auxParametro : tipo ID r_registrar_parametro
                | tipo ID r_registrar_parametro COMA auxParametro
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
    asignacion : lista_ids EQUAL r_push_operator exp r_check_equal SEMICOLON
    '''

def p_m(p):
    '''
    m : t auxM r_check_sum
    '''

def p_auxM(p):
    '''
    auxM : PLUS r_push_operator m
            | MINUS r_push_operator m
            | empty
    '''

def p_r_push_operator(p):
    '''
    r_push_operator : 
    '''
    Pila_Oper.append(p[-1])



def p_t(p):
    '''
    t : z auxT r_check_mult
    '''

def p_r_check_sum(p):
    '''
    r_check_sum :
    '''
    if len(Pila_Oper) > 0 :
        if Pila_Oper[len(Pila_Oper)-1] == '+' or Pila_Oper[len(Pila_Oper)-1] == '-':
            opDer = Pila_Names.pop()
            typeDer = Pila_Types.pop() 
            opIzq = Pila_Names.pop()
            typeIzq = Pila_Types.pop()
            operador = Pila_Oper.pop()
            result_Type = cuboSemantico.typeOperator[typeIzq][typeDer][operador]
            if result_Type is not None :
                termporalResultado = getAddress(result_Type)
                cuad = [operador, opIzq,opDer,termporalResultado]
                quadruples.append(cuad)
                Pila_Names.append(termporalResultado)
                Pila_Types.append(result_Type)
            else:
                print("Error, en el match *, / de tipos")
                sys.exit() 


def p_r_check_mult(p):
    '''
    r_check_mult :
    '''
    if len(Pila_Oper) > 0 :
        if Pila_Oper[len(Pila_Oper)-1] == '*' or Pila_Oper[len(Pila_Oper)-1] == '/':
            opDer = Pila_Names.pop()
            typeDer = Pila_Types.pop() 
            opIzq = Pila_Names.pop()
            typeIzq = Pila_Types.pop()
            operador = Pila_Oper.pop()
            result_Type = cuboSemantico.typeOperator[typeIzq][typeDer][operador]
            if result_Type is not None :
                termporalResultado = getAddress(result_Type)
                cuad = [operador, opIzq,opDer,termporalResultado]
                quadruples.append(cuad)
                Pila_Names.append(termporalResultado)
                Pila_Types.append(result_Type)
            else:
                print("Error, en el match +, - de tipos")
                sys.exit() 

def p_auxT(p):
    '''
    auxT : MULT r_push_operator t
        | DIV r_push_operator t
        | MONEY t
        | EXCLAMATION t
        | QUESTION t
        | empty
    '''

def p_f(p):
    '''
    f : m auxF r_check_Comparison
    '''

def p_auxF(p):
    '''
    auxF : LESSTHAN r_push_operator f
        | GREATERTHAN r_push_operator f
        | LESSEQUALTHAN r_push_operator f
        | GREATEREQUALTHAN r_push_operator f
        | EQUALX2 r_push_operator f
        | empty
    '''

def p_r_check_Comparison(p):
    '''
    r_check_Comparison : 
    '''
    if len(Pila_Oper) > 0 :
        if Pila_Oper[len(Pila_Oper)-1] == '<' or Pila_Oper[len(Pila_Oper)-1] == '>' or Pila_Oper[len(Pila_Oper)-1] == '<=' or Pila_Oper[len(Pila_Oper)-1] == '>=' or Pila_Oper[len(Pila_Oper)-1] == '==':       
            opDer = Pila_Names.pop()
            typeDer = Pila_Types.pop() 
            opIzq = Pila_Names.pop()
            typeIzq = Pila_Types.pop()
            operador = Pila_Oper.pop()
            result_Type = cuboSemantico.typeOperator[typeIzq][typeDer][operador]
            if result_Type is not None :
                if operador == '<' :
                    resultado = opIzq < opDer

                elif operador == '>' :
                    resultado = opIzq > opDer

                elif operador == '<=' :
                    resultado = opIzq <= opDer

                elif operador == '>=' :
                    resultado = opIzq >= opDer

                elif operador == '==':
                    resultado = opIzq == opDer

                termporalResultado = getAddress(result_Type)
                cuad = [operador, opIzq,opDer,termporalResultado]
                quadruples.append(cuad)
                Pila_Names.append(termporalResultado)
                Pila_Types.append(result_Type)
            else:
                print("Error, en el match de tipos de comparacion")
                sys.exit() 



def p_exp(p):
    '''
    exp : x auxExp r_check_OR
    '''

def p_auxExp(p):
    '''
    auxExp : OR r_push_operator exp
        | empty
    '''

def p_r_check_OR(p):
    '''
    r_check_OR : 
    '''
    if len(Pila_Oper) > 0 :
        if Pila_Oper[len(Pila_Oper)-1] == '|':
            opDer = Pila_Names.pop()
            typeDer = Pila_Types.pop() 
            opIzq = Pila_Names.pop()
            typeIzq = Pila_Types.pop()
            operador = Pila_Oper.pop()
            result_Type = cuboSemantico.typeOperator[typeIzq][typeDer][operador]
            if result_Type is not None :
                termporalResultado = getAddress(result_Type)
                cuad = [operador, opIzq,opDer,termporalResultado]
                quadruples.append(cuad)
                Pila_Names.append(termporalResultado)
                Pila_Types.append(result_Type)
            else:
                print("Error, en el match de tipos")
                sys.exit() 

def p_x(p):
    '''
    x : f auxX r_check_And
    '''

def p_auxX(p):
    '''
    auxX : AND r_push_operator f
        | empty
    '''

def p_z(p):
    '''
    z : var_cte 
        | r_false_add_bottom L_PARENT exp R_PARENT r_false_quit_bottom
        | lista_ids
        | llamada
        | empty
    '''

def p_r_check_And(p):
    '''
    r_check_And : 
    '''
    if len(Pila_Oper) > 0 :
        if Pila_Oper[len(Pila_Oper)-1] == '&' :
            opDer = Pila_Names.pop()
            typeDer = Pila_Types.pop() 
            opIzq = Pila_Names.pop()
            typeIzq = Pila_Types.pop()
            operador = Pila_Oper.pop()
            result_Type = cuboSemantico.typeOperator[typeIzq][typeDer][operador]
            if result_Type is not None :
                termporalResultado = getAddress(result_Type)
                cuad = [operador, opIzq,opDer,termporalResultado]
                quadruples.append(cuad)
                Pila_Names.append(termporalResultado)
                Pila_Types.append(result_Type)
            else:
                print("Error, en el match de tipos")
                sys.exit() 

def p_r_false_add_bottom(p):
    '''
    r_false_add_bottom :
    '''
    Pila_Oper.append("B")

def p_r_false_quit_bottom(p):
    '''
    r_false_quit_bottom :
    '''
    Pila_Oper.pop()


def p_var_cte(p):
    '''
    var_cte : CTE_I r_registrar_constante_int
            | CTE_F r_registrar_constante_float
    '''

def p_r_registrar_constante_int(p):
    '''
    r_registrar_constante_int : 
    '''
    global constants, current_variable,CTE_BASE, constant_next_int
    current_variable = p[-1]
    aux = constant_next_int 

    if constants[current_func].get(current_variable) is None:
        if constant_next_int >= constant_next_float :
            print("Error, espacio de constantes enteras lleno.")
            sys.exit()
                    
        constants[current_func][current_variable] = {
                    'address': aux,
                    'type': 'int'
        }
        Pila_Names.append(aux)
        Pila_Types.append('int')
        constant_next_int += 1
    else :
        dirr = constants[current_func][current_variable]['address']
        Pila_Names.append(dirr)
        Pila_Types.append('int')
    
        

def p_r_registrar_constante_float(p):
    '''
    r_registrar_constante_float : 
    '''
    global constants, current_variable,CTE_BASE, constant_next_float
    current_variable = p[-1]
    aux = constant_next_float 

    if constants[current_func].get(current_variable) is None:
        if constant_next_float >= constant_next_char :
            print("Error, espacio de constantes float lleno.")
            sys.exit()
         
        constants[current_func][current_variable] = {
                   'address': aux,
                   'type': 'float'
        }
        Pila_Names.append(aux)
        Pila_Types.append('float')
        constant_next_float += 1
    else :
        dirr = constants[current_func][current_variable]['address']
        Pila_Names.append(dirr)
        Pila_Types.append('float')


def p_llamada(p):
    '''
    llamada : ID r_funcionERA L_PARENT auxLlamada R_PARENT r_funcionGOSUB r_reiniciaContadorParametrosLlamadas 
    '''

def p_auxLlamada(p):
    '''
    auxLlamada : exp r_funcionParametros
                | exp r_funcionParametros COMA auxLlamada
    '''

def p_retorno(p):
    '''
    retorno : RETURN r_push_operator L_PARENT exp R_PARENT r_checkReturn SEMICOLON
    '''

def p_r_checkReturn(p):
    '''
    r_checkReturn :
    '''
    if len(Pila_Oper) > 0 :
        if Pila_Oper[len(Pila_Oper)-1] == 'return':
            opDer = Pila_Names.pop()
            Pila_Types.pop()
            operador = Pila_Oper.pop()
            cuad = [operador, None,None,opDer]
            quadruples.append(cuad)

def p_lectura(p):
    '''
    lectura : READ r_push_operator  L_PARENT  auxLectura  R_PARENT r_check_Lectura SEMICOLON
    '''

def p_r_check_Lectura(o):
    '''
    r_check_Lectura :
    '''
    if len(Pila_Oper) > 0 :
        if Pila_Oper[len(Pila_Oper)-1] == 'read':
            opDer = Pila_Names.pop()
            Pila_Types.pop()
            operador = Pila_Oper.pop()
            cuad = [operador, None,None,opDer]
            quadruples.append(cuad)
    
          

def p_auxLectura(p):
    '''
    auxLectura : lista_ids 
            | lista_ids  COMA auxLectura 
    '''

def p_escritura(p):
    '''
    escritura : WRITE r_push_operator L_PARENT auxEscritura R_PARENT SEMICOLON
    '''


def p_r_check_Escritura(p):
    '''
    r_check_Escritura : 
    '''
    if len(Pila_Oper) > 0 :
        if Pila_Oper[len(Pila_Oper)-1] == 'write':
            opDer = Pila_Names.pop()
            Pila_Types.pop()
            operador = Pila_Oper.pop()
            cuad = [operador, None,None,opDer]
            quadruples.append(cuad)

def p_r_check_Escritura_String(p):
    '''
    r_check_Escritura_String :
    '''
    if len(Pila_Oper) > 0 :
            if Pila_Oper[len(Pila_Oper)-1] == 'write':
                operador = Pila_Oper.pop()
                cuad = [operador,None,None,p[-1]]
                quadruples.append(cuad)
                

def p_auxEscritura(p):
    '''
    auxEscritura : auxString 
                 | auxExpEscritura 
    '''

def p_auxString(p):
    '''
    auxString : CTE_STRING r_check_Escritura_String
              | CTE_STRING r_check_Escritura_String COMA r_pushOtherWrite auxEscritura 
    '''

def p_auxExpEscritura(p):
    '''
    auxExpEscritura : exp r_check_Escritura 
                    | exp r_check_Escritura COMA r_pushOtherWrite auxEscritura 
    '''

def p_r_pushOtherWrite(p):
    '''
    r_pushOtherWrite : 
    '''
    Pila_Oper.append("write")


def p_decision(p):
    '''
    decision : IF L_PARENT exp R_PARENT r_checkIF SO bloque auxDecision r_checkIFB
    '''

def p_r_checkIFB(p):
    '''
    r_checkIFB :
    '''
    end = Pila_Saltos.pop()
    fill(end,len(quadruples))

#Funcion que llena los distintos saltos que hay
def fill(cuadr, salto):
    quadruples[cuadr][3] = salto



def p_r_checkIF(p):
    '''
    r_checkIF :
    '''
    exp_Type = Pila_Types.pop()
    ##exp_Name = Pila_Names.pop()
    if exp_Type != "bool" :
        print("Error de tipo")
        sys.exit()
    else :
        result = Pila_Names.pop()
        cuad = ["GOTOF", result,None,"resultado_salto"]      
        quadruples.append(cuad)
        Pila_Saltos.append(len(quadruples)-1)


def p_auxDecision(p):
    '''
    auxDecision : r_checkElse ELSE bloque
                | empty
    '''

def p_r_checkElse(p):
    '''
    r_checkElse : 
    '''
    cuad = ["GOTO", None,None,len(quadruples)] 
    quadruples.append(cuad)
    falso = Pila_Saltos.pop()
    Pila_Saltos.append(len(quadruples)-1)
    fill(falso,len(quadruples))


def p_repeticion(p):
    '''
    repeticion : condicional
                | nocondicional
    '''

def p_condicional(p):
    '''
    condicional : WHILE r_checkWhile L_PARENT exp R_PARENT r_checkWhileB DO bloque r_checkWhileC
    '''

def p_r_checkWhile(p):
    '''
    r_checkWhile :
    '''
    Pila_Saltos.append(len(quadruples))

def p_r_checkWhileB(p):
    '''
    r_checkWhileB :
    '''
    exp_Type = Pila_Types.pop()
    ##exp_Name = Pila_Names.pop()
    if exp_Type != "bool" :
        print("Error de tipo")
        sys.exit()
    else :
        result = Pila_Names.pop()
        cuad = ["GOTOF", result,None,len(quadruples)-1]   
        quadruples.append(cuad)
        Pila_Saltos.append(len(quadruples)-1)

def p_r_checkWhileC(p):
    '''
    r_checkWhileC :
    '''
    end = Pila_Saltos.pop()
    regresa = Pila_Saltos.pop()
    cuad = ["GOTO", None,None,regresa] 
    quadruples.append(cuad)
    fill(end,len(quadruples))  


def p_nocondicional(p):
    '''
    nocondicional : FROM r_checkFor lista_ids EQUAL r_push_operator exp TO exp r_push_operator DO r_checkForB bloque r_checkForC
    '''

def p_r_checkFor(p):
    '''
    r_checkFor :
    '''
    Pila_Saltos.append(len(quadruples))

def p_r_checkForB(p):
    '''
    r_checkForB :
    '''
    exp_Type = Pila_Types.pop()
    ##exp_Name = Pila_Names.pop()
    if exp_Type != "int" :
        print("Error de tipo")
        sys.exit()
    else :      
        opDer = Pila_Names.pop()
        typeDer = Pila_Types.pop() 
        opIzq = Pila_Names.pop()
        typeIzq = Pila_Types.pop()
        operador = "<"
        result_Type = cuboSemantico.typeOperator[typeIzq][typeDer][operador]
        termporalResultado = getAddress(result_Type)
        cuad1 = [operador,opIzq,opDer,termporalResultado]
        quadruples.append(cuad1)
        cuad = ["GOTOF", None,None,len(quadruples)-1]   
        quadruples.append(cuad)
        Pila_Saltos.append(len(quadruples)-1)
        '''
        operador2 = "+"
        result_Type2 = cuboSemantico.typeOperator[typeIzq][typeDer][operador2]
        termporalResultado2 = getAddress(result_Type2)
        cuad2 = [operador2,opIzq,opIzq,termporalResultado2]
        quadruples.append(cuad2)
        operador3 = "="
        cuad3 = [operador3,termporalResultado2,None,opIzq]
        quadruples.append(cuad3)
        '''
       
        
        

def p_r_checkForC(p):
    '''
    r_checkForC :
    '''
    end = Pila_Saltos.pop()
    regresa = Pila_Saltos.pop()
    cuad = ["GOTO", None,None,regresa] 
    quadruples.append(cuad)
    fill(end,len(quadruples))  

def p_empty(p):
    ''' 
    empty : 
    '''

##error function for parser
def p_error(p):
    global success
    success = False
    print("Error de sintaxis en '%s'" % p)


## rules
def p_r_registrar_programa(p):
    '''
    r_registrar_programa :
    '''
    symbols['name'] = p[-1]

## Las reglas de registrar es para guardar en tabla de variables
## Reglas de push son para guardar en pilas
def p_r_registrar_variable(p):
    '''
    r_registrar_variable :
    '''
    global symbols, current_variable, pila_Variables_Globales, pila_Variables_Generales, pila_Variables_Funciones
    aux_Funcion = ''
    current_variable = p[-1]

    if symbols[current_func].get(current_variable) is None:
        if(current_func == 'global'):
            pila_Variables_Globales.append(current_variable)
        elif(current_func == 'main'):
            pila_Variables_Generales.append(current_variable)
        else :
            pila_Variables_Funciones.append(tuple((current_func,current_variable)))
            '''
            pila_Variables_Funciones.append(current_variable)           
            aux_Funcion = current_func
            
            if current_func != aux_Funcion :
                pila_Variables_Funciones.clear()'''
        if variable_comun(pila_Variables_Globales, pila_Variables_Generales) is True:
            print("Variable en main ya declarada globalmente")
            sys.exit()
        if duplicados_Tupla(pila_Variables_Funciones) is True:
            print("Variable en funcion local repetida")
            sys.exit()
        if len(pila_Variables_Globales) is not len(set(pila_Variables_Globales)):
            print("Variable ya declarada en el espacio global")
            sys.exit()            
        symbols[current_func]['vars'][current_variable] = {
                   'type':current_tipo,
                   'address':getAddress(current_tipo)
        }
       
    else :
        print("Error")



def duplicados_Tupla(listaTupla):     
    flag = False
    listaAuxiliar = []   
    contador = 0
    for key in listaTupla: 
          
        if key in listaAuxiliar:   
            flag = True
            continue
          
        else: 
            contador = 0
            for b in listaTupla: 
                if b[0] == key[0] and b[1] == key[1]: 
                    contador = contador + 1            
            if(contador > 1):  
                return True 
            listaAuxiliar.append(key) 
                       
    if flag == False: 
        return False

def variable_comun(listaA,listaB):
    resultado = False

    for x in listaA:
        for y in listaB:
            if x == y:
                resultado = True
    return resultado

def p_r_registrar_func_name(p):
    '''
    r_registrar_func_name : 
    '''
    global symbols, current_func 
    current_func = p[-1]
    newFunction()
    if symbols.get(current_func) is None:
        symbols[current_func]= {
            'type': current_tipo,
            'start': len(quadruples),
            'params': {},
            'vars': {}
        }
        constants[current_func] ={}

        if current_tipo != "void" :
            symbols['global']['vars'][current_func] = {
            'address': getAddress(current_tipo, force_global=True),
            'type': current_tipo
        }

    else :
        print("funcion repetida " + current_func)
        sys.exit()
  

def p_r_registrar_main(p):
    '''
    r_registrar_main : 
    '''
    global symbols, current_func
    current_func = p[-1]
    symbols[current_func]= {
        'params': {},
        'vars': {}
    }

def p_r_registrar_tipo(p):
    '''r_registrar_tipo : '''
    global current_tipo
    current_tipo = p[-1]
    

def p_r_registrar_parametro(p):
    '''
    r_registrar_parametro :
    '''
    global symbols, current_param
    current_param = p[-1]
    symbols[current_func]['params'][current_param] = {
        'type':current_tipo,
        'address': getAddress(current_tipo)
    }
  

    
## Funcion para ingresar a las pilas de variables y de tipos
def p_r_push_Name(p):
    '''
    r_push_Name : 
    '''
    ## Se registra en las pilas de variables y de tipos
    if(symbols[current_func]['vars'].get(p[-1]) is not None): 
        ## Se registran en funciones locales
        Pila_Names.append(symbols[current_func]['vars'].get(p[-1])['address'])
        Pila_Types.append(symbols[current_func]['vars'].get(p[-1])['type'])
         ## Se registran en el espacio global
    elif(symbols['global']['vars'].get(p[-1]) is not None):
        Pila_Names.append(symbols['global']['vars'].get(p[-1])['address'])
        Pila_Types.append(symbols['global']['vars'].get(p[-1])['type'])
         ## Se registran parametros en las funciones
    elif(symbols[current_func]['params'].get(p[-1]) is not None):
        Pila_Names.append(symbols[current_func]['params'].get(p[-1])['address'])
        Pila_Types.append(symbols[current_func]['params'].get(p[-1])['type'])
    else :
        print("Error en la funcion " + "\""+ current_func +"\"" +" la variable " + "\"" + p[-1] + "\""+ " no esta definida")
        sys.exit()


## Regla para generar cuadruplo con igual
def p_r_check_equal(p):
    '''
    r_check_equal :
    '''
    if len(Pila_Oper) > 0 :
        if Pila_Oper[len(Pila_Oper)-1] == '=':
            opDer = Pila_Names.pop()
            typeDer = Pila_Types.pop() 
            opIzq = Pila_Names.pop()
            typeIzq = Pila_Types.pop()
            operador = Pila_Oper.pop()
            result_Type = cuboSemantico.typeOperator[typeIzq][typeDer][operador]
            if result_Type is not None :
                termporalResultado = getAddress(result_Type)
                cuad = [operador, opDer,None,opIzq]
                quadruples.append(cuad)
                Pila_Names.append(termporalResultado)
                Pila_Types.append(result_Type)
            else:
                print("Error, en el match de tipos")
                sys.exit() 

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