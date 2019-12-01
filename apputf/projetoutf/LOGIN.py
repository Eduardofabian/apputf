from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

# janela
from pip._vendor.colorama import Back

janela = Tk()
janela.title("Crip Invest")
janela.geometry("400x400")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)

# carregar imagens
Logo = PhotoImage(file="icons/loguinho.png")
photo1 = PhotoImage(file="icons/dogecoin.png")
photo2 = PhotoImage(file="icons/TETHER.png")
photo3 = PhotoImage(file="icons/STELLAR.png")
photo4 = PhotoImage(file="icons/XRP.png")
photo5 = PhotoImage(file="icons/LISK.png")
photo6 = PhotoImage(file="icons/LITECOIN.png")
photo7 = PhotoImage(file="icons/ETHEREUM.png")
photo8 = PhotoImage(file="icons/DASH.png")
photo9 = PhotoImage(file="icons/bitecoin.png")

# ===== Widgets ==================


RightFrame = Frame(janela, width=400, height=400, bg="white", relief="raise")
RightFrame.pack(side=RIGHT)

WelcomeLabel = Label(RightFrame, text="Bem vindo ao cripvest", font=("Baskerville Old Face", 20), bg="white",
                     fg="Khaki")
WelcomeLabel.place(x=100, y=50)
UserLabel = Label(RightFrame, text="Usuario:", font=("Baskerville Old Face", 20), bg="white", fg="black")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Senha:", font=("Baskerville Old Face", 20), bg="white", fg="black")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)


def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users 
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem Vindo!") \
                (command=TelaInvestidor())
        else:
            messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se esta cadastro no sistema!")

    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se esta cadastro no sistema!")


# Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)


# tipos de investidores-------------------------------------------------------------------
# tela conservador--------------------------
# telas moedas conservadores


def TelaDogecoin():
    # removendo widgets da tela dogecoin
    Dogecoin.place(x=5000)
    Tether.place(x=5000)
    Stellar.place(x=5000)
    BackTelainvestidor.place(x=5000)
    # adicionando widget tela dogecoin
    BackTelaConservador.place(x=125, y=260)
    photodogecoin.place(x=50, y=25)


photodogecoin = Label(RightFrame, image=photo1, bg="black")


def TelaTether():
    # removendo widgets da tela tether
    Dogecoin.place(x=5000)
    Tether.place(x=5000)
    Stellar.place(x=5000)
    BackTelainvestidor.place(x=5000)
    # adicionando widget tela tether
    phototether.place(x=50, y=25)
    BackTelaConservador.place(x=125, y=260)


phototether = Label(RightFrame, image=photo2, bg="black")


def TelaStellar():
    # removendo widgets da tela stellar
    Dogecoin.place(x=5000)
    Tether.place(x=5000)
    Stellar.place(x=5000)
    BackTelainvestidor.place(x=5000)
    # adicionando widget tela stellar
    photostellar.place(x=50, y=25)
    BackTelaConservador.place(x=125, y=260)


photostellar = Label(RightFrame, image=photo3, bg="black")


def BackTelaConservador():
    # Removendo Widgets de tela moedas conservadores
    photodogecoin.place(x=5000)
    phototether.place(x=5000)
    photostellar.place(x=5000)
    BackTelaConservador.place(x=5000)
    # Inserindo Widgets da tela conservador
    Dogecoin.place(x=130, y=110)
    Tether.place(x=130, y=140)
    Stellar.place(x=130, y=170)
    BackTelainvestidor.place(x=125)


BackTelaConservador = ttk.Button(RightFrame, text="Voltar Tela Conservador", width=20, command=BackTelaConservador)

BackTelaConservador.place(x=125, y=260)


def TelaConservador():
    # Removendo widgets de telainvestidor
    Conservador.place(x=5000)
    Moderado.place(x=5000)
    Agressivo.place(x=5000)
    BackLogin.place(x=5000)
    LoginButton.place(x=5000)
    # Inserindo Widgets da tela conservador
    Dogecoin.place(x=130, y=110)
    Tether.place(x=130, y=140)
    Stellar.place(x=130, y=170)
    BackTelainvestidor.place(x=125)


