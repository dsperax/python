import forca
import adivinhacao

print("********************************")
print("*******Escolha o seu jogo*******")
print("********************************")

print("(1) Forca \n(2) Advinhação")

jogo = int(input("Digite o número referente ao jogo:"))

if (jogo == 1):
    print("forca")
    forca.jogar()
elif(jogo == 2):
    print("adivinhacao")
    adivinhacao.jogar()