"""Persistencia en archivo de texto. Una línea por expediente, campos separados por '|'."""
import os

SEP = "|"
NUM_CAMPOS = 8


def guardar(ruta, tabla):
    """Guarda todos los expedientes. Reemplaza el separador dentro del texto."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        for i in range(len(tabla[0])):
            campos = [tabla[c][i].replace(SEP, "/") for c in range(NUM_CAMPOS)]
            archivo.write(SEP.join(campos) + "\n")


def cargar(ruta):
    """Carga los expedientes. Si no existe el archivo, devuelve tabla vacía."""
    tabla = [[] for _ in range(NUM_CAMPOS)]
    if not os.path.exists(ruta):
        return tabla
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            campos = linea.rstrip("\n").split(SEP)
            if len(campos) != NUM_CAMPOS:  # línea corrupta: se ignora
                continue
            for c in range(NUM_CAMPOS):
                tabla[c].append(campos[c])
    return tabla
