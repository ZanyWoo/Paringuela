import random
Max_Number = int(input("Numero Limite= "))

Number_1 = random.randint(1, Max_Number)
Number_2 = random.randint(1, Max_Number)
Result = Number_1 + Number_2

print("{}+X={}".format(Number_1, Result))
chute = int(input("X=?, "))
if (chute == Number_2) :
    print("Ganhou")
elif (chute < Number_2) :
    print("Errou, {} foi menor, deu {}".format(Number_1, Number_2))
elif (chute > Number_2) :
    print("Errou, {} foi maior, deu {}".format(Number_1,Number_2))