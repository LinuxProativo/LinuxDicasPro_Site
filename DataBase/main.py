from PIL import ImageTk
from lista_produtos import ListaProdutos
from screeninfo import get_monitors
import tkinter as tk
from tkinter import ttk, font, PhotoImage
from form_comunicados import FormularioComunicados
from form_links import FormularioLinks
from form_produtos import FormularioProdutos
from lista_comunicados import ListaComunicados
from lista_links import ListaLinks

class TwoColumnResizableApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulário para DataBase LinuxDicasPro")
        self.minsize(900, 500)

        icone: PhotoImage = ImageTk.PhotoImage(file="placeholder.png")
        self.iconphoto(True, icone)

        # Estilo
        style = ttk.Style()
        style.theme_use('clam')
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="TkDefaultFont", size=10)
        self.option_add("*Font", default_font)
        self.option_add("*TButton.Font", default_font)
        self.option_add("*TLabel.Font", default_font)

        # Collections
        self.categories = [
            "Comunicados",
            "Links",
            "Produtos"
        ]
        self.product_platforms = [
            "Amazon",
            "Mercado Livre",
            "Shopee",
            "Hotmart"
        ]

        # PanedWindow
        self.paned = tk.PanedWindow(self, orient="horizontal", sashrelief="raised")
        self.paned.pack(fill="both", expand=True)

        # Frames principais
        self.left_frame = ttk.Frame(self.paned, padding=10)
        self.right_frame = ttk.Frame(self.paned, padding=10)
        self.paned.add(self.left_frame, minsize=450)
        self.paned.add(self.right_frame, minsize=450)

        # Seleção de categoria
        ttk.Label(self.left_frame, text="Selecione a categoria:").pack(anchor="w", pady=(0,2))
        self.category_combo = ttk.Combobox(self.left_frame, values=self.categories, state="readonly")
        self.category_combo.pack(fill="x")
        self.category_combo.current(0)
        self.category_combo.bind("<<ComboboxSelected>>", self.on_category_change)

        # Frame para plataforma Opcional
        self.platform_frame = ttk.Frame(self.left_frame)
        self.platform_frame.pack(fill="x")
        self.platform_label = ttk.Label(self.platform_frame, text="Plataforma:")
        self.platform_combo = ttk.Combobox(self.platform_frame, values=self.product_platforms, state="readonly")

        # Frame para Formulários
        self.form_container = ttk.Frame(self.left_frame)
        self.form_container.pack(fill="both", expand=True, pady=(20,0))

        # Opções de listas
        self.lista_comunicados = ListaComunicados(self.right_frame)
        self.lista_comunicados.pack(fill="both", expand=True)
        self.lista_links = ListaLinks(self.right_frame, placeholder_image_path="placeholder.png")
        self.lista_produtos = ListaProdutos(self.right_frame, self.platform_combo, placeholder_image_path="placeholder.png")

        # Configurações Iniciais
        self.current_form = None
        self.load_form("Comunicados")
        self.geometry("900x500")
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        mouse_x = self.winfo_pointerx()
        mouse_y = self.winfo_pointery()

        target_monitor = None
        for m in get_monitors():
            if m.x <= mouse_x < m.x + m.width and m.y <= mouse_y < m.y + m.height:
                target_monitor = m
                break

        if not target_monitor:
            target_monitor = get_monitors()[0]

        x = target_monitor.x + (target_monitor.width - width) // 2
        y = target_monitor.y + (target_monitor.height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    def load_form(self, category):
        self.form_container.pack_forget()
        self.platform_frame.pack_forget()
        self.lista_comunicados.pack_forget()
        self.lista_links.pack_forget()
        self.lista_produtos.pack_forget()

        for widget in self.form_container.winfo_children():
            widget.destroy()

        for widget in self.platform_frame.winfo_children():
            widget.pack_forget()

        if category == "Comunicados":
            self.current_form = FormularioComunicados(self.form_container, self.lista_comunicados)
            self.current_form.pack(fill="both", expand=True)
            self.form_container.pack(fill="both", expand=True, pady=(20, 0))

            self.lista_comunicados.atualizar_lista()
            self.lista_comunicados.pack(fill="both", expand=True)

        elif category == "Links":
            self.current_form = FormularioLinks(self.form_container, self.lista_links)
            self.current_form.pack(fill="both", expand=True)
            self.form_container.pack(fill="both", expand=True, pady=(20, 0))

            self.lista_links.atualizar_lista()
            self.lista_links.pack(fill="both", expand=True)

        elif category == "Produtos":
            self.platform_frame.pack(fill="x")
            self.platform_label.pack(anchor="w", pady=(20,2))
            self.platform_combo.current(0)
            self.platform_combo.pack(fill="x")
            self.current_form = FormularioProdutos(self.form_container, self.platform_combo, self.lista_produtos)
            self.current_form.pack(fill="both", expand=True)
            self.form_container.pack(fill="both", expand=True, pady=(20, 0))

            self.lista_produtos.atualizar_lista()
            self.lista_produtos.pack(fill="both", expand=True)

    def on_category_change(self, _event):
        category = self.category_combo.get()
        self.load_form(category)

if __name__ == "__main__":
    app = TwoColumnResizableApp()
    app.mainloop()
