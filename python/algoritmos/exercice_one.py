print("Média ponderada")
situacao = ""
name = str(input("Qual seu nome: "))
primeira_nota = int(input("Digite a primeira nota: "))
segunda_nota = int(input("Digite a segunda nota: "))
terceira_nota = int(input("Digite a terceira nota: "))
calc_nota = (primeira_nota * 0.35) + (segunda_nota * 0.35) + (terceira_nota * 0.30)

while primeira_nota < 0 or primeira_nota > 10 or segunda_nota < 0 or segunda_nota > 10 or terceira_nota < 0 or terceira_nota > 10:
    primeira_nota = int(input("Reescreva a nota da prova de matemática 1: "))
    segunda_nota = int(input("Reescreva a nota da prova de matemática 2: "))
    terceira_nota = int(input("Reescreva a nota da prova de matemática 3: "))
    calc_nota = (primeira_nota * 0.35) + (segunda_nota * 0.35) + (terceira_nota * 0.30)

if calc_nota >= 7:
    situacao = "Aprovado"
elif calc_nota >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Olá {name}! Sua nota é {calc_nota} e você foi {situacao}.")
