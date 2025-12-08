import customtkinter as ctk
import ttkbootstrap as tb
import pandas as pd
import os
import tkinter as tk
from tkinter import ttk, messagebox

NOMBRE_ARCHIVO = "db.xlsx"


# ============================================
#    DICCIONARIOS DE IDIOMA
# ============================================

TEXTOS = {
    "es": {
        "title": "Sorteo de Equipos",
        "sortear": "🎲 Sortear Equipo",
        "guardar": "💾 Guardar",
        "recargar": "🔄 Recargar Excel",
        "claro": "🌞 Claro",
        "oscuro": "🌙 Oscuro",
        "idioma": "Idioma",
        "ganador_titulo": "Equipo Ganador",
        "ganador_msg": "🏆 EQUIPO: {}\\n🌍 LIGA: {}",
        "no_elegibles": "No hay equipos marcados como X.",
        "no_archivo": "No existe el archivo 'db.xlsx'.",
        "error_excel": "El Excel debe contener la columna 'Elegible'.",
        # NUEVOS TEXTOS - Interfaz
        "stats_teams": "⚽️ Equipos: {}",
        "stats_elegibles": "✔️ Elegibles: {} ({:.2f}%)",
        "filter_all": "Todas",
        "filter_placeholder": "Buscar Equipo...",
        "select_all": "✅ Seleccionar Todo",
        "deselect_all": "❌ Deseleccionar Todo",
        # NUEVOS TEXTOS - Advertencias
        "warning_no_data": "No hay datos cargados para modificar.",
        "warning_col_missing": "La columna '{}' no se encuentra.",
        # NUEVOS TEXTOS - Ventana Ganador
        "winner_title_custom": "🏆 ¡EQUIPO GANADOR! 🏆",
        "winner_league_custom": "🌍 Liga: {}",
        "winner_accept_btn": "Aceptar"
    },
    "en": {
        "title": "Team Lottery",
        "sortear": "🎲 Draw Team",
        "guardar": "💾 Save",
        "recargar": "🔄 Reload Excel",
        "claro": "🌞 Light",
        "oscuro": "🌙 Dark",
        "idioma": "Language",
        "ganador_titulo": "Winning Team",
        "ganador_msg": "🏆 TEAM: {}\\n🌍 LEAGUE: {}",
        "no_elegibles": "No teams marked as X.",
        "no_archivo": "The file 'db.xlsx' does not exist.",
        "error_excel": "The Excel must contain the 'Elegible' column.",
        # NUEVOS TEXTOS - Interfaz
        "stats_teams": "⚽️ Teams: {}",
        "stats_elegibles": "✔️ Eligible: {} ({:.2f}%)",
        "filter_all": "All",
        "filter_placeholder": "Search Team...",
        "select_all": "✅ Select All",
        "deselect_all": "❌ Deselect All",
        # NUEVOS TEXTOS - Advertencias
        "warning_no_data": "No data loaded to modify.",
        "warning_col_missing": "The column '{}' was not found.",
        # NUEVOS TEXTOS - Ventana Ganador
        "winner_title_custom": "🏆 WINNING TEAM! 🏆",
        "winner_league_custom": "🌍 League: {}",
        "winner_accept_btn": "Accept"
    }
}


