import tkinter as tk
from tkinter import ttk

from form_editor import FormEditor
from gestor_json import GestorJSON
from list_base import ListaBase

class ListaComunicados(ListaBase):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.atualizar_lista()

    def render_items(self):
        gestor = GestorJSON()
        for i, comunicado in enumerate(gestor.listar_comunicados()):
            container = tk.Frame(self.inner_frame, background="#f0f0f0", padx=10)
            container.pack(fill="x")

            titulo_label = ttk.Label(container, background="#f0f0f0", text=comunicado["titulo"], font=("TkDefaultFont", 18, "bold"))
            titulo_label.pack(anchor="w", pady=(5,0))

            descricao_label = ttk.Label(container, background="#f0f0f0", text=comunicado["descricao"], font=("TkDefaultFont", 10))
            descricao_label.pack(anchor="w", pady=(0,5))

            btn_frame = tk.Frame(container, background="#f0f0f0")
            btn_frame.pack(fill="x")
            ttk.Button(btn_frame, text="Editar", width=10,
                       command=lambda idx=i: self.editar_comunicado(idx)).pack(side="left", padx=(0,5), pady=(0,10))
            ttk.Button(btn_frame, text="Remover", width=10,
                       command=lambda idx=i: self.remover_comunicado(idx)).pack(side="left", pady=(0,10))

            self.bind_item_scroll(container)

    def editar_comunicado(self, indice):
        gestor = GestorJSON()
        comunicado = gestor.listar_comunicados()[indice]
        labels = ["título", "descrição"]
        campos = ["titulo", "descricao"]

        def salvar_callback(novos_valores):
            gestor.editar_comunicado(indice, novos_valores)
            self.atualizar_lista()

        FormEditor(self, "Editar Comunicado", labels, campos, comunicado, salvar_callback, multiline_fields=["descricao"])

    def remover_comunicado(self, indice):
        gestor = GestorJSON()
        gestor.remover_comunicado(indice)
        self.atualizar_lista()