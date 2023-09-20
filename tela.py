import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x400")

def clique():
    print("Fazer Login")

texto = customtkinter.CTkLabel(janela, text="Sistema de cadastros")
email = customtkinter.CTkEntry(janela,
                               placeholder_text="E-mail")
senha = customtkinter.CTkEntry(janela,
                               placeholder_text="Senha", show="*")
botao = customtkinter.CTkButton(janela, text="Login",
                                command=clique)



texto.pack(padx=20, pady=20)
email.pack(padx=20, pady=20)
senha.pack(padx=20, pady=20)
botao.pack(padx=20, pady=20)
janela.mainloop()