from random import randint

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = randint(0,10)
    total_tentativas = 3
    print(numero_secreto)

    for rodada in range(0, total_tentativas):

        chute = int(input("Chute um número de 0 a 10: "))

        if(chute < 0 or chute > 10):
            print("------ ATENÇÃO!!!!!  ------ O numero deve estar entre 0 e 10!")
            rodada -= 1
            continue

        print(f"Você digitou: {chute}")

        if (numero_secreto != chute):
            print("Você errou!")
            print(f"Você ja usou {rodada + 1} de suas {total_tentativas} tentativas.")

        else:
            print("Parabéns! Você acertou")
            break

if(__name__ == "__main__"): #quando executado diretamente a condição é atendida internamente
    jogar()