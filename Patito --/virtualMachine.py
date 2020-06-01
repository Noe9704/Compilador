import memoria
import sys

symbols = {}
quadruples = []
constants = {}

memoriaGlobal = memoria.Memoria()
memoriaConstante = memoria.Memoria()
memoriaLocales = [memoria.Memoria()]

ip = 0 # Sirve para regresar de la funcion
paramPila = [] # Guardo los parametros de la funcion

if len(sys.argv) != 2:
    print('Error, leyendo el objeto del archivo')
    raise SyntaxError('Necesitas enviar un archivo .txto correcto')
else: 
    data = sys.argv[1]
    with open(data, 'r', newline='\n') as file:
        inputRead = eval(file.read())
        symbols = inputRead['symbols']
        quadruples = inputRead['quadruples']
        constants = inputRead['constants']
        #run()

for key in symbols['global']['vars'].keys():
    keyAddress = symbols['global']['vars'][key]['address']
    keyType = symbols['global']['vars'][key]['type']
    memoriaGlobal.inserta_Dir_Globales(keyAddress,keyType)


for key in constants.keys():
    keyValue = key
    keyType = constants[key]['type']
    memoriaConstante.inserta_Dir_Constantes(keyValue,keyType)

"""
print("Memoria Virtual")
print(memoriaGlobal)
print("Constantes")
print(memoriaConstante)
print("Locales")
print(memoriaLocales[0])
"""

def ejecuta(cuad,pos):
    global ip
    currentERA = 'main'
    if(cuad[0] == 'GOTO'): 
        return int(cuad[3])
#ENDPROC
    if(cuad[0] == 'ENDPROC'):
        if len(memoriaLocales) > 1:
            memoriaLocales.pop()
        return ip
        

    if cuad[0] == '+':
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        type1 = memoriaGlobal.getType(opIzq)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if opDer < 10000 :
            valorDer = memoriaGlobal.getValue(opDer)
        elif opDer >= 10000 and opDer < 20000:
            valorDer = memoriaLocales[-1].getValue(opDer)
            if valorDer == None:
                keyAddress = opDer
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorDer = memoriaLocales[-1].getValue(opDer)                      
        elif opDer >= 20000 and opDer < 30000:
            valorDer = memoriaConstante.getValue(opDer)
        type2 = memoriaGlobal.getType(opDer)
        
        typeR = memoriaGlobal.getType(resultado)

        if(typeR == "int"):
            resultadoCuad = int(valorIzq) + int(valorDer )
        elif(typeR == "float"):
            resultadoCuad = float(valorIzq) + float(valorDer )

        #print("res", resultadoCuad)
        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)     
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        
        return pos +1
##Resta
    if cuad[0] == '-':
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        type1 = memoriaGlobal.getType(opIzq)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if opDer < 10000 :
            valorDer = memoriaGlobal.getValue(opDer)
        elif opDer >= 10000 and opDer < 20000:
            valorDer = memoriaLocales[-1].getValue(opDer)
            if valorDer == None:
                keyAddress = opDer
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorDer = memoriaLocales[-1].getValue(opDer)                      
        elif opDer >= 20000 and opDer < 30000:
            valorDer = memoriaConstante.getValue(opDer)
        type2 = memoriaGlobal.getType(opDer)
        
        typeR = memoriaGlobal.getType(resultado)

        if(typeR == "int"):
            resultadoCuad = int(valorIzq) - int(valorDer )
        elif(typeR == "float"):
            resultadoCuad = float(valorIzq) - float(valorDer )

        #print("res", resultadoCuad)
        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)     
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        
        return pos +1
## Mult
    elif cuad[0] == '*':
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        type1 = memoriaGlobal.getType(opIzq)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if opDer < 10000 :
            valorDer = memoriaGlobal.getValue(opDer)
        elif opDer >= 10000 and opDer < 20000:
            valorDer = memoriaLocales[-1].getValue(opDer)
            if valorDer == None:
                keyAddress = opDer
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorDer = memoriaLocales[-1].getValue(opDer)                      
        elif opDer >= 20000 and opDer < 30000:
            valorDer = memoriaConstante.getValue(opDer)
        type2 = memoriaGlobal.getType(opDer)
        
        typeR = memoriaGlobal.getType(resultado)

        if(typeR == "int"):
            resultadoCuad = int(valorIzq) * int(valorDer )
        elif(typeR == "float"):
            resultadoCuad = float(valorIzq) * float(valorDer )

        #print("res", resultadoCuad)
        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)     
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        
        return pos +1

