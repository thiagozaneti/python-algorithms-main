from datetime import datetime

produtos = [
    {"id": 1, "descrição": "Celular", "preco": 1999},
    {"id": 2, "descrição": "Boneca", "preco": 200},
    {"id": 3, "descrição": "notebook", "preco": 1500}
]

clientes = [
    {"id": 1, "nome": "Thiago", "telefone": "17981213736", "cpf": "53245324"},
    {"id": 2, "nome": "Zaneti", "telefone": "17981213536", "cpf": "53245324"},
    {"id": 3, "nome": "Santos", "telefone": "17981223736", "cpf": "53245354"}
]

print(produtos, clientes)

esc_produtos = int(input("Escolha um produto para comprar: ")) - 1
esc_clientes = int(input("Escolha o cliente que vai comprar: ")) - 1
esc_quantidade = int(input("Escolha a quantidade de produtos que o cliente vai comprar: "))

products = produtos[esc_produtos]
clients = clientes[esc_clientes]

result = products["preco"] * esc_quantidade


def create_vendas():
    venda =+ 1
    vendas = [{"id": venda, "data": datetime.today(), "cliente_id": clients, "produto_id": products["id"]}]
    print(vendas)
    print(f"escolheu: {esc_quantidade} produtos, dando valor total: ${result}")

create_vendas()