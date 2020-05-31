# ------------------------------------------------------------
# Luis Marcelo Flores Canales A01280943
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

## Direcciones para guarda locales
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
    def __init__(self):
        self.ints = {}
        self.floats = {}
        self.chars = {}
        self.bools = {}
    
    def __repr__(self):  
        return "Integer:% s Float:% s Char:% s  bool:% s " % (self.ints, self.floats, self.chars,self.bools) 

    def inserta_Dir_Globales(self,var,tipo):
        global global_int, global_float, global_char, global_bool
        if tipo == "int":
            direccion = global_int
            global_int += 1
            self.ints[direccion] = None
            return direccion
        elif tipo == "float":
            direccion = global_float
            global_float += 1
            self.floats[direccion] = None
            return direccion
        elif tipo == "char":
            direccion = global_char
            global_char += 1
            self.char[direccion] = None
            return direccion
        elif tipo == "bool":
            direccion = global_bool
            global_bool += 1
            self.bools[direccion] = None
            return direccion

    def inserta_Dir_Constantes(self, const,tipo):
        global constante_int, constante_float, constante_char, constante_bool
        if tipo == "int":
            direccion = constante_int
            constante_int += 1
            print(constante_int)
            self.ints[direccion] = const
            return direccion
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

    def inserta_Dir_Locales(self,var,tipo):
        global local_int, local_float, local_char, local_bool
        if tipo == "int":
            direccion = local_int
            local_int += 1
            self.int[direccion] = var
            return direccion
        elif tipo == "float":
            direccion = local_float
            local_float += 1
            self.float[direccion] = var
            return direccion
        elif tipo == "char":
            direccion = local_char
            local_char += 1
            self.char[direccion] = var
            return direccion
        elif tipo == "bool":
            direccion = local_bool
            local_bool += 1
            self.bool[direccion] = var
            return direccion
    
    def inserta_Dir_temporales(self,var,tipo):
        global local_int, local_float, local_char, local_bool
        if tipo == "int":
            direccion = local_int
            local_int += 1
            self.int[direccion] = var
            return direccion
        elif tipo == "float":
            direccion = local_float
            local_float += 1
            self.float[direccion] = var
            return direccion
        elif tipo == "char":
            direccion = local_char
            local_char += 1
            self.char[direccion] = var
            return direccion
        elif tipo == "bool":
            direccion = local_bool
            local_bool += 1
            self.bool[direccion] = var
            return direccion

    def getType(self,varAddress):
        if (int(varAddress) / 1000) % 10 == 0:
            return 'int'
        elif (int(varAddress) / 1000) % 10 == 1:
            return 'float'
        elif (int(varAddress) / 1000) % 10 == 2:
            return 'char'
        elif (int(varAddress) / 1000) % 10 == 3:
            return 'bool'
    
    def getValue(self,address):
        if (int(address) / 1000) % 10 < 1:
            for key in self.ints :
                if address == key :
                    return self.ints[key]
        elif (int(address) / 1000) % 10 < 2:
            for key in floats:
                if address == key :
                    return self.floats[key]
        elif (int(address) / 1000) % 10 < 3:
            for key in char:
                if address == key :
                    return self.char[key]
        elif (int(address) / 1000) % 10 < 4:
            for key in bool:
                if address == key :
                    return self.bool[key]
        
#print(symbols)
#print(quadruples)
#print(constants)
"""

"""
def asigna(direccion,valor):
    if direccion < CTE_BASE and direccion > LOCAL_BASE :
        memoriaLocales[-1] = valor
    else :
        memoriaGlobal[-1] = valor


def asignaParametros():
    pass
    

####Logica, no hacer mucho caso
def run():
    if quadruples[-1] == "+":
        operand = quadruples[-1]
        opIzq = quadruples[-1]
        opDer = quadruples[-1]
        newValor = opIzq + opDer
        quadruples[-1] = newValor
        ##Se debe actualizar la direccion 


############################