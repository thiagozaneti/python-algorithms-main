def maior_number(number, number_new):
    while number > number_new:
        number_new = float(input(f"Digite um número maior que {number}: ")) 
    print(f"{number_new} é maior que {number}")
    if number_new < number:
        print("Numero maior")
number = float(input("Digite o primeiro número: "))
number_two = float(input("Digite o segundo número: "))
maior_number(number, number_two)

