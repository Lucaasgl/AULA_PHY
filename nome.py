# Armazenando as informações do usuário em variáveis
nome = "Lucas"
sobrenome = "Matheus Glowienka"
idade = 18
altura = 1.74
peso = 75

# Verificando se o usuário é maior de idade
if idade >= 18:
    maior_idade = True
else:
    maior_idade = False

# Exibindo os resultados
print("Nome completo:", nome, sobrenome)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Peso:", peso, "kg")
if maior_idade:
    print("Maior de idade: Sim")
else:
    print("Maior de idade: Não")