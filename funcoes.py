def rolar_dados(vezes):
    import random
    lista_dados = []
    for i in range(vezes):
        lista_dados.append(random.randint(1,6))
    return lista_dados

def guardar_dado(dados_rolados1, dados_guardados, indice):
    dados_rolados2 = []
    for i in range(len(dados_rolados1)):
        if i == indice:
            dados_guardados.append(dados_rolados1[i])
        else:
            dados_rolados2.append(dados_rolados1[i])
    lista = []
    lista.append(dados_rolados2)
    lista.append(dados_guardados)
    return (lista)

def remover_dado(dados_rolados, dados_guardados, indice):
    dados_guardados2 = []
    for i in range(len(dados_rolados)):
        if i == indice:
            dados_rolados.append(dados_guardados[i])
        else:
            dados_guardados2.append(dados_guardados[i])
    lista = []
    lista.append(dados_rolados)
    lista.append(dados_guardados2)
    return (lista)