Dogecoin = ttk.Button(RightFrame, text="Dogecoin", width=20, command=TelaDogecoin)
Tether = ttk.Button(RightFrame, text="Tether", width=20, command=TelaTether)
Stellar = ttk.Button(RightFrame, text="Stellar", width=20, command=TelaStellar)


# tela moderado-----------------------------------------------------------

def TelaXrp():
    # removendo widgets da tela dogecoin
    Xrp.place(x=5000)
    Lisk.place(x=5000)
    Litecoin.place(x=5000)
    BackTelainvestidor.place(x=5000)
    # adicionando widget tela dogecoin
    BackTelaModerado.place(x=125, y=260)
    photoxrp.place(x=50, y=25)


photoxrp = Label(RightFrame, image=photo4, bg="black")


def TelaLisk():
    # removendo widgets da tela tether
    Xrp.place(x=5000)
    Lisk.place(x=5000)
    Litecoin.place(x=5000)
    BackTelainvestidor.place(x=5000)
    # adicionando widget tela dogecoin
    photolisk.place(x=50, y=25)
    BackTelaModerado.place(x=125, y=260)


photolisk = Label(RightFrame, image=photo5, bg="black")


def TelaLitecoin():
    # removendo widgets da tela stellar
    Xrp.place(x=5000)
    Lisk.place(x=5000)
    Litecoin.place(x=5000)
    BackTelainvestidor.place(x=5000)

    # adicionando widget tela dogecoin
    photolitecoin.place(x=50, y=25)
    BackTelaModerado.place(x=125, y=260)


photolitecoin = Label(RightFrame, image=photo6, bg="black")


def BackTelaModerado():
    # Removendo Widgets de tela moedas moderadas
    photoxrp.place(x=5000)
    photolitecoin.place(x=5000)
    photolisk.place(x=5000)
    BackTelaModerado.place(x=5000)
    # Inserindo Widgets da tela moderado
    Xrp.place(x=130, y=110)
    Lisk.place(x=130, y=140)
    Litecoin.place(x=130, y=170)
    BackTelainvestidor.place(x=125)


BackTelaModerado = ttk.Button(RightFrame, text="Voltar Tela Moderado", width=20, command=BackTelaModerado)

BackTelaModerado.place(x=125, y=260)


def TelaModerado():
    # Removendo widgets de telainvestidor
    Conservador.place(x=5000)
    Moderado.place(x=5000)
    Agressivo.place(x=5000)
    BackLogin.place(x=5000)
    LoginButton.place(x=5000)
    # Inserindo Widgets da tela agressivo
    Xrp.place(x=130, y=110)
    Lisk.place(x=130, y=140)
    Litecoin.place(x=130, y=170)
    BackTelainvestidor.place(x=125)


Xrp = ttk.Button(RightFrame, text="Xrp", width=20, command=TelaXrp)
Lisk = ttk.Button(RightFrame, text="Lisk", width=20, command=TelaLisk)
Litecoin = ttk.Button(RightFrame, text="Litecoin", width=20, command=TelaLitecoin)


# tela agressivo-----------------------------------------------------------

def TelaEthereum():
    # removendo widgets da tela
    Ether.place(x=5000)
    Dash.place(x=5000)
    Bitcoin.place(x=5000)
    BackTelainvestidor.place(x=5000)
    # adicionando widget tela dogecoin
    BackTelaAgressivo.place(x=125, y=260)
    photoEthereum.place(x=50, y=25)


photoEthereum = Label(RightFrame, image=photo7, bg="black")


def TelaDash():
    # removendo widgets da tela tether
    Ether.place(x=5000)
    Dash.place(x=5000)
    Bitcoin.place(x=5000)
    BackTelainvestidor.place(x=5000)
    # adicionando widget tela dogecoin
    photoDash.place(x=50, y=25)
    BackTelaAgressivo.place(x=125, y=260)


