#Faça um programa que armazene em uma lista as 
#compras e em outra os valores de ca
#da item comprado para exibi los da seguinte maneira
list_product = ["martelo","serrote", "macete","chave de fenda"]
list_value = ["$20.10", "$40.00", "$22", "$10", "$20"]
for product, value in zip(list_value, list_product):
    print(f"Produto:{product} - {value}")





