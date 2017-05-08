python-programming-problems
===========================

Resolución de problemas de programación utilizando Python.

Los enunciados de los problemas se encuentran en la carpeta [enunciados]() y soluciones su respectiva [carpeta]().


### Problema 1

>Solitario mágico

Considera un mazo de n cartas, donde se cumple que n = 1 + 2 + 3 + … + k, donde k es un número
natural <= 20. El mazo se reparte en m montones de cartas, cada uno de ellos con una cantidad arbitraria
ci de cartas, i=1 … m.
El juego consiste en reorganizar los montes de la siguiente manera: Se toma una carta de cada montón y
con estas cartas se forma un nuevo montón que se coloca al final de todos. En este proceso, los montones
que solo tengan una carta desaparecen.
Tu programa deberá llevar a cabo la reorganización descrita cuantas veces sea necesario hasta que haya
un montón de una 1 carta, seguido de otro de 2 cartas, luego uno de 3, y así sucesivamente hasta llegar
al de k cartas. [Ver problema.]() 


##### Solucion 

Lo primero es declarar 2 arreglos uno para que almacene el array que debe cumplir la 
condicion expuesta en el problema (n = 1 + 2 + 3 + … + k)  y otro para almacenar los valores 
iniciales de los montones y sus iteraciones, asi:

```python
must_satisfy = []
cards_values = []
```

Luego capturamos el valor de *k* verificando que no sea mayor a 20 y se crea el array que sasisfase la condicion:

```python
k = int(raw_input("Valor de k: "))
if  k <= 20:
    must_satisfy  = [x for x in range(1, k+1)]
else:
    print "El valor de k ser menor a 20"
```

Seguidamente se obtienen en numero de 'montones' y los valores iniciales de cada uno de estos.
```python
m = raw_input("Numero de montones: ")
for x in range(1, int(m)+1):
    cards_values.append(int(raw_input("Cantidad monton #%s: " % x)))      
```


Finalmente se itera modificando los valores en cards_values de acuerdo a las condiciones del problema,
primero se sustrae 1 de cada motón (cada valor de array), se agrega un nuevo valor al final con la sumatoria de lo que se 
sustrajo, y el paso final consiste en eliminar cualquier valor que sea igual a 0, las funciones a continuación
se presentan en orden y cada una realiza una operación de las condiciones:

```python
def sustract_one_card(c):
    """Toma una carta de cada montón"""
    for x in range (0, len(c)):
        c[x] = c[x] - 1

def add_n_deck_cards(c):
    """Agrega un nuevo 'montón' de cartas al final con el valor del tamaño de la lista"""
    c.append(len(c))

def check_zeros(c):
    """Busca y elimina los ceros"""
    for x in range(0, len(c)-1):
        if  c[x] == 0:
            c.remove(0)
```

##### Resultado

