disciplina = [{"Nome": "Historia", "Serie": "2", "Codigo": "201"},
              {"Nome": "Matematica", "Serie": "2", "Codigo": "202"},
              {"Nome": "Biologia", "Serie": "3", "Codigo": "301"}]
alunos = {}
menu = 0
aux = 0
opt = 0


def main():
    leArquivo()
    global menu
    ans = True
    while ans:
        if menu == 0:
            print("""
            #### MENU PRINCIPAL ###
            1.Consultar Estudantes
            2.Gerenciar Estudantes
            3.Consultar Disciplinas
            4.Sair
            """)
            ans = input("Escolha uma opção: ")
            if ans == "1":
                print("\n Consulta de Estudantes:")
                consultaEstudantes()
            elif ans == "2":
                print("\n Gerência de Estudantes:")
                gerenciaEstudantes()
            elif ans == "3":
                print("\n Consulta de Disciplinas:")
                consultaDisciplina()
            elif ans == "4":
                print("\n Saindo...")
                escreveArquivo()
                menu = 1
            elif ans != "":
                print("\n Escolha Inválida! Tente Novamente!")
        else:
            ans = False

def consultaEstudantes ():
    global numMatricula
    global menu
    global alunos
    menuCe = 0
    ansCE = True
    while ansCE:
        if menuCe == 0:
            if len(alunos) == 0:
                print("Lista de alunos vazia!")
                menuCe= 1
                menu = 0
            else:
                print("""
                    1.Consultar Por Nome
                    2.Consultar Por CPF
                    3.Consultar Por Matrícula
                    4.Consultar Por Disciplina
                    5.Consultar Por Ano de Nascimento
                    6.Consultar Por Série
                    7.Consultar Por Situação
                    8.Voltar ao Menu Principal
                    """)
                ansCE = input("Escolha uma opção: ")
                if ansCE == "1":
                    consultaNome()
                    menuCe = 1
                    menu = 0
                elif ansCE == "2":
                    consultaCpf()
                    menuCe = 1
                    menu = 0
                elif ansCE == "3":
                    numero = int(input("\n Digite a matrícula a ser buscada:"))
                    print(alunos.get(numero))
                    menuCe = 1
                    menu = 0
                elif ansCE == "4":
                    buscaDisciplina()
                    menuCe = 1
                    menu = 0
                elif ansCE == "5":
                    consultaAno()
                    menuCe = 1
                    menu = 0
                elif ansCE == "6":
                    consultaSerie()
                elif ansCE == "7":
                    consultaSituacao()
                    menuCe = 1
                    menu = 0
                elif ansCE == "8":
                    print("\n Voltando ao Menu Principal...")
                    menuCe = 1
                    menu = 0
                elif ansCE != "":
                    print("\n Escolha Inválida! Tente Novamente!")
                    menuCe = 0
        else:
            ansCE = False
    return menu

def gerenciaEstudantes():
    global menu
    global alunos
    global numMatricula
    menuGe = 0
    ansGE = True
    while ansGE:
        if menuGe == 0:
            print("""
                   1.Cadastrar Aluno
                   2.Atualizar Cadastro
                   3.Deletar Aluno
                   4.Voltar ao Menu Principal
                   """)
            ansGE = input("Escolha uma opção: ")
            if ansGE == "1":
                cadastroAluno()
                menuGe = 1
                menu = 0
            elif ansGE == "2":
                atualizaAluno()
                menuGe = 1
                menu = 0
            elif ansGE == "3":
                deletaAluno()
                menuGe = 1
                menu = 0
            elif ansGE == "4":
                print("\n Voltando ao Menu Principal...:")
                menuGe = 1
                menu = 0
            elif ansGE != "":
                print("\n Escolha Inválida! Tente Novamente!")
                menuGe = 0

        else:
            ansGE = False
    return menu




def consultaNome():
    nome = input("\n Digite o nome a ser buscado:")
    numero = nome
    contador = 0
    for key in alunos.keys():
        if numero in alunos[key]:
            print("Aluno: %s" % alunos[key][0])
            contador = contador+1
            continue
    if contador == 0:
        print("Não encontrado!")
def consultaCpf():
    print("\n Digite o CPF a ser buscado:")
    cpf = input()
    numero = cpf
    contador = 0
    for key in alunos.keys():
        if numero in alunos[key]:
            print("Aluno: %s" % alunos[key][0])
            contador = contador +1
            continue
    if contador == 0:
            print("Não encontrado!")
def buscaDisciplina():
    disciplina = input("\n Digite a disciplina a ser buscada:")
    numero = disciplina
    contador = 0
    for key in alunos.keys():
        if numero in alunos[key][3]:
            print("Aluno: %s" % alunos[key][0])
            contador = contador + 1
            continue
    if contador == 0:
            print("Não encontrado!")
def consultaAno():
    ano = input("\n Digite o ano a ser buscado:")
    numero = ano
    contador = 0
    for key in alunos.keys():
        if numero in alunos[key]:
            print("Aluno: %s" % alunos[key][0])
            contador = contador +1
            continue
    if contador == 0:
            print("Não encontrado!")
def consultaSerie():
    serie = input("\n Digite a série a ser buscada:")
    numero = serie
    contador = 0
    for key in alunos.keys():
        if numero in alunos[key]:
            print(key)
            contador = contador + 1
            continue
    if contador == 0:
            print("Não encontrado!")
def consultaSituacao():
    situacao = input("\n Digite a situação a ser buscada:")
    numero = situacao
    contador = 0
    for key in alunos.keys():
        if numero in alunos[key]:
            print("Aluno: %s" % alunos[key][0])
            contador = contador + 1
            continue
    if contador == 0:
            print("Não encontrado!")

