"""user = input("Digite user: ")
senha = input("Digite senha: ")
funçao = input("Digite funçao: ")

arq = open('ArqReuniões', 'r')
conteudo = arq.readlines()
argumento = str(f"{user} {senha} {funçao} \n")
conteudo.append(argumento)
arq = open('arquivoDeLogin.txt', 'w')
arq.writelines(conteudo) #Aqui ele escreve as str de condeudo dentro de uma linha
arq.close()  #infortante fechar o arquivo, se nao ele apaga e se perde

#---------- varrer as infos dentro do arquivo ---------------------

arq = open('arquivoDeLogin', 'r')
for linha in arq:
    valor = linha.split()
    print(valor[0])
arq.close()

reunioespublicas = {}
reunioespublicas["antony"] = "teu cu"
reunioespublicas["antony2"] = "teu cu2"
reunioespublicas["antony3"] = "teu cu3"
for i in reunioespublicas.keys():
    if i=="Antony":
         valorchave = reunioespublicas.get(i)
         chave = i
         print(chave, valorchave)"""


'''arq = open('arquivoDeLogin.txt', 'r')
for linha in arq:
    valor = linha.split()
    print(valor[0])
arq.close()'''


participantes = []
listadeespera = []
for i in range(participantesquanti):
    listadeespera.append(input("digite o username do usuario participante: "))



naoconfirmouPr[nome] = listadeespera














