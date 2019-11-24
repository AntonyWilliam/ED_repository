reunioespublicas = {}
reunioesprivadas = {}
atareunioespublicas = {}
atareunioesprivadas = {}
proprietarioreuniao = {}
listdedicionarios = [reunioespublicas, reunioesprivadas, atareunioespublicas, atareunioesprivadas, proprietarioreuniao]
from datetime import date
import outromenu
from time import localtime
data_atual = date.today()
from datetime import datetime
import datetime
import coordenadormenu
import usuarioativo
import calendar
import pygame
usuario = usuarioativo.pegarusuario()

def addreuniaoPr(nome, datar, hora, local):
    reunioesprivadas[nome] = "{}".format(datar), "{}".format(hora), "{}".format(local)
def addreuniaoPu(nome, datar, hora, local):
    reunioespublicas[nome] = "{}".format(datar), "{}".format(hora), "{}".format(local)
def addatareuniaoPr(nome, ata):
    atareunioesprivadas[nome] = [ata]
def addatareuniaoPu(nome, ata):
    atareunioespublicas[nome] = [ata]
def addpropriatarioareuniao(nome, usuario):
    proprietarioreuniao[nome] = [usuario]

def criarreuniaoPrC():
    from pygame import mixer
    nome = str(input("Defina o nome da reunião: "))
    ata = str(input("Defina o assunto aboradado na reunião: "))
    local = int(input("Defina a sala da reunião: "))
    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião: "))
    M = int(input("Coloque o minuto da reunião: "))
    hora = ("{}:{}".format(H, M))
    print("Reunião:{}.\nLocal:{}.\nData:{}.\nHora--{}:{}\n".format(nome, local, datar, H, M))
    verificacao = "{}".format(datar), "{}".format(hora), "{}".format(local)
    for valor in reunioesprivadas.values():
        if verificacao == valor:
            print("Ja existe uma reunião marcada para esta sala, neste dia e neste horario!!")
            criarreuniaoPrC()
        else:
            print("REUNIÃO CRIADA")
    correcao = str(input("Deseja mudar os dados sim(s) não(n)"))
    if correcao == "s":
        criarreuniaoPrC()
    else:
        addreuniaoPr(nome, datar, hora, local)
        print(reunioesprivadas)
        addatareuniaoPr(nome, ata)
    coordenadormenu.omenuC()
    while True:
        if localtime().tm_hour == int(H) and localtime().tm_min == int(M) and datah == datarsimple:
            for i in range(1):
                print("ESTA NA HORA DA RUNIÃO: ", nome)
                mixer.init()
                mixer.music.load("alarm.mp3")
                mixer.music.play()
                coordenadormenu.omenuC()
def criarreuniaoPuC():
    from pygame import mixer
    nome = str(input("Defina o nome da reunião: "))
    ata = str(input("Defina o assunto aboradado na reunião: "))
    local = int(input("Defina a sala da reunião: "))
    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião "))
    M = int(input("Coloque o minuto da reunião"))
    hora = ("{}:{}".format(H, M))
    print("Reunião:{}.\nLocal:{}.\nData:{}.\nHora--{}:{}\n".format(nome, local, datar, H, M))
    verificacao = "{}".format(datar), "{}".format(hora), "{}".format(local)
    for valor in reunioespublicas.values():
        if verificacao == valor:
            print("Ja existe uma reunião marcada para esta sala, neste dia e neste horario!!")
            criarreuniaoPuC()
        else:
            print("REUNIÃO CRIADA")
    correcao = str(input("Deseja mudar os dados sim(s) não(n): "))
    if correcao == "s":
        criarreuniaoPuC()
    else:
        addreuniaoPu(nome, datar, hora, local)
        print(reunioespublicas)
        addatareuniaoPu(nome, ata)
    coordenadormenu.omenuC()
    while True:
        if localtime().tm_hour == int(H) and localtime().tm_min == int(M) and datah == datarsimple:
            for i in range(1):
                print("ESTA NA HORA DA RUNIÃO: ", nome)
                mixer.init()
                mixer.music.load("alarm.mp3")
                mixer.music.play()
                coordenadormenu.omenuC()
