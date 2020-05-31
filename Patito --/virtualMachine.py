import memoria
import sys

symbols = {}
quadruples = []
constants = {}

memoriaGlobal = memoria.Memoria()
memoriaConstante = memoria.Memoria()
memoriaLocales = [memoria.Memoria()]

if len(sys.argv) != 2:
    print('Error, leyendo el objeto del archivo')
    raise SyntaxError('Necesitas enviar un archivo .txto correcto')
else: 
    data = sys.argv[1]
    with open(data, 'r', newline='\n') as file:
        input = eval(file.read())
        symbols = input['symbols']
        quadruples = input['quadruples']
        constants = input['constants']
        #run()

for key in symbols['global']['vars'].keys():
    keyAddress = symbols['global']['vars'][key]['address']
    keyType = symbols['global']['vars'][key]['type']
    memoriaGlobal.inserta_Dir_Globales(keyAddress,keyType)

for key in constants.keys():
    keyValue = key
    keyType = constants[key]['type']
    memoriaConstante.inserta_Dir_Constantes(keyValue,keyType)


'''
print("Memoria Virtual")
print(memoriaGlobal)
print("Constantes")
print(memoriaConstante)
'''

# quadruples = [["+",10001,10002,10003],["-",10004,10005,10006],["*",10007,10008,10009]]

##example = [['GOTO', None, None, 3], ['+', 10001, 20000, 10002], ['=', 10002, None, 10000], ['ENDPROC', None, None, None], ['=', 20000, None, 10004], ['+', 10006, 20001, 10008], ['=', 10008, None, 10005], ['END', None, None, None]]

def ejecuta(cuad,pos):
    currentERA = 'main'
    if(cuad[0] == 'GOTO'): 
        return int(cuad[3])

    if(cuad[0] == 'ENDPROC'):
        if len(memoriaLocales) > 1:
            memoriaLocales.pop()
        return pos + 1 

    if cuad[0] == '+':
        memTem = memoria.Memoria()
        opIzq = cuad[1] # Direccion de memoria 1
        opDer = cuad[2]

        type1=memoriaGlobal.getType(opIzq)
        type2=memoriaGlobal.getType(opDer)

        #valorIzq = opIzq # Traer datos de la direccion
        #valorDer = opDer
        ##print(memoriaConstante.getValue(opIzq))
        if(type1 == 'int') :
            valorIzq = memoriaConstante.getValue(opIzq)
        elif(type1 == 'float') :
            valorIzq = memoriaConstante.getValue(opIzq)
        elif(type1 == 'char') :
            valorIzq = memoriaConstante.getValue(opIzq)
        elif(type1 == 'bool') :
            valorIzq = memoriaConstante.getValue(opIzq)
        ##print("Valor")
        ##print(valorIzq)
        #valorIzq = memoriaGlobal

        #nuevoResultado = valorIzq + valorDer # Operacion de los valores

        #memoriasTemporales.append(memTem)
    elif cuad[0] == '-':
        opIzq = cuad[1]
        opDer = cuad[2]

        valorIzq = opIzq
        valorDer = opDer
        nuevoResultado = valorIzq - valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        quadruples.pop(0)
        ##contador
        ##return contador
        
        ##print(quadruples[0])
    
    elif cuad[0] == '*':
        opIzq = cuad[1]
        opDer = cuad[2]

        valorIzq = opIzq
        valorDer = opDer
        nuevoResultado = valorIzq * valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        quadruples.pop(0)
        ##contador
        ##return contador
        
        ##print(quadruples[0])
    elif cuad[0] == '/':
        opIzq = cuad[1]
        opDer = cuad[2]

        valorIzq = opIzq
        valorDer = opDer
        nuevoResultado = valorIzq / valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        quadruples.pop(0)
        ##contador
        ##return contador
        
      
    elif cuad[0] == '<':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq < valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        quadruples.pop(0)
        ##contador
        ##return contador
        
       
    elif cuad[0] == '>':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq > valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        quadruples.pop(0)
        ##contador
        ##return contador        
       

    elif cuad[0] == '<=':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq <= valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        quadruples.pop(0)
        ##contador
        ##return contador        
      

    elif cuad[0] == '>=':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq <= valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        quadruples.pop(0)
        ##contador
        ##return contador        
      

    elif cuad[0] == '==':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq == valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        quadruples.pop(0)
        ##contador
        ##return contador        
       
       
    elif cuad[0] == '=':
        opIzq = cuad[1] 
        opDer = cuad[2] # Siempre es None por el igual
        ##resultado a memoria
        valorIzq = -1
        valorDer = -1
        # Solo sacamos tipo1 porque el otro siempre es None
        type1=memoriaGlobal.getType(opIzq)
        print("OpIzq")
        print(opIzq) 
        if opIzq < 10000 :
            valorIzq = memoriaGlobal.getValue(opIzq)
        elif opIzq >= 10000 and opIzq < 20000:
            valorIzq = memoriaLocales[-1].getValue(opIzq)
            if valorIzq == -1:
                keyAddress = opIzq
                keyType = type1
                memoriaLocales[-1].inserta_Dir_Locales(keyAddress,keyType)
                valorIzq = memoriaLocales[-1].getValue(opIzq) 
                     
        elif opIzq >= 20000 and opIzq < 30000:
            valorIzq = memoriaConstante.getValue(opIzq)
        return pos +1

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
        

    elif cuad[0] == "END":
        print("Codigo ejecutado con exito! :)")
        return pos + 1

        
    


    
        
    
    

cont = 0
while quadruples[cont][0] != 'END':
    
    print(quadruples[cont])
    
    
    cont = ejecuta(quadruples[cont],cont)
    ##print(cont)
    #i = switch(quad[i], i)

     