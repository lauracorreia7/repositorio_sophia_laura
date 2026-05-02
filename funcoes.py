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
    resposta = 0
    if 1 in faces and 2 in faces and 3 in faces and 4 in faces:
        resposta = 15
    if 2 in faces and 3 in faces and 4 in faces and 5 in faces:
        resposta = 15
    if 3 in faces and 4 in faces and 5 in faces and 6 in faces:
        resposta = 15
    return resposta

def calcula_pontos_sequencia_alta(faces):
    resposta = 0
    if 1 in faces and 2 in faces and 3 in faces and 4 in faces and 5 in faces:
        resposta = 30
    if 2 in faces and 3 in faces and 4 in faces and 5 in faces and 6 in faces:
        resposta = 30
    return resposta

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
        pontos = dicionario[str_categoria]
        dic_cartela['regra_avancada'][str_categoria] = pontos
    else:
        numero = int(str_categoria)
        total = calcula_pontos_regra_simples(lis_dados)
        pontos = total[numero]
        dic_cartela['regra_simples'][numero] = pontos
    return dic_cartela

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)