import tkinter as tk
from tkinter import ttk

from screeninfo import get_monitors


class FormEditor(tk.Toplevel):
    def __init__(self, parent, titulo, labels, campos, valores_iniciais, on_save, multiline_fields=None):
        super().__init__(parent)
        self.title(titulo)
        self.resizable(False, False)
        self.minsize(600, 200)
        self.transient(parent)
        self.grab_set()

        style = ttk.Style()
        style.configure("Bordered.TFrame", background="#d9d9d9", borderwidth=1, relief="solid")

        self.campos = campos
        self.labels = labels
        self.entries = {}
        self.on_save = on_save
        self.multiline_fields = multiline_fields or []

        self.columnconfigure(1, weight=1)

        # Criação dos campos
        for i, campo in enumerate(campos):
            ttk.Label(self, text=self.labels[i].capitalize() + ":").grid(
                row=i, column=0, padx=10, pady=5, sticky="nw"
            )

            if campo in self.multiline_fields:
                frame = ttk.Frame(self, style="Bordered.TFrame")
                frame.grid(row=i, column=1, padx=10, pady=5, sticky="ew")

                txt = tk.Text(frame, height=12, wrap="word", relief="flat", bd=0,
                              highlightthickness=1, highlightcolor="#007acc")
                txt.grid(padx=1, pady=1)
                txt.insert("1.0", valores_iniciais.get(campo, ""))
                self.entries[campo] = txt
            else:
                entry = ttk.Entry(self)
                entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
                entry.insert(0, valores_iniciais.get(campo, ""))
                self.entries[campo] = entry

        # Botões
        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=len(campos), column=0, columnspan=2, pady=10)

        ttk.Button(btn_frame, text="Salvar", command=self.salvar).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Cancelar", command=self.destroy).pack(side="left", padx=5)

        self.update_idletasks()
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

    def salvar(self):
        novos_valores = {}
        for campo, widget in self.entries.items():
            if isinstance(widget, tk.Text):
                novos_valores[campo] = widget.get("1.0", "end-1c")
            else:
                novos_valores[campo] = widget.get()
        self.on_save(novos_valores)
        self.destroy()
