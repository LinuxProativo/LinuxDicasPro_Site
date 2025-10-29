import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser

class ListaBase(tk.Frame):
    def __init__(self, parent, placeholder_image_path=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.placeholder_image_path = placeholder_image_path

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Vertical.TScrollbar", gripcount=0, width=12)

        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, background="#f0f0f0")
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview,
                                       style="Custom.Vertical.TScrollbar")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.inner_frame = tk.Frame(self.canvas, background="#f0f0f0")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.inner_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel)
        self.inner_frame.bind("<Button-4>", self._on_mousewheel)
        self.inner_frame.bind("<Button-5>", self._on_mousewheel)

    def _on_frame_configure(self, _event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        canvas_height = self.canvas.winfo_height()
        frame_height = self.inner_frame.winfo_reqheight()
        if frame_height <= canvas_height:
            return
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")
        else:
            self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    def bind_item_scroll(self, widget):
        widget.bind("<Button-4>", self._on_mousewheel)
        widget.bind("<Button-5>", self._on_mousewheel)
        widget.bind("<MouseWheel>", self._on_mousewheel)
        for child in widget.winfo_children():
            self.bind_item_scroll(child)

    def carregar_imagem(self, url, size=256):
        try:
            if url:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
            else:
                img = Image.open(self.placeholder_image_path)
            img = img.resize((size, size))
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(e)
            if self.placeholder_image_path:
                img = Image.open(self.placeholder_image_path).resize((size, size))
                return ImageTk.PhotoImage(img)
            return None

    @staticmethod
    def abrir_link(url):
        if url:
            webbrowser.open(url)

    def atualizar_lista(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        self.render_items()

    def render_items(self):
        raise NotImplementedError
