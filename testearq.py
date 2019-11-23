
def login():

    '''user = input("Digite user: ")
    senha = input("Digite senha: ")
    funçao = input("Digite funçao: ")

    arq = open('arquivoDeLogin.txt', 'r')
    conteudo = arq.readlines()

    argumento = str(f"{user} {senha} {funçao}")

    conteudo.append(argumento)

    arq = open('arquivoDeLogin.txt', 'w')
    arq.writelines(conteudo)
    arq.close()'''

    arq = open('arquivoDeLogin.txt', 'r')
    for linha in arq:
        valor = linha.split()
        print(valor[2])
    arq.close()


login()