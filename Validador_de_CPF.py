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

def remover_Ocorrências(lista, item):
    resultado = [i for i in lista if i != item]
    return resultado

print("Insira o CPF a ser validado.")
valor_Inserido = input()

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
else:
    print("CPF inválido.")