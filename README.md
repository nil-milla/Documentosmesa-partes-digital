# Mesa de Partes Digital (prototipo)

Prototipo en Python para registrar, validar, buscar, ordenar y guardar expedientes, desarrollado para el curso **Fundamentos de Programación (CIIN1205P)** - UPN.

El caso se basa en el proceso de inscripción observado en la UPN: el postulante presenta DNI, constancia de secundaria y pago, y el sistema genera un código con el que se consulta después. El prototipo sirve como respaldo local cuando el sistema principal se cae.

## Funciones
- Registrar postulantes con validación de DNI, nombre, correo, constancia y método de pago.
- Generar un código correlativo por expediente (formato `EXP-AAAA-NNNN`).
- Buscar un expediente por código (búsqueda binaria).
- Listar expedientes ordenados por código (ordenamiento burbuja).
- Guardar los datos de forma permanente en `expedientes.txt`.

## Estructura
| Archivo | Contenido |
|---|---|
| `main.py` | Menú principal |
| `expedientes.py` | Registrar, consultar y cambiar estado |
| `validaciones.py` | Validación de datos |
| `algoritmos.py` | Ordenamiento y búsqueda sobre arreglos paralelos |
| `archivos.py` | Guardar y cargar en archivo de texto |
| `pruebas.py` | Casos de prueba |

## Cómo ejecutarlo
Requiere Python 3. En Windows:

```
py main.py      # abrir el menú
py pruebas.py   # ejecutar las pruebas
```

## Conceptos aplicados
Estructuras de control, funciones, arreglos paralelos, cadenas de caracteres, archivos y control de versiones con Git y GitHub.

## Autoríaparticipado
Integrantes: Nil Anderson Milla Layme , DHAN JANIOS TRUJILLO CARDENAS y HALIMA ELIANA CORNEJO TAKI.

