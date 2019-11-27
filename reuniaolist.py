reunioespublicas = {}
reunioesprivadas = {}
atareunioespublicas = {}
atareunioesprivadas = {}
proprietarioreuniao = {}
naoconfirmouPr = {}
naoconfirmouPu = {}
listdedicionarios = [reunioespublicas, reunioesprivadas, atareunioespublicas, atareunioesprivadas, proprietarioreuniao]
listadesalas = ["Sala01", "Sala02", "Sala03"]
from datetime import date
import outromenu
from time import localtime
data_atual = date.today()
from datetime import datetime
import datetime
import coordenadormenu
import usuarioativo
import gestormenu
import calendar
import pygame
usuario = usuarioativo.pegarusuario()


def addreuniaoPr(nome, datar, hora, local, horario, participantes):
    reunioesprivadas[nome] = [datar, hora, local, horario, participantes]
def addreuniaoPu(nome, datar, hora, local, horario, participantes):
    reunioespublicas[nome] = [datar, hora, local, horario, participantes]
def addatareuniaoPr(nome, ata):
    atareunioesprivadas[nome] = [ata]
def addatareuniaoPu(nome, ata):
    atareunioespublicas[nome] = [ata]
def addpropriatarioareuniao(nome, usuario):
    proprietarioreuniao[nome] = [usuario]