# ============================================
#         APLICACIÓN PRINCIPAL
# ============================================

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Estado global
        self.idioma = "es"
        self.tema = "dark"
        self.df = None

        # Interfaz
        self.title(TEXTOS[self.idioma]["title"])
        self.geometry("1200x700")
        # Referencia al switch de edición activo
        self.switch_edicion_activo = None 
        # Enlazar un clic global para destruir el switch
        self.bind("<Button-1>", self.destruir_switch_si_activo)

        # Icono personalizado
        try:
            self.iconbitmap("icon.ico") # Usa un archivo .ico
        except tk.TclError:
            print("No se encontró 'icon.ico'. Usando icono por defecto.")
            pass # Continúa si el icono no se encuentra

        # Tema CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Tema ttkbootstrap
        self.style = tb.Style("darkly")

        self.crear_interfaz()
        self.cargar_excel()

    # --------------------------------------------------------------
    def crear_interfaz(self):

        # ▬▬▬▬▬▬▬▬ Barra superior ▬▬▬▬▬▬▬▬▬▬
        top = ctk.CTkFrame(self)
        top.pack(fill="x", pady=10)

        # Botones principales
        self.btn_sortear = ctk.CTkButton(
            top, text=TEXTOS[self.idioma]["sortear"], command=self.sortear
        )
        self.btn_sortear.pack(side="left", padx=10)

        # self.btn_guardar = ctk.CTkButton(
        #     top, text=TEXTOS[self.idioma]["guardar"], command=self.guardar_excel
        # )
        # self.btn_guardar.pack(side="left", padx=10)

        # self.btn_recargar = ctk.CTkButton(
        #     top, text=TEXTOS[self.idioma]["recargar"], command=self.cargar_excel
        # )
        # self.btn_recargar.pack(side="left", padx=10)

        # Selector de idioma
        self.idioma_selector = ctk.CTkComboBox(
            top, values=["Español", "English"], command=self.cambiar_idioma
        )
        self.idioma_selector.set("Español")
        self.idioma_selector.pack(side="right", padx=10)

        # Selector de modo claro/oscuro
        self.tema_btn = ctk.CTkButton(
            top,
            text=TEXTOS[self.idioma]["oscuro"],
            command=self.toggle_tema
        )
        
        self.tema_btn.pack(side="right", padx=10)

        # Sección de Filtros
        
        # Filtro de Liga
        ligas = ["Todas"] # Se rellenará dinámicamente en cargar_excel
        self.liga_filtro = ctk.CTkComboBox(
            top, 
            values=ligas, 
            command=self.aplicar_filtros, 
            width=200
        )
        self.liga_filtro.set("Todas")
        self.liga_filtro.pack(side="left", padx=10)
        
        # Campo de Búsqueda
        self.busqueda_var = tk.StringVar()
        self.busqueda_entry = ctk.CTkEntry(
            top, 
            placeholder_text="Buscar Equipo...", 
            textvariable=self.busqueda_var, 
            width=200
        )
        self.busqueda_entry.pack(side="left", padx=10)
        
        # Vínculo para aplicar filtro al escribir
        self.busqueda_var.trace_add("write", lambda name, index, mode: self.aplicar_filtros())

        # Etiqueta para estadísticas
        self.stats_label = ctk.CTkLabel(top, text="", anchor="w")
        self.stats_label.pack(side="left", padx=20)

        # ▬▬▬▬▬▬▬▬ Tabla moderna ▬▬▬▬▬▬▬▬▬▬
        frame_tabla = tb.Frame(self)
        frame_tabla.pack(expand=True, fill="both", padx=15, pady=15)

        self.tree = tb.Treeview(
            frame_tabla,
            bootstyle="info",
            show="headings"
        )
        self.tree.pack(expand=True, fill="both")

        # ⭐️ Nuevo: Frame para los botones de control global
        control_frame = ctk.CTkFrame(self)
        control_frame.pack(fill="x", pady=(0, 10), padx=10)

        # ⭐️ Botón 'Seleccionar Todo'
        self.seleccionar_btn = ctk.CTkButton(
            control_frame, 
            text="✅ Seleccionar Todo",
            command=lambda: self.gestionar_elegibles("X")
        )
        self.seleccionar_btn.pack(side="left", padx=10)

        # ⭐️ Botón 'Deseleccionar Todo'
        self.deseleccionar_btn = ctk.CTkButton(
            control_frame, 
            text="❌ Deseleccionar Todo",
            command=lambda: self.gestionar_elegibles("")
        )
        self.deseleccionar_btn.pack(side="left", padx=10)

        # Activar doble clic para editar Elegible
        self.tree.bind("<Double-1>", self.editar_elegible)

    # --------------------------------------------------------------
    def cambiar_idioma(self, seleccion):
        self.idioma = "es" if seleccion == "Español" else "en"
        t = TEXTOS[self.idioma]

        self.title(t["title"])
        self.btn_sortear.configure(text=t["sortear"])
        # self.btn_guardar.configure(text=t["guardar"])
        # self.btn_recargar.configure(text=t["recargar"])

        self.tema_btn.configure(text=t["claro"] if self.tema == "dark" else t["oscuro"])

    # --------------------------------------------------------------
    def toggle_tema(self):
        self.tema = "light" if self.tema == "dark" else "dark"
        ctk.set_appearance_mode(self.tema)
        self.style.theme_use("flatly" if self.tema == "light" else "darkly")

        t = TEXTOS[self.idioma]
        self.tema_btn.configure(text=t["claro"] if self.tema == "dark" else t["oscuro"])

    # --------------------------------------------------------------
    def cargar_excel(self):
        t = TEXTOS[self.idioma]

        if not os.path.exists(NOMBRE_ARCHIVO):
            messagebox.showerror("Error", t["no_archivo"])
            return

        self.df = pd.read_excel(NOMBRE_ARCHIVO)

        if "Elegible" not in self.df.columns:
            messagebox.showerror("Error", t["error_excel"])
            return

        # Reemplazar NaN por cadena vacía
        self.df = self.df.fillna('')

        # Rellenar ComboBox de Ligas
        if 'Liga' in self.df.columns:
            ligas = ["Todas"] + sorted(self.df["Liga"].unique().tolist())
            self.liga_filtro.configure(values=ligas)
            self.liga_filtro.set("Todas")

        # Configurar columnas
        self.tree.delete(*self.tree.get_children())
        self.tree.configure(columns=list(self.df.columns))

        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=160)

        # Insertar filas
        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))

        # Aplicar los filtros al cargar, que también llena la tabla
        self.aplicar_filtros(cargar_inicial=True)
        # Actualizar estadísticas después de cargar
        self.actualizar_estadisticas()

    # --------------------------------------------------------------
    def guardar_excel(self):
        data = [self.tree.item(i)["values"] for i in self.tree.get_children()]
        df = pd.DataFrame(data, columns=list(self.df.columns))
        df.to_excel(NOMBRE_ARCHIVO, index=False)
        
        # Actualizar estadísticas
        self.actualizar_estadisticas()

    # --------------------------------------------------------------
    def sortear(self):
        t = TEXTOS[self.idioma]

        data = [self.tree.item(i)["values"] for i in self.tree.get_children()]
        df = pd.DataFrame(data, columns=list(self.df.columns))

        df["Elegible_Norm"] = df["Elegible"].astype(str).str.strip().str.upper()

        candidatos = df[df["Elegible_Norm"] == "X"]

        if candidatos.empty:
            messagebox.showwarning("Aviso", t["no_elegibles"])
            return

        ganador = candidatos.sample(1).iloc[0]

        # ⭐️ Nuevo: Usar animación que luego llama a la ventana personalizada
        self.animar_sorteo(ganador, t)
        
        # ⚠️ ELIMINAR O COMENTAR la siguiente línea si estaba aquí:
        # messagebox.showinfo(
        #     t["ganador_titulo"],
        #     t["ganador_msg"].format(ganador["Equipo"], ganador["Liga"])
        # )

    # --------------------------------------------------------------
    #     EDITOR ELEGANTE (SWITCH) PARA "Elegible"
    # --------------------------------------------------------------
    def editar_elegible(self, event):
        # Destruir el switch activo si existe
        if self.switch_edicion_activo is not None:
            self.switch_edicion_activo.destroy()
            self.switch_edicion_activo = None
        item = self.tree.identify_row(event.y)
        col = self.tree.identify_column(event.x)

        if not item or not col:
            return

        col_index = int(col.replace("#", "")) - 1
        if self.df.columns[col_index] != "Elegible":
            return

        bbox = self.tree.bbox(item, col)
        if not bbox:
            return

        x, y, width, height = bbox

        # Convertir coordenadas a ventana
        abs_x = self.tree.winfo_rootx() - self.winfo_rootx() + x
        abs_y = self.tree.winfo_rooty() - self.winfo_rooty() + y

        valor_actual = self.tree.item(item)["values"][col_index]

        # Switch moderno (CustomTkinter)
        switch = ctk.CTkSwitch(
            master=self,
            text="",
            onvalue="X",
            offvalue="",
            width=60
        )
        switch.place(x=abs_x, y=abs_y)
        switch.select() if valor_actual == "X" else switch.deselect()

        # Guardar referencia al nuevo switch activo
        self.switch_edicion_activo = switch

        def guardar(event=None):
            nuevo = switch.get()
            valores = list(self.tree.item(item)["values"])
            valores[col_index] = nuevo
            self.tree.item(item, values=valores)
            switch.destroy()
            # Destruir el switch y limpiar la referencia
            self.switch_edicion_activo = None
            self.guardar_excel()

        # Vinculaciones
        switch.bind("<Button-1>", guardar)  # Click en el switch

        switch.bind("<ButtonRelease-1>", guardar)
        switch.bind("<FocusOut>", lambda e: guardar())
