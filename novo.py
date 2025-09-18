import customtkinter as ctk


app = ctk.CTk()
app.title("Frutaria Do zé")
app.geometry("900x800")
app.resizable(False,False)


entry = ctk.CTkEntry(app, placeholder_text="66")
entry.pack()




app.mainloop()