## Div
    elif cuad[0] == '/':
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        type1 = memoriaGlobal.getType(opIzq)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if opDer < 10000 :
            valorDer = memoriaGlobal.getValue(opDer)
        elif opDer >= 10000 and opDer < 20000:
            valorDer = memoriaLocales[-1].getValue(opDer)
            if valorDer == None:
                keyAddress = opDer
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorDer = memoriaLocales[-1].getValue(opDer)                      
        elif opDer >= 20000 and opDer < 30000:
            valorDer = memoriaConstante.getValue(opDer)
        type2 = memoriaGlobal.getType(opDer)
        
        typeR = memoriaGlobal.getType(resultado)

        if(typeR == "int"):
            resultadoCuad = int(valorIzq) / int(valorDer )
        elif(typeR == "float"):
            resultadoCuad = float(valorIzq) / float(valorDer )

        #print("res", resultadoCuad)
        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)     
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        
        return pos +1
        
## LESSTHAN
    elif cuad[0] == '<':
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        type1 = memoriaGlobal.getType(opIzq)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if opDer < 10000 :
            valorDer = memoriaGlobal.getValue(opDer)
        elif opDer >= 10000 and opDer < 20000:
            valorDer = memoriaLocales[-1].getValue(opDer)
            if valorDer == None:
                keyAddress = opDer
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorDer = memoriaLocales[-1].getValue(opDer)                      
        elif opDer >= 20000 and opDer < 30000:
            valorDer = memoriaConstante.getValue(opDer)
        type2 = memoriaGlobal.getType(opDer)
        
        typeR = memoriaGlobal.getType(resultado)
        #print("type", typeR)
        
        resultadoCuad = bool(int(valorIzq) < int(valorDer ))

        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)     
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        
        return pos +1
## GREATERTHAN   
    elif cuad[0] == '>':
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        type1 = memoriaGlobal.getType(opIzq)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if opDer < 10000 :
            valorDer = memoriaGlobal.getValue(opDer)
        elif opDer >= 10000 and opDer < 20000:
            valorDer = memoriaLocales[-1].getValue(opDer)
            if valorDer == None:
                keyAddress = opDer
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorDer = memoriaLocales[-1].getValue(opDer)                      
        elif opDer >= 20000 and opDer < 30000:
            valorDer = memoriaConstante.getValue(opDer)
        type2 = memoriaGlobal.getType(opDer)
        
        typeR = memoriaGlobal.getType(resultado)
        
        resultadoCuad = bool(int(valorIzq) > int(valorDer ))

        """
        if(typeR == "int"):
            if(int(valorIzq) < int(valorDer )):
                resultadoCuad = True
            else:
                resultadoCuad = False
        elif(typeR == "float"):
            if(float(valorIzq) < float(valorDer )):
                resultadoCuad = True
            else:
                resultadoCuad = False
        """
        #print("res", resultadoCuad)
        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)     
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        
        return pos +1       
       
## LESS THAN EQUAL
    elif cuad[0] == '<=':
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        type1 = memoriaGlobal.getType(opIzq)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if opDer < 10000 :
            valorDer = memoriaGlobal.getValue(opDer)
        elif opDer >= 10000 and opDer < 20000:
            valorDer = memoriaLocales[-1].getValue(opDer)
            if valorDer == None:
                keyAddress = opDer
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorDer = memoriaLocales[-1].getValue(opDer)                      
        elif opDer >= 20000 and opDer < 30000:
            valorDer = memoriaConstante.getValue(opDer)
        type2 = memoriaGlobal.getType(opDer)
        
        typeR = memoriaGlobal.getType(resultado)
        
        resultadoCuad = bool(int(valorIzq) <= int(valorDer ))

        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)     
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        
        return pos +1             
      
# GREATER THAN EQUAL
    elif cuad[0] == '>=':
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        type1 = memoriaGlobal.getType(opIzq)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if opDer < 10000 :
            valorDer = memoriaGlobal.getValue(opDer)
        elif opDer >= 10000 and opDer < 20000:
            valorDer = memoriaLocales[-1].getValue(opDer)
            if valorDer == None:
                keyAddress = opDer
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorDer = memoriaLocales[-1].getValue(opDer)                      
        elif opDer >= 20000 and opDer < 30000:
            valorDer = memoriaConstante.getValue(opDer)
        type2 = memoriaGlobal.getType(opDer)
        
        typeR = memoriaGlobal.getType(resultado)
        
        resultadoCuad = bool(int(valorIzq) >= int(valorDer ))

        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)     
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        
        return pos +1       
      
