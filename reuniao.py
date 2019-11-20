reunioespublicas = []
reunioesprivadas = []

def criarreuniao():
    assunto = str(input("Defina o assunto da sua reuniao: "))
    data = str(input("Defina a data da sua reuniao: "))
    local = str(input("Defina o local da sua reuniao: "))
    hinicial = str(input("Defina o horario de inicio da sua reuniao: "))
    hfinal = str(input("Defina o horario em que sua reuniao encerra: "))
    ata = str(input("Defina o horario em que sua reuniao encerra: "))


def tiporeuniao():
    visibilidade = int(input("Sua reuniao é 1(publica) ou 2(privada)? "))
    return visibilidade