cliente = [
    {"nome": "cliente1", "email": "th2006zadosa@gmail.com", "senha": "thiago006"}
]
produto_tv = [
    "id":1",
    "philco",
    "R$1470"
]
produto_lavadora = [
    "id":1",
    "daku",
    "R$450"
]
produtos = {
    1:produto_tv,
    2:produto_lavadora
} 

Carrinho = {}

while True:
    select = str(input("Deseja fazer um cadastro?"))
    if select == "sim":
        nome = str(input("Digite o nome"))
        email = str(input("Digite o email"))
        senha = str(input("Digite a senha"))
        cliente.append([nome, email, senha])
        print(cliente)
    elif select == "nao":
        break
    else:
        print("Erro")

while True:
    attempt = input("Digite a senha [sair]: ")
    if attempt == cliente[0]["senha"]:
        print("Logado com sucesso")
        print(produtos)
        selecao = int(input("Selecione o produto para comprar: "))
        carrinho = produtos[selecao]
        print(f"seu carrinho: {carrinho}")
    elif attempt == "sair":
        break
    else:
        print("Falha, tente novamente")


