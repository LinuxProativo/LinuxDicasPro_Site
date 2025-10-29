import tkinter as tk
from tkinter import ttk
from gestor_json import GestorJSON


class FormularioLinks(tk.Frame):
    def __init__(self, parent, atualizar_lista_callback=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.atualizar_lista_callback = atualizar_lista_callback

        # Título
        ttk.Label(self, text="Título:").grid(row=0, column=0, sticky="w", pady=(0,2))
        self.titulo_entry = ttk.Entry(self)
        self.titulo_entry.grid(row=1, column=0, sticky="ew", pady=(0,10))

        # Subtítulo
        ttk.Label(self, text="Subtítulo:").grid(row=2, column=0, sticky="w", pady=(0,2))
        self.subtitulo_entry = ttk.Entry(self)
        self.subtitulo_entry.grid(row=3, column=0, sticky="ew", pady=(0,10))

        # Link
        ttk.Label(self, text="Link:").grid(row=4, column=0, sticky="w", pady=(0,2))
        self.link_entry = ttk.Entry(self)
        self.link_entry.grid(row=5, column=0, sticky="ew", pady=(0,10))

        # Link da Imagem
        ttk.Label(self, text="Link da Imagem:").grid(row=6, column=0, sticky="w", pady=(0,2))
        self.link_imagem_entry = ttk.Entry(self)
        self.link_imagem_entry.grid(row=7, column=0, sticky="ew", pady=(0,10))

        # Botão para capturar valores
        self.botao_salvar = ttk.Button(self, text="Adicionar", command=self.salvar_link)
        self.botao_salvar.grid(row=8, column=0, pady=20)

        self.grid_columnconfigure(0, weight=1)

    def salvar_link(self):
        titulo = self.titulo_entry.get().strip()
        subtitulo = self.subtitulo_entry.get().strip()
        link = self.link_entry.get().strip()
        link_imagem = self.link_imagem_entry.get().strip()

        gestor = GestorJSON()
        if titulo and link:
            gestor.adicionar_link(titulo, subtitulo, link, link_imagem)
            self.titulo_entry.delete(0, tk.END)
            self.subtitulo_entry.delete(0, tk.END)
            self.link_entry.delete(0, tk.END)
            self.link_imagem_entry.delete(0, tk.END)

            if self.atualizar_lista_callback:
                self.atualizar_lista_callback.atualizar_lista()
