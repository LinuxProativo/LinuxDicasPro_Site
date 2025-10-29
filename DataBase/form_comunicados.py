import tkinter as tk
from tkinter import ttk
from gestor_json import GestorJSON


class FormularioComunicados(tk.Frame):
    def __init__(self, parent, atualizar_lista_callback=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.atualizar_lista_callback = atualizar_lista_callback

        style = ttk.Style()
        style.configure("Bordered.TFrame",  background="#d9d9d9", borderwidth=1, relief="solid")

        # Campo: Título
        ttk.Label(self, text="Título:").grid(row=0, column=0, sticky="w", pady=(0,2))
        self.titulo_entry = ttk.Entry(self)
        self.titulo_entry.grid(row=1, column=0, sticky="ew", pady=(0,10))

        ttk.Label(self, text="Descrição:").grid(row=2, column=0, sticky="w", pady=(0, 2))
        self.descricao_frame = ttk.Frame(self, style="Bordered.TFrame")
        self.descricao_frame.grid(row=3, column=0, sticky="ew", pady=(0, 10))

        self.descricao_text = tk.Text(self.descricao_frame, height=12, wrap="word",
                                      relief="flat", bd=0, highlightthickness=1, highlightcolor="#007acc")
        self.descricao_text.pack(fill="both", expand=True, padx=1, pady=1)

        # Botão salvar
        self.botao_salvar = ttk.Button(self, text="Adicionar", command=self.salvar_comunicado)
        self.botao_salvar.grid(row=4, column=0, pady=20)

        self.grid_columnconfigure(0, weight=1)

    def salvar_comunicado(self):
        titulo = self.titulo_entry.get().strip()
        descricao = self.descricao_text.get("1.0", "end").strip()

        gestor = GestorJSON()
        if titulo and descricao:
            gestor.adicionar_comunicado(titulo, descricao)
            self.titulo_entry.delete(0, tk.END)
            self.descricao_text.delete("1.0", tk.END)

            if self.atualizar_lista_callback:
                self.atualizar_lista_callback.atualizar_lista()
