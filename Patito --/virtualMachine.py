import memoria
import sys

symbols = {}
quadruples = []
constants = {}

memoriaGlobal = memoria.Memoria()
memoriaConstante = memoria.Memoria()
memoriaLocales = []

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



print("Memoria Virtual")
print(memoriaGlobal)
print("Constantes")
print(memoriaConstante)

# quadruples = [["+",10001,10002,10003],["-",10004,10005,10006],["*",10007,10008,10009]]

def ejecuta(cuad,pos):
    currentERA = 'main'
    if(cuad[0] == 'GOTO'): 
        return int(cuad[3])

    if(cuad[0] == 'ENDPROC'):
        return pos + 1 

    if cuad[0] == '+':
        memTem = memoria.Memoria()
        opIzq = cuad[1] # Direccion de memoria 1
        opDer = cuad[2]

        type1=memoriaGlobal.getType(opIzq)
        type2=memoriaGlobal.getType(opDer)

        #valorIzq = opIzq # Traer datos de la direccion
        #valorDer = opDer
        print(memoriaConstante.getValue(opIzq))
        if(type1 == 'int') :
            valorIzq = memoriaConstante.getValue(opIzq)
        elif(type1 == 'float') :
            valorIzq = memoriaConstante.getValue(opIzq)
        elif(type1 == 'char') :
            valorIzq = memoriaConstante.getValue(opIzq)
        elif(type1 == 'bool') :
            valorIzq = memoriaConstante.getValue(opIzq)
        print("Valor")
        print(valorIzq)
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
        
        print(quadruples[0])
    
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
        
        print(quadruples[0])
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
        
        print(quadruples[0])
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
        
        print(quadruples[0])
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
        print(quadruples[0])

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
        print(quadruples[0])

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
        print(quadruples[0])

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
        print(quadruples[0])
       
    elif cuad[0] == '=':
        print("Estoy en '='")
        opIzq = cuad[1] # Direccion de memoria
        opDer = cuad[2] # Siempre es None por el igual

        # Revisar que exista en tabla de constantes, locales, globales
        # Asignar valor encontrado o direccion encontrada en valorIzq o valorDer



        ##resultado a memoria
        valorIzq = 0
        valorDer = 0

        # Solo sacamos tipo1 porque el otro siempre es None
        type1=memoriaGlobal.getType(opIzq)

        # Traer datos de la direccion
        # Buscamos si no es global
        if(type1 == 'int') :
            valorIzq = memoriaConstante.getValue(opIzq)
        elif(type1 == 'float') :
            valorIzq = memoriaConstante.getValue(opIzq)
        elif(type1 == 'char') :
            valorIzq = memoriaConstante.getValue(opIzq)
        elif(type1 == 'bool') :
            valorIzq = memoriaConstante.getValue(opIzq)
            
        resultado = valorIzq


        #valorIzq = opIzq # Traer datos de la direccion
        #valorDer = opDer      
        return pos +1
        




    '''
    elif cuad[0] == 'write':
        resultado = cuad[3]
        valorResultado = resultado ## se manda a memoria el memory.getValor(resultado)
        
        
        print(cuadruplo[0])
    '''




cont = 0
while quadruples[cont][0] != 'END':
    print(quadruples[cont])
    
    cont = ejecuta(quadruples[cont],cont)
    print(cont)
    #i = switch(quad[i], i)
     