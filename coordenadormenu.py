import reuniao
def omenuC():
    opcao = str(input("Escolha uma opção - 1(criar reuniao) 2(confirmar ou negar presença) 3(vizualizar ata de reuniao)"
                      "/n 4(editar ata de reuniao) 5(baixar ata de reuniao) 6(adicionar participantes as reuniões)/n "
                      "/n 7(realocar reuniões)"))
    if opcao == "1":
        print("CRIAR REUNIAO")
        reuniao.tiporeuniao()
        tipo = reuniao.tiporeuniao()

        if tipo == "1":
            reuniao.reunioespublicas.append(reuniao.criarreuniao())
        elif tipo == "2":
            reuniao.reunioesprivadas.append(reuniao.criarreuniao())

    elif opcao == "2":
        print("CONFIRMAR PRESENÇA")
    elif opcao == "3":
        print("VIZUALIZAR ATA")
    elif opcao == "4":
        print("EDITAR ATA")
    elif opcao == "5":
        print("BAIXAR ATA")
    elif opcao == "6":
        print("ADICIONAR PARTICIPANTE")
    elif opcao == "7":
        print("REALOCAR REUNIÕES")
