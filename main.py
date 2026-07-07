import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("SmartFleet AI")
app.geometry("1200x700")

app.mainloop()

from interface.app import App

if __name__ == "__main__":
    app = App()
    app.mainloop()