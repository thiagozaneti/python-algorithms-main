import time
print("Seja bem vindo ao gmail")
time.sleep(2)
print("mande uma mensagem")
nome = input ("Qual é o seu nome? ")
time.sleep(1)
email = str(input("Digite o email para quem quer enviar: "))
time.sleep(1)
assunto = str(input("assunto: "))
time.sleep(1)
mensagem = str(input("Digite a mensagem: "))
time.sleep(1)
print(f"Nova mensagem! - {assunto}\nOlá,Gostaria de falar sobre: {mensagem}.\n\n Atenciosamente!\n\n{nome}\n {email}.")