# --------------------------------------------------------------
    def gestionar_elegibles(self, nuevo_valor):
        t = TEXTOS[self.idioma]

        # Comprueba si hay datos cargados (usa la traducción)
        if self.df is None or self.df.empty:
            messagebox.showwarning("Aviso", t["warning_no_data"])
            return

        try:
            # Identificar el índice de la columna "Elegible"
            col_elegible_index = list(self.df.columns).index("Elegible")
        except ValueError:
            # Mensaje de error si la columna no existe (usa la traducción)
            messagebox.showerror("Error", t["warning_col_missing"].format("Elegible"))
            return

        # 1. Determinar el tag a aplicar: "elegible" si nuevo_valor es 'X', vacío si no lo es.
        tags_a_aplicar = ("elegible",) if nuevo_valor.upper() == "X" else ()
        
        # 2. Iterar sobre todos los elementos visibles en el Treeview
        #    (Esto asegura que solo se actualizan las filas visibles si hay filtros aplicados)
        for item_id in self.tree.get_children():
            # Obtener los valores actuales de la fila
            valores = list(self.tree.item(item_id)["values"])
            
            if len(valores) > col_elegible_index:
                # Actualizar el valor en la posición de "Elegible"
                valores[col_elegible_index] = nuevo_valor
                
                # Aplicar los nuevos valores Y el nuevo tag al Treeview para colorear/descolorear
                self.tree.item(item_id, values=valores, tags=tags_a_aplicar)
                
        # 3. Guardar los cambios en el archivo Excel y actualizar las estadísticas
        self.guardar_excel()
    # --------------------------------------------------------------
    def actualizar_estadisticas(self):
        if self.df is None or self.df.empty:
            self.stats_label.configure(text="")
            return

        # Obtener datos de la tabla (ya procesados y actualizados)
        data = [self.tree.item(i)["values"] for i in self.tree.get_children()]
        df_actual = pd.DataFrame(data, columns=list(self.df.columns))

        # El valor de Elegible_Norm lo necesitamos aquí para contar
        if 'Elegible' not in df_actual.columns:
            return

        # ⚠️ Nota: 'X' es el valor que se usa en editar_elegible
        elegibles = df_actual['Elegible'].astype(str).str.strip().str.upper()
        
        total_equipos = len(elegibles)
        equipos_elegibles = (elegibles == 'X').sum()
        
        porcentaje = (equipos_elegibles / total_equipos) * 100 if total_equipos > 0 else 0

        texto = f"⚽️ Equipos: **{total_equipos}** | ✔️ Elegibles: **{equipos_elegibles}** ({porcentaje:.2f}%)"
        self.stats_label.configure(text=texto)
        
        # Asegúrate de llamar a esta función en `cargar_excel` (modificación ya incluida arriba)
        # y en `guardar_excel` (la llamaremos a continuación)

    # --------------------------------------------------------------
    def aplicar_filtros(self, seleccion=None, cargar_inicial=False):
        if self.df is None:
            return

        # 1. Obtener la selección actual del filtro de liga
        liga_seleccionada = self.liga_filtro.get() if not cargar_inicial else "Todas"
        
        # 2. Obtener el texto de búsqueda
        texto_busqueda = self.busqueda_var.get().strip().lower()

        # 3. Aplicar filtros al DataFrame
        df_filtrado = self.df.copy()

        # Filtro por Liga
        if liga_seleccionada != "Todas" and "Liga" in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado["Liga"] == liga_seleccionada]
        
        # Filtro por Búsqueda de Equipo
        if texto_busqueda and "Equipo" in df_filtrado.columns:
            df_filtrado = df_filtrado[
                df_filtrado["Equipo"].astype(str).str.lower().str.contains(texto_busqueda, na=False)
            ]

        # 4. Limpiar y rellenar la tabla (Treeview)
        self.tree.delete(*self.tree.get_children())
        
        for _, row in df_filtrado.iterrows():
            self.tree.insert("", "end", values=list(row))
        
        # 5. Si es una recarga completa, configurar las columnas
        if cargar_inicial and not df_filtrado.empty:
            self.tree.configure(columns=list(df_filtrado.columns))
            for col in df_filtrado.columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=160)

        # NOTA: Las estadísticas se actualizan con la función `actualizar_estadisticas`, 
        # que lee **toda** la base de datos, no solo la vista filtrada.

