import random
RSP = ["tesoura", "papel", "pedra"]
escolha = input("Escolha sua opção: ")
Oponente = random.choice(RSP)
#casos para ganhar
if escolha == "tesoura" and Oponente =="papel":
    print ("Você ganhou")
elif escolha == "papel" and Oponente =="pedra":
    print("Você ganhou")
elif escolha == "pedra" and Oponente =="tesoura":
    print("Você ganhou")
elif escolha == "tesoura" and Oponente =="pedra":
    print ("Você perdeu")
elif escolha == "papel" and Oponente =="tesoura":
    print("Você perdeu")
elif escolha == "pedra" and Oponente =="papel":
    print("Você perdeu")
else:
    print("Empate")
print("O Adversário escolheu: " + Oponente)