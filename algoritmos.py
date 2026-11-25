"""Algoritmos de ordenamiento y búsqueda sobre arreglos paralelos.

Los expedientes se guardan en una lista de arreglos paralelos:
    tabla = [codigos, dnis, nombres, correos, constancias, pagos, fechas, estados]
El índice i de cada arreglo corresponde al mismo expediente.
"""

IDX_CODIGO = 0


def intercambiar(tabla, i, j):
    """Intercambia la posición i y j en TODOS los arreglos paralelos."""
    for columna in tabla:
        columna[i], columna[j] = columna[j], columna[i]


def ordenar_por_codigo(tabla):
    """Ordenamiento burbuja ascendente por código (mantiene el paralelismo)."""
    codigos = tabla[IDX_CODIGO]
    n = len(codigos)
    for pasada in range(n - 1):
        hubo_cambio = False
        for i in range(n - 1 - pasada):
            if codigos[i] > codigos[i + 1]:
                intercambiar(tabla, i, i + 1)
                hubo_cambio = True
        if not hubo_cambio:  # optimización: ya está ordenado
            break


def busqueda_lineal(codigos, buscado):
    """Devuelve el índice del código o -1. Sirve con datos sin ordenar."""
    for i in range(len(codigos)):
        if codigos[i] == buscado:
            return i
    return -1


def busqueda_binaria(codigos, buscado):
    """Devuelve el índice del código o -1. Requiere arreglo ordenado."""
    inicio, fin = 0, len(codigos) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if codigos[medio] == buscado:
            return medio
        if codigos[medio] < buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1


# ---------------------------------------------------------------------------
# Versiones recursivas (Tema 7). Cada una tiene caso base y caso recursivo.
# ---------------------------------------------------------------------------

def busqueda_binaria_recursiva(codigos, buscado, inicio=0, fin=None):
    """Igual que busqueda_binaria, pero la repetición se hace con recursividad.

    Caso base 1: inicio > fin   -> el código no está (devuelve -1).
    Caso base 2: codigos[medio] == buscado -> devuelve medio.
    Caso recursivo: se llama con la mitad izquierda o la derecha (el rango se reduce).
    """
    if fin is None:
        fin = len(codigos) - 1
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if codigos[medio] == buscado:
        return medio
    if codigos[medio] < buscado:
        return busqueda_binaria_recursiva(codigos, buscado, medio + 1, fin)
    return busqueda_binaria_recursiva(codigos, buscado, inicio, medio - 1)


def contar_iterativo(valores, buscado):
    """Cuenta cuántas veces aparece 'buscado' en la lista (versión con for)."""
    total = 0
    for valor in valores:
        if valor == buscado:
            total += 1
    return total


def contar_recursivo(valores, buscado, inicio=0, fin=None):
    """Cuenta apariciones dividiendo la lista en dos mitades (profundidad ~ log2 n).

    Caso base 1: rango vacío (inicio > fin) -> 0.
    Caso base 2: un solo elemento (inicio == fin) -> 1 si coincide, 0 si no.
    Caso recursivo: suma lo contado en cada mitad.
    Se divide en mitades (y no de 1 en 1) para no superar el límite de recursión
    de Python (unas 1000 llamadas) cuando hay muchos expedientes.
    """
    if fin is None:
        fin = len(valores) - 1
    if inicio > fin:
        return 0
    if inicio == fin:
        return 1 if valores[inicio] == buscado else 0
    medio = (inicio + fin) // 2
    return (contar_recursivo(valores, buscado, inicio, medio)
            + contar_recursivo(valores, buscado, medio + 1, fin))
