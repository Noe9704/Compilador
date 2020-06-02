import memoria
import sys

symbols = {}
quadruples = []
constants = {}

memoriaGlobal = memoria.Memoria()
memoriaConstante = memoria.Memoria()
memoriaLocales = [memoria.Memoria()]

ip = [] # Sirve para regresar de la funcion
currentFunction = []
paramPila = [] # Guardo los parametros de la funcion
returnArray = []


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
    global ip, paramPila, currentFunction, returnArray
    currentERA = 'main'
    if(cuad[0] == 'GOTO'): 
        return int(cuad[3])
#ENDPROC
    if(cuad[0] == 'ENDPROC'):
       
        memoriaLocales.pop()

        
        currentFunctionName = currentFunction.pop()
        #print(currentFunctionName)
        """
        addressCurrentFunction = symbols['global']['vars'][currentFunctionName]['address']
        typeCurrentFunction = symbols['global']['vars'][currentFunctionName]['type']
        
        value = returnArray.pop()
        address = value[0]
        values = value[1]


        #print("addres",address)
        #print("value",values)
        #print("adc",addressCurrentFunction)
        
        memoriaGlobal.upDateVal(addressCurrentFunction,values)
        """
        return ip.pop()
        

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
            #print("valorIZQ",valorIzq)
            #print("memoriaLocalIZQ",memoriaLocales[-1])
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
            memoriaGlobal[-1].inserta_Dir_Globales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress, keyType, resultadoCuad)  
            #print("memoriaLocalEnresta",memoriaLocales[-1])   
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaConstante[-1].inserta_Dir_Constantes(keyAddress,keyType, resultadoCuad)
        
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
        # print("resultado",cuad)
        if resultado < 10000 :
            valor = memoriaGlobal.getValue(resultado)
            #print("Valor",valor)         
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
        #Funcion en la que estoy
        currentFunction.append(cuad[3])
        memoriaLocales.append(memoria.Memoria())

        list(symbols[cuad[3]]['params'])
        aux = 0
        
        while aux < len(list(symbols[cuad[3]]['params'])) :
            name = list(symbols[cuad[3]]['params'])[0]
            address = symbols[cuad[3]]['params'][name]['address']
            type1 = symbols[cuad[3]]['params'][name]['type']
            # Error aqui
            
            memoriaLocales[-1].inserta_Dir_Locales(address,type1,memoriaLocales[-2].getValue(address))
            
            aux +=1

        #print("CurrentFunction", currentFunction[-1])
        print("memoriaLocalesERA", memoriaLocales[-1])
        return pos + 1
# GOSUB

    elif cuad[0] == "GOSUB":
        ip.append(pos + 1)
        """
        iCont = 0
        while iCont < len(paramPila) :
            varAddress = paramPila[iCont][1]
            type1 = memoriaLocales[-1].getType(varAddress)
            valor = paramPila[iCont][0]
            #print("curr",currentFunction[-1])
            #Change value
            newVar = list(symbols[currentFunction[-1]]['params'])[iCont]
            newVarAddress =symbols[currentFunction[-1]]['params'][newVar]['address']
            newVarType = symbols[currentFunction[-1]]['params'][newVar]['type']
            if newVarAddress >= 10000 and newVarAddress < 20000:
                memoriaLocales[-1].inserta_Dir_Locales(newVarAddress,newVarType,valor)
            
            iCont += 1
            print("MEMORIALOCAL",memoriaLocales[-1])
        paramPila = []
        """
        return symbols[cuad[3]]['start']

#PARAM
    elif cuad[0] == "PARAM":
        # Nuevo Parametro
        parametro = cuad[1]
        whichParam = cuad[3]
        splitParam = whichParam.find("r") + 1
        whichParam = int(whichParam[splitParam:len(whichParam)]) -1
        valueParam = None
        
        print("valueParam", valueParam)
        paramFunction = list(symbols[currentFunction[-1]]['params'])
        paramFunctionAddress =symbols[currentFunction[-1]]['params'][paramFunction[0]]['address']
        paramFunctionType =symbols[currentFunction[-1]]['params'][paramFunction[0]]['type']

        print("MemoriaLocalParam", memoriaLocales[-2])
        if parametro < 10000:
            valueParam = memoriaGlobal.getValue(parametro)
        elif parametro >= 10000 and parametro < 20000:
            valueParam = memoriaLocales[-1].getValue(parametro) # Error aqui
            if (valueParam == None) :
                valueParam = memoriaLocales[-1].getValue(paramFunctionAddress)
        elif parametro >= 20000 and parametro < 30000:
            valueParam = memoriaConstante.getValue(parametro)

        print("MemoriaLocalParam", memoriaLocales[-1])
        ####
        # ERROR
        memoriaLocales[-1].upDateVal(paramFunctionAddress, valueParam)

        print("MemoriaLocalParam", memoriaLocales[-1])

        return pos + 1

#Return
    elif cuad[0] == "return":

        if cuad[3] >= 20000:
            value = memoriaConstante.getValue(cuad[3])
        elif cuad[3] >= 10000 and cuad[3] < 20000:
            value = memoriaLocales[-1].getValue(cuad[3])
        elif cuad[3] < 10000:
            value = memoriaGlobal.getValue(cuad[3])

        direccionFuncion = symbols['global']['vars'][currentFunction[-1]]['address']
        memoriaGlobal.upDateVal(direccionFuncion,value)
        #print("value",value)
        #print("cuad",cuad[3])
        """
        print("Hola")
        print("ReturnArray", returnArray)
        returnArray.append([cuad[3],value])
        """
    
        return pos + 1
#OR
    elif cuad[0] == "|":
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
        
        resultadoCuad = bool(bool(valorIzq) or bool(valorDer))

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
    
#And
    elif cuad[0] == "&" :
        return pos +1

        
    
        
    

cont = 0
breakCont = 0
while cont < len(quadruples):
    #print(cont,quadruples[cont])
    cont = ejecuta(quadruples[cont],cont)
    ##print(cont)
    #i = switch(quad[i], i)
    """
    breakCont += 1
    if(breakCont > 30) :
        break
    """
    
"""
print("Memoria Global")
print(memoriaGlobal)
print("Memoria Local")
print(memoriaLocales[0])
"""