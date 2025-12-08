# Random Team Selector / Selector Aleatorio de Equipos

---
## 🌐 Language / Idioma
- [English](#english) 🇬🇧
- [Español](#español) 🇪🇸

---

<a name="english"></a>
# 🇬🇧 ENGLISH VERSION

## Overview

This project is a tool for randomly selecting football teams from an Excel file. The system filters teams marked as eligible and selects one at random as the winner.

**Available in two versions:**
- **Python Version**: Executable script using Python
- **Executable Version**: Ready-to-use .exe application (no dependencies required)

## Project Structure

### Python Version
```
random_team_selector/
│
├── equipos.xlsx         # Excel file with team database
├── app.py               # Main script (Python)
├── requirements.txt     # Project dependencies
└── README.md           # This documentation
```

### Executable Version
```
random_team_selector/
│
├── app.exe              # Main executable application (Windows)
├── equipos.xlsx         # Excel file with team database
└── README.md           # This documentation
```

## Excel File Structure (`equipos.xlsx`)

The Excel file contains the following columns:

| Column | Description | Example |
|---------|-------------|---------|
| **Pais** | Team country | Spain, England, Italy |
| **Liga** | Competing league | Premier League, La Liga, Serie A |
| **Equipo** | Team name | Real Madrid, Arsenal, Juventus |
| **Elegible** | Eligibility mark | `x` (yes) or empty (no) |

### Data Example

```excel
| Pais      | Liga        | Equipo        | Elegible |
|-----------|-------------|---------------|----------|
| Spain     | La Liga     | Barcelona     | x        |
| England   | Premier L.  | Arsenal       |          |
| Italy     | Serie A     | Juventus      | x        |
```

**Valid eligibility marks:**
- `x` or `X` → Team eligible for selection
- `si` or `sí` (case-insensitive) → Also valid
- **Any other value or empty** → Team **not eligible**

---

# 🚀 EXECUTABLE VERSION (.exe)

### Features
- **No Python installation required**
- **No additional dependencies needed**
- **Double-click execution**
- **Compatible with Windows 10/11**
- **Everything works locally, no internet required**

### Quick Installation

1. **Download** the exe folder

![Step 1.](https://raw.githubusercontent.com/cristian-haro/random_team_selector/refs/heads/main/img/Readme_1.png "Step 1")

![Step 2](https://raw.githubusercontent.com/cristian-haro/random_team_selector/refs/heads/main/img/Readme_2.png "Step 2")

2. **Configure your Excel**:
   - Open `equipos.xlsx`
   - Mark eligible teams with `x`
   - Save changes

3. **Run** by double-clicking `app.exe`

### ⚠️ Security Note (Windows)

It's normal for Windows Defender to show a warning. This happens with compiled Python applications. To run it:

1. Click "More info"
2. Select "Run anyway"
3. The application is 100% safe and contains no malware

### Using the Executable

1. **Prepare your Excel** with eligible teams marked with `x`
2. **Run** `app.exe`
3. **See the result** immediately:

```
==============================
🎲 DRAW RESULT 🎲
==============================
🏆 TEAM:  Atlético
🌍 LEAGUE:    La Liga
==============================

Press Enter to exit...
```

4. **Press Enter** to close the window

---

# PYTHON VERSION

## Main Script: `app.py`

### Features

1. **Data reading**: Reads the Excel file `equipos.xlsx`
2. **Validation**: Verifies file and required columns exist
3. **Data cleaning**: Normalizes the "Elegible" column to avoid errors
4. **Filtering**: Selects only teams marked as eligible
5. **Random selection**: Chooses a winning team at random from eligible ones
6. **Presentation**: Displays results clearly and attractively

## Installation and Configuration

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or copy files** to a local folder
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install pandas openpyxl
   ```

### Dependencies (`requirements.txt`)

- **pandas** (>=1.3.0): For tabular data manipulation
- **openpyxl** (>=3.0.0): For Excel file reading/writing

## Usage

### Basic Execution

1. Ensure `equipos.xlsx` is in the same folder as the script
2. Mark teams you want to participate with `x`
3. Run the script:
   ```bash
   python app.py
   ```
4. The result will display in the console

### Expected Output

```
==============================
🎲 DRAW RESULT 🎲
==============================
🏆 TEAM:  Atlético
🌍 LEAGUE:    La Liga
==============================
```

---

# Troubleshooting

## Common Issues

| Problem | Solution |
|----------|----------|
| **"Windows protected your PC"** | Click "More info" → "Run anyway" |
| **"equipos.xlsx not found"** | Ensure Excel is in the same folder |
| **"No eligible teams"** | Mark at least one team with `x` in Excel |
| **Error opening Excel** | Close Excel before running the program |
| **Always same result** | Verify you have multiple teams marked with `x` |

## For Python Version

If `app.py` doesn't work:
1. Verify Python is installed: `python --version`
2. Install dependencies: `pip install pandas openpyxl`
3. Ensure you're in the correct folder

---

# Customization

## Modifying Team List

1. Open `equipos.xlsx`
2. Edit, add, or remove teams
3. Mark with `x` those you want to be eligible
4. Save changes

## Using for Other Purposes

The tool is flexible and can be used for:
- Gift draws
- Random participant selection
- Team assignments in games
- Any list requiring random selection

Just maintain the column structure:
- **Pais/Liga**: Categories (can be anything)
- **Equipo**: Items to draw
- **Elegible**: Which items are available

---

# Support and Contributions

## Reporting Issues
1. Verify you followed the steps correctly
2. Ensure files are in the same folder
3. If problem persists, contact me

## Improvement Suggestions
Contributions are welcome.

---

**Version**: 2.0.0    
**Last updated**: December 2025  
**Compatibility**: Windows 10/11, Python 3.7+

---

<a name="español"></a>
# 🇪🇸 VERSIÓN EN ESPAÑOL

## Descripción General

Este proyecto consiste en una herramienta para realizar un sorteo aleatorio de equipos de fútbol a partir de un archivo Excel. El sistema filtra los equipos marcados como elegibles y selecciona uno al azar para ser el ganador.

**Disponible en dos versiones:**
- **Versión Python**: Script ejecutable con Python 
- **Versión Ejecutable**: Aplicación .exe lista para usar (sin dependencias)

## Estructura del Proyecto

### Versión Python
```
random_team_selector/
│
├── equipos.xlsx         # Archivo Excel con la base de datos de equipos
├── app.py               # Script principal del sorteo (Python)
├── requirements.txt     # Dependencias del proyecto
└── README.md           # Esta documentación
```

### Versión Ejecutable
```
random_team_selector/
│
├── app.exe   # Aplicación ejecutable principal (Windows)
├── equipos.xlsx        # Archivo Excel con la base de datos de equipos
└── README.md           # Esta documentación
```

## Estructura del Archivo Excel (`equipos.xlsx`)

El archivo Excel contiene las siguientes columnas:

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| **Pais** | País del equipo | España, Inglaterra, Italia |
| **Liga** | Liga en la que compite | Premier League, La Liga, Serie A |
| **Equipo** | Nombre del equipo | Real Madrid, Arsenal, Juventus |
| **Elegible** | Marca de elegibilidad | `x` (sí) o vacío (no) |

### Ejemplo de Datos

```excel
| Pais      | Liga        | Equipo        | Elegible |
|-----------|-------------|---------------|----------|
| España    | La Liga     | Barcelona     | x        |
| Inglaterra| Premier L.  | Arsenal       |          |
| Italia    | Serie A     | Juventus      | x        |
```

**Marcas como elegible:**
- `x` o `X` → Equipo elegible para el sorteo
- `si` o `sí` (en mayúsculas/minúsculas) → También válido
- **Cualquier otro valor o vacío** → Equipo **no elegible**

---

# 🚀 VERSIÓN EJECUTABLE (.exe)

### Características
- **No requiere instalación de Python**
- **No necesita dependencias adicionales**
- **Ejecución con doble clic**
- **Compatible con Windows 10/11**
- **Todo funciona localmente, sin internet**

### Instalación Rápida

1. **Descarga** la carpeta exe:

![Step 1.](https://raw.githubusercontent.com/cristian-haro/random_team_selector/refs/heads/main/img/Readme_1.png "Step 1")

![Step 2](https://raw.githubusercontent.com/cristian-haro/random_team_selector/refs/heads/main/img/Readme_2.png "Step 2")

2. **Configura tu Excel**:
   - Abre `equipos.xlsx`
   - Marca con `x` los equipos elegibles
   - Guarda los cambios

3. **Ejecuta** haciendo doble clic en `app.exe`

### ⚠️ Nota de Seguridad (Windows)

Es normal que Windows Defender muestre una advertencia. Esto ocurre con aplicaciones Python compiladas. Para ejecutarlo:

1. Haz clic en "Más información"
2. Selecciona "Ejecutar de todas formas"
3. La aplicación es 100% segura y no contiene malware

### Uso del Ejecutable

1. **Prepara tu Excel** con los equipos elegibles marcados con `x`
2. **Ejecuta** `app.exe`
3. **Verás el resultado** inmediatamente:

```
==============================
🎲 RESULTADO DEL SORTEO 🎲
==============================
🏆 EQUIPO:  Atlético
🌍 LIGA:    La Liga
==============================

Presiona Enter para salir...
```

4. **Presiona Enter** para cerrar la ventana

---

# VERSIÓN PYTHON

## Script Principal: `app.py`

### Funcionalidades

1. **Lectura de datos**: Lee el archivo Excel `equipos.xlsx`
2. **Validación**: Verifica que el archivo y las columnas necesarias existan
3. **Limpieza de datos**: Normaliza la columna "Elegible" para evitar errores
4. **Filtrado**: Selecciona solo los equipos marcados como elegibles
5. **Sorteo aleatorio**: Elige un equipo ganador al azar entre los elegibles
6. **Presentación**: Muestra el resultado de forma clara y atractiva

## Instalación y Configuración

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o copiar los archivos** en una carpeta local
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   O instalar manualmente:
   ```bash
   pip install pandas openpyxl
   ```

### Dependencias (`requirements.txt`)

- **pandas** (>=1.3.0): Para manipulación de datos tabulares
- **openpyxl** (>=3.0.0): Para lectura/escritura de archivos Excel

## Uso del Programa

### Ejecución Básica

1. Asegúrate de que el archivo `equipos.xlsx` esté en la misma carpeta que el script
2. Marca con `x` los equipos que quieras que participen en el sorteo
3. Ejecuta el script:
   ```bash
   python app.py
   ```
4. El resultado se mostrará en la consola

### Salida Esperada

```
==============================
🎲 RESULTADO DEL SORTEO 🎲
==============================
🏆 EQUIPO:  Atlético
🌍 LIGA:    La Liga
==============================
```

---

# Solución de Problemas

## Problemas Comunes

| Problema | Solución |
|----------|----------|
| **"Windows protegido tu PC"** | Haz clic en "Más información" → "Ejecutar de todas formas" |
| **"equipos.xlsx no encontrado"** | Asegúrate de que el Excel esté en la misma carpeta |
| **"No hay equipos elegibles"** | Marca con `x` al menos un equipo en el Excel |
| **Error al abrir Excel** | Cierra Excel antes de ejecutar el programa |
| **Resultado siempre igual** | Verifica que tengas múltiples equipos marcados con `x` |

## Para la Versión Python

Si `app.py` no funciona:
1. Verifica que Python esté instalado: `python --version`
2. Instala las dependencias: `pip install pandas openpyxl`
3. Asegúrate de estar en la carpeta correcta

---

# Personalización

## Modificar la Lista de Equipos

1. Abre `equipos.xlsx`
2. Edita, añade o elimina equipos
3. Marca con `x` los que quieras que sean elegibles
4. Guarda los cambios

## Usar para Otros Propósitos

La herramienta es flexible y puede usarse para:
- Sorteos de regalos
- Selección aleatoria de participantes
- Asignación de equipos en juegos
- Cualquier lista que necesite selección aleatoria

Solo mantén la estructura de columnas:
- **Pais/Liga**: Categorías (pueden ser cualquier cosa)
- **Equipo**: Elementos a sortear
- **Elegible**: Qué elementos están disponibles

---

# Soporte y Contribuciones

## Reportar Problemas
1. Verifica que sigas los pasos correctamente
2. Asegúrate de tener los archivos en la misma carpeta
3. Si el problema persiste, contáctame

## Sugerencias de Mejora
Las contribuciones son bienvenidas.

---

**Versión**: 2.0.0  
**Última actualización**: Diciembre 2025  
**Compatibilidad**: Windows 10/11, Python 3.7+