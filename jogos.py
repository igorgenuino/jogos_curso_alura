import forca
import adivinhacao

def escolhe_jogo():
    print("**************************************")
    print("***********Escolha seu jogo***********")
    print("**************************************")

    print("Os jogos disponíveis são: ")
    print("(1) Forca  (2) Adivinhação")
    jogo = int(input("Qual jogo você escolhe??\n"))

    if(jogo == 1):
        print("Jogo da forca selecionado!!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo da adivinhação selecionado!!")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()


