# Patito++

Proyecto de Compiladores 2020, un patito más complejo.
Patito++ es un lenguaje procedural, imperativo, basado en sintaxis de c, que permite generar funciones, variables y arreglos, así como operaciones aritméticas entre ellos y la capacidad de declarar y sobre escribir datos.

##  :beginner: Hacerca de
Tomando la ventaja del alto nivel de abstracción del lenguaje python, se espera crear un lenguaje de programación que cumpla con los siguientes lineamientos:

- Contener la estructura: nombre de programa, funciones, y main (principal).
- Manipualar 4 tipos de datos (int, float, char, string).
- Utilizar operaciones de control de flujo como if, while, for.
- Tener la capacidad de crear, accesar y modificar matrices de los tipos previos.
- Crear funciones, haciendo una división entre el contexto de la misma y entorno global

## :notebook: Para Empezar

Asegurate que los archivos: ``` yacc.py , lex.py``` existan en el mismo directorio que ```PatitoPlusPlus.py```.

### Prerequisitos

* python >= 3.6
* ply 2.6 (pre-instalado)

### :zap: Ejecución

Windows:
```
python3 compiler/__init.py__ (archivo)
python3 virtualMachine/virtualMachine.py
```
ó 
```
python compiler/__init.py (archivo)
python virtualMachine/virtualMachine.py
```

\*nix:
```
python3 compiler/__init.py__ (archivo)
python3 virtualMachine/virtualMachine.py
```
ó 
```
python compiler/__init.py (archivo)
python virtualMachine/virtualMachine.py
```
ó
```
./patitoplusplus (archivo)
```

Acepta todo archivo patito++ válido, pero la terminación preferida es:  ```.duckpp```



##  Para empezar.

### ¿En qué consiste un programa patito++?

```
%% Esto es un comentario, el compilador ignora todo lo que ves aquí
programa id_de_programa;
var <tipo_de_variable> <id_de_variable>;

func <tipo_de_variable>  <id_de_función> ( <tipo_de_parametro> <id_de_parametro> )
var <tipo_de_variable> <id_de_variable>;
{
<Asignaciónes o Estatutos>;
regresa <id_de_varible>;
}

principal()
var <tipo_de_variable> <id_de_variable>;
{
<Asignaciónes o Estatutos>;
}
```

Notarás que toda función (incluyendo principal) puede poseer variables (¡declaradas en var!) y pueden declararse de esta forma:

```
%% Cada función utiliza solo un var! 
var int Matrix[10][10], intA;
float floatB;
```

### Características del lenguaje.

PatitoPlusPlus soporta sólo los siguientes tipos de datos:

| Entero (int)     | 9, 0, 1000000              |
|------------------|----------------------------|
| Flotante (float) | .0001, 9.0, 3.14159        |
| Caracter (char)  | ‘a’, ‘\n’, ‘+’             |
| Strings (string) | “Hola Mundo”, “ab”, “.+\n” |


Estas son los puntos de partida para el juego con los datos, ¡operaciones aritméticas!: 

```
%% Nótese la diferencia entre los valores!
intA = 10;
Matrix[1][1] = 0;
floatB = 1.0 * 2.0;
```

PatitoPlusPlus soporta los siguientes tipos de operaciones:

| =                              |   De Asignacion                |
|--------------------------------|--------------------------------|
| +, -, /, * %                   | Aritmeticas                    |
| >, <, >=, <=, ==, !=, &&, \|\| | Booleanas                      |
| (, )                           |  De priorizacion o jerarquicas |


No todas de ellas pueden utilizarse con todos los tipos de datos, existe toda una sección que solo depende de las operaciones booleanas: lo que me lleva al siguiente tema: 

### Controles de flujo

Vea el siguiente ejemplo:

```
%% ¿Qué texto crees que aparezca?
programa desicion;

principal()
var int i;
{
   i = 0
   si ( i == 2) entonces {
    escribe("i era igual a 2 todo este tiempo";
   } sino {
    escribe("i realmente NO era igual a 0");
   }
}
```
**Output:** ``` i realmente NO era igual a 0 ```

PatitoPlusPlus soporta diferentes controladores de flujo, tales como:

| Desde                |   desde k = 0 hasta 10 hacer { escribe(k); }                          |
|----------------------|-----------------------------------------------------------------------|
| Mientras             | %% i fue declarado a 0 mientras(x < 10) haz { escribe(k) x = x + 1; } |
| Si / Entonces / Sino | _Visto en el ejemplo anterior_                                        |

Si no lo notaste, ¡los dos ejemplos imprimen un conteo de 0  a 10! Es sorprendente el control que puedes tener con ellos, pero, existe algo aún más poderoso:

### Funciones / módulos

Una vez más un ejemplo:

```
%% Mi propia funcion
programa mifuncion;

%%Use la palabra "función"
funcion void inicia(int a, int b)
var int x;
{
    escribe(a + b);
}

principal(){
   inicia(3, 5);
}
```

**Output**: ```8```

Pero te preguntas, ¿ qué hay de escribir ? Definitivamente parece una función que no hice. Y estarias en razón, PatitoPlusPlus soporta las siguientes funciones predefinidas: 

| lee(var1, [var2]             | Pide al usuario darle valor a la(s) variable(s) (de 1 a n)      |
|------------------------------|-----------------------------------------------------------------|
| escribe(  var1 , [var2], ….) | Imprime algo en pantalla! (Puedes imprimir de 1 a n variables.) |

## Hecho con

* [PLY](https://www.dabeaz.com/ply/) - Python Lex-Yacc


## Autores

* **Linetes** - *Initial work* - [linetes](https://github.com/linetes)
* **olefran** - *Initial work* - [olefran](https://github.com/olefran)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
