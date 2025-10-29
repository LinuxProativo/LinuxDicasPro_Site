import tkinter as tk
from tkinter import ttk, PhotoImage

from form_editor import FormEditor
from gestor_json import GestorJSON
from list_base import ListaBase


class ListaProdutos(ListaBase):
    def __init__(self, parent, platform_combo, placeholder_image_path=None, **kwargs):
        self.platform_combo = platform_combo
        super().__init__(parent, placeholder_image_path, **kwargs)
        self.platform_combo.bind("<<ComboboxSelected>>", lambda e: self.atualizar_lista())
        self.atualizar_lista()

    def render_items(self):
        gestor = GestorJSON()
        plataforma_atual = self.platform_combo.get().strip().lower().replace(" ", "_")

        for i, produto in enumerate(gestor.listar_produtos(plataforma_atual)):
            container = tk.Frame(self.inner_frame, background="#f0f0f0", pady=10)
            container.pack(fill="x", padx=10, pady=5)

            # Imagem
            img: PhotoImage = self.carregar_imagem(produto.get("link_imagem"))
            img_label = tk.Label(container, image=img, background="#f0f0f0")
            img_label.image = img
            img_label.pack(side="left", padx=(0, 10))

            text_frame = tk.Frame(container, background="#f0f0f0")
            text_frame.pack(side="left", fill="both", expand=True)

            text_frame.grid_rowconfigure(0, weight=1)
            text_frame.grid_rowconfigure(2, weight=1)

            content = tk.Frame(text_frame, background="#f0f0f0")
            content.grid(row=1, column=0, sticky="n")

            titulo = produto.get("nome", "")
            subtitulo = produto.get("descricao", "")
            link = produto.get("link", "")

            tk.Label(content, text=titulo, font=("TkDefaultFont", 18, "bold"), anchor="w", background="#f0f0f0").pack(fill="x")
            if subtitulo:
                tk.Label(content, text=subtitulo, font=("TkDefaultFont", 10), anchor="w",
                         background="#f0f0f0").pack(fill="x", pady=(2, 0))

            if link:
                link_label = tk.Label(content, text=link, font=("TkDefaultFont", 10, "underline"), fg="blue",
                                      cursor="hand2", anchor="w", background="#f0f0f0")

                link_label.pack(fill="x", pady=(2, 0))
                link_label.bind("<Button-1>", lambda e, url=link: self.abrir_link(url))

            btn_frame = tk.Frame(content, background="#f0f0f0")
            btn_frame.pack(fill="x", pady=(5, 0))

            editar_btn = ttk.Button(btn_frame, text="Editar", width=10, command=lambda p=i: self.editar_produto(p))
            remover_btn = ttk.Button(btn_frame, text="Remover", width=10,
                                    command=lambda p=i: self.remover_produto(p))

            editar_btn.pack(side="left", padx=(0, 5))
            remover_btn.pack(side="left")
            self.bind_item_scroll(container)

    def editar_produto(self, indice):
        gestor = GestorJSON()
        plataforma = self.platform_combo.get().strip().lower().replace(" ", "_")
        produto = gestor.listar_produtos(plataforma)[indice]
        labels = ["nome", "descrição", "link", "link da imagem"]
        campos = ["nome", "descricao", "link", "link_imagem"]

        def salvar_callback(novos_valores):
            gestor.editar_produto(plataforma, indice, novos_valores)
            self.atualizar_lista()

        FormEditor(self, "Editar Produto", labels, campos, produto, salvar_callback)

    def remover_produto(self, indice):
        gestor = GestorJSON()
        gestor.remover_produto(self.platform_combo.get().strip().lower().replace(" ", "_"), indice)
        self.atualizar_lista()