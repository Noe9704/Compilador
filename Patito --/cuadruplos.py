
pilaOperadores = []
pilaTipos = []
pilaId = []
opDer = 0
opIzq = 0
operador = 0

opsEXP = {
    "+",
    "-",
    "*",
    "/"    
}


def eval(cuadruplo):
    tokens = cuadruplo.split()
    for token in tokens:
        if(token in opsEXP):
            pilaOperadores.append(token)
        else:
            pilaId.append(token)
        if(pilaOperadores[-1] == "*" or pilaOperadores[-1] == "/"):
            opDer = pilaId.pop()
            opIzq = pilaId.pop()

            operador = pilaOperadores.pop()
            generaCuadruplo(operador, opDer, opIzq, "12")
            

def generaCuadruplo(operador , opIzq, opDer , respuesta):
    print(operador,opIzq,opDer,respuesta)


    
    ##print(pilaOperadores)
    ##print(pilaId)
    





eval('4 + 5 * 6')