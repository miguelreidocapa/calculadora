def calculadora():
    print("=== Calculadora Simples ===")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    
    # Escolha da operação
    escolha = input("Digite o número da operação (1/2/3/4): ")

    # Entrada dos números
    num1 = float(input("Digit e o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif escolha == '2':
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif escolha == '3':
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif escolha == '4':
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Erro! Não é possível dividir por zero.")
    else:
        print("Opção inválida!")


# Executar a calculadora
calculadora()
