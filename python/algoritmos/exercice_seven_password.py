list_information_person = ["thiagoZaneti", "thiago006"]
for elementos in range(3):
    attempt = input("Digite a senha: ")
    if attempt == list_information_person[1]:
        print("Logado com sucesso")
        break
    else:
        print("Falha, tente novamente")