# import omenu
# import usuarionovo
# import outromenu
import sys
reunioespublicas = []
reunioesprivadas = []
sistema = True
usuarios = []
'''global status (dando erro)'''
status = "nulo"


def menu1():

    status = str(input("Você é um usuario cadastrado? Digite s(sim) ou n(não)! Digite x para sair!"))
    if status == "s":
        usuarioativo()
    elif status == "n":
        usuarios.append(usuarionovo())

    elif status == "x":
        sys.exit()

def usuarionovo():

    username = str(input("Crie seu nome de usuário: "))
    while username in usuarios:
        print("Username ja existe! Tente Novamente!")
        username = str(input("Crie seu nome de usuário: "))

    funcao = str(input("Qual a sua função? c (Coordenador), g (gestor) ou o(outra): "))
    while funcao != "c" and funcao !="g" and funcao !="o":
        print("Comando INVÁLIDO! Tente Novamente!")
        funcao = str(input("Qual a sua função? c (Coordenador), g (gestor) ou o(outra): "))

    senha = str(input("Crie sua senha: "))
    confirmasenha = str(input("Confirme sua senha: "))
    while senha != confirmasenha:
        print("Campos não correspondem! Tente Novamente!")
        senha = str(input("Crie sua senha: "))
        confirmasenha = str(input("Confirme sua senha: "))

    usuarios.append(username)
    usuarios.append(senha)
    usuarios.append(funcao)

def usuarioativo():


    username = str(input("Digite seu Username: "))
    senha = str(input("Digite sua senha: "))

    if username in usuarios:
        uindex = usuarios.index(username)
        sindex = uindex + 1
        findex = sindex + 1
        # essa estrutura é temporaria ate eu conseguir concertar os imports
        if usuarios[sindex] == senha:

            if usuarios[findex] == "c":
                import coordenadormenu
                print("Funçao de coordenador")
                coordenadormenu.omenuC()

            elif usuarios[findex] == "g":
                import gestormenu
                print("Funçao de gestor")
                gestormenu.Gestormenu()
            else:
                import outromenu
                print("Funçao de usuario comum")
                outromenu.ousuariomenu()
        else:
            print("Senha INCORRETA!")

    else:
        print("Usuario não existe")


while status != "x":
    menu1()