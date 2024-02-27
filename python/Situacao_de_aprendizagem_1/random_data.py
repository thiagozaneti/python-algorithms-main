#lista deve conter nome, salário, idade e profissão
import random

nomes = ["João", "Maria", "Pedro", "Ana", "José", "Sara", "Miguel", "Carla", "Paulo", "Teresa",
    "André", "Marta", "Luís", "Inês", "Rui", "Diana", "António", "Lúcia", "Hugo", "Catarina",
    "Fernando", "Rita", "David", "Andreia", "Daniel", "Susana", "Manuel", "Cátia", "Nuno", "Eva",
    "Vasco", "Lara", "Gonçalo", "Bárbara", "Carlos", "Filipa", "Francisco", "Carolina", "Tiago", "Elsa",
    "Jorge", "Patrícia", "Alexandre", "Sofia", "Ruben", "Beatriz", "Vitor", "Raquel", "Eduardo", "Vanessa",
    "Alberto", "Isabel", "Leonardo", "Ângela", "Bruno", "Cláudia", "Hélder", "Andreia", "Adriano", "Daniela",
    "Nelson", "Isabela", "Gustavo", "Cristina", "Ricardo", "Tânia", "Renato", "Mónica", "Luisa", "Mariana",
    "Marcelo", "Andreia", "Júlio", "Dulce", "Sérgio", "Tatiana", "Nicolau", "Diana", "Paula", "Cátia",
    "Victor", "Lorena", "Roberto", "Sara", "Rodrigo", "Alexandra", "Bernardo", "Fátima", "Salvador", "Carina",
    "Duarte", "Rute", "Mário", "Sandra", "Santiago", "Teresa", "Simão", "Marta", "Miguel", "Vera",
    "Hugo", "Inês", "Rúben", "Clara", "Francisco", "Carolina", "Tomás", "Susana", "Mateus", "Lúcia",
    "Daniel", "Catarina", "Filipe", "Rita", "Martim", "Andreia", "Samuel", "Mónica", "Artur", "Vanessa",
    "Diogo", "Isabel", "António", "Margarida", "Ricardo", "Tânia", "Manuel", "Diana", "Alexandre", "Carla",
    "Rui", "Bárbara", "Joana", "Sofia", "André", "Rosa", "Luisa", "Cláudia", "Luís", "Filipa",
    "Gonçalo", "Mariana", "Pedro", "Beatriz", "Paulo", "Ana", "Sérgio", "Inês", "Hélder", "Tatiana",
    "Nuno", "Carolina", "Ruben", "Rute", "David", "Eva", "Leonardo", "Teresa", "Eduardo", "Andreia",
    "Vasco", "Rita", "Carlos", "Mónica", "Alberto", "Lara", "Bruno", "Dulce", "Jorge", "Sara",
    "Adriano", "Cátia", "Nelson", "Vanessa", "Renato", "Isabel", "Júlio", "Cristina", "Victor", "Diana",
    "Mário", "Lorena", "Marcelo", "Alexandra", "Bernardo", "Fátima", "Salvador", "Carina", "Duarte", "Andreia",
    "Simão", "Margarida", "Rodrigo", "Rute", "Tomás", "Sofia", "Mateus", "Rosa", "Diogo", "Clara"
         ]

profissoes = ["Desenvolvedor de Software",
    "Engenheiro de Software",
    "Analista de Sistemas",
    "Arquiteto de Sistemas",
    "Administrador de Banco de Dados",
    "Administrador de Redes",
    "Analista de Segurança da Informação",
    "Analista de Suporte Técnico",
    "Designer de Experiência do Usuário (UX/UI)",
    "Desenvolvedor Web",
    "Desenvolvedor Mobile",
    "Engenheiro de Dados",
    "Cientista de Dados",
    "Especialista em Cloud Computing",
    "Engenheiro de DevOps",
    "Analista de Qualidade de Software",
    "Gestor de Projetos de TI",
    "Consultor de TI",
    "Especialista em Inteligência Artificial",
    "Especialista em Blockchain",
    "Especialista em Cibersegurança",
    "Especialista em IoT (Internet das Coisas)",
    "Especialista em Robótica",
    "Especialista em Realidade Virtual e Aumentada"]

pessoas = []

for _ in range(1000):
    nome = random.choice(nomes)
    salario = random.randint(1599, 12000)  
    idade = random.randint(20, 60)  
    profissao = random.choice(profissoes)
    pessoa = {"nome": nome, "salário": salario, "idade": idade, "profissão": profissao}
    pessoas.append(pessoa)



