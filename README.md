# Random Team Selector

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

**Versión**: 1.1.0  
**Última actualización**: Diciembre 2025  
**Compatibilidad**: Windows 10/11, Python 3.7+