list_name = ["alunos:"]
list_nota = ["notas:"]
for elementos in range(5):
    name = input("digite os nomes:  ")
    nota = input("Digite as notas: ")
    list_name.append(name)
    list_nota.append(nota)
print(list_name, list_nota)