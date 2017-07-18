import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    rodada = 1
    pontos = 1000
    total_de_tentativas = 0
    numero_secreto = random.randrange(1,101)
    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel= int(input("Defina o nível de dificuldade: "))

    if(nivel ==1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas=5

    for rodada in range(1, total_de_tentativas+1):
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)
        acertou = chute==numero_secreto
        maior = chute>numero_secreto
        menor = chute<numero_secreto

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        if(chute < 1 or chute >100):
            print("Você deve chutar um número entre 1 e 100")
            continue

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        elif(maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos




    print("***********Fim de jogo***********")

if(__name__ == "__main__"):
    jogar()