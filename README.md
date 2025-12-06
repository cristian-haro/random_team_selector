# Random Team Selector

## Descripción General

Este proyecto consiste en un script de Python que realiza un sorteo aleatorio de equipos de fútbol a partir de un archivo Excel. El sistema filtra los equipos marcados como elegibles y selecciona uno al azar para ser el ganador.

## Estructura del Proyecto

```
random_team_selector/
│
├── equipos.xlsx         # Archivo Excel con la base de datos de equipos
├── app.py    # Script principal del sorteo
├── requirements.txt     # Dependencias del proyecto
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
🏆 EQUIPO:  Barcelona
🌍 LIGA:    La Liga
==============================
```

## Licencia

Este proyecto está creado para uso educativo y personal. Puedes modificarlo y distribuirlo libremente.

## Contribuciones

Las sugerencias y mejoras son bienvenidas. 

---
