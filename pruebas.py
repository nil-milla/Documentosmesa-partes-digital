"""Casos de prueba. Ejecutar: python pruebas.py
TODO (equipo): agregar casos con los datos reales de la observación en la UPN."""
import os
import algoritmos, archivos, expedientes, validaciones

def caso(nombre, condicion):
    print(("PASA  " if condicion else "FALLA ") + nombre)
    assert condicion, nombre

caso("DNI válido", validaciones.validar_dni("12345678")[0])
caso("DNI con letras", not validaciones.validar_dni("1234567a")[0])
caso("DNI corto", not validaciones.validar_dni("1234")[0])
caso("Nombre con números", not validaciones.validar_nombre("Ana123")[0])
caso("Correo válido", validaciones.validar_correo("ana@mail.com")[0])
caso("Correo sin arroba", not validaciones.validar_correo("anamail.com")[0])
caso("Constancia SI", validaciones.validar_constancia("si")[0])
caso("Constancia NO rechazada", not validaciones.validar_constancia("no")[0])
caso("Pago BCP válido", validaciones.validar_metodo_pago("transferencia bcp")[0])
caso("Pago desconocido", not validaciones.validar_metodo_pago("trueque")[0])

t = expedientes.nueva_tabla()
ok1, c1 = expedientes.registrar(t, "12345678", "ana pérez", "ana@mail.com", "SI", "TRANSFERENCIA BCP")
ok2, c2 = expedientes.registrar(t, "87654321", "luis soto", "luis@mail.com", "SI", "OTRO MEDIO")
caso("Registro 1 correcto", ok1 and c1.endswith("0001"))
caso("Registro 2 correlativo", ok2 and c2.endswith("0002"))
caso("DNI duplicado rechazado", not expedientes.registrar(t, "12345678", "Ana Pérez", "a@b.pe", "SI", "OTRO MEDIO")[0])
caso("Sin constancia rechazado", not expedientes.registrar(t, "11112222", "Pedro Ruiz", "p@b.pe", "NO", "OTRO MEDIO")[0])

for col in t:
    col.reverse()
algoritmos.ordenar_por_codigo(t)
caso("Orden ascendente", t[0] == sorted(t[0]))
caso("Paralelismo conservado", t[2][0] == "Ana Pérez")
caso("Búsqueda binaria encontrada", algoritmos.busqueda_binaria(t[0], c2) == 1)
caso("Búsqueda binaria inexistente", algoritmos.busqueda_binaria(t[0], "EXP-0000-0000") == -1)
caso("Consulta por código", expedientes.consultar(t, c1.lower())[2] == "Ana Pérez")

archivos.guardar("prueba.txt", t)
caso("Guardar y cargar conserva datos", archivos.cargar("prueba.txt") == t)
caso("Archivo inexistente → tabla vacía", archivos.cargar("no_existe.txt")[0] == [])
os.remove("prueba.txt")
print("\nTodas las pruebas pasaron.")
