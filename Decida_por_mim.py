"""

Decida por mim

Neste projeto tem-se intuito de criar um "bot"
que responderá uma limitada quantidade de
respostas.

"""
from random import randint

respostas = ["Sim", "Não", "Sim, vai lá", "Não, você não deveria ir"]

fim = "N"

while(fim != "S" or fim != "s"):

    pergunta = input("Informe uma pergunta: ")

    print(f"{respostas[randint(0, len(respostas)-1)]}")

    fim = input("Deseja continuar?[S/N]")
    
    if fim == "S" or fim == "s":
        break