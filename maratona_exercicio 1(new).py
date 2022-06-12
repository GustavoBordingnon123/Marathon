
from re import L


nomes_e_notas_dos_alunos = []
nome_de_um_aluno = 'aluno'
aluno_reprovado = "aluno_reprovado9" 
aluno_anterior = '9'
nota = '9'

quantidade_de_alunos = int(input("a quantidade de alunos na sala é = "))


while quantidade_de_alunos > 100 or quantidade_de_alunos < 1:
    quantidade_de_alunos = int(input("numero invalido, por favor digite um numero entre 1 a 100: "))
for contador in range(quantidade_de_alunos):
    nomes_e_notas_dos_alunos.append(input("digite o nome do aluno, e quantos exercicios ele resolveu: "))
    nome_de_um_aluno = nomes_e_notas_dos_alunos[contador] 
    while len(nome_de_um_aluno) > 30 or len(nome_de_um_aluno) < 1:
        nomes_e_notas_dos_alunos[contador] = (input("numero invalido, digite o nome do aluno, e quantos exercicios ele resolveu: "))
        nome_de_um_aluno = nomes_e_notas_dos_alunos

for cont in range(quantidade_de_alunos):
    for cont2 in range(quantidade_de_alunos):
        aluno_anterior = nota
        alunox = nomes_e_notas_dos_alunos[cont]
        tamanho = len(alunox) - 1
        nota = (alunox[tamanho])
        if nota == '0':
            tamanho = len(alunox) - 2
            nota = (alunox[tamanho])
            if nota == '1': 
                nota = '9'
        elif nota > aluno_anterior:
            nota = aluno_anterior
        elif nota < aluno_anterior: 
            aluno_reprovado = alunox
        elif nota == aluno_anterior:
            if aluno_reprovado < alunox:
                aluno_reprovado = alunox


print("o aluno(a) reprovado foi:", aluno_reprovado[0:len(aluno_reprovado)-2])
