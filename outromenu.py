import reuniao
def ousuariomenu():

     opcao = str(input("Escolha uma opção - 1(criar reuniao) 2(confirmar ou negar presença) 3(vizualizar ata de reuniao)"
                      "/n 4(editar ata de reuniao) 5(baixar ata de reuniao) 6 (Adicionar participantes) 7( Redigir atas de reuniões do qual é o proprietário)"
                      "/n 8( Editar atas de reuniões do qual é o proprietário) "
                      "/n 9 (Sugerir local da reunião)"))
     if opcao == "1":
        reuniao.tiporeuniao()
        tipo = reuniao.tiporeuniao()
        if tipo == "1":
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
        print("ADICIONAR PARTICIPANTES")
     elif opcao == "7":
        print("REDIGIR ATAS DE REUNIÕES DO QUAL E PROPRIETARIO")
     elif opcao == "8":
        print("EDITAR ATAS DE REUNIÃO DE QUAL SE E PROPRIETARIO")
     elif opcao == "9":
        print("SUGERIR LOCAL DE REUNIÃO")
ousuariomenu()

def criarreuniao():
        visibilidade = str(input("Sua reuniao é 1(publica) ou 2(privada)? "))

        assunto = str(input("Defina o assunto da sua reuniao: "))
        data = str(input("Defina a data da sua reuniao: "))
        local = str(input("Defina o local da sua reuniao: "))
        hinicial = str(input("Defina o horario de inicio da sua reuniao: "))
        hfinal = str(input("Defina o horario em que sua reuniao encerra: "))
        ata = str(input("Defina o horario em que sua reuniao encerra: "))
