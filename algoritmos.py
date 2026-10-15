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
