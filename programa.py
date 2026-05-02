from funcoes import rolar_dados
from funcoes import guardar_dado
from funcoes import remover_dado
from funcoes import faz_jogada
from funcoes import imprime_cartela
guardados = []
numero_dados = 5
cartela = {'regra_simples':{1:-1,2:-1,3:-1,4:-1,5:-1,6:-1},'regra_avancada':{'sem_combinacao':-1,'quadra':-1,'full_house':-1,'sequencia_baixa':-1,'sequencia_alta':-1,'cinco_iguais':-1}}
print(imprime_cartela(cartela))
for rodada in range(12):
    dados = rolar_dados(numero_dados)
    print(f'Dados rolados: {dados}\nDados guardados: {guardados}\nDigite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    numero = 1
    contagem = 0
    while numero!=0:
        numero = int(input(''))
        if numero==0:
            print('Digite a combinação desejada:')
            jogada = input('')
            i = 0
            while i==0:
                if jogada in ['0','1','2','3','4','5','6']:
                    opcoes = cartela['regra_simples']
                    nova = int(jogada)
                    if opcoes[nova]!=-1:
                        print('Essa combinação já foi utilizada.')
                        jogada = input('')
                    else:
                        pontos = faz_jogada(dados,jogada,cartela)
                        opcoes[nova] = pontos['regra_simples'][nova]
                        i = 10
                elif jogada in ['sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais']:
                    opcoes = cartela['regra_avancada']
                    if opcoes[jogada]!=-1:
                        print('Essa combinação já foi utilizada.')
                        jogada = input('')
                    else:
                        pontos = faz_jogada(dados,jogada,cartela)
                        opcoes[jogada] = pontos['regra_avancada'][jogada]
                        i = 10
                else:
                    print('Combinação inválida. Tente novamente.')
                    jogada = input('')
        elif numero==1:
            print('Digite o índice do dado a ser guardado (0 a 4):')
            dado = int(input(''))
            lista = guardar_dado(dados,guardados,dado)
            dados = lista[0]
            guardados = lista[1]
        elif numero==2:
            print('Digite o índice do dado a ser removido (0 a 4):')
            dado = int(input(''))
            lista = remover_dado(dados,guardados,dado)
            dados = lista[0]
            guardados = lista[1]
        elif numero==3:
            if contagem<2:
                dados = rolar_dados(numero_dados)
                contagem = contagem+1
            else:
                print('Você já usou todas as rerrolagens.')
        elif numero==4:
            cartela = imprime_cartela(cartela)
            print(cartela)
        else:
            print('Opção inválida. Tente novamente.')
        print(f'Dados rolados: {dados}\nDados guardados: {guardados}\nDigite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
pontuacao = 0
for tipo in cartela:
    for pontos in tipo:
        pontuacao = pontuacao + cartela[tipo][pontos]
print(imprime_cartela(cartela))
print(f'Pontuação total: {pontuacao}')