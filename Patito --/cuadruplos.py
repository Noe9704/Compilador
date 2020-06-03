# No se utiliza
import sys

cont = 0 
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
        print("Token:")
        print(token)
        if(token not in opsEXP):
            pilaId.append(token)
        else :
            pilaOperadores.append(token)
            continue
          
        if len(pilaOperadores) > 0:
          if(pilaOperadores[-1] == "*" or pilaOperadores[-1] == "/"):
              opIzq = pilaId.pop()
              opDer = pilaId.pop()
            
              operador = pilaOperadores.pop()
              generaCuadruplo(operador, opDer, opIzq,"t" + str(cont))
                  
      
 
def generaCuadruplo(operador , opDer, opIzq , respuesta):
    global cont
    cont = cont + 1
    print(operador,opDer,opIzq,respuesta)
    pilaId.append(respuesta)

eval('A + B * C / D - E')
    
    ##print(pilaOperadores)
    ##print(pilaId)