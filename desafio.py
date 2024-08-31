def recomendar_plano(consumo_mensal):

    if consumo_mensal <= 10:
        plano = "Plano Essencial Fibra - 50Mbps"
    elif consumo_mensal <= 20:
        plano = "Plano Prata Fibra - 100Mbps"
    else:
        plano = "Plano Premium Fibra - 300Mbps"    

    return plano

# Exemplo de uso da função
consumo = float(input())
plano_recomendado = recomendar_plano(consumo)
print(plano_recomendado)





