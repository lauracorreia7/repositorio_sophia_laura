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
    lados = ''
    for lado in faces:
        lado = str(lado)
        lados = lados + lado
    resultado = 0
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

def calcula_pontos_full_house(faces):
    dicionario = {}
    soma = 0
    resultado = 0
    for lado in faces:
        if lado not in dicionario:
            dicionario[lado] = 1
            soma = soma + lado
        else:
            dicionario[lado] = dicionario[lado] + 1
            soma = soma + lado
    if 3 in dicionario.values() and 2 in dicionario.values():
        resultado = soma
    return resultado

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

def calcula_pontos_quina(faces):
    dicionario = {}
    resposta = 0
    for lado in faces:
        if lado not in dicionario:
            dicionario[lado] = 1
        else:
            dicionario[lado] = dicionario[lado] + 1
    for lado in dicionario:
        if dicionario[lado]>=5:
            resposta = 50
    return resposta

def calcula_pontos_regra_avancada(faces):
    dicionario = {}
    dicionario['cinco_iguais'] = calcula_pontos_quina(faces)
    dicionario['full_house'] = calcula_pontos_full_house(faces)
    dicionario['quadra'] = calcula_pontos_quadra(faces)
    dicionario['sem_combinacao'] = calcula_pontos_soma(faces)
    dicionario['sequencia_alta'] = calcula_pontos_sequencia_alta(faces)
    dicionario['sequencia_baixa'] = calcula_pontos_sequencia_baixa(faces)
    return dicionario

def faz_jogada(lis_dados, str_categoria, dic_cartela):
    lista = ['sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais']
    if str_categoria in lista:
        dicionario = calcula_pontos_regra_avancada(lis_dados)
        pontos = dicionario['str_categoria']
    else:
        total = calcula_pontos_regra_simples(lis_dados)
        pontos = total['str_categoria']
    dic_cartela[str_categoria] = dic_cartela[str_categoria] + pontos
    return dic_cartela