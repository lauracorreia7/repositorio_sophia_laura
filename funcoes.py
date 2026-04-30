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

def calcula_pontos_sequencia_baixa(faces):
    lados = ''.join(faces)
    if lados.find('1')!=-1:
        if lados.find('2')!=-1:
            if lados.find('3')!=-1:
                if lados.find('4')!=-1:
                    resultado = 15
    elif lados.find('2')!=-1:
        if lados.find('3')!=-1:
            if lados.find('4')!=-1:
                if lados.find('5')!=-1:
                    resultado = 15
    elif lados.find('3')!=-1:
        if lados.find('4')!=-1:
            if lados.find('5')!=-1:
                if lados.find('6')!=-1:
                    resultado = 15
    else:
        resultado = 0
    return resultado

def calcula_pontos_sequencia_alta(faces):
    if 2 in faces and 3 in faces and 4 in faces and 5 in faces:
        if 1 in faces:
            resultado = 30
        elif 6 in faces:
            resultado = 30 
        else:
            resultado = 0
    else:
        resultado = 0   
    return resultado

def calcula_pontos_full_house(lista):
    dados_3 = []
    dados_3[0] = lista[0]
    dados_2 = []
    soma = 0
    i = 1
    while i < lista:
        if lista[i] == dados_3[0]:
            dados_3.append(lista[i])
        else:
            dados_2.append(lista[i])
        i += 1
    if len(dados_3) == 3:
        for elemento in dados_2:
            if dados_2[0] == dados_2[1]:
                for elemento in dados_3:
                    soma += elemento
                for elemento in dados_2:
                    soma += elemento
    if len(dados_2) == 3:
        for elemento in dados_3:
            if dados_3[0] == dados_3[1] and dados_3[0] == dados_3[2]: 
                for elemento in dados_3:
                    soma += elemento
                for elemento in dados_2:
                    soma += elemento
    return soma

def calcula_pontos_quadra(faces):
    dicionario = {}
    resposta = 0
    soma = 0
    for lado in faces:
        if lado not in dicionario:
            dicionario[lado] = 1
            soma = soma + lado
        else:
            dicionario[lado] = dicionario[lado] + 1
            soma = soma + lado

    for lado in dicionario:
        if dicionario[lado]>=4:
            resposta = soma
    return resposta
