import sys

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
        
        if(token not in opsEXP):
            pilaId.append(token)
        else :
            pilaOperadores.append(token)
        print(pilaOperadores)    
        
        if len(pilaOperadores) > 1:
            if(pilaOperadores[len(pilaOperadores)- 1] == "+" or pilaOperadores[len(pilaOperadores)-1] == "-"):
                opDer = pilaId.pop()
                opIzq = pilaId.pop()
                operador = pilaOperadores.pop()
            else :
                print("ERROR DE SUMA")
                sys.exit()
            if(pilaOperadores[-1] == "*" or pilaOperadores[-1] == "/"):
                opDer = pilaId.pop()
                opIzq = pilaId.pop()
                operador = pilaOperadores.pop()
            else :
                print("ERROR DE MULTIPLICACION")
                sys.exit()
            generaCuadruplo(operador,opDer,opIzq,"12")
            
        
       





        '''     
        if(token in opsEXP):
            pilaOperadores.append(token)            
        else:
            pilaId.append(token) 
            if len(pilaOperadores) > 0:
              if(pilaOperadores[-1] == "*" or pilaOperadores[-1] == "/"):
                  opDer = pilaId.pop()
                  opIzq = pilaId.pop()
              
                  operador = pilaOperadores.pop()
                  generaCuadruplo(operador, opDer, opIzq,"12")
                  '''
      

            
         
            


            
def generaCuadruplo(operador , opDer, opIzq , respuesta):
    print(operador,opDer,opIzq,respuesta)
    ##pilaId.append(respuesta)

eval('4 + 5 * 6')
    
    ##print(pilaOperadores)
    ##print(pilaId)
    





