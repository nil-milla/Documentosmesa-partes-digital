"""Casos de prueba. Ejecutar: python pruebas.py

Los últimos grupos (CAMPO, RECURSIVIDAD, PERSISTENCIA) usan casos basados en el
proceso observado en la UPN Ate (14/10/2026). Los nombres y DNI son ficticios.
"""
import os
import algoritmos, archivos, expedientes, validaciones

total = 0


def caso(nombre, condicion):
    global total
    total += 1
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

# --- CAMPO: situaciones vistas en la ventanilla de inscripciones --------------
print("\n-- Casos de campo (UPN Ate) --")
t = expedientes.nueva_tabla()
ok, a = expedientes.registrar(t, "70123456", "  maría peña núñez ", "maria.pena@mail.com", "SI", "TRANSFERENCIA BCP")
caso("Campo: postulante con tilde y ñ se registra", ok and t[2][0] == "María Peña Núñez")
ok, b = expedientes.registrar(t, " 45678912 ", "carlos quispe", "cquispe@mail.com", "sí", "otro medio")
caso("Campo: DNI con espacios y pago en minúsculas", ok and t[1][1] == "45678912" and t[5][1] == "OTRO MEDIO")
ok, c = expedientes.registrar(t, "71234567", "rosa huamán", "rosa@mail.com", "SI", "TRANSFERENCIA BCP")
caso("Campo: tercer código correlativo", ok and c.endswith("0003"))
caso("Campo: DNI de 7 dígitos rechazado", not expedientes.registrar(t, "7123456", "Rosa Huamán", "r@m.pe", "SI", "OTRO MEDIO")[0])
caso("Campo: correo sin dominio rechazado", not expedientes.registrar(t, "72345678", "Luis Soto", "luis@mail", "SI", "OTRO MEDIO")[0])
caso("Campo: nombre con símbolo rechazado", not expedientes.registrar(t, "72345678", "Luis S0to", "luis@mail.com", "SI", "OTRO MEDIO")[0])
caso("Campo: pago no aceptado rechazado", not expedientes.registrar(t, "72345678", "Luis Soto", "luis@mail.com", "SI", "EFECTIVO")[0])
caso("Campo: rechazos no crean expedientes", len(t[0]) == 3)
caso("Campo: consulta de código inexistente", expedientes.consultar(t, "EXP-2026-0999") is None)
caso("Campo: cambiar estado a OBSERVADO", expedientes.cambiar_estado(t, b.lower(), "OBSERVADO") and expedientes.consultar(t, b)[7] == "OBSERVADO")
caso("Campo: cambiar estado de código inexistente", not expedientes.cambiar_estado(t, "EXP-2026-0999", "OBSERVADO"))
caso("Campo: consulta en tabla vacía", expedientes.consultar(expedientes.nueva_tabla(), "EXP-2026-0001") is None)

# --- RECURSIVIDAD (Tema 7): la versión recursiva debe dar lo mismo -----------
print("\n-- Recursividad vs. iteración --")
algoritmos.ordenar_por_codigo(t)
iguales = all(algoritmos.busqueda_binaria_recursiva(t[0], x) == algoritmos.busqueda_binaria(t[0], x)
              for x in t[0] + ["EXP-2026-0000", "EXP-2026-9999"])
caso("Recursiva: misma posición que la iterativa (hallados y no hallados)", iguales)
caso("Recursiva: lista vacía devuelve -1 (caso base)", algoritmos.busqueda_binaria_recursiva([], "EXP-2026-0001") == -1)
caso("Recursiva: conteo por estado", algoritmos.contar_recursivo(t[7], "REGISTRADO") == 2
     and algoritmos.contar_recursivo(t[7], "OBSERVADO") == 1)
caso("Recursiva: conteo igual al iterativo", algoritmos.contar_recursivo(t[7], "EN REVISION") == algoritmos.contar_iterativo(t[7], "EN REVISION") == 0)
grande = ["REGISTRADO"] * 5000
caso("Recursiva: 5000 elementos sin RecursionError", algoritmos.contar_recursivo(grande, "REGISTRADO") == 5000)

# --- PERSISTENCIA: simula que el sistema se cae y se vuelve a abrir -----------
print("\n-- Persistencia y caída del sistema --")
archivos.guardar("prueba.txt", t)
caso("Persistencia: no queda archivo temporal", not os.path.exists("prueba.txt.tmp"))
reabierta = archivos.cargar("prueba.txt")
caso("Persistencia: tras reiniciar se recupera todo", reabierta == t)
caso("Persistencia: se puede consultar tras reiniciar", expedientes.consultar(reabierta, a)[2] == "María Peña Núñez")
ok, d = expedientes.registrar(reabierta, "73456789", "ana ríos", "ana@mail.com", "SI", "OTRO MEDIO")
caso("Persistencia: el correlativo continúa tras reiniciar", ok and d.endswith("0004"))
with open("prueba.txt", "a", encoding="utf-8") as f:
    f.write("LINEA|CORRUPTA\n\n")
caso("Persistencia: línea corrupta o vacía se ignora", len(archivos.cargar("prueba.txt")[0]) == 3)
os.remove("prueba.txt")

print("\nPruebas aprobadas:", total, "de", total)
print("Todas las pruebas pasaron.")
