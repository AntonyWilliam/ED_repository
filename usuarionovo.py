#tentei importar para a main mas ainda nao consegui
def usuarionovo():

    usuario = []
    username = str(input("Crie seu nome de usuário: "))
    while username in usuario:
        print("Username ja existe! Tente Novamente!")
        username = str(input("Crie seu nome de usuário: "))

    funcao = str(input("Qual a sua função? c (Coordenador), g (gestor) ou o(outra): "))
    while funcao != "c" and funcao != "g" and funcao != "o":
        print("Comando INVÁLIDO! Tente Novamente!")
        funcao = str(input("Qual a sua função? c (Coordenador), g (gestor) ou o(outra): "))

    senha = str(input("Crie sua senha: "))
    confirmasenha = str(input("Confirme sua senha: "))
    while senha != confirmasenha:
        print("Campos não correspondem! Tente Novamente!")
        senha = str(input("Crie sua senha: "))
        confirmasenha = str(input("Confirme sua senha: "))

    usuario.append(username)
    usuario.append(senha)
    usuario.append(funcao)


    return usuario


usuarionovo()


def main():

    print("Desespero")

main()
