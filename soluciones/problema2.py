# -*- coding: utf-8 -*-
n1 = []
n2 = []

def get_input():
    global n1, n2
    s1 = raw_input("Lista de numeros #1  (seprados por espacios): ")
    s2 = raw_input("Lista de numeros #2  (seprados por espacios): ")
    n1 = map(int, s1.split())
    n2 = map(int, s2.split())

def get_binary_tree(n):
    n0 = []
    """Obtiene una representacion binaria de la posicion de los nodos
    recibe como parametro un arreglo con los valores de cada nodo."""
    for x in range(0, len(n) - 1):

        if n[x] >= n[x + 1]:
            n0.append(0)
        else:
            n0.append(1)

    return n0


def check_is_equal(n1, n2):
    """Recibe 2 arregleglos de enteros, calcula el arbol binario y compara 
        si estos son iguales o diferentes.
    """
    is_equal = None

    # Verificamos que el tama;o de ambos sea igual
    if  len(n1) == len(n2):

        n1_bi = get_binary_tree(n1)
        n2_bi = get_binary_tree(n2)

        print n1_bi, n2_bi
        i = 0
        j = 0

        for x in range(0, len(n1_bi)):

            if n1_bi[x] != n2_bi[x]:
                # Si al comparar todos los valores estan invertidos significa que es el mismo arbol negado
                # Por lo tanto son arboles con la misma estructura
                i = i + 1
                if i == len(n1_bi):
                    is_equal = True
                else:
                    # Si algun valor varia son diferentes
                    is_equal = False

            if n1_bi[j] == n2_bi[j]:
                # Si todos los valores son identicos, son iguales
                j = j + 1
                if j == len(n1_bi):
                    is_equal = True
                else:
                    # Si alguno varia son diferentes
                    is_equal = False
    else:
        print "El tamaño debe ser igual"

    return is_equal


def run():
    print ":::::ESTRUCTURA DE ÁRBOLES BINARIOS::::::"
    print "-----DATOS DE ENTRADA------"
    get_input()
    print "-----DATOS DE SALIDA-------"
    if check_is_equal(n1,n2):
        print "IGUALES"
    else:
        print "DIFERENTES"

run()


