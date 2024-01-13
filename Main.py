import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()

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

        usuario = ctk.CTkEntry(frame, placeholder_text= "Seu usuário", width=300, font=('Roboto', 14)).place(x=25,y=155)

        senha = ctk.CTkEntry(frame, placeholder_text= "Sua senha", show="*",
                                        width=300, font=('Roboto', 14)).place(x=25,y=195)

        checkbox = ctk.CTkCheckBox(frame, text="Mostrar senha?",  onvalue=1,
                                            offvalue=0, width=50, height=15).place(x=205,y=235)

        botao = ctk.CTkButton(frame, text="Entrar").place(x=110,y=280)



Application()



