def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  
            return num1 / num2
        else:
            return 0
    


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
op = int(input("Digite o número da operação (1 para Soma, 2 para Subtração, 3 para Multiplicação, 4 para Divisão): "))

resultado = calculadora(numero1, numero2, op)

if resultado != 0:
    print("Resultado:", resultado)