def criarreuniaoPrC():
    from pygame import mixer
    nome = str(input("Defina o nome da reunião: "))
    while nome in reunioesprivadas.keys():
        print("Esse nome ja existe tente outro")
        nome = str(input("Defina o nome da reunião: "))

    ata = str(input("Defina a ata da sua reunião: "))

    print("---- SALAS DE REUNIAO ----")
    for i in range(len(listadesalas)):
        print(listadesalas[i])
    print("---- ESCOLHA UMA SALA ----")
    local = str(input("Defina a sala da reunião: "))

    print("--- USUARIOS DO SISTEMA ---")
    arq = open('arquivoDeLogin.txt', 'r')
    for linha in arq:
        valor = linha.split()
        print(valor[0])
    arq.close()
    print("--- ------------------- ---")
    participantesquanti = int(input("Quantos participantes na sua reuniao: "))
    participantes = []
    listadeespera = []
    for i in range(participantesquanti):
        listadeespera.append(input("digite o username do usuario participante: "))

    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    horario = str(input("Defina horario para a reuniao 1(7-8) 2(8-9) 3(9-10) 4(10-11): "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião: "))
    M = int(input("Coloque o minuto da reunião: "))
    hora = ("{}:{}".format(H, M))
    print("Reunião:{}.\nLocal:{}.\nData:{}.\nHora--{}:{}\n".format(nome, local, datar, H, M))


    for valor in reunioesprivadas.values():
        if valor[0] == datar and valor[1] == hora and valor[2] == local and valor[3] == horario:
            print("Ja existe uma reunião marcada para esta sala, neste dia e neste horario!!")
            criarreuniaoPrC()
        else:
            print("REUNIÃO CRIADA")

    correcao = str(input("Deseja mudar os dados sim(s) não(n)"))
    if correcao == "s":
        criarreuniaoPrC()
    else:
        addreuniaoPr(nome, datar, hora, local, horario, participantes)
        naoconfirmouPr[nome] = listadeespera
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
    while nome in reunioespublicas.keys():
        print("Esse nome ja existe tente outro")
        nome = str(input("Defina o nome da reunião: "))

    ata = str(input("Defina a ata da sua reunião: "))

    print("---- SALAS DE REUNIAO ----")
    for i in range(len(listadesalas)):
        print(listadesalas[i])
    print("---- ESCOLHA UMA SALA ----")
    local = str(input("Defina a sala da reunião: "))

    print("--- USUARIOS DO SISTEMA ---")
    arq = open('arquivoDeLogin.txt', 'r')
    for linha in arq:
        valor = linha.split()
        print(valor[0])
    arq.close()
    print("--- ------------------- ---")
    participantesquanti = int(input("Quantos participantes na sua reuniao: "))
    participantes = []
    listadeespera = []
    for i in range(participantesquanti):
        listadeespera.append(input("digite o username do usuario participante: "))

    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    horario = str(input("Defina horario para a reuniao 1(7-8) 2(8-9) 3(9-10) 4(10-11): "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião "))
    M = int(input("Coloque o minuto da reunião"))
    hora = ("{}:{}".format(H, M))
    print("Reunião:{}.\nLocal:{}.\nData:{}.\nHora--{}:{}\n".format(nome, local, datar, H, M))

    for valor in reunioesprivadas.values():
        if valor[0] == datar and valor[1] == hora and valor[2] == local and valor[3] == horario:
            print("Ja existe uma reunião marcada para esta sala, neste dia e neste horario!!")
            criarreuniaoPrC()
        else:
            print("REUNIÃO CRIADA")
    correcao = str(input("Deseja mudar os dados sim(s) não(n): "))
    if correcao == "s":
        criarreuniaoPuC()
    else:
        addreuniaoPu(nome, datar, hora, local, horario, participantes)
        print(reunioespublicas)
        naoconfirmouPr[nome] = listadeespera
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
    while nome in reunioesprivadas.keys():
        print("Esse nome ja existe tente outro")
        nome = str(input("Defina o nome da reunião: "))

    ata = str(input("Defina a ata da sua reunião: "))

    print("---- SALAS DE REUNIAO ----")
    for i in range(len(listadesalas)):
        print(listadesalas[i])
    print("---- ESCOLHA UMA SALA ----")
    local = str(input("Defina a sala da reunião: "))

    print("--- USUARIOS DO SISTEMA ---")
    arq = open('arquivoDeLogin.txt', 'r')
    for linha in arq:
        valor = linha.split()
        print(valor[0])
    arq.close()
    print("--- ------------------- ---")
    participantesquanti = int(input("Quantos participantes na sua reuniao: "))
    participantes = []
    listadeespera = []
    for i in range(participantesquanti):
        listadeespera.append(input("digite o username do usuario participante: "))

    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    horario = str(input("Defina horario para a reuniao 1(7-8) 2(8-9) 3(9-10) 4(10-11): "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião: "))
    M = int(input("Coloque o minuto da reunião: "))
    hora = ("{}:{}".format(H, M))
    print("Reunião:{}.\nLocal:{}.\nData:{}.\nHora--{}:{}\n".format(nome, local, datar, H, M))

    for valor in reunioesprivadas.values():
        if valor[0] == datar and valor[1] == hora and valor[2] == local and valor[3] == horario:
            print("Ja existe uma reunião marcada para esta sala, neste dia e neste horario!!")
            criarreuniaoPrC()
        else:
            print("REUNIÃO CRIADA")
    correcao = str(input("Deseja mudar os dados sim(s) não(n)"))
    if correcao == "s":
        criarreuniaoPrO()
    else:
        reunioespublicas[nome] = [datar, hora, local, horario, participantes]
        naoconfirmouPr[nome] = listadeespera
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
    while nome in reunioespublicas.keys():
        print("Esse nome ja existe tente outro")
        nome = str(input("Defina o nome da reunião: "))

    ata = str(input("Defina a ata da sua reunião: "))

    print("---- SALAS DE REUNIAO ----")
    for i in range(len(listadesalas)):
        print(listadesalas[i])
    print("---- ESCOLHA UMA SALA ----")
    local = str(input("Defina a sala da reunião: "))

    print("--- USUARIOS DO SISTEMA ---")
    arq = open('arquivoDeLogin.txt', 'r')
    for linha in arq:
        valor = linha.split()
        print(valor[0])
    arq.close()
    print("--- ------------------- ---")
    participantesquanti = int(input("Quantos participantes na sua reuniao: "))
    participantes = []
    listadeespera = []
    for i in range(participantesquanti):
        listadeespera.append(input("digite o username do usuario participante: "))

    ano = int(input("Defina o ano de sua reunião: "))
    mes = int(input("Defina o mês de sua reunião: "))
    dia = int(input("Defina o dia de sua reunião: "))
    horario = str(input("Defina horario para a reuniao 7-8, 8-9, 9-10, 10-11: "))
    datar = datetime.date(ano, mes, dia)
    datarsimple = "{}".format(datar)
    datah = datetime.date.today()
    H = int(input("Defina o hora inicial da sua reunião: "))
    M = int(input("Coloque o minuto da reunião: "))
    hora = ("{}:{}".format(H, M))
    print("Reunião:{}.\nLocal:{}.\nData:{}.\nHora--{}:{}\n".format(nome, local, datar, H, M))

    for valor in reunioesprivadas.values():
        if valor[0] == datar and valor[1] == hora and valor[2] == local and valor[3] == horario:
            print("Ja existe uma reunião marcada para esta sala, neste dia e neste horario!!")
            criarreuniaoPrC()
        else:
            print("REUNIÃO CRIADA")
    correcao = str(input("Deseja mudar os dados sim(s) não(n): "))
    if correcao == "s":
        criarreuniaoPuO()
    else:
        reunioespublicas[nome] = [datar, hora, local, horario, participantes]
        naoconfirmouPr[nome] = listadeespera
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

def gestoraddnovasala():

    print("---- SALAS EXISTENTES ----")
    for i in range(len(listadesalas)):
        print(listadesalas[i])
    print("---- ESCOLHA UMA SALA ----")
    novasala = str(input("Define o nome da nova sala: "))

    listadesalas.append(novasala)
    gestormenu.Gestormenu()

def outroaddparticipantes():

    for valor in proprietarioreuniao.values():
        if valor == usuario:
            print(proprietarioreuniao.keys())
        else:
            print("primeiro crie uma reunaio")
            outromenu.ousuariomenu()

    escolha = str(input("Escolha uma reniao para adicionar participantes"))

    if escolha in reunioespublicas:
        valor = reunioespublicas[escolha]
        datar = valor[0]
        hora = valor[1]
        local = valor[2]
        horario = valor[3]
        participantes = valor[4]
        listadeespera = naoconfirmouPu[escolha]
        print(listadeespera)
        print("--- USUARIOS DO SISTEMA ---")
        arq = open('arquivoDeLogin.txt', 'r')
        for linha in arq:
            valor = linha.split()
            print(valor[0])
        arq.close()
        print("--- ------------------- ---")
        participantesquanti = int(input("Quantos participantes voce quer add: "))
        for i in range(participantesquanti):
            listadeespera.append(input("digite o username do usuario participante: "))

        addreuniaoPu(escolha, datar, hora, local, horario, participantes)
        naoconfirmouPu[escolha] = listadeespera

    elif escolha in reunioesprivadas:
        valor = reunioesprivadas[escolha]
        datar = valor[0]
        hora = valor[1]
        local = valor[2]
        horario = valor[3]
        participantes = valor[4]
        listadeespera = naoconfirmouPu[escolha]
        print(listadeespera)
        print("--- USUARIOS DO SISTEMA ---")
        arq = open('arquivoDeLogin.txt', 'r')
        for linha in arq:
            valor = linha.split()
            print(valor[0])
        arq.close()
        print("--- ------------------- ---")
        participantesquanti = int(input("Quantos participantes voce quer add: "))
        for i in range(participantesquanti):
            listadeespera.append(input("digite o username do usuario participante: "))

        addreuniaoPr(escolha, datar, hora, local, horario, participantes)
        naoconfirmouPu[escolha] = listadeespera
    else:
        print("Digite uma reuniao do sistema!")
        outromenu.ousuariomenu()


def confirmarpresença():

    print("--- REUNIOES EM VOCE FOI CONVIDADO ---")
    print("---- PRIVADAS ----")
    for valor in naoconfirmouPr.values():
        listadeespera = valor
        for i in range(len(listadeespera)):
            if i == usuario:
                print(naoconfirmouPr)
    print("---- PUBLICAS ----")
    for valor in naoconfirmouPu.values():
        listadeespera = valor
        for i in range(len(listadeespera)):
            if i == usuario:
                print(naoconfirmouPu)

    nome = str(input("Digite o nome da reuniao: "))
    tipo = str(input("Reuniao 1-privada ou 2-publica: "))

    if tipo == "1":
        # remover da lista de espera
        listadeespera = naoconfirmouPr[nome]
        if usuario in listadeespera:
                listadeespera.remove(usuario)
        # colocar como participante da reuniao
        valor2 = reunioesprivadas[nome]
        datar = valor2[0]
        hora = valor2[1]
        local = valor2[2]
        horario = valor2[3]
        participantes = valor2[4]
        participantes.append(usuario)
        addreuniaoPr(nome, datar, hora, local, horario, participantes)
        # redirecionar para menu de usuario
        arq = open('arquivoDeLogin', 'r')
        for linha in arq:
            valor = linha.split()
            if valor[0] == usuario:
                funçao = valor[2]
        arq.close()
        if funçao == "o":
            outromenu.ousuariomenu()
        else:
            coordenadormenu.omenuC()

    elif tipo == "2":
        # remover da lista de espera
        listadeespera = naoconfirmouPu[nome]
        if usuario in listadeespera:
            listadeespera.remove(usuario)
        # colocar como participante da reuniao
        valor2 = reunioespublicas[nome]
        datar = valor2[0]
        hora = valor2[1]
        local = valor2[2]
        horario = valor2[3]
        participantes = valor2[4]
        participantes.append(usuario)
        addreuniaoPu(nome, datar, hora, local, horario, participantes)
        # redirecionar para menu de usuario
        arq = open('arquivoDeLogin', 'r')
        for linha in arq:
            valor = linha.split()
            if valor[0] == usuario:
                funçao = valor[2]
        arq.close()
        if funçao == "o":
            outromenu.ousuariomenu()
        else:
            coordenadormenu.omenuC()

def negarpresença():

    print("--- REUNIOES EM VOCE FOI CONVIDADO ---")
    print("---- PRIVADAS ----")
    for valor in naoconfirmouPr.values():
        listadeespera = valor
        for i in range(len(listadeespera)):
            if i == usuario:
                print(naoconfirmouPr)
    print("---- PUBLICAS ----")
    for valor in naoconfirmouPu.values():
        listadeespera = valor
        for i in range(len(listadeespera)):
            if i == usuario:
                print(naoconfirmouPu)

    nome = str(input("Digite o nome da reuniao a negar convite: "))
    tipo = str(input("Reuniao 1-privada ou 2-publica: "))

    if tipo == "1":
        # remover da lista de espera
        listadeespera = naoconfirmouPr[nome]
        if usuario in listadeespera:
                listadeespera.remove(usuario)

        # redirecionar para menu de usuario
        arq = open('arquivoDeLogin', 'r')
        for linha in arq:
            valor = linha.split()
            if valor[0] == usuario:
                funçao = valor[2]
        arq.close()
        if funçao == "o":
            outromenu.ousuariomenu()
        else:
            coordenadormenu.omenuC()

    elif tipo == "2":
        # remover da lista de espera
        listadeespera = naoconfirmouPu[nome]
        if usuario in listadeespera:
            listadeespera.remove(usuario)
        # redirecionar para menu de usuario
        arq = open('arquivoDeLogin', 'r')
        for linha in arq:
            valor = linha.split()
            if valor[0] == usuario:
                funçao = valor[2]
        arq.close()
        if funçao == "o":
            outromenu.ousuariomenu()
        else:
            coordenadormenu.omenuC()

def mudarlocal():
    tipo = str(input("Voce deseja editar o local de uma reunião publica(1) ou privada(2)?"))
    if tipo == "2":
        nome = str(input("Voce deseja editar o local de qual reunião?"))
        if nome in reunioesprivadas:
            local = str(input("Coloque o novo local!!"))
            atareunioesprivadas[nome] = "{}".format(local)
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
