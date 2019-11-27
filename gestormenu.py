import main
import reuniaolist


def Gestormenu():
    opcao = str(input("Escolha uma opção - 1(Cadastrar nova sala de reunião)"))
    if opcao == "1":
        print("Cadastrar nova sala de reunião")
        reuniaolist.gestoraddnovasala()
    else:
        main.menu1()



