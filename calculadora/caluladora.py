from menu import menu_opcoes


def soma():
    valores = None
    lista = []

    while valores != 0.0:
        valores = float(input('Valor a ser somado: : '))
        if valores != 0.0:
            lista.append(valores)
        else:
            break

    result_soma = sum(lista)
    print("Resultado: ", result_soma)


def divisao():
    a = float(input("Valor a ser dividido: "))
    b = float(input("Valor a ser dividido: "))

    resultado_divisao = (a / b)
    print(f'Resultado: {resultado_divisao}')


def subtracao():
    a = float(input("Valor a ser subtraido: "))
    b = float(input("Valor a ser subtraido: "))

    resultado_subtracao = (a - b)
    print(f'Resultado: {resultado_subtracao}')


def multiplicacao():
    a = float(input("Valor a ser multiplicado: "))
    b = float(input("Valor a ser multiplicado: "))

    result_multiplicacao = (a * b)
    print(f'Resultado: {result_multiplicacao}')


while True:
    menu_opcoes()
    opcoes = input("Qual operação deseja realizar? ").lower()
    print('Pressione 0 para realizar a operação.')
    if opcoes not in ['s', 'm', 'd', '-']:
        print("Opção invalida!")
        continue

    if opcoes == 's':
        soma()

    if opcoes == 'm':
        multiplicacao()

    if opcoes == '-':
        subtracao()

    if opcoes == 'd':
        divisao()