def cadastroAluno():
    global disc
    global alunos
    nome = input("\n Digite o nome do aluno a ser cadastrado:")
    cpf = input("\n Digite o CPF do aluno a ser cadastrado:")
    numMatricula = len(alunos)+1
    nascimento = input("\n Digite o ano de nascimento do aluno a ser cadastrado:")
    Ndisciplinas = int(input("\n Digite o número de disciplinas que o aluno cursará:"))
    disciplinas = []
    for i in range(0, Ndisciplinas):
        print("Digite o código da disciplina:")
        validaDisciplina()
        disciplinas.append(disc)
    situacao = str(input("\n Digite a situação do aluno:"))
    if situacao == 'Trancado' or 'Matriculado':
        print("Aluno cadastrado com sucesso!")
    else:
        print("Situação Inválida!")
    alunos[numMatricula] = [nome, cpf, nascimento, disciplinas, situacao]
    print(alunos)


def atualizaAluno():
    global disc
    print(alunos)
    matricula = int(input("\n Digite a matrícula do aluno a ser atualizado:"))
    global aux
    global matriculaN
    matriculaN = matricula
    print(alunos[matricula])
    menuUpdate = 0
    ansUpdate = True
    while ansUpdate:
        if menuUpdate == 0:
            print("""
                   1.Atualizar nome do aluno
                   2.Atualizar cpf do aluno
                   3.Atualizar ano de nascimento do aluno
                   4.Atualizar disciplinas que o aluno cursa
                   5.Atualizar situação do aluno
                   6.Voltar ao menu principal
                   """)
            ansUpdate = int(input("Escolha uma Opção"))
            if ansUpdate == 1:
                opt = input("Digite o novo nome do aluno:")
                alunos[matricula][0] = opt
                print(alunos[matricula])
                menuUpdate = 1
            elif ansUpdate == 2:
                opt = input("Digite o novo CPF do aluno:")
                alunos[matricula][1] = opt
                print(alunos[numMatricula])

                menuUpdate = 1
            elif ansUpdate == 3:
                opt = input("Digite o novo ano de nascimento do aluno:")
                alunos[matricula][2] = opt
                print(alunos[numMatricula])

                menuUpdate = 1
            elif ansUpdate == 4:
                opt = int(input("Digite a nova quantidade de disciplinas que o aluno cursar:"))
                disciplinas = []
                for i in range(0, opt):
                    print("Digite o código da disciplina:")
                    validaDisciplina()
                    disciplinas.append(disc)
                    alunos[matricula][3] = disciplinas
                print(alunos[matricula])

                menuUpdate = 1
            elif ansUpdate == 5:
                opt = input("Digite a nova situação do aluno:")
                alunos[matricula][4] = opt
                print(alunos[matricula])

                menuUpdate = 1
            elif ansUpdate == 6:
                print("Voltando ao menu inicial...")

                menuUpdate = 1
            elif ansUpdate != "":
                print("Opção Inválida!")
                menuUpdate = 0
        else:
            ansUpdate = False

def deletaAluno():
    global alunos
    matricula = input("\n Digite a matrícula do aluno a ser deletado:")
    matricula = numMatricula
    del alunos[numMatricula]
    print("Aluno deletado com sucesso!")
    print(alunos)



def consultaDisciplina():
    global menu
    global disciplina
    menuCd = 0
    ansCD = True
    while ansCD:
        if menuCd == 0:
            print("""
                       1.Listar Disciplinas Cadastradas
                       2.Voltar ao Menu Principal
                       """)
            ansCD = input("Escolha uma opção: ")
            if ansCD == "1":
                for i in disciplina:
                    print ("")
                    print ("Nome: %s"%i["Nome"])
                    print("Serie: %s" % i["Serie"])
                    print("Codigo: %s" % i["Codigo"])
                menuCd = 1
                menu = 0
            elif ansCD == "2":
                print("\n Voltando ao Menu Principal...:")
                menuCd = 1
                menu = 0
            elif ansCD != "":
                print("\n Escolha Inválida! Tente Novamente!")
                menuCd = 0

        else:
            ansCD = False
    return menu

def validaDisciplina():
    numero = input()
    var = 0
    var2 = 0
    global disc
    ans = True
    while ans:
        if var2 == 0:
            for i in disciplina:
                if numero == i["Codigo"]:
                    print(i["Nome"])
                    var = 1
                    var2 = 1
                    disc = i["Codigo"]
            if var == 0:
                print("Disciplina não encontrada, tente novamente")
                var2 = 0
                numero = input()
        else:
            ans = False
    return disc

def escreveArquivo():
    global alunos

    arquivo = open('listaAlunos.txt', 'w')
    for i in alunos:
        arquivo.write("%s#"%alunos[i][0])
        arquivo.write("%s#" % alunos[i][1])
        arquivo.write("%s#" % alunos[i][2])
        arquivo.write("%s#" % alunos[i][3])
        arquivo.write("%s\n" % alunos[i][4])
    arquivo.close()

def leArquivo():
    global alunos
    arquivo = open('listaAlunos.txt', "r")
    linhas = arquivo.readlines()
    for i in linhas:
        numMatricula = len(alunos)+1
        aux = i.split('#')
        cynthia = aux[3].rstrip("']")
        cynthia =cynthia .lstrip("['")
        cynthia = cynthia.split("', '")
        aux[3] = cynthia
        aux[4] = aux[4].rstrip('\n')
        alunos[numMatricula] = aux









if __name__ == "__main__":
    main()

