def remover_Ocorrências(lista, item):
    resultado = [i for i in lista if i != item]
    return resultado

def validação_Estrutura_Valor_Inserido(valor_Inserido):
    while True:
        if len(valor_Inserido) != 14:
            while len(valor_Inserido) != 14:
                print("O valor inserido é inválido. Favor inserir uma sequência de 14 carácteres (incluindo pontos '.' e um hífem '-').")
                print("Favor tentar novamente:")
                valor_Inserido = input()
        elif valor_Inserido not in caracteres_Obrigatórios:
            while valor_Inserido not in caracteres_Obrigatórios:
                print("O valor inserido não possui pontos e/ou um hífem.")
                print("Favor tentar novamente:")
                valor_Inserido = input()
        else:
            return None


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
    caracteres_Obrigatórios = ["-", "."]

    print("Insira o CPF a ser validado.")
    valor_Inserido = input()

    validação_Estrutura_Valor_Inserido(valor_Inserido)

    for i in valor_Inserido:
        valor = i
        cpf.append(valor)

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