# menu e funções devem exibir:
# quatidade de pessoas maiores que 50 anos
# A quantidade de pessoas que ganham mais de R$ 2000 e a porcentagem; que isso representa do todo;
# O nome, salário, idade e profissão das 3 pessoas com maiores salários;
# A média salarial de cada profissão;
# O  intervalo da maioria das idades e o sexo de quem ganha mais de R$ 2000.
# (M 39-50, F 29-30)

# Código feito por Thiago Zaneti Dos Santos
# Computador número 28

from random_data import pessoas


def menu():
    print(
        """
    Pessoas maiores que 50 anos [1]
    Pessoas que ganham mais que 2000 e porcentagem [2]
    3 maiores salários [3]
    media salárial [4]
    intervalo de idade [5]
    Mostrar todos as pessoas [6]
    Sair [7]
"""
    )
    # menu atuando como uma função mãe, onde coloco as demais funções nas escolhas do menu
    while True:
        user_select = int(input("selecione sua escolha: "))
        if user_select == 1:
            contador_de_idade()
        elif user_select == 2:
            # função
            counter_salario(pessoas)
        elif user_select == 3:
            # função
            tres_maiores_salarios()
        elif user_select == 4:
            imprimir_media()
        elif user_select == 5:
            intervalo_de_idade(pessoas)
        elif user_select == 6:
            print("mostrar toda lista: ")
            mostrar_lista()
        elif user_select == 7:
            break
        else:
            print("Seleção incorreta")
        if user_select < 1 and user_select > 8:
            print("Seção encerrada")
            break
        menu()


def mostrar_lista():
    print(pessoas)  # essa função irá mostrar a lista inteira


# função de contar idade maiores que 50
def contador_de_idade():
    contador = 0  # começamos com um contador
    for pessoa in pessoas:  # percorrendo a lista
        if (
            pessoa["idade"] > 50
        ):  # se as idades da lista forem maiores que 50, contador será incrementado +1
            contador += 1
            print(
                f"Quantidade de pessaos que tem +50 anos {contador} "
            )  # print da função


# função de contar salario maior de 2000 reais e calcular a porcentagem
def counter_salario(pessoas):
    contador_salario_percent = 0
    contador_salario_total = 0

    for pessoa in pessoas:
        if pessoa["salario"] > "2000":
            contador_salario_percent += 1
        contador_salario_total += 1

    if contador_salario_total != 0:
        total_percent = (contador_salario_percent / contador_salario_total) * 100
    else:
        total_percent = 0

    print("Número de pessoas com salário maior que 2000:", contador_salario_percent)
    print("Total de pessoas:", contador_salario_total)
    print("Porcentagem de pessoas com salário maior que 2000:", total_percent)

    return contador_salario_total


# função para obter os três maiores salarios
def tres_maiores_salarios():
    # função sorted ordena a lista da maior para a menor
    # buscando a lista pessoas e indo diretamente em salario
    pessoas_ordenadas_por_salario = sorted(
        pessoas, key=lambda x: x["salario"], reverse=True
    )
    print("As 3 pessoas com maiores salários são:")
    for pessoa in pessoas_ordenadas_por_salario[:3]:
        # percorre pessoas dentro da variável pessoas_ordenadas_por_salario e pega as três primeiras, printando
        print(
            f"Nome: {pessoa['nome']}, Salário: {pessoa['salario']}, Idade: {pessoa['idade']}, Profissão: {pessoa['profissao']}"
        )


def calcular_media_salarios(pessoas):
    # Dicionário para armazenar os salários de cada profissão
    salarios_por_profissao = {}
    contador_por_profissao = {}
    # Itera sobre cada pessoa na lista
    for pessoa in pessoas:
        profissao = pessoa["profissao"]
        salario = float(pessoa["salario"])  # Convertendo para float
        # Adiciona o salário ao total para essa profissão
        salarios_por_profissao[profissao] = (
            salarios_por_profissao.get(profissao, 0) + salario
        )
        contador_por_profissao[profissao] = contador_por_profissao.get(profissao, 0) + 1
    # Calcula a média para cada profissão
    media_salarios = {}
    for profissao, total_salarios in salarios_por_profissao.items():
        contador = contador_por_profissao[profissao]
        media_salarios[profissao] = total_salarios / contador
    return media_salarios
# Calcula a média salarial para cada profissão

def imprimir_media():
    medias = calcular_media_salarios(pessoas)
    # Imprime os resultados
    for profissao, media in medias.items():
        print(f"Média salarial de {profissao}: R${media:.2f}")


# Definindo a função intervalo_de_idade que recebe uma lista de dicionários chamada 'pessoas'
def intervalo_de_idade(pessoas):
    # Inicializa uma lista vazia para armazenar pessoas com salário acima de 2000
    lista_mais_2000 = []
    # Itera sobre cada pessoa no parâmetro 'pessoas'
    for pessoa in pessoas:
        # Obtém o valor associado à chave 'salario' no dicionário 'pessoa'. Se a chave não existir, retorna 0.
        salarios = pessoa.get("salario", 0)
        # Verifica se o salário é maior que "2000" (o que compara como strings, não como números).
        if salarios > "2000":
            # Se o salário for maior que "2000", adiciona a pessoa à lista_mais_2000
            lista_mais_2000.append(pessoa)
    # Verifica se há pessoas na lista_mais_2000
    if lista_mais_2000:
        # Cria uma lista de idades a partir dos dicionários de pessoas em lista_mais_2000
        idades = [pessoa.get("idade", 0) for pessoa in lista_mais_2000]
        # Cria uma lista de sexos a partir dos dicionários de pessoas em lista_mais_2000
        sexo = [pessoa.get("sexo") for pessoa in lista_mais_2000]
        # Calcula a média das idades
        idade_media = sum(idades) / len(idades)
        # Encontra o sexo mais frequente na lista
        sexo_mais_frequente = max(set(sexo), key=sexo.count)
        # Imprime a média das idades e o sexo mais frequente no formato "{idade_media},{sexo_mais_frequente}"
        print(f"{idade_media},{sexo_mais_frequente}")
