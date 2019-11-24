import reuniaolist
import usuarioativo
def ousuariomenu():

     opcao = str(input("Escolha uma opção:\n"
                       "1(criar reuniao)\n"
                       "2(confirmar ou negar presença)\n"
                       "3(vizualizar ata de reuniao)\n"
                       "4(baixar ata de reuniao)\n"
                       "5(Adicionar participantes)\n"
                      "6( Editar atas de reuniões do qual é o proprietário)\n"
                      "7 (Sugerir local da reunião)"))
     if opcao == "1":
         print("CRIAR REUNIAO")
         tipo = str(input("Coloque o tipo de reunião publica(1) privada(2)"))
         if tipo == "1":
             reuniaolist.criarreuniaoPrO()
         elif tipo == "2":
             reuniaolist.criarreuniaoPrO()
     elif opcao == "2":
        print("CONFIRMAR PRESENÇA")
     elif opcao == "3":
        reuniaolist.visualizaratasOutro()
     elif opcao == "4":
        reuniaolist.salvaratareuniaoOutro()
     elif opcao == "5":
        print("ADICIONAR PARTICIPANTES")
     elif opcao == "6":
         reuniaolist.editaratasOutro()
     elif opcao == "7":
        print("SUGERIR LOCAL DE REUNIÃO")

