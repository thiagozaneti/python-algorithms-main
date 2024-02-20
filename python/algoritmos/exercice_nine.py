carros = ["Vectra", "Astra", "Palio", "Saveiro", "Masserati"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
select = int(input("digite o index que quer remover"))
counter = len(carros)
if select < counter and select > counter:
    print("Error")
elif select >= counter and select <= counter:
    del carros[select]
print(carros)



