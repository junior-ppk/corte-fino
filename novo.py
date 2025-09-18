import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Vendas Serras Online")
app.geometry("290x585")
app.resizable(False,False)
botao_arredondado = ctk.CTkButton(app, text="clique aqui ", corner_radius=15)
botao_arredondado.pack(pady=20)

label = ctk.CTkLabel(app, text="Olá \n Bem-vindo ", fg_color="transparent")
label.pack (padx=30, pady=20)


label = ctk.CTkLabel(app, text="Digite seu nome abaixo", fg_color="transparent")
label.pack (padx=10, pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Digite aqui ")
entry.pack()

label = ctk.CTkLabel(app, text="Digite o CNPJ da sua empresa abaixo  ", fg_color="transparent")
label.pack (padx=10, pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Digite aqui ")
entry.pack()







app.mainloop()