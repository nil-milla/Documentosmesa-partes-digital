"""Persistencia en archivo de texto. Una línea por expediente, campos separados por '|'."""
import os

SEP = "|"
NUM_CAMPOS = 8


def guardar(ruta, tabla):
    """Guarda todos los expedientes de forma segura (escritura atómica).

    Primero escribe en un archivo temporal y recién cuando terminó lo reemplaza
    por el definitivo con os.replace. Si el programa o la PC se cae a la mitad de
    la escritura, expedientes.txt conserva la última versión completa.
    """
    ruta_temporal = ruta + ".tmp"
    with open(ruta_temporal, "w", encoding="utf-8") as archivo:
        for i in range(len(tabla[0])):
            campos = [tabla[c][i].replace(SEP, "/") for c in range(NUM_CAMPOS)]
            archivo.write(SEP.join(campos) + "\n")
        archivo.flush()
        os.fsync(archivo.fileno())  # obliga al sistema a escribir en disco
    os.replace(ruta_temporal, ruta)


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
