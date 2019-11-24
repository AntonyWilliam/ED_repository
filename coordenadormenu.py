import reuniaolist
def omenuC():
    opcao = str(input("Escolha uma opção - 1(criar reuniao) 2(confirmar ou negar presença) 3(vizualizar ata de reuniao)"
                      "/n 4(editar ata de reuniao) 5(baixar ata de reuniao) 6(adicionar participantes as reuniões)/n "
                      "/n 7(realocar reuniões)"))
    if opcao == "1":
        print("CRIAR REUNIAO")
        tipo = str(input("Coloque o tipo de reunião publica(1) privada(2)"))
        if tipo == "1":
            reuniaolist.criarreuniaoPuC()
        elif tipo == "2":
            reuniaolist.criarreuniaoPrC()
    elif opcao == "2":
        print("CONFIRMAR PRESENÇA")
    elif opcao == "3":
        reuniaolist.visualizaratasCordenador()
    elif opcao == "4":
        reuniaolist.editaratasCordenador()
    elif opcao == "5":
        reuniaolist.salvaratareuniaoCordenador()
    elif opcao == "6":
        print("ADICIONAR PARTICIPANTE")
    elif opcao == "7":
        print("REALOCAR REUNIÕES")