alunos = {}

for x in range(3):
    nome = str(input('Informe o Nome do Aluno:')).capitalize()
    nota = float(input('Informe a Note do Aluno:'))
    alunos[nome] = nota

soma = 0
for y in alunos.values():
    soma += nota

media = soma / len(alunos)

print("A média das notas dos alunos é:", media)
