<h1>Manual de usuario del lenguaje Patito--</h1>
<hr>
<h3>Para empezar</h3>
<p> El lenguaje patito esta estructurado de una forma sencilla y amigable con el usuario, para que este pueda codificar de una </p>
<p> manera sencilla  </p>
<p> Primero, para empezar es necesario crear un programa, la sintaxis correcta para crear un programa es la siguiente</p>
<pre>
    <code>program patito:
          main(){}  
    </code>
</pre>

<h3>Declarar una variable</h3>
<p>Despues de declarar de forma correcta un programa, el siguiente paso es poder crear una variable</p>
<p> El lenguaje patito soporta la declaracion de tipos enteros,flotantes y strings</p>
<p> Patito no permite la declaracion de variables booleanas, pero este tipo de dato si es usado al momento de realizar comparaciones</p>
<p> Una vez que sabemos esto, podemos empezar a declarar variables como en el siguiente ejemplo</p>
<pre>
    <code>program patito:
          main()
         var int : x,y;
         var float : z;
        {
        }
          </code>
</pre>
<p> Es importante mencionar que patito solamente permite la declaracion de variables en la parte superior de la funcion</p>
<p> Si se intenta hacer una declaracion de variable dentro del bloque de la funcion, se producira un error</p>

<h3>Asignar valor a una variable</h3>
<p> El objetivo de una variable es la de manipular y almacenar datos, entonces la sintaxis correcta en patito para hacer eso es la siguiente</p>
<p> El lenguaje patito permite hacer uso de diferentes operaciones aritmeticas y logicas </p>
<p> operadores permitidos: + , - , *, /, = , ==, <, >, <=, >= </p>
<pre>
    <code>program patito:
          main()
         var int : x,y;
         var float : z;
        {
            x = 2 + 3;
            z = 2.5;
        }
          </code>
</pre>
<p>* No intentes asignar un valor a una variable que no concuerde con el tipo, o te marcara un error de tipos </p>
<p></p>

<h3>Escribir en la consola</h3>
<p>Es muy posible que quieres mostrar en pantalla ya sean mensajes o valores de variables, para hacer esto </p>
<p>Es necesario seguir la siguiente sintaxis</p>
<pre>
    <code>program patito:
          main()
         var int : x,y;
         var float : z;
        {
            x = 2 + 3;
            z = 2.5;
            write("Hola mundo, el valor de mi variable es:");
            write(x);
        }
        </code>
</pre>
<p>Al ejecutar el ejemplo anterior , se mostrara en la terminal de la siguiente forma</p>
<pre>
    <code>
            "Hola mundo, el valor de mi variable es:"
            5
            Codigo ejecutado con exito! :) 
        </code>
</pre>

<p></p>

<h3>Ingresar datos a una variable por medio de un input</h3>
<p>Muchos programas requieren de la interaccion con el usuario, y muchas veces se necesita ingresar valores directamente del teclado</p>
<p>Para hacer eso  es necesario seguir la siguiente sintaxis</p>
<pre>
    <code>program patito:
          main()
         var int : x,y;
         var float : z;
        {
            read(x);
            write("Hola mundo, el valor de mi variable es:",x);
        }
        </code>
</pre>
<p>Como se puede observar en el ejemplo pasado, es posible desplegar distintos mensajes siempre y cuando se separe con una coma (,)</p>
<p></p>

<h3>Uso de condicionales</h3>
<p>El uso de condicionales es soportado por el lenguaje patito, y funciona de manera que si se cumple una condicion</p>
<p>entonces se seguira por un camino, de lo contrario seguira otra ruta</p>
<p>Para hacer eso es necesario seguir la siguiente sintaxis</p>
<pre>
    <code>
        if ((n == 1) | (n == 2)) so {
          return (1);
        } else {
         return (3);
       }
        </code>
</pre>
<p></p>

