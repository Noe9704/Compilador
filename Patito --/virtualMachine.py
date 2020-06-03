# ------------------------------------------------------------
# Luis Marcelo Flores Canales A01280943
# Noé Flores Sifuentes A00949282
# ------------------------------------------------------------


import memoria
import sys

# Inicializamos la tabla de simbolos, cuadruplos y constantes
symbols = {}
quadruples = []
constants = {}

# Creamos los bloques de memoria correspondientes
memoriaGlobal = memoria.Memoria()
memoriaConstante = memoria.Memoria()
memoriaLocales = [memoria.Memoria()] # Este se genera en pilas para tener control del bloque

ip = [] # Sirve para regresar de la funcion
currentFunction = [] # Sirve para saber la funcion actual
paramPila = [] # Guardo los parametros de la funcion
returnArray = []

# Revisa que el al momento de ejecutar se envio un objeto
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

# Llenamos la memoria global con lo datos de la tabla de simbolos
for key in symbols['global']['vars'].keys():
    keyAddress = symbols['global']['vars'][key]['address']
    keyType = symbols['global']['vars'][key]['type']
    memoriaGlobal.inserta_Dir_Globales(keyAddress,keyType)

# Llenamos la memoria de constantes con los datos de la tabla de constantes
for key in constants.keys():
    keyValue = key
    keyType = constants[key]['type']
    memoriaConstante.inserta_Dir_Constantes(keyValue,keyType)