photoDash = Label(RightFrame, image=photo8, bg="black")


def TelaBitecoin():
    # removendo widgets da tela stellar
    Ether.place(x=5000)
    Dash.place(x=5000)
    Bitcoin.place(x=5000)
    BackTelainvestidor.place(x=5000)

    # adicionando widget tela dogecoin
    photoBitecoin.place(x=50, y=25)
    BackTelaAgressivo.place(x=125, y=260)


photoBitecoin = Label(RightFrame, image=photo9, bg="black")


def BackTelaAgressivo():
    # Removendo Widgets de tela moedas moderadas
    photoEthereum.place(x=5000)
    photoBitecoin.place(x=5000)
    photoDash.place(x=5000)
    BackTelaAgressivo.place(x=5000)
    # Inserindo Widgets da tela moderado
    Ether.place(x=130, y=110)
    Dash.place(x=130, y=140)
    Bitcoin.place(x=130, y=170)
    BackTelainvestidor.place(x=125)


BackTelaAgressivo = ttk.Button(RightFrame, text="Voltar Tela Agressivo", width=20, command=BackTelaAgressivo)

BackTelaAgressivo.place(x=125, y=260)


def TelaAgressivo():
    # Removendo widgets de telainvestidor
    Conservador.place(x=5000)
    Moderado.place(x=5000)
    Agressivo.place(x=5000)
    BackLogin.place(x=5000)
    LoginButton.place(x=5000)
    # Inserindo Widgets da tela agressivo
    Ether.place(x=130, y=110)
    Dash.place(x=130, y=140)
    Bitcoin.place(x=130, y=170)
    BackTelainvestidor.place(x=125)


Ether = ttk.Button(RightFrame, text="Ethereum", width=20, command=TelaEthereum)
Dash = ttk.Button(RightFrame, text="Dash", width=20, command=TelaDash)
Bitcoin = ttk.Button(RightFrame, text="Bitecoin", width=20, command=TelaBitecoin)


def TelaInvestidor():
    # Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    WelcomeLabel.place(x=5000)
    UserLabel.place(x=5000)
    PassLabel.place(x=5000)
    UserEntry.place(x=5000)
    PassEntry.place(x=5000)
    EsqueceuSenhaLabel.place(x=5000)
    EsqueceuSenhaButton.place(x=5000)
    # Inserindo Widgets da tela 1
    Conservador.place(x=130, y=110)
    Moderado.place(x=130, y=140)
    Agressivo.place(x=130, y=170)
    BackLogin.place(x=125)


Conservador = ttk.Button(RightFrame, text="Conservador", width=20, command=TelaConservador)
Agressivo = ttk.Button(RightFrame, text="Agressivo", width=20, command=TelaAgressivo)
Moderado = ttk.Button(RightFrame, text="Moderado", width=20, command=TelaModerado)


def BackTelainvestidor():
    # Removendo Widgets de Login
    Dogecoin.place(x=5000)
    Tether.place(x=5000)
    Stellar.place(x=5000)
    Xrp.place(x=5000)
    Lisk.place(x=5000)
    Litecoin.place(x=5000)
    Ether.place(x=5000)
    Dash.place(x=5000)
    Bitcoin.place(x=5000)
    BackTelainvestidor.place(x=5000)
    # Inserindo Widgets da tela 1
    Conservador.place(x=130, y=110)
    Moderado.place(x=130, y=140)
    Agressivo.place(x=130, y=170)
    BackLogin.place(x=125, y=260)


BackTelainvestidor = ttk.Button(RightFrame, text="Voltar investidor", width=20, command=BackTelainvestidor)
BackTelainvestidor.place(x=125, y=260)























# --------------------tipos de investidor------------------------------------------------------


