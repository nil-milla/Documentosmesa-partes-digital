"""Mide cuántas comparaciones hacen los algoritmos (eficiencia básica).

Ejecutar: python eficiencia.py
Se usa una cadena que cuenta cada comparación (==, <, >) para no modificar
los algoritmos de algoritmos.py.
"""
import algoritmos


class Cod(str):
    """Código que cuenta cuántas veces se compara."""
    comparaciones = 0

    def __eq__(self, otro):
        Cod.comparaciones += 1
        return str.__eq__(self, otro)

    def __lt__(self, otro):
        Cod.comparaciones += 1
        return str.__lt__(self, otro)

    def __gt__(self, otro):
        Cod.comparaciones += 1
        return str.__gt__(self, otro)

    __hash__ = str.__hash__


def contar(funcion, *args):
    Cod.comparaciones = 0
    funcion(*args)
    return Cod.comparaciones


def lista_codigos(n):
    return [Cod("EXP-2026-" + str(i + 1).zfill(4)) for i in range(n)]


def peor_caso_lista(n):
    """Lista en orden inverso (peor caso del burbuja)."""
    return list(reversed(lista_codigos(n)))


print("n      | lineal (peor) | binaria (peor) | binaria rec. | burbuja (inverso)")
for n in (10, 100, 1000, 5000):
    ordenada = lista_codigos(n)
    ausente = Cod("EXP-2026-9999")
    lineal = contar(algoritmos.busqueda_lineal, ordenada, ausente)
    binaria = contar(algoritmos.busqueda_binaria, ordenada, ausente)
    recursiva = contar(algoritmos.busqueda_binaria_recursiva, ordenada, ausente)
    if n <= 1000:
        tabla = [peor_caso_lista(n)]
        burbuja = contar(algoritmos.ordenar_por_codigo, tabla)
    else:
        burbuja = "-"
    print(str(n).ljust(6), "|", str(lineal).ljust(13), "|", str(binaria).ljust(14), "|",
          str(recursiva).ljust(12), "|", burbuja)
