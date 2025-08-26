from operacoes import soma, subtrai, multiplica, divide

def calculadora():
    print("=== Calculadora Simples ===")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    escolha = input("Digite o número da operação (1/2/3/4): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = soma(num1, num2)
    elif escolha == '2':
        resultado = subtrai(num1, num2)
    elif escolha == '3':
        resultado = multiplica(num1, num2)
    elif escolha == '4':
        resultado = divide(num1, num2)
    else:
        resultado = "Opção inválida!"

    print(f"Resultado: {resultado}")