# --------------------------------------------------------------
    def destruir_switch_si_activo(self, event=None):
        """Destruye el switch de edición si está activo y el evento no es parte de él."""
        
        # Verificar si el evento de clic ocurre dentro del treeview o en el switch
        # Si el switch existe, lo destruimos solo si el clic no fue sobre él.
        if self.switch_edicion_activo is not None:
            
            # Comprobar si el clic fue en el Treeview, en cuyo caso editar_elegible
            # se encargará de destruirlo antes de crear el nuevo. 
            # Si el evento no viene del Treeview, destruimos el switch.
            if event and event.widget != self.tree:
                self.switch_edicion_activo.destroy()
                self.switch_edicion_activo = None
# --------------------------------------------------------------
    def animar_sorteo(self, ganador, textos, iteraciones=0):
            t = textos
            items = self.tree.get_children()
            
            if iteraciones < 10: 
                # ... (Lógica de parpadeo de color)

                self.after(100, lambda: self.animar_sorteo(ganador, t, iteraciones + 1))
            else:
                # Terminar la animación y mostrar el ganador
                self.style.configure("Treeview", background="", fieldbackground="", foreground="") 
                
                # ⭐️ Nuevo: Llamar a la ventana personalizada
                self.mostrar_ganador_personalizado(ganador, t) # <--- CAMBIO AQUÍ