#Compare
    elif cuad[0] == '==':
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        type1 = memoriaGlobal.getType(opIzq)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if opDer < 10000 :
            valorDer = memoriaGlobal.getValue(opDer)
        elif opDer >= 10000 and opDer < 20000:
            valorDer = memoriaLocales[-1].getValue(opDer)
            if valorDer == None:
                keyAddress = opDer
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorDer = memoriaLocales[-1].getValue(opDer)                      
        elif opDer >= 20000 and opDer < 30000:
            valorDer = memoriaConstante.getValue(opDer)
        type2 = memoriaGlobal.getType(opDer)
        
        typeR = memoriaGlobal.getType(resultado)
        
        resultadoCuad = bool(int(valorIzq) == int(valorDer ))

        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)     
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, resultadoCuad)
        
        return pos +1           
       
#EQUAL    
#EQUAL    
    elif cuad[0] == '=':
        opIzq = cuad[1] 
        opDer = cuad[2] # Siempre es None por el igual
        resultado = cuad[3]
        
        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1
        # Solo sacamos tipo1 porque el otro siempre es None
        type1=memoriaGlobal.getType(resultado)
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if resultado < 10000 :
            resultadoCuad = memoriaGlobal.getValue(resultado)
            memoriaGlobal.upDateVal(resultado,valorIzq)
        elif resultado >= 10000 and resultado < 20000:
            keyValue = valorIzq
            keyAddress = resultado
            keyType = memoriaLocales[-1].getType(resultado)
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType,keyValue)
            resultadoCuad = memoriaLocales[-1].getValue(resultado) 
        elif resultado >= 20000 and resultado < 30000:
            resultadoCuad = memoriaConstante.getValue(resultado)
        
        return pos +1

    elif cuad[0] == 'write':
        resultado = cuad[3]
        #print("resultado",cuad)
        if resultado < 10000 :
            valor = memoriaGlobal.getValue(resultado)         
        elif resultado >= 10000 and resultado < 20000:
            valor = memoriaLocales[-1].getValue(resultado)    
        elif resultado >= 20000 and resultado < 30000:
            valor = memoriaConstante.getValue(resultado)
        
        if(valor == -1):
            print("Variable sin asignacion")
            sys.exit()
        else :
            print(valor)
        return pos + 1

    elif cuad[0] == "END":
        print("Codigo ejecutado con exito! :)")
        return pos + 1
    
    elif cuad[0] == "GOTOF":
        #print(cuad)
        opIzq = cuad[1] 
        opDer = cuad[2] # Siempre es None por el igual
        resultado = cuad[3] # Determinante del true o false

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1
        # Solo sacamos tipo1 porque el otro siempre es None
        type1=memoriaGlobal.getType(resultado)

        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == None:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, keyAddress)
                valorIzq = memoriaLocales[-1].getValue(opIzq)                      
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)

        if(valorIzq == False) :
            return resultado
        else:
            return pos + 1
#READ
    elif cuad[0] == "read":
        
        var = input()
        direccion = cuad[3]
        if direccion < 10000 :
            memoriaGlobal.upDateVal(direccion,var)
        elif direccion >= 10000 and direccion < 20000:
            valorIzq = memoriaLocales[-1].getValue(direccion)
            if valorIzq == None:
                keyAddress = direccion
                keyType = memoriaLocales[-1].getType(direccion)
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType, var)
            else :
                memoriaLocales.upDateVal(direccion,var)   
        
        return pos + 1             

# ERA
    elif cuad[0] == "ERA":
        #print(cuad)
        memoriaLocales.append(memoria.Memoria())

        return pos + 1
# GOSUB

    elif cuad[0] == "GOSUB":
        ip = pos + 1
        return symbols[cuad[3]]['start']

#PARAM
    elif cuad[0] == "PARAM":
        return pos + 1

#Return
    elif cuad[0] == "RETURN":
        return pos + 1

        
    
        
    

cont = 0
while cont < len(quadruples):
    #print(cont,quadruples[cont])
    cont = ejecuta(quadruples[cont],cont)
    ##print(cont)
    #i = switch(quad[i], i)
print("Memoria Local")
print(memoriaLocales[0])