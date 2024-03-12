import random
print("##### Bem vindo ao jogo de adivinhação ##### \n")
sorteio = random.randint(1, 10)

contador = 1
max_chances = int(input("Números de tentativas: \n"))
while (contador <= max_chances):
    chute = int(input("Tentativa {} de {} Digite um numero de 1 a 10 \n".format(contador, max_chances)))
    acertou = chute == sorteio
    if (acertou) :
        print("Parabéns, você ganhou!")
        break
    elif (chute > sorteio) :
        print("O número sorteado é menor")
    elif (chute < sorteio) :
        print("O número sorteado é maior")
    contador = contador + 1
print("##### Fim de jogo :P #####")