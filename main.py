
import usuarionovo
import usuarioativo
# import outromenu
import sys
sistema = True


status = "nulo"


def menu1():

    status = str(input("Você é um usuario cadastrado? Digite s(sim) ou n(não)! Digite x para sair!"))
    if status == "s":
        usuarioativo.usuarioativo()
    elif status == "n":
        usuarionovo.usuarionovo()

    elif status == "x":
        sys.exit()

    while status != "x":
        menu1()


menu1()