def criarreuniaoPrO():
    from pygame import mixer
    nome = str(input("Defina o nome da reunião: "))
    ata = str(input("Defina o assunto aboradado na reunião: "))
    local = int(input("Defina a sala da reunião: "))
    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião: "))
    M = int(input("Coloque o minuto da reunião: "))
    hora = ("{}:{}".format(H, M))
    print("Reunião:{}.\nLocal:{}.\nData:{}.\nHora--{}:{}\n".format(nome, local, datar, H, M))
    verificacao = "{}".format(datar), "{}".format(hora), "{}".format(local)
    for valor in reunioesprivadas.values():
        if verificacao == valor:
            print("Ja existe uma reunião marcada para esta sala, neste dia e neste horario!!")
            criarreuniaoPrO()
        else:
            print("REUNIÃO CRIADA")
    correcao = str(input("Deseja mudar os dados sim(s) não(n)"))
    if correcao == "s":
        criarreuniaoPrO()
    else:
        reunioesprivadas[nome] = "{}".format(datar), "{}".format(hora), "{}".format(local)
        print(reunioesprivadas)
        addatareuniaoPr(nome, ata)
    outromenu.ousuariomenu()
    while True:
        if localtime().tm_hour == int(H) and localtime().tm_min == int(M) and datah == datarsimple:
            for i in range(1):
                print("ESTA NA HORA DA RUNIÃO: ", nome)
                mixer.init()
                mixer.music.load("alarm.mp3")
                mixer.music.play()
                outromenu.ousuariomenu()
def criarreuniaoPuO():
    from pygame import mixer
    nome = str(input("Defina o nome da reunião: "))
    ata = str(input("Defina o assunto aboradado na reunião: "))
    local = int(input("Defina a sala da reunião: "))
    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião: "))
    M = int(input("Coloque o minuto da reunião: "))
    hora = ("{}:{}".format(H, M))
    print("Reunião:{}.\nLocal:{}.\nData:{}.\nHora--{}:{}\n".format(nome, local, datar, H, M))
    verificacao = "{}".format(datar), "{}".format(hora), "{}".format(local)
    for valor in reunioespublicas.values():
        if verificacao == valor:
            print("Ja existe uma reunião marcada para esta sala, neste dia e neste horario!!")
            criarreuniaoPuO()
        else:
            print("REUNIÃO CRIADA")
    correcao = str(input("Deseja mudar os dados sim(s) não(n): "))
    if correcao == "s":
        criarreuniaoPuO()
    else:
        reunioespublicas[nome] = "{}".format(datar), "{}".format(hora), "{}".format(local)
        print(reunioespublicas[nome])
        addatareuniaoPu(nome, ata)
    while True:
        if localtime().tm_hour == int(H) and localtime().tm_min == int(M) and datah == datarsimple:
            for i in range(1):
                print("ESTA NA HORA DA RUNIÃO: ", nome)
                mixer.init()
                mixer.music.load("alarm.mp3")
                mixer.music.play()
                outromenu.ousuariomenu()

def visualizaratasOutro():
    tipo = str(input("A reunião que deseja visualizar e publica(1) ou privada(2)?"))
    if tipo == "1":
        nome = str(input("Qual o nome da reunião?"))
        for chave in reunioespublicas.keys():
            if chave == nome:
                ata = reunioespublicas.get(chave)
                print("A reunião", chave," tem como ata: ",ata)
            else:
                print("Essa reunião publica não existe")
                outromenu.ousuariomenu()
    elif tipo == "2":
        nome = str(input("Qual o nome da reunião?"))
        for chave in reunioesprivadas.keys():
            if chave == nome:
                ata = reunioesprivadas.get(chave)
                print("A reunião", chave, " tem como ata: ", ata)
            else:
                print("A reunião não existe!!")
                outromenu.ousuariomenu()
def visualizaratasCordenador():
    tipo = str(input("A reunião que deseja visualizar e publica(1) ou privada(2)?"))
    if tipo == "1":
        nome = str(input("Qual o nome da reunião?"))
        for chave in reunioespublicas.keys():
            if chave == nome:
                ata = reunioespublicas.get(chave)
                print("A reunião", chave, " tem como ata: ", ata)
            else:
                print("Essa reunião publica não existe")
                coordenadormenu.omenuC()
    elif tipo == "2":
        nome = str(input("Qual o nome da reunião?"))
        for chave in reunioesprivadas.keys():
            if chave == nome:
                ata = reunioesprivadas.get(chave)
                print("A reunião", chave, " tem como ata: ", ata)
            else:
                print("A reunião não existe!!")
                coordenadormenu.omenuC()

