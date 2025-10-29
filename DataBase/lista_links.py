import tkinter as tk
from tkinter import ttk, PhotoImage

from form_editor import FormEditor
from gestor_json import GestorJSON
from list_base import ListaBase


class ListaLinks(ListaBase):
    def __init__(self, parent, placeholder_image_path=None, **kwargs):
        super().__init__(parent, placeholder_image_path, **kwargs)
        self.atualizar_lista()

    def render_items(self):
        gestor = GestorJSON()
        for i, link_item in enumerate(gestor.listar_links()):
            container = tk.Frame(self.inner_frame, background="#f0f0f0", pady=10)
            container.pack(fill="x", padx=10, pady=5)

            # Coluna da imagem
            img: PhotoImage = self.carregar_imagem(link_item.get("link_imagem"))
            img_label = tk.Label(container, image=img, background="#f0f0f0")
            img_label.image = img
            img_label.pack(side="left", padx=(0, 10))

            # Coluna do conteúdo → grid para centralizar verticalmente
            text_frame = tk.Frame(container, background="#f0f0f0")
            text_frame.pack(side="left", fill="both", expand=True)

            text_frame.grid_rowconfigure(0, weight=1)
            text_frame.grid_rowconfigure(2, weight=1)

            content = tk.Frame(text_frame, background="#f0f0f0")
            content.grid(row=1, column=0, sticky="n")

            titulo = link_item.get("titulo", "")
            subtitulo = link_item.get("subtitulo", "")
            link = link_item.get("link", "")

            tk.Label(content, text=titulo, font=("TkDefaultFont", 18, "bold"),
                     anchor="w", background="#f0f0f0").pack(fill="x")
            if subtitulo:
                tk.Label(content, text=subtitulo, font=("TkDefaultFont", 10),
                         anchor="w", background="#f0f0f0").pack(fill="x")
            if link:
                link_label = tk.Label(content, text=link, font=("TkDefaultFont", 10, "underline"), fg="blue",
                                      cursor="hand2", anchor="w", background="#f0f0f0")
                link_label.pack(fill="x")
                link_label.bind("<Button-1>", lambda e, url=link: self.abrir_link(url))

            btn_frame = tk.Frame(content, background="#f0f0f0")
            btn_frame.pack(fill="x", pady=(5, 0))

            editar_btn = ttk.Button(btn_frame, text="Editar", width=10,
                                   command=lambda idx=i: self.editar_link(idx))
            remover_btn = ttk.Button(btn_frame, text="Remover", width=10,
                                    command=lambda idx=i: self.remover_link(idx))

            editar_btn.pack(side="left", padx=(0, 5))
            remover_btn.pack(side="left")

            self.bind_item_scroll(container)

    def editar_link(self, indice):
        gestor = GestorJSON()
        link_item = gestor.listar_links()[indice]
        labels = ["título", "subtítulo", "link", "link da imagem"]
        campos = ["titulo", "subtitulo", "link", "link_imagem"]

        def salvar_callback(novos_valores):
            gestor.editar_link(indice, novos_valores)
            self.atualizar_lista()

        FormEditor(self, "Editar Link", labels, campos, link_item, salvar_callback)

    def remover_link(self, indice):
            gestor = GestorJSON()
            gestor.remover_link(indice)
            self.atualizar_lista()