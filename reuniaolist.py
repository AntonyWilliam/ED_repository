reunioespublicas = {}
reunioesprivadas = {}
from datetime import date
import outromenu
import calendar
import pygame
from time import localtime
data_atual = date.today()
from datetime import datetime
import datetime
import coordenadormenu

def addreuniaoPr(nome, datar, hora, local):
    reunioesprivadas[nome] = "{}".format(datar), "{}".format(hora), "{}".format(local)

def addreuniaoPu(nome, datar, hora, local):
    reunioespublicas[nome] = "{}".format(datar), "{}".format(hora), "{}".format(local)

def criarreuniaoPrC():
    from pygame import mixer
    nome = str(input("Defina o nome da reunião: "))
    local = int(input("Defina a sala da reunião: "))
    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião: "))
    M = int(input("Coloque o minuto da reunião: "))
    hfinal = str(input("Defina o horario em que sua reuniao encerra: "))
    ata = str(input("Defina o horario em que sua reuniao encerra: "))
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
    local = int(input("Defina a sala da reunião: "))
    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião "))
    M = int(input("Coloque o minuto da reunião"))
    hfinal = str(input("Defina o horario em que sua reuniao encerra: "))
    ata = str(input("Defina o horario em que sua reuniao encerra: "))
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
    local = int(input("Defina a sala da reunião: "))
    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião: "))
    M = int(input("Coloque o minuto da reunião: "))
    hfinal = str(input("Defina o horario em que sua reuniao encerra: "))
    ata = str(input("Defina o horario em que sua reuniao encerra: "))
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
    local = int(input("Defina a sala da reunião: "))
    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião: "))
    M = int(input("Coloque o minuto da reunião: "))
    hfinal = str(input("Defina o horario em que sua reuniao encerra: "))
    ata = str(input("Defina o horario em que sua reuniao encerra: "))
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
    while True:
        if localtime().tm_hour == int(H) and localtime().tm_min == int(M) and datah == datarsimple:
            for i in range(1):
                print("ESTA NA HORA DA RUNIÃO: ", nome)
                mixer.init()
                mixer.music.load("alarm.mp3")
                mixer.music.play()
                outromenu.ousuariomenu()