def editaratasOutro():
    tipo = str(input("Voce deseja editar a ata de uma reunião publica(1) ou privada(2)?"))
    if tipo == "2":
        nome = str(input("Voce deseja editar a ata de qual reunião?"))
        if nome in proprietarioreuniao.values():
            proprietario = proprietarioreuniao.get(nome)
            if proprietario == usuario:
                ata = str(input("Coloque a nova ata!!"))
                atareunioesprivadas[nome] = "{}".format(ata)
            else:
                print("Voce não e proprietario dessa reunião!!")
                outromenu.ousuariomenu()
        else:
            print("Essa reunião não existe!!")
            outromenu.ousuariomenu()
    elif tipo == "1":
        nome = str(input("Voce deseja editar a ata de qual reunião?"))
        if nome in proprietarioreuniao.values():
            proprietario = proprietarioreuniao.get(nome)
            if proprietario == usuario:
                ata = str(input("Coloque a nova ata!!"))
                atareunioespublicas[nome] = "{}".format(ata)
            else:
                print("Voce não e proprietario dessa reunião!!")
                outromenu.ousuariomenu()
        else:
            print("Essa reunião não existe!!")
            outromenu.ousuariomenu()
def editaratasCordenador():
    tipo = str(input("Voce deseja editar a ata de uma reunião publica(1) ou privada(2)?"))
    if tipo == "2":
        nome = str(input("Voce deseja editar a ata de qual reunião?"))
        if nome in reunioesprivadas:
          ata = str(input("Coloque a nova ata!!"))
          atareunioesprivadas[nome] = "{}".format(ata)
        else:
            print("Essa reunião não existe!!")
            coordenadormenu.omenuC()
    elif tipo == "1":
        nome = str(input("Voce deseja editar a ata de qual reunião?"))
        if nome in reunioespublicas:
            ata = str(input("Coloque a nova ata!!"))
            atareunioesprivadas[nome] = "{}".format(ata)
        else:
            print("Essa reunião não existe!!")
            coordenadormenu.omenuC()

def salvaratareuniaoOutro():
     tipo = str(input("Voce deseja salvar a ata de uma reunião publica(1) ou privada(2)?"))
     if tipo == "1":
        nome = str(input("Escreva o nome da reunião que deseja baixar a ata: "))
        if nome in atareunioesprivadas:
          nomedearquivo = str(input("Defina o nome do arquivo onde quer salvar a ata: "))
          ata = reunioesprivadas.get(nome)
          nomeeata = "Reunião: ",nome,"ATA:",ata
          ataparabaixar = nomeeata
          arqata = open(nomedearquivo + '.txt', 'w')
          arqata.writelines(ataparabaixar)
          arqata.close()
        else:
            print("Reunião não existe")
            outromenu.ousuariomenu()
     elif tipo == "2":
         nome = str(input("Escreva o nome da reunião que deseja baixar a ata: "))
         if nome in atareunioesprivadas:
             nomedearquivo = str(input("Defina o nome do arquivo onde quer salvar a ata: "))
             ata = reunioespublicas.get(nome)
             nomeeata = "Reunião: ", nome, "ATA:", ata
             ataparabaixar = nomeeata
             arqata = open(nomedearquivo + '.txt', 'w')
             arqata.writelines(ataparabaixar)
             arqata.close()
         else:
             print("Reunião não existe")
             outromenu.ousuariomenu()
def salvaratareuniaoCordenador():
    tipo = str(input("Voce deseja salvar a ata de uma reunião publica(1) ou privada(2)?"))
    if tipo == "1":
        nome = str(input("Escreva o nome da reunião que deseja baixar a ata: "))
        if nome in atareunioesprivadas:
            nomedearquivo = str(input("Defina o nome do arquivo onde quer salvar a ata: "))
            ata = reunioesprivadas.get(nome)
            nomeeata = "Reunião: ", nome, "ATA:", ata
            ataparabaixar = nomeeata
            arqata = open(nomedearquivo + '.txt', 'w')
            arqata.writelines(ataparabaixar)
            arqata.close()
        else:
            print("Reunião não existe")
            coordenadormenu.omenuC()
    elif tipo == "2":
        nome = str(input("Escreva o nome da reunião que deseja baixar a ata: "))
        if nome in atareunioesprivadas:
            nomedearquivo = str(input("Defina o nome do arquivo onde quer salvar a ata: "))
            ata = reunioespublicas.get(nome)
            nomeeata = "Reunião: ", nome, "ATA:", ata
            ataparabaixar = nomeeata
            arqata = open(nomedearquivo + '.txt', 'w')
            arqata.writelines(ataparabaixar)
            arqata.close()
        else:
            print("Reunião não existe")
            coordenadormenu.omenuC()



