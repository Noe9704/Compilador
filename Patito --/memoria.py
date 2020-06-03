# ------------------------------------------------------------
# Luis Marcelo Flores Canales A01280943
# Noé Flores Sifuentes A00949282
# ------------------------------------------------------------

import sys

## Tipos de bases para guardar direcciones
INT_BASE = 0
FLOAT_BASE = 1000
CHAR_BASE = 2000
BOOL_BASE = 3000

## Direcciones locales y globales
GLOBAL_BASE = 0
LOCAL_BASE = 10000
CTE_BASE = 20000
MAX_BASE = 30000

## Direcciones para guardar locales
local_int = LOCAL_BASE + INT_BASE
local_float = LOCAL_BASE + FLOAT_BASE
local_char = LOCAL_BASE + CHAR_BASE
local_bool = LOCAL_BASE + BOOL_BASE

## Direcciones para guardar globales
global_int = GLOBAL_BASE + INT_BASE
global_float = GLOBAL_BASE + FLOAT_BASE
global_char = GLOBAL_BASE + CHAR_BASE
global_bool = GLOBAL_BASE + BOOL_BASE


## Direcciones para guardar constantes
constante_int = CTE_BASE + INT_BASE
constante_float = CTE_BASE + FLOAT_BASE
constante_char = CTE_BASE + CHAR_BASE
constante_bool = CTE_BASE + BOOL_BASE

## Clase memoria

class Memoria:
    ## Estructura de la clase
    def __init__(self):
        self.ints = {}
        self.floats = {}
        self.chars = {}
        self.bools = {}
    
    ## Funcion que se utiliza solamente para imprimir la memoria
    def __repr__(self):  
        return "Integer:% s Float:% s Char:% s  bool:% s " % (self.ints, self.floats, self.chars,self.bools) 

    ## Funcion para insertar variables GLOBALES en el bloque de memoria
    def inserta_Dir_Globales(self,var,tipo):
        global global_int, global_float, global_char, global_bool
        if tipo == "int": # Si es tipo int entra en la condicion
            direccion = global_int # Se trae la ultima direccion disponible
            global_int += 1 # Se le suma 1 para indicar que la memoria pasada a sido utilizada
            self.ints[direccion] = var # Se asigna en ints[direccion] la variable traida
            return direccion # Retorna la direccion
        elif tipo == "float":
            direccion = global_float
            global_float += 1
            self.floats[direccion] = var
            return direccion
        elif tipo == "char":
            direccion = global_char
            global_char += 1
            self.chars[direccion] = var
            return direccion
        elif tipo == "bool":
            direccion = global_bool
            global_bool += 1
            self.bools[direccion] = var
            return direccion

    ## Funcion para insertar variables CONSTANTES en el bloque de memoria
    def inserta_Dir_Constantes(self, const,tipo):
        global constante_int, constante_float, constante_char, constante_bool
        if tipo == "int": # Si es tipo int entra en la condicion
            direccion = constante_int # Se trae la ultima direccion disponible
            constante_int += 1 # Se le suma 1 para indicar que la memoria pasada a sido utilizada
            ##print(constante_int)
            self.ints[direccion] = const # Se asigna en ints[direccion] la constante traida
            return direccion # Retorna la direccion
        elif tipo == "float":
            direccion = constante_float
            constante_float += 1
            self.floats[direccion] = const
            return direccion
        elif tipo == "char":
            direccion = constante_char
            constante_char += 1
            self.chars[direccion] = const
            return direccion
        elif tipo == "bool":
            direccion = constante_bool
            constante_bool += 1
            self.bools[direccion] = const
            return direccion

    ## Funcion para insertar variables LOCALES y TEMPORALES en el bloque de memoria
    def inserta_Dir_Locales(self,var,tipo, value):
        global local_int, local_float, local_char, local_bool
        if tipo == "int": # Si es tipo int entra en la condicion
            direccion = var # Se trae la ultima direccion disponible
            local_int += 1 # Se le suma 1 para indicar que la memoria pasada a sido utilizada
            self.ints[direccion] = value # Se asigna en ints[direccion] la constante traida
            return direccion # Retorna la direccion
        elif tipo == "float":
            direccion = var
            local_float += 1
            self.floats[direccion] = value
            return direccion
        elif tipo == "char":
            direccion = var
            local_char += 1
            self.chars[direccion] = value
            return direccion
        elif tipo == "bool":
            direccion = var
            local_bool += 1
            self.bools[direccion] = value
            return direccion
    ## No la utilizamos
    def inserta_Dir_temporales(self,var,tipo):
        global local_int, local_float, local_char, local_bool
        if tipo == "int":
            direccion = local_int
            local_int += 1
            self.ints[direccion] = var
            return direccion
        elif tipo == "float":
            direccion = local_float
            local_float += 1
            self.floats[direccion] = var
            return direccion
        elif tipo == "char":
            direccion = local_char
            local_char += 1
            self.chars[direccion] = var
            return direccion
        elif tipo == "bool":
            direccion = local_bool
            local_bool += 1
            self.bools[direccion] = var
            return direccion

    ## Funcion para actualizar el valor de una direccion
    def upDateVal(self,address,valor):
        ## La funcion recibe una direccion y con esta se puede determinar el tipo
        ## Conociendo el tipo podemos saber en que seccion actualizar
        if (int(address) / 1000) % 10 < 1:
            self.ints[address] = valor ## Guardamos el nuevo valor en la direccion
        elif (int(address) / 1000) % 10 < 2:
            self.floats[address] = valor
        elif (int(address) / 1000) % 10 < 3:
            self.chars[address] = valor
        elif (int(address) / 1000) % 10 < 4:
            self.bools[address] = valor
        
    ## Funcion que obtiene el tipo de una direccion
    def getType(self,varAddress):
        ## Se utiliza la direccion con una operacion para saber que tipo es
        if (int(varAddress) / 1000) % 10 < 1:
            return 'int'
        elif (int(varAddress) / 1000) % 10 < 2:
            return 'float'
        elif (int(varAddress) / 1000) % 10 < 3:
            return 'char'
        elif (int(varAddress) / 1000) % 10 < 4:
            return 'bool'
    
    ## Funcion para obtener el valor de una direccion
    def getValue(self,address):
        ## Con la direccion obtenida obtenemos que tipo es
        if (int(address) / 1000) % 10 < 1:
            for key in self.ints : ## Hacemos un for para recorrer toda la clase y encontrar la llave
                if address == key :
                    return self.ints[key]
        elif (int(address) / 1000) % 10 < 2:
            for key in self.floats:
                if address == key :
                    return self.floats[key]
        elif (int(address) / 1000) % 10 < 3:
            for key in self.chars:
                if address == key :
                    return self.chars[key]
        elif (int(address) / 1000) % 10 < 4:
            for key in self.bools:
                if address == key :
                    return self.bools[key]

        
#print(symbols)
#print(quadruples)
#print(constants)
"""

"""
'''
def asigna(direccion,valor):
    if direccion < CTE_BASE and direccion > LOCAL_BASE :
        memoriaLocales[-1] = valor
    else :
        memoriaGlobal[-1] = valor


def asignaParametros():
    pass
    
'''
####Logica, no hacer mucho caso
'''
def run():
    if quadruples[-1] == "+":
        operand = quadruples[-1]
        opIzq = quadruples[-1]
        opDer = quadruples[-1]
        newValor = opIzq + opDer
        quadruples[-1] = newValor
        ##Se debe actualizar la direccion 

'''
############################
