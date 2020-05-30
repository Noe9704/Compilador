

cuadruplo = [["+",10001,10002,10003],["-",10004,10005,10006],["*",10007,10008,10009]]

def ejecuta():
    global cuadruplo 
    cuad = cuadruplo[0]
    if cuad[0] == '+':
        opIzq = cuad[1]
        opDer = cuad[2]
        valorIzq = opIzq
        valorDer = opDer
        nuevoResultado = valorIzq + valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        cuadruplo.pop(0)
        ##contador
        ##return contador
        
        print(cuadruplo[0])
    elif cuad[0] == '-':
        opIzq = cuad[1]
        opDer = cuad[2]

        valorIzq = opIzq
        valorDer = opDer
        nuevoResultado = valorIzq - valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        cuadruplo.pop(0)
        ##contador
        ##return contador
        
        print(cuadruplo[0])
    elif cuad[0] == '*':
        opIzq = cuad[1]
        opDer = cuad[2]

        valorIzq = opIzq
        valorDer = opDer
        nuevoResultado = valorIzq * valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        cuadruplo.pop(0)
        ##contador
        ##return contador
        
        print(cuadruplo[0])
    elif cuad[0] == '/':
        opIzq = cuad[1]
        opDer = cuad[2]

        valorIzq = opIzq
        valorDer = opDer
        nuevoResultado = valorIzq / valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        cuadruplo.pop(0)
        ##contador
        ##return contador
        
        print(cuadruplo[0])
    elif cuad[0] == '<':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq < valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        cuadruplo.pop(0)
        ##contador
        ##return contador
        
        print(cuadruplo[0])
    elif cuad[0] == '>':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq > valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        cuadruplo.pop(0)
        ##contador
        ##return contador        
        print(cuadruplo[0])

    elif cuad[0] == '<=':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq <= valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        cuadruplo.pop(0)
        ##contador
        ##return contador        
        print(cuadruplo[0])

    elif cuad[0] == '>=':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq <= valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        cuadruplo.pop(0)
        ##contador
        ##return contador        
        print(cuadruplo[0])

    elif cuad[0] == '==':
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0
        nuevoResultado = valorIzq == valorDer
        ##actualiza el resultado del cuadruplo  con nuevoResultado
        cuadruplo.pop(0)
        ##contador
        ##return contador        
        print(cuadruplo[0])
       
    elif cuad[0] == '=':
        '''
        opIzq = cuad[1]
        opDer = cuad[2]
        resultado = cuad[3]
        ##resultado a memoria
        valorIzq = 0
        valorDer = 0


        cuadruplo.pop(0)
        ##contador
        ##return contador        
        print(cuadruplo[0])
        '''




    '''
    elif cuad[0] == 'write':
        resultado = cuad[3]
        valorResultado = resultado ## se manda a memoria el memory.getValor(resultado)
        
        
        print(cuadruplo[0])
    '''




if __name__ == "__main__":
    ejecuta()        