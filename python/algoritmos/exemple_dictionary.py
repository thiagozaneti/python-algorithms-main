alunos = {
    1:"Alberto",
    2:"Neto",
    3:"Sandra",
    4:"Paulo",
}
print(alunos[1])
alunos["novo"] = "silas"
print(alunos)
del alunos[1]

list = [alunos]

for chave, valor in alunos.items():
    print(chave, valor)
for item in alunos.items():
    print(item[0],item[1])

print(list)