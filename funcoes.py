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

def calcula_pontos_regra_simples(faces):
    dicio = {1:0,2:0,3:0,4:0,5:0,6:0}
    for face in faces:
        if face==1:
            dicio[1]=dicio[1]+1
        if face==2:
            dicio[2]=dicio[2]+2
        if face==3:
            dicio[3]=dicio[3]+3
        if face==4:
            dicio[4]=dicio[4]+4
        if face==5:
            dicio[5]=dicio[5]+5
        if face==6:
            dicio[6]=dicio[6]+6
    return dicio

def calcula_pontos_soma(faces):
    soma = 0
    for lado in faces:
        soma = soma + lado
    return soma