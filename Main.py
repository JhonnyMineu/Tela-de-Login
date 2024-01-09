import tkinter

janela = tkinter.Tk()
janela.geometry("500x300")

def clique():
    print("Teste")
    
texto = tkinter.Label(janela, text="Login")
texto.pack(padx=10, pady=10)

email = tkinter.Entry(janela)
email.pack(padx=10, pady=10)

senha = tkinter.Entry(janela, show="*")
senha.pack(padx=10, pady=10)

checkbox = tkinter.Checkbutton (janela, text="Mostrar senha?")
checkbox.pack(padx=10, pady=10)

botao = tkinter.Button(janela, text="Entrar", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()