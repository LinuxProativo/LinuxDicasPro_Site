import tkinter as tk
from tkinter import ttk
from gestor_json import GestorJSON


class FormularioProdutos(tk.Frame):
    def __init__(self, parent, plataforma, atualizar_lista_callback=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.plataforma = plataforma
        self.atualizar_lista_callback = atualizar_lista_callback

        # Nome do Produto
        ttk.Label(self, text="Nome do Produto:").grid(row=0, column=0, sticky="w", pady=(0,2))
        self.nome_entry = ttk.Entry(self)
        self.nome_entry.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        # Descrição
        ttk.Label(self, text="Descrição:").grid(row=2, column=0, sticky="w", pady=(0, 2))
        self.descricao_entry = ttk.Entry(self)
        self.descricao_entry.grid(row=3, column=0, sticky="ew", pady=(0, 10))

        # Link do Produto
        ttk.Label(self, text="Link do Produto:").grid(row=4, column=0, sticky="w", pady=(0, 2))
        self.link_entry = ttk.Entry(self)
        self.link_entry.grid(row=5, column=0, sticky="ew", pady=(0, 10))

        # Link da Imagem
        ttk.Label(self, text="Link da Imagem:").grid(row=6, column=0, sticky="w", pady=(0, 2))
        self.link_imagem_entry = ttk.Entry(self)
        self.link_imagem_entry.grid(row=7, column=0, sticky="ew", pady=(0, 10))

        # Botão salvar
        self.botao_salvar = ttk.Button(self, text="Adicionar", command=self.salvar_produto)
        self.botao_salvar.grid(row=8, column=0, pady=20)

        # Faz coluna expandir
        self.grid_columnconfigure(0, weight=1)

    def salvar_produto(self):
        nome = self.nome_entry.get().strip()
        descricao = self.descricao_entry.get().strip()
        link = self.link_entry.get().strip()
        link_imagem = self.link_imagem_entry.get().strip()

        gestor = GestorJSON()
        if nome and descricao and link and link_imagem:
            gestor.adicionar_produto(self.plataforma.get().strip().lower().replace(" ", "_"), nome, descricao, link, link_imagem)
            self.nome_entry.delete(0, tk.END)
            self.descricao_entry.delete(0, tk.END)
            self.link_entry.delete(0, tk.END)
            self.link_imagem_entry.delete(0, tk.END)

            if self.atualizar_lista_callback:
                self.atualizar_lista_callback.atualizar_lista()