def Register():
    # Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    WelcomeLabel.place(x=5000)
    # Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Nome:", font=("Baskerville Old Face", 20), bg="white", fg="black")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Baskerville Old Face", 20), bg="white", fg="black")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Erro ao registrar",
                                 message="Preencha Todos os Campos")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Informacoes", message="Conta Criada Com Sucesso")

    Register = ttk.Button(RightFrame, text="Registrar", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        # Removendo Widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        Conservador.place(x=5000)
        Conservador.place(x=5000)
        Conservador.place(x=5000)
        # Trazendo de volta os Widgets de Login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)
        WelcomeLabel.place(x=100)

    Back = ttk.Button(RightFrame, text="Voltar", width=20, command=BackToLogin)
    Back.place(x=125, y=260)


RegisterButton = ttk.Button(RightFrame, text="Registrar", width=20, command=Register)
RegisterButton.place(x=125, y=260)

EsqueceuSenhaLabel = Label(RightFrame, text="Esqueceu a senha?", bg="red", fg="white", bd=0,
                           font=("Baskerville Old Face", 12))
EsqueceuSenhaLabel.place(x=50, y=305)


def RecuperaSenha():
    # Removendo os widgets de senha
    PassLabel.place(x=5000)
    PassEntry.place(x=5000)
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    EsqueceuSenhaLabel.place(x=5000)
    EsqueceuSenhaButton.place(x=5000)
    WelcomeLabel.place(x=5000)

    # Adicionando o widget de email
    EmailRecuperationLabel.place(x=5)
    EmailRecuperationButton.place(x=150)
    RecuperaSenhaTitulo.place(x=5)
    RecuperaSenhaButton.place(x=100)
    BackLogin.place(x=125)


EsqueceuSenhaButton = Button(RightFrame, text="Recupere Aqui!", bg="white", fg="black", bd=0,
                             font=("Baskerville Old Face", 12), command=RecuperaSenha)
EsqueceuSenhaButton.place(x=210, y=302)

EmailRecuperationLabel = Label(RightFrame, text="Email:", font=("Baskerville Old Face", 20), bg="white", fg="black")
EmailRecuperationLabel.place(x=5000, y=150)

EmailRecuperationButton = ttk.Entry(RightFrame, width=30)
EmailRecuperationButton.place(x=5000, y=160)

RecuperaSenhaTitulo = Label(RightFrame, text="Recuperar Senha \n Preencha os campos abaixo!",
                            font=("Baskerville Old Face", 18), bg="white", fg="black")
RecuperaSenhaTitulo.place(x=5000, y=5)


def GetSenha():
    NewUser = UserEntry.get()
    NewEmail = EmailRecuperationButton.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users 
    WHERE (User = ? and Email = ?)
    """, (NewUser, NewEmail))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    DataBaser.cursor.execute("""
    SELECT Password FROM Users
    WHERE User = ? and Email = ?
    """, (NewUser, NewEmail))
    MostraSenha = DataBaser.cursor.fetchone()
    if (NewUser in VerifyLogin and NewEmail in VerifyLogin):
        messagebox.showinfo(title="Aviso", message=("Senha:", MostraSenha))
    else:
        messagebox.showinfo(title="Aviso", message="Dados Invalidos")


RecuperaSenhaButton = ttk.Button(RightFrame, text="Recuperar Senha", width=30, command=GetSenha)
RecuperaSenhaButton.place(x=5000, y=225)  # x=100


def BackToLogin2():
    # Removendo Widgets de Cadastro
    EmailRecuperationLabel.place(x=5000)
    EmailRecuperationButton.place(x=5000)
    BackLogin.place(x=5000)
    RecuperaSenhaButton.place(x=5000)
    RecuperaSenhaTitulo.place(x=5000)
    # Trazendo de volta os Widgets de Login
    LoginButton.place(x=100)
    RegisterButton.place(x=125)
    PassLabel.place(x=5)
    PassEntry.place(x=150)
    EsqueceuSenhaLabel.place(x=50)
    EsqueceuSenhaButton.place(x=210)
    WelcomeLabel.place(x=100)


BackLogin = ttk.Button(RightFrame, text="Voltar", width=20, command=BackToLogin2)
BackLogin.place(x=5000, y=260)  # x=125

janela.mainloop()