![Imgur](http://i.imgur.com/r5TpN1o.png)


Ver [script final]()


### Problema 2

>Estructura de árboles binarios

Deberás escribir un programa que recibe dos secuencias de números enteros, cada secuencia son las
entradas para crear un árbol binario. El programa deberá determinar si los dos árboles tienen la misma
estructura o no. Por ejemplo, la secuencias (34 21 76 27) y (25 68 1 17) producen los siguientes árboles,
los cuales tienen la misma estructura:

![1](http://i.imgur.com/TbnaCdJ.png)

[Ver problema.]() 


##### Solucion 

Para este problema creamos 2 arrays con cada una de las cadenas recibidas, así:

```python
s1 = raw_input("Cadena (seprados por espacios): ")
n1 = map(int, s1.split())
```

Esto convierte la entrada de una cadena del estilo `"34 21 76 27"` en un array `[34,21,76,27]`

En el siguiente paso obtenemos una array que contenga la presentación binarias de los nodos del árbol generado.

Ej: `[34,21,76,27]` , el primer valor corresponde al nodo raíz (no se incluye en el resultado)

luego se compara el siguiente valor con el anterior y si es menor se inserta un valor de '0' en el array (izquierda), 
si es mayor el valor es de '1' (derecha), resultando para el ejemplo `[0,1,0]`, cada valor representa las 
posición(izquierda, derecha) de los nodos después del raíz.
Por tanto la interpretación del resultado seria 21 -> 0 (izquierda), 76 -> 1 (derecha), 27->0 (izquierda), 
a continuación la función que realiza esta operación:

```python
def get_binary_tree(n):
    n0 = []
    """Obtiene una representación binaria de la posición de los nodos
    recibe como parámetro un arreglo con los valores de cada nodo."""
    for x in range(0, len(n) - 1):

        if n[x] >= n[x + 1]:
            n0.append(0)
        else:
            n0.append(1)

    return n0
```
La función anterior se aplica a las dos cadenas recibidas y los resultados se someten a comparación 
para determinar si ambas poseen una misma estructura. Ej:  las representación binaria `[0,1,0]` es igual a `[0,1,0]`
lo mismo aplica por propiedad simétrica binaria a `[0,1,0]` y `[1,0,1]`. Entonces tomando como referencia el tamaño de 
uno de los dos arreglos (ambos son iguales) se itera y se hace comparación uno a uno del conjunto de valores de 
cada árbol.


```python
def check_is_equal(n1, n2):
    """Recibe 2 arrays de enteros, calcula el árbol binario y compara 
        si estos son iguales o diferentes.
    """
    is_equal = None

    # Verificamos que el tamaño de ambos sea igual
    if  len(n1) == len(n2):

        n1_bi = get_binary_tree(n1)
        n2_bi = get_binary_tree(n2)

        print n1_bi, n2_bi
        i = 0
        j = 0

        for x in range(0, len(n1_bi)):

            if n1_bi[x] != n2_bi[x]:
                # Si al comparar todos los valores están invertidos significa que es el mismo árbol negado
                # Por lo tanto son arboles con la misma estructura
                i = i + 1
                if i == len(n1_bi):
                    is_equal = True
                else:
                    # Si algun valor varia son diferentes
                    is_equal = False

            if n1_bi[j] == n2_bi[j]:
                # Si todos los valores son idénticos, son iguales
                j = j + 1
                if j == len(n1_bi):
                    is_equal = True
                else:
                    # Si alguno varia son diferentes
                    is_equal = False
    else:
        print "El tamaño debe ser igual"

    return is_equal
```

##### Resultado

![Imgur](http://i.imgur.com/1HH5MXE.png)

Ver [script final]()


### Problema 3

>Balance de paréntesis

Dada una cadena que contiene únicamente los símbolos: ( ) [ ] { }. Se dice que una cadena de este tipo
se considera balanceada si:
1. Si es una cadena vacía.
2. Si A es una cadena correcta, (A), [A] y {A} son también cadenas correctas.
3. Si las cadenas A y B son correctas, AB es correcta y también BA.
Escribe un programa que pida una cadena de este tipo y compruebe si está o no balanceada. Considera
que la cantidad máxima de símbolos es de 128.
[Ver problema.]() 


##### Solución 


Debemos verificar que la cadena cumpla las condiciones del problema, verificamos el tamaño y que solamente contenta
los caracteres especificados, así siendo `p` la cadena de entrada :

```python
allowed = set("()[]{}")
    
if len(p) >= 128:
    print "Solo se permiten 128 caracteres!"
    sys.exit()

if not set(p) <= allowed:
    print "Solo se permiten ()[]{} !"
    sys.exit()
```

Luego con la cadena validada, se inspecciona si esta balanceada contando cada una de la ocurrencias para los
caracteres dados, finalmente se compara cada par de caracteres correspondientes y para que cumplan deben ser iguales
los que abren y cierran de cada tipo, así:

```python
def is_balanced(p0):
    c1 = p0.count('(')
    c2 = p0.count(')')
    c3 = p0.count('[')
    c4 = p0.count(']')
    c5 = p0.count('{')
    c6 = p0.count('}')

    if  c1 == c2 and c3 == c4 and c5 == c6:
        return True
    else:
        return False
```

##### Resultado

![3](http://i.imgur.com/BOTBUaH.png)

Ver [script final]()
