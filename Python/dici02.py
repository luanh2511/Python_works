alunos={}
print ("'Leitura dos dados")
while True:
    matr= int(input("Digite a matricula: "))
    if matr == 0:
        break
    elif matr in alunos:
        print ("A matricula {} já existe no cadastro" .format (matr))
        continue
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    alunos[matr] = (nome, idade, curso)
    
print ("Fim da leitura dos dados\n")

print ("Cadastro de Alunos:")

for matricula, dados in alunos.items():
    print ("Aluno: {}".format (dados[0]))
    print ("Nr. Matricula: {}".format (matricula))
    print ("Idade: {}".format (dados[1]))
    print ("Curso: {}".format (dados[2]))
print ("\nFIM DO PROGRAMA")
