"""Mesa de Partes Digital - prototipo (Fundamentos de Programación, CIIN1205P)."""
import algoritmos
import archivos
import expedientes

RUTA = "expedientes.txt"
ESTADOS = ["REGISTRADO", "EN REVISION", "OBSERVADO"]


def mostrar_menu():
    print("\n=== MESA DE PARTES DIGITAL ===")
    print("1. Registrar postulante")
    print("2. Consultar por código")
    print("3. Listar expedientes (ordenados por código)")
    print("4. Cambiar estado")
    print("5. Salir")


def opcion_registrar(tabla):
    dni = input("DNI: ")
    nombre = input("Nombre completo: ")
    correo = input("Correo electrónico: ")
    constancia = input("¿Presentó constancia de secundaria? (SI/NO): ")
    print("Método de pago: 1=Transferencia BCP, 2=Otro medio")
    metodo = "TRANSFERENCIA BCP" if input("Opción: ").strip() == "1" else "OTRO MEDIO"
    ok, resultado = expedientes.registrar(tabla, dni, nombre, correo, constancia, metodo)
    if ok:
        archivos.guardar(RUTA, tabla)
        print("✔ Registrado (respaldo local guardado). Código:", resultado)
    else:
        print("✘ Error:", resultado)


def opcion_consultar(tabla):
    exp = expedientes.consultar(tabla, input("Código (ej. EXP-2026-0001): "))
    print(expedientes.formatear(exp) if exp else "No se encontró el expediente.")


def opcion_listar(tabla):
    if not tabla[0]:
        print("No hay expedientes registrados.")
        return
    algoritmos.ordenar_por_codigo(tabla)
    print("\nCódigo          | DNI      | Postulante           | Estado")
    for i in range(len(tabla[0])):
        print(tabla[0][i].ljust(15), "|", tabla[1][i], "|", tabla[2][i][:20].ljust(20), "|", tabla[7][i])
    print("Total:", len(tabla[0]))


def opcion_estado(tabla):
    codigo = input("Código: ")
    print("Estados:", ", ".join(str(i + 1) + "=" + ESTADOS[i] for i in range(3)))
    eleccion = input("Nuevo estado (1-3): ").strip()
    if eleccion not in ("1", "2", "3"):
        print("✘ Opción de estado no válida.")
    elif expedientes.cambiar_estado(tabla, codigo, ESTADOS[int(eleccion) - 1]):
        archivos.guardar(RUTA, tabla)
        print("✔ Estado actualizado.")
    else:
        print("No se encontró el expediente.")


def main():
    tabla = archivos.cargar(RUTA)
    print("Expedientes cargados:", len(tabla[0]))
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            opcion_registrar(tabla)
        elif opcion == "2":
            opcion_consultar(tabla)
        elif opcion == "3":
            opcion_listar(tabla)
        elif opcion == "4":
            opcion_estado(tabla)
        elif opcion != "5":
            print("Opción no válida.")
    print("Hasta pronto.")


if __name__ == "__main__":
    main()
