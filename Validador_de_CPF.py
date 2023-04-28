númerosObrigatórios = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
todosOsNúmeros = []

def remover_Ocorrências(lista, item):
    resultado = [i for i in lista if i != item]
    return resultado

def validação_Estrutura_Valor_Inserido(valor_Inserido):
    while len(valor_Inserido) != 14 or caracteres_Obrigatórios1 not in valor_Inserido or caracteres_Obrigatórios2 not in valor_Inserido:
        if len(valor_Inserido) != 14:
            print("O valor inserido é inválido. Favor inserir uma sequência de 14 carácteres (incluindo os números, os pontos e um hífem).")
        if caracteres_Obrigatórios1 not in valor_Inserido:
            print("O valor inserido não possui pontos.")
        if caracteres_Obrigatórios2 not in valor_Inserido:
            print("O valor inserido não possui um hífem.")
        valor_Inserido = input("Favor tentar novamente: ")
    return valor_Inserido

while True:
    cpf = []
    cpfOriginal = []
    multiplicadores = []
    multiplicadores2 = []
    multiplicador = 10
    multiplicador2 = 11
    index = -1
    index2 = -2
    multiplicações = []
    multiplicações2 = []
    caracteres_Obrigatórios2 = "-"
    caracteres_Obrigatórios1 =  "."

    print("Insira o CPF a ser validado.")
    valor_Inserido = input()

    valor_Inserido = validação_Estrutura_Valor_Inserido(valor_Inserido)

    cpf = list(valor_Inserido)

    cpf = remover_Ocorrências(cpf, ".")
    cpfOriginal = remover_Ocorrências(cpf, "-")
    cpf = remover_Ocorrências(cpf, "-")

    cpf.pop()
    cpf.pop()

    for i in cpf:
        multiplicadores.append(multiplicador)
        multiplicador -= 1

    for i in cpf:
        index += 1
        multiplicação = int(cpf[(index)]) * int(multiplicadores[(index)])
        multiplicações.append(multiplicação)

    somaDasMultiplicações = sum(multiplicações)
    resto = somaDasMultiplicações%11

    if resto >= 2:
        dígito1 = 11 - resto
    else:
        dígito1 = 0

    cpf.append(str(dígito1))

    for i in cpf:
        multiplicadores2.append(multiplicador2)
        multiplicador2 -= 1

    for i in cpf:
        index2 += 1
        multiplicação = int(cpf[(index2)]) * int(multiplicadores2[(index2)])
        multiplicações2.append(multiplicação)

    soma = sum(multiplicações2)
    resto = soma%11

    if resto >= 2:
        dígito2 = 11 - resto
    else:
        dígito2 = 0

    cpf.append(str(dígito2))

    if cpf == cpfOriginal:
        print("CPF válido.")
        break
    else:
        print("CPF inválido. Favor tentar novamente:")