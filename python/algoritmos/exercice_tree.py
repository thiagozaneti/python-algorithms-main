
nome_um = str(input("Digite o nome do primeiro: "))
nome_dois = str(input("Digite o nome do segundo: "))
nome_tres = str(input("Digite o nome do terceiro: "))

primeira_nota_um = int(input("Digite a primeira nota do primeiro aluno: "))
segunda_nota_um = int(input("Digite a segunda nota do primeiro aluno: "))
terceira_nota_um = int(input("Digite a terceira nota do primeiro aluno: "))

while primeira_nota_um < 0 and segunda_nota_um >10 and 10 < terceira_nota_um > 10:
    primeira_nota_um = int(input("Digite a primeira nota do primeiro aluno: "))
    segunda_nota_um = int(input("Digite a segunda nota do primeiro aluno: "))
    terceira_nota_um = int(input("Digite a terceira nota do primeiro aluno: "))

primeira_nota_dois = int(input("Digite a primeira nota do segundo aluno: "))
segunda_nota_dois = int(input("Digite a segunda nota do segundo aluno: "))
terceira_nota_dois = int(input("Digite a terceira nota do segundo aluno: "))

while primeira_nota_dois < 0 and segunda_nota_dois >10 and 10 < terceira_nota_dois > 10:
    primeira_nota_dois = int(input("Digite a primeira nota do segundo aluno: "))
    segunda_nota_dois = int(input("Digite a segunda nota do segundo aluno: "))
    terceira_nota_dois = int(input("Digite a terceira nota do segundo aluno: "))

primeira_nota_tres = int(input("Digite a primeira nota do terceiro aluno: "))
segunda_nota_tres = int(input("Digite a segunda nota do terceiro aluno: "))
terceira_nota_tres = int(input("Digite a terceira nota do terceiro aluno: "))

while primeira_nota_tres < 0 and segunda_nota_tres > 10 and 10 < terceira_nota_tres > 10:
    primeira_nota_tres = int(input("Digite a primeira nota do terceiro aluno: "))
    segunda_nota_tres = int(input("Digite a segunda nota do terceiro aluno: "))
    terceira_nota_tres = int(input("Digite a terceira nota do terceiro aluno: "))

media_aluno_um = (primeira_nota_um + segunda_nota_um + terceira_nota_um) /3
media_aluno_dois = (primeira_nota_dois + segunda_nota_dois + terceira_nota_dois) /3
media_aluno_tres = (primeira_nota_tres + segunda_nota_tres + terceira_nota_tres) /3

if media_aluno_um > media_aluno_dois > media_aluno_tres:
    print(f"O aluno {nome_um} teve a maior média {media_aluno_um}")
elif media_aluno_dois > media_aluno_um > media_aluno_tres:
    print(f"O aluno {nome_dois} teve a maior média {media_aluno_dois}")
elif media_aluno_tres > media_aluno_dois > media_aluno_um:
    print(f"O aluno {nome_tres} teve a maior média {media_aluno_tres}")
else:
    print("inválido")