# Funcion para recorrer los cuadruplos
def ejecuta(cuad,pos):
    global ip, paramPila, currentFunction, returnArray
    # CurrentERA guarda la funcion actual, siempre se empieza por el main
    currentERA = 'main'

    # Funcion GOTO
    if(cuad[0] == 'GOTO'): 
        return int(cuad[3])

    # Funcion ENDPROC
    if(cuad[0] == 'ENDPROC'):
        # Se elimina la ultima posicion de la memoria local por que se termino la funcion
        memoriaLocales.pop()
        # Se saca de la pila la ultima funcion por que se termino
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
        
    # Funcion suma
    if cuad[0] == '+':
        # Guardo los cuadruplos
        opIzq = cuad[1] 
        opDer = cuad[2]
        resultado = cuad[3]

        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        resultadoCuad = -1

        # Busco el valor izquierdo en memoria, si no existe lo guardo
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

        # Busco el valor derecho en memoria, si no existe lo guardo
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

        # Hago la operacion con los resultados
        if(typeR == "int"):
            resultadoCuad = int(valorIzq) + int(valorDer )
        elif(typeR == "float"):
            resultadoCuad = float(valorIzq) + float(valorDer )

        # Asigno el nuevo valor en el bloque de memoria
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

    # Funcion resta
    if cuad[0] == '-':
        # Guardo los cuadruplos
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

        if resultado < 10000 : 
            keyAddress = resultado
            keyType = typeR
            memoriaGlobal[-1].inserta_Dir_Globales(keyAddress,keyType, resultadoCuad)
        elif resultado >= 10000 and resultado < 20000:
            keyAddress = resultado
            keyType = typeR
            memoriaLocales[-1].inserta_Dir_Locales(keyAddress, keyType, resultadoCuad)   
        elif resultado >= 20000 and resultado < 30000:
            keyAddress = resultado
            keyType = typeR
            memoriaConstante[-1].inserta_Dir_Constantes(keyAddress,keyType, resultadoCuad)
        
        return pos +1

    # Funcion multiplicacion
    elif cuad[0] == '*':
        # Guardo los cuadruplos
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

    # Funcion division
    elif cuad[0] == '/':
        # Guardo los cuadruplos
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
        
    # Funcion LESSTHAN
    elif cuad[0] == '<':
        # Guardo los cuadruplos
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

    # Funcion GREATERTHAN   
    elif cuad[0] == '>':
        # Guardo los cuadruplos
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
       
    # Funcion LESS THAN EQUAL
    elif cuad[0] == '<=':
        # Guardo los cuadruplos
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
      
    # Funcion GREATER THAN EQUAL
    elif cuad[0] == '>=':
        # Guardo los cuadruplos
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
      
    # Funcion de comparacion
    elif cuad[0] == '==':
        # Guardo los cuadruplos
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
    
    # Funcion del igual    
    elif cuad[0] == '=':
        # Guardo los cuadruplos
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

    # Funcion WRITE
    elif cuad[0] == 'write':
        resultado = cuad[3]
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

    # Funcion END
    elif cuad[0] == "END":
        print("Codigo ejecutado con exito! :)")
        return pos + 1

    # Funcion GOTOF
    elif cuad[0] == "GOTOF":
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
    # Funcion Read
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

    # Funcion ERA
    elif cuad[0] == "ERA":
        currentFunction.append(cuad[3])
        memoriaLocales.append(memoria.Memoria())

        list(symbols[cuad[3]]['params'])
        aux = 0
        
        while aux < len(list(symbols[cuad[3]]['params'])) :
            name = list(symbols[cuad[3]]['params'])[0]
            address = symbols[cuad[3]]['params'][name]['address']
            type1 = symbols[cuad[3]]['params'][name]['type']
            
            memoriaLocales[-1].inserta_Dir_Locales(address,type1,memoriaLocales[-2].getValue(address))
            aux +=1
        
        return pos + 1

    # Funcion GOSUB
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

    # Funcion PARAM
    elif cuad[0] == "PARAM":
        # Nuevo Parametro
        parametro = cuad[1]
        whichParam = cuad[3]
        splitParam = whichParam.find("r") + 1
        whichParam = int(whichParam[splitParam:len(whichParam)]) -1
        valueParam = None
        # Guardamos los datos del parametro de la funcion
        paramFunction = list(symbols[currentFunction[-1]]['params'])
        paramFunctionAddress =symbols[currentFunction[-1]]['params'][paramFunction[0]]['address']
        paramFunctionType =symbols[currentFunction[-1]]['params'][paramFunction[0]]['type']
        # Obtenemos el valor del parametro
        if parametro < 10000:
            valueParam = memoriaGlobal.getValue(parametro)
        elif parametro >= 10000 and parametro < 20000:
            valueParam = memoriaLocales[-1].getValue(parametro) 
            if (valueParam == None) :
                valueParam = memoriaLocales[-1].getValue(paramFunctionAddress)
        elif parametro >= 20000 and parametro < 30000:
            valueParam = memoriaConstante.getValue(parametro)

        # Lo asignamos, si no esta en esta memoria, lo buscamos en el bloque de memoria pasado
        if(valueParam == None):
            valueParam = memoriaLocales[-2].getValue(parametro)
        memoriaLocales[-1].upDateVal(paramFunctionAddress, valueParam)
            

        return pos + 1

    # Funcion Return
    elif cuad[0] == "return":

        if cuad[3] >= 20000:
            value = memoriaConstante.getValue(cuad[3])
        elif cuad[3] >= 10000 and cuad[3] < 20000:
            value = memoriaLocales[-1].getValue(cuad[3])
        elif cuad[3] < 10000:
            value = memoriaGlobal.getValue(cuad[3])

        direccionFuncion = symbols['global']['vars'][currentFunction[-1]]['address']
        memoriaGlobal.upDateVal(direccionFuncion,value)
    
        return pos + 1

    # Funcion OR
    elif cuad[0] == "|":
        # Guardo los cuadruplos
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
    
    # Funcion AND
    elif cuad[0] == "&" :
        # Guardo los cuadruplos
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
        
        resultadoCuad = bool(bool(valorIzq) and bool(valorDer))

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

        
# Contador para recorrer los caudrulos
cont = 0
# breakCont = 0

# While que se encarga de recorrer la lista de los cuadruplos
while cont < len(quadruples):
    # Se envia a la funcion el cuadruplo y su indice
    cont = ejecuta(quadruples[cont],cont)
 
    """
    breakCont += 1
    if(breakCont > 50) :
        break
    """
    
"""
print("Memoria Global")
print(memoriaGlobal)
print("Memoria Local")
print(memoriaLocales[0])
"""