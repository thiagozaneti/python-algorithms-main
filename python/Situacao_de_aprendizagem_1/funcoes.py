#menu e funções devem exibir:
#quatidade de pessoas maiores que 50 anos
#A quantidade de pessoas que ganham mais de R$ 2000 e a porcentagem; que isso representa do todo;
#O nome, salário, idade e profissão das 3 pessoas com maiores salários;
#A média salarial de cada profissão;
#O  intervalo da maioria das idades e o sexo de quem ganha mais de R$ 2000.
#(M 39-50, F 29-30)
from random_data import *

def menu():
    print("""
    Pessoas maiores que 50 anos [1]
    Pessoas que ganham mais que 2000 e porcentagem [2]
    3 maiores salários [3]
    media salárial [4]
    intervalo de idade [5]
    Mostrar todos as pessoas [6]
    Sair [7]
""")
    
    while True:
        user_select = int(input("selecione sua escolha: "))
        if user_select ==1:
            print("Seleção 1")
            contador_de_idade()
        elif user_select == 2:
            #função 
            print("Seleção 1")
        elif user_select == 3:
            #função 
            print("Seleção 1")
        elif user_select == 4:
            #função 
            print("Seleção 1")
        elif user_select == 5:
            #função 
            print("Seleção 1")
        elif user_select == 6:
            print("mostrar toda lista: ") 
            mostrar_pessoas()
        elif user_select == 7:
            break
        else:
            print("Seleção incorreta")
        menu()

#função de mostrar pessoas
def mostrar_pessoas():
    for pessoa in pessoas:
     print("Nome:", pessoa["nome"])
     print("Salário:", pessoa["salário"])
     print("Idade:", pessoa["idade"])
     print("Profissão:", pessoa["profissão"])

#função de contar idade maiores que 50
def contador_de_idade():
    contador = 0
    for pessoa in pessoas:
        if pessoa["idade"] >= 50:
            contador +=1
            print(f"Quantidade de pessaos que tem +50 anos {contador} ")

def porcentagem():
    contador_porcentagem = 0
    for salarios in salario:
        if salario >= 2000:
            contador_porcentagem +=1
            print(f"Quantidade de pessaos que tem +50 anos {contador_porcentagem} ")

            

