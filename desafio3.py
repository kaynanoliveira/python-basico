import re

def validar_numero_telefone(numero):
    # Define o padrão do número de telefone esperado
    padrao = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    
    # Utiliza a função re.match() para verificar se o número está no formato correto
    if re.match(padrao, numero):
        return True
    else:
        return False

def solicitar_e_validar_telefone():
    numero = input()   

    if validar_numero_telefone(numero):
        print("Número de telefone válido.")
    else:
        print("Número de telefone inválido.")

solicitar_e_validar_telefone()