<h3>Declarar una funcion con retorno de datos</h3>
<p>Para poder declarar una funcion es necesario seguir la siguiente sintaxis</p>
<pre>
    <code>
    program patito:
    funcion int fibonacci(int n): 
    var int : w,x;
    {
    if ((n == 1) | (n == 2)) so {
      return (1);
    } else {
            return (fibonacci(n-1) + fibonacci(n-2));
        }
    }
    main()
    var int : x, num;
    {
        write("Escribe el numero de la sucesion que deseas");
        read(x);
        write(fibonacci(x));
    }
     </code>
</pre>
<p>Como se puede observar en el ejemplo anterior, se creo el clasico ejemplo de la funcion fibonacci</p>
<p>El ejemplo pasado es un ejemplo perfecto para poder practicar el uso de funciones y recursividad</p>
<p></p>


<h3>Ciclo while</h3>
<p>Patito permite el uso de ciclo de tipo while, el cual ejecutara una instruccion hasta que se cumpla alguna condicion</p>
<p>Ejemplo de sintaxis a continuacion </p>

<pre>
    <code>
    program patito:

    funcion int prueba(int n):
    var int : actual,ant1,ant2,k;          
    {
    actual = 1;
    while(actual <= n)do{
    write("hola mundo");

    actual = actual + 1;
   }
}

main()
var int : x, num;
{
   write("Escribe la cantidad de veces que quieres que se escriba el mensaje:");
   read(x);
   prueba(x);
}

</code>
</pre>
<p>Al ejecutar el codigo anterior, el resultado se deplegara en la terminal de la siguiente forma</p>

<pre>
    <code>
        "Escribe la cantidad de veces que quieres que se escriba el mensaje:"
        4
        "hola mundo"
        "hola mundo"
        "hola mundo"
        "hola mundo"
        Codigo ejecutado con exito! :)
     </code>
</pre>

<h3>Ciclo For</h3>
<p>Otro tipo de ciclo permitido por Patito es el ciclo for, el cual por medio de iteraciones ira actualizando el valor de </p>
<p>una variable de uno en uno hasta que se cumpla una condicion</p>
<p>Ejemplo de sintaxis a continuacion </p>

<pre>
<code>
program patito:

funcion int fiboIterativo(int n):
var int : actual,ant1,ant2,k;
{
   ant1 = 1;
   ant2 = 1;

   if((n == 1) | (n == 2)) so{
      actual = 1;

   }
   else{
      if(n == 0)so{
         actual = 0;
         
      }
   }
   write(0);
   write(1);
   write(1);
   from k = 3 to n do  {
      actual = ant1 + ant2;
      ant2 = ant1;
      ant1 = actual;
      write(actual);
   }
}

main()
var int : x, num;
{
   write("Escribe el numero que quieres de la sucesion");
   read(x);
   fiboIterativo(x);
}

</code>
</pre>
<p>El ejemplo anterior mostraba el funcionamiento de un for con un proble de fibonnacci de manera iterativa</p>
<p>Al ejecutar el codigo anterior, el resultado se deplegara en la terminal de la siguiente forma</p>

<pre>
    <code>
        "Escribe el numero que quieres de la sucesion:"
        6      
        0
        1
        1
        2
        3
        5
        8
        Codigo ejecutado con exito! :)
     </code>
</pre>


<p></p>
<h3>Compilacion y ejecucion del programa</h3>
<p>Para poder compilar el programa escrito, es necesario usar la siguiente instruccion</p>

<pre>
    <code>
       python .\patito.py testFile.txt
     </code>
</pre>
<p>* El archivo testFile.txt debe de ser reemplazado por el nombre de tu archivo en donde creaste el codigo</p>

<p></p>
<p>Para poder ejecutar el codigo escrito es necesario usar la siguiente instruccion</p>
<p>* Necesitas python 3 o superior</p>
<pre>
    <code>
       python .\virtualMachine.py testFile.txto
     </code>
</pre>
<p>* El archivo testFile.txto debe de ser reemplazado por el nombre de tu archivo en donde creaste el codigo con la extension .txto</p>