# --------------------------------------------------------------
    def mostrar_ganador_personalizado(self, ganador, textos):
        t = textos
        
        # Crear la ventana TopLevel (similar a un pop-up)
        ganador_ventana = ctk.CTkToplevel(self)
        ganador_ventana.title(t["ganador_titulo"])
        ganador_ventana.geometry("450x300")
        ganador_ventana.resizable(False, False)
        
        # Centrar la ventana sobre la principal (opcional, pero mejor UX)
        self.update_idletasks()
        ancho_app = self.winfo_width()
        alto_app = self.winfo_height()
        pos_x = self.winfo_x() + (ancho_app // 2) - (450 // 2)
        pos_y = self.winfo_y() + (alto_app // 2) - (300 // 2)
        ganador_ventana.geometry(f'+{pos_x}+{pos_y}')

        # Asegurar que el pop-up esté siempre encima y no se pueda usar la ventana principal
        ganador_ventana.grab_set() 
        
        # --- Contenido y Estilo ---
        
        # 1. Título
        ctk.CTkLabel(
            ganador_ventana, 
            text="🏆 ¡EQUIPO GANADOR! 🏆", 
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=(20, 10))
        
        # 2. Equipo
        ctk.CTkLabel(
            ganador_ventana, 
            text=f'⚽ {ganador["Equipo"]}', 
            font=ctk.CTkFont(size=36, weight="bold", family="Arial")
        ).pack(pady=10)
        
        # 3. Liga
        ctk.CTkLabel(
            ganador_ventana, 
            text=f'🌍 Liga: {ganador["Liga"]}', 
            font=ctk.CTkFont(size=18)
        ).pack(pady=5)

        # 4. Botón de Cierre
        ctk.CTkButton(
            ganador_ventana, 
            text="Aceptar", 
            command=ganador_ventana.destroy,
            fg_color="green", # Resaltar el botón
            hover_color="#1F7A1F"
        ).pack(pady=(30, 20), ipadx=10, ipady=5)
# ============================================
#                EJECUCIÓN
# ============================================

if __name__ == "__main__":
    app = App()
    app.mainloop()
