"""Módulo de validaciones: cada función devuelve (es_valido, mensaje)."""


def validar_dni(dni):
    """El DNI peruano debe tener exactamente 8 dígitos."""
    dni = dni.strip()
    if len(dni) != 8 or not dni.isdigit():
        return False, "El DNI debe tener exactamente 8 dígitos numéricos."
    return True, ""


def validar_nombre(nombre):
    """Mínimo 3 caracteres, solo letras y espacios."""
    nombre = nombre.strip()
    if len(nombre) < 3:
        return False, "El nombre debe tener al menos 3 caracteres."
    for caracter in nombre:
        if not (caracter.isalpha() or caracter == " "):
            return False, "El nombre solo puede contener letras y espacios."
    return True, ""


def validar_correo(correo):
    """Validación básica para notificaciones electrónicas (Ley 31170)."""
    correo = correo.strip()
    if correo.count("@") != 1:
        return False, "El correo debe contener un único '@'."
    usuario, dominio = correo.split("@")
    if usuario == "" or "." not in dominio or dominio.startswith(".") or dominio.endswith("."):
        return False, "Formato de correo no válido (ej: usuario@dominio.pe)."
    if " " in correo:
        return False, "El correo no puede tener espacios."
    return True, ""


def validar_asunto(asunto):
    """El asunto del trámite debe tener entre 5 y 100 caracteres."""
    asunto = asunto.strip()
    if len(asunto) < 5 or len(asunto) > 100:
        return False, "El asunto debe tener entre 5 y 100 caracteres."
    return True, ""


METODOS_PAGO = ["TRANSFERENCIA BCP", "OTRO MEDIO"]


def validar_constancia(respuesta):
    """La constancia de secundaria es requisito: debe responderse SI."""
    if respuesta.strip().upper() not in ("SI", "SÍ", "S"):
        return False, "Sin constancia de secundaria no se puede registrar."
    return True, ""


def validar_metodo_pago(metodo):
    """El pago debe estar hecho con uno de los medios aceptados."""
    if metodo.strip().upper() not in METODOS_PAGO:
        return False, "Método de pago no reconocido."
    return True, ""
