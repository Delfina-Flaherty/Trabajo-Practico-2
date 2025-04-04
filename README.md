# En este archivo tengo que anotar todo lo que necesité instalar para mi proyecto

# Simulación de partidas y ranking en shooter online
Este trabajo simula partidas de un juego de disparos (shooter) y genera un ranking de jugadores basado en kills, asistencias, muertes, puntaje total y cantidad de veces que fueron MVP (Mejor Jugador del Partido/).

# Estructura del proyecto
```
Tp2/ 
├── Notebooks/ 
│ └── Ejercicio10.ipynb # Notebook principal para correr el ejercicio 
├── src/ 
│ ├── __init__.py
│ └── shooter.py # Funciones necesarias para procesar las rondas 
├── requirements.txt # Dependencias del proyecto 
└── README.md # Este archivo
```

El codigo fuente con las funciones necesarias se encuentra en el directorio `src`, mientras que los notebooks de analisis estan en la carpeta `Notebooks`.

# Requisitos

Python 3.12.9
pip (gestor de paquetes de Python)

Para ejecutar este proyecto, se recomienda crear un entorno virtual y luego instalar las dependencias necesarias.

# 1. Crear un entorno virtual 
```bash
python -m venv venv
```

# 2. Activar el entorno virtual en Windows:
  ```bash
  venv\Scripts\activate
  ```

# 3. Instalar Jupyter Notebook
Con el entorno virtual activado, correr:
```bash
pip install notebook
```
Esto instala Jupyter Notebook para que poder ejecutar los archivos de tipo .ipynb.

# 4. Chequear que esté todo bien instalado
```bash
jupyter --version
```

# 5. Instalar dependencias
Ejecutar el siguiente comando en la terminal dentro del proyecto:
```bash
pip install -r requirements.txt
```
# 6. Correr el programa
Asegurarse de estar en el entorno virtual y luego abrir Jupyter Notebook, navegar hasta la carpeta `Notebooks` y ejecutar:
`Ejercicio10.ipynb`

# Flaherty Delfina 18018/1