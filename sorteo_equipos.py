import pandas as pd
import sys
import os

# --- CONFIGURACIÓN ---
NOMBRE_ARCHIVO = 'equipos.xlsx'
# ---------------------

def seleccionar_equipo_aleatorio():
    # Verificar si el archivo existe
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"❌ Error: No encuentro el archivo '{NOMBRE_ARCHIVO}'.")
        print("Asegúrate de que el Excel está en la misma carpeta que este script.")
        return

    try:
        # 1. Leer el Excel
        df = pd.read_excel(NOMBRE_ARCHIVO)

        # 2. Limpieza de datos para evitar errores humanos
        # Convertimos la columna 'Elegible' a texto, quitamos espacios y ponemos mayúsculas
        if 'Elegible' not in df.columns:
            print("❌ Error: No encuentro la columna 'Elegible' en el Excel.")
            return
            
        df['Elegible_Norm'] = df['Elegible'].astype(str).str.strip().str.upper()

        # 3. Filtrar los equipos
        # Aceptamos 'X', 'SI', 'SÍ' (con tilde)
        criterios_aceptados = ['X', 'SI', 'SÍ']
        filtro = df['Elegible_Norm'].isin(criterios_aceptados)
        
        equipos_candidatos = df[filtro]

        # 4. Verificar si hay candidatos
        if equipos_candidatos.empty:
            print("⚠️ No hay ningún equipo marcado como Elegible ('X' o 'Sí').")
            return

        # 5. Selección Aleatoria (sample elige una fila al azar)
        ganador = equipos_candidatos.sample(n=1).iloc[0]

        # 6. Imprimir el resultado
        print("\n" + "="*30)
        print("🎲 RESULTADO DEL SORTEO 🎲")
        print("="*30)
        print(f"🏆 EQUIPO:  {ganador['Equipo']}")
        print(f"🌍 LIGA:    {ganador['Liga']}")
        print("="*30 + "\n")

    except Exception as e:
        print(f"💥 Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    seleccionar_equipo_aleatorio()
    # Pausa para que no se cierre la ventana inmediatamente si lo ejecutas con doble clic
    input("Presiona Enter para salir...")