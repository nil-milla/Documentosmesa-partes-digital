"""Lógica de negocio: registrar, consultar y listar expedientes (inscripción)."""
from datetime import date

import algoritmos
import validaciones

NUM_CAMPOS = 8
(IDX_CODIGO, IDX_DNI, IDX_NOMBRE, IDX_CORREO,
 IDX_CONSTANCIA, IDX_PAGO, IDX_FECHA, IDX_ESTADO) = range(NUM_CAMPOS)


def nueva_tabla():
    return [[] for _ in range(NUM_CAMPOS)]


def generar_codigo(tabla):
    """Código con formato EXP-AAAA-NNNN (correlativo por año)."""
    anio = str(date.today().year)
    mayor = 0
    for codigo in tabla[IDX_CODIGO]:
        partes = codigo.split("-")
        if partes[1] == anio and int(partes[2]) > mayor:
            mayor = int(partes[2])
    return "EXP-" + anio + "-" + str(mayor + 1).zfill(4)


def registrar(tabla, dni, nombre, correo, constancia, metodo_pago):
    """Valida requisitos (DNI, constancia, pago) y registra. Devuelve (ok, mensaje/código)."""
    for validar, valor in ((validaciones.validar_dni, dni),
                           (validaciones.validar_nombre, nombre),
                           (validaciones.validar_correo, correo),
                           (validaciones.validar_constancia, constancia),
                           (validaciones.validar_metodo_pago, metodo_pago)):
        ok, mensaje = validar(valor)
        if not ok:
            return False, mensaje
    if dni.strip() in tabla[IDX_DNI]:
        return False, "Ya existe un registro con ese DNI."
    codigo = generar_codigo(tabla)
    datos = [codigo, dni.strip(), nombre.strip().title(), correo.strip().lower(),
             "SI", metodo_pago.strip().upper(), date.today().isoformat(), "REGISTRADO"]
    for c in range(NUM_CAMPOS):
        tabla[c].append(datos[c])
    return True, codigo


def consultar(tabla, codigo):
    """Busca por código (ordena primero para poder usar búsqueda binaria)."""
    algoritmos.ordenar_por_codigo(tabla)
    pos = algoritmos.busqueda_binaria(tabla[IDX_CODIGO], codigo.strip().upper())
    if pos == -1:
        return None
    return [tabla[c][pos] for c in range(NUM_CAMPOS)]


def cambiar_estado(tabla, codigo, nuevo_estado):
    pos = algoritmos.busqueda_lineal(tabla[IDX_CODIGO], codigo.strip().upper())
    if pos == -1:
        return False
    tabla[IDX_ESTADO][pos] = nuevo_estado
    return True


def formatear(expediente):
    etiquetas = ["Código", "DNI", "Postulante", "Correo", "Constancia secundaria",
                 "Método de pago", "Fecha", "Estado"]
    return "\n".join("  " + etiquetas[i] + ": " + expediente[i] for i in range(NUM_CAMPOS))
