import chute
import forca


def escolhe_jogo():
    print("******************************************")
    print("**           ESCOLHA O JOGO!            **")
    print("******************************************")

    print("(1) Forca | (2) Chute")
    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando Forca")
        forca.jogar()
    else:
        print("Jogando Chute")
        chute.jogar()


if __name__ == "__main__":
    escolhe_jogo()