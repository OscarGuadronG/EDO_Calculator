import customtkinter as ctk

ctk.set_appearance_mode("dark")  # "light" o "system"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Hola, CustomTkinter!")
label.pack(pady=20)

app.mainloop()