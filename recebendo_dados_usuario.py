"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String
"""
# Entrada de dados
print("Qual o seu nome?")
nome = input()  # input -> entrada

# exemplo de print antigo da v1
print("Seja bem vindo(a) %s" % nome)

print("Qual a sua idade?")
idade = input()  # input -> entrada

# processamento

# saída - exemplo de print da v2
print("{0} tem {1} anos".format(nome, idade))

# exemplo de print atual v3
print(f"Lembrando o nome de {nome}")
print(f"Meu nome é {nome} e eu tenho {idade}")
print(f"{nome} nasceu em {2020-int(idade)}")

peso = input(f"Qual o seu peso, {nome} ?")

# já usando cast para converter a string em int
peso = int(input(f"Qual o seu peso, {nome} ?"))

