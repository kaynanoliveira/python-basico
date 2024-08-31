numero1 = float(input("Entre com um número: "))

numero2 = float(input("Entre com um número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "*":
    resultado = numero1 * numero2

elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2

else:
    print("Operação invalida!")

print(f"O resultado da operação é igual a: {resultado}")