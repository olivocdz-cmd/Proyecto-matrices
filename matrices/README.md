# Operaciones con Matrices en Python

Programa interactivo desarrollado en **Python** que permite realizar operaciones algebraicas entre matrices de forma eficiente. El sistema cuenta con una arquitectura modular, validación estricta de dimensiones y un manejo de errores robusto para garantizar una experiencia de usuario fluida y profesional.

## 🚀 Funcionalidades

El software soporta las siguientes operaciones matemáticas:

* **Suma de matrices:** Suma algebraica tradicional de dos matrices de dimensiones idénticas.
* **Multiplicación de matrices:** Producto de puntos (dot product) siguiendo la regla de compatibilidad $m \times n$ y $n \times p$.
* **Producto de Hadamard:** Multiplicación elemento a elemento entre matrices de igual tamaño.
* **Producto de Kronecker:** Operación que resulta en una matriz de bloques de dimensiones multiplicadas.

## 🛠️ Requisitos e Instalación

### Requisitos
* **Python 3.6** o superior.
* Sin dependencias externas (solo utiliza la biblioteca estándar de Python).

### Instalación y Ejecución
Para poner en marcha el proyecto, clona el repositorio y ejecuta el archivo principal:

```bash
# Clonar el repositorio
git clone https://github.com/olivocdz-cmd/Proyecto-matrices.git

# Acceder al directorio
cd Proyecto-matrices/matrices

# Ejecutar la aplicación
python main.py
```

## 📂 Estructura del Proyecto

El código se organiza de forma modular para facilitar su mantenimiento y escalabilidad:

```text
matrices/
├── main.py                   # Punto de entrada de la aplicación
├── entrada.py                # Lógica para la captura y validación de datos por teclado
├── operaciones_matrices.py   # Núcleo matemático y algoritmos de matrices
├── menu.py                   # Gestión de la interfaz de usuario en consola
└── README.md                 # Documentación del proyecto
```

## 📖 Guía de Uso

1.  **Menú Principal:** Seleccione una operación ingresando el número correspondiente (**1 a 5**).
2.  **Configuración de Matrices:**
    * Defina el número de **filas**.
    * Defina el número de **columnas**.
    * Ingrese los valores de cada fila separándolos por **espacios** (Ej: `1 2 3`).
3.  **Resultado:** El sistema validará si las dimensiones son aptas para la operación elegida y mostrará el resultado en pantalla.
4.  **Repetición:** Al finalizar, podrá regresar al menú o seleccionar la opción **5** para salir.

---

**Autor:** [Carlos Diaz](https://github.com/olivocdz-cmd)  
**Asignatura:** Programación I - Universidad Industrial de Santander  
**Profesor:** Andrés Ríos-Gutiérrez
