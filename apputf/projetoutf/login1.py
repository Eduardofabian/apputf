

from tkinter import *
from tkinter import messagebox


#comandos

def comando(op) :
    if (op == 1):
        print("tela ligada")
    elif (op == 2):
        print("tela ligada")

def register():
    #removendo botoes
    bt1.place(x=5000, y=5000)
    bt2.place(x=5000, y=5000)
    bt3 = 

janela = Tk()
janela.title('Tela Inicial')
janela.geometry("200x150+100+100")
janela.configure(background="white")
janela.attributes("-alpha", 0.9)



#carregando img
Logo = PhotoImage(file="icons/loguinho.png")

lb3 = Label(janela, text="Bem vindo ao CRIPVEST")
lb1 = Label(janela, text="Login: ")
lb2 = Label(janela, text="Senha")

ed1 = Entry(janela,)
ed2 = Entry(janela, show="*")

bt1 = Button(janela, text="Confirmar")
bt2 = Button(janela, text="Registrar", command=register)


lb3.grid(row=0, column=1)
lb1.grid(row=1, column=0)
lb2.grid(row=2, column=0)
ed1.grid(row=1, column=1)
ed2.grid(row=2, column=1)
bt1.grid(row=3, column=1)
bt2.grid(row=4, column=1)
bt3.grid(row=4, column=1)


janela.mainloop()


