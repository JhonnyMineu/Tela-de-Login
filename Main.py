import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import csv

janela = ctk.CTk()

check_var = ctk.IntVar(value=0)

class Application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.janela_login()
        janela.mainloop()

    def tema(self):
        # Estilo da janela
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

    def tela(self):
        # Janela de login
        janela.geometry("700x400")
        janela.title("Controle MS Ao Vivo")
        janela.resizable(width=FALSE,height=FALSE)
        janela.iconbitmap("logo.ico")

    def janela_login(self):

        def checkbox_event():
            if checkbox.get() == 1:
                senha.configure(show="",placeholder_text= "Sua senha")
            else:
                senha.configure(show="*",placeholder_text= "Sua senha")

        def validar_login():
            with open('Users.txt', 'r') as f:
                leitor = csv.DictReader(f)  # cria um leitor de CSV que mapeia os valores em cada linha para um dicionário ordenado
                for linha in leitor:
                    if linha['Login'] == usuario.get() and linha['Senha'] == senha.get():  # compara os valores de 'Login' e 'Senha' com 'entry' e 'senha'
                        return print('Login bem-sucedido!')
            return messagebox.showinfo("Acesso negado!",message="Login ou senha incorretos.")

        # Imagem do bidu 
        img = PhotoImage(file="C:/Users/jhow_/OneDrive/Documentos/GitHub/Tela-de-Login/bidu.png")
        label_img = ctk.CTkLabel(janela, image=img, text="")
        label_img.place(x=20,y=35)

        # Parte direita da janela
        frame = ctk.CTkFrame(janela, width=350, height=396)
        frame.pack(side=RIGHT)

        # Campos de input do usuário
        texto = ctk.CTkLabel(frame, text="Login", font=('Roboto', 30, 'bold'), text_color= ('white'))
        texto.place(x=140,y=60)

        usuario = ctk.CTkEntry(frame, placeholder_text= "Seu usuário", width=300, font=('Roboto', 14))
        usuario.place(x=25,y=155)

        senha = ctk.CTkEntry(frame, placeholder_text= "Sua senha", show="*",
                                    width=300, font=('Roboto', 14))
        senha.place(x=25,y=195)


        checkbox = ctk.CTkCheckBox(frame, text="Mostrar senha?",command=checkbox_event, variable=check_var,  onvalue=1,
                                            offvalue=0, width=50, height=15)
        checkbox.place(x=205,y=235)

        botao = ctk.CTkButton(frame, text="Entrar",font=('Roboto', 14), command=validar_login)
        botao.place(x=110,y=280)



Application()



