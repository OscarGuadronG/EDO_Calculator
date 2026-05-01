import customtkinter as ctk
from view.style import theme

class CreateSeccion(ctk.CTkFrame):

    def __init__(self, master, title, options, on_select):
        super().__init__(master)

        self.on_select = on_select
        self.build(title, options)
    
    def build(self, title, options):
        label = ctk.CTkLabel(self, text=title, 
                               font=theme.FONT_TITLE, 
                               text_color=theme.PRIMARY_COLOR)
        label.pack(pady=[20, 5], padx=10, anchor="w")

        for text, value in options:
            btn = ctk.CTkButton(self, text=text,
                                height=theme.BUTTON_HEIGHT,
                                command=lambda v=value: self.on_select(v)
                                )
            btn.pack(fill="x", pady=5, padx=10)
    
