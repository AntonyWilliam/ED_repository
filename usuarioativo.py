import coordenadormenu
import gestormenu
import outromenu


def pegarusuario():
     return username

def usuarioativo():
    global username
    username = str(input("Digite seu Username: "))

    senha = str(input("Digite sua senha: "))
    arq = open('arquivoDeLogin.txt', 'r')
    for linha in arq:
        valor = linha.split()
        if valor[0] == username and valor[1] == senha and valor[2] == "c":
            coordenadormenu.omenuC()
        elif valor[0] == username and valor[1] == senha and valor[2] == "g":
            gestormenu.Gestormenu()
        elif valor[0] == username and valor[1] == senha and valor[2] == "o":
            outromenu.ousuariomenu()
        else:
            print("Usuario e senha nao correspondem! ")

    arq.close()
    return username, senha


