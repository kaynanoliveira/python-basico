def cadastrar_equipamentos():
#    Função para cadastrar equipamentos e exibir a lista com os equipamentos cadastrados.
    itens = []  # Lista para armazenar os equipamentos    


    equipamento = input(f"")
    itens.append(equipamento)
    
    # Exibir a lista de equipamentos com marcação
    print("Lista de Equipamentos:")
    for equipamento in itens:
        print(f" - {equipamento}")

# Chamar a função para executar o programa
cadastrar_equipamentos()