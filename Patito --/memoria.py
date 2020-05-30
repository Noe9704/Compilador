
# Tipos de bases para guardar direcciones
INT_BASE = 0
FLOAT_BASE = 1000
CHAR_BASE = 2000
BOOL_BASE = 3000

# direcciones locales y globales
GLOBAL_BASE = 0
LOCAL_BASE = 10000
CTE_BASE = 20000
MAX_BASE = 30000

##Direcciones locales
local_int = LOCAL_BASE + INT_BASE
local_float = LOCAL_BASE + FLOAT_BASE
local_char = LOCAL_BASE + CHAR_BASE
local_bool = LOCAL_BASE + BOOL_BASE

##Direcciones globales
global_int = GLOBAL_BASE + INT_BASE
global_float = GLOBAL_BASE + FLOAT_BASE
global_char = GLOBAL_BASE + CHAR_BASE
global_bool = GLOBAL_BASE + global_bool


#Direcciones de constantes
constante_int = CTE_BASE + INT_BASE
constante_float = CTE_BASE + FLOAT_BASE
constante_char = CTE_BASE + CHAR_BASE
constante_bool = CTE_BASE + BOOL_BASE

symbols = {}
quadruples = []
constants = {}
memoriaGlobal = Memoria()
memoriaLocales = []

def asigna(direccion,valor):
    if direccion < CTE_BASE and direccion > LOCAL_BASE :
        memoriaLocales[-1] = valor
    else :
        memoriaGlobal[-1] = valor



def asignaParametros():
    pass


if len(sys.argv) is not 2:
    print('Error, leyendo el objeto del archivo')
    raise SyntaxError('Patito necesita de un archivo')
else: 
    data = sys.argv[1]
    with open(data, 'r', newline='\n') as file:
        input = eval(file.read())
        global symbols, quadruples, constants
        symbols = input['symbols']
        quadruples = input['quadruples']
        constants = input['constants']
        run()


def inserta_Dir_Locales(var,tipo):
    global local_int, local_float, local_char, local_bool
    if tipo == "int":
        direccion = local_int
        local_int += 1
        memoriaLocales.append(var)
        return direccion
    elif tipo == "float":
        direccion = local_float
        local_float += 1
        memoriaLocales.append(var)
        return direccion
    elif tipo == "char":
        direccion = local_char
        local_char += 1
        memoriaLocales.append(var)
        return direccion
    elif tipo == "bool":
        direccion = local_bool
        local_bool += 1
        memoriaLocales.append(var)
        return direccion
    

def inserta_Dir_Constantes(self, const,tipo):
    global constante_int, constante_float, constante_char, constante_bool
    if tipo == "int":
        direccion = constante_int
        constante_int += 1
        constants[direccion] = const
        return direccion
    elif tipo == "float":
        direccion = constante_float
        constante_float += 1
        constants[direccion] = const
        return direccion
    elif tipo == "char":
        direccion = constante_char
        constante_char += 1
        constants[direccion] = const
        return direccion
    elif tipo == "bool":
        direccion = constante_bool
        constante_bool += 1
        constants[direccion] = const
        return direccion


class Memoria :
    def __init__(self):
        self.ints = {}
        self.floats = {}
        self.chars = {}
        self.bools = {}

    def inserta_Dir_Globales(self,var,tipo):
        global global_int, global_float, global_char, global_bool
        if tipo == "int":
            direccion = global_int
            global_int += 1
            self.ints[direccion] = var
            return direccion
        elif tipo == "float":
            direccion = global_float
            global_float += 1
            self.floats[direccion] = var
            return direccion
        elif tipo == "char":
            direccion = global_char
            global_char += 1
            self.char[direccion] = var
            return direccion
        elif tipo == "bool":
            direccion = global_bool
            global_bool += 1
            self.bools[direccion] = var
            return direccion
    

####Logica, no hacer mucho caso
def run():
    if quadruples[-1] = "+":
        operand = quadruples[-1]
        opIzq = quadruples[-1]
        opDer = quadruples[-1]
        newValor = opIzq + opDer
        quadruples[-1] = newValor
        ##Se debe actualizar la direccion 


############################