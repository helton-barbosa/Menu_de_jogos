import random


def jogar():
    print("******************************************")
    print("*******BEM-VINDO AO JOGO DO CHUTE!********")
    print("******************************************")

    numero_secreto = random.randrange(1, 100)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade que deseja?")
    print("(1) Fácil | (2) Médio | (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print("Desculpe... valor inválido! Escolha um valor entre 1 e 100.")
            continue

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if acertou:
            print("Você ACERTOU! E fez {} pontos\n".format(pontos))
            break
        else:
            if maior:
                print("Você NÃO ACERTOU! O seu chute foi maior que o número secreto.\n")
            elif menor:
                print("Você NÃO ACERTOU! O seu chute foi menor que o número secreto.\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")


if __name__ == "__main__":
    jogar()
