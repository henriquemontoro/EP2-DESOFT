from funcoes import *

cartela_de_pontos = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela_de_pontos)

for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    jogada_feita = False

    while jogada_feita == False:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')

        opcao = input()

        if opcao == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            indice = int(input())
            lista = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = lista[0]
            dados_guardados = lista[1]

        elif opcao == '2':
            print('Digite o índice do dado a ser removido (0 a 4):')
            indice = int(input())
            lista = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = lista[0]
            dados_guardados = lista[1]

        elif opcao == '3':
            if rerrolagens < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            else:
                print('Você já usou todas as rerrolagens.')

        elif opcao == '4':
            imprime_cartela(cartela_de_pontos)

        elif opcao == '0':
            print('Digite a combinação desejada:')
            combinacao = input()

            if combinacao == '1' or combinacao == '2' or combinacao == '3' or combinacao == '4' or combinacao == '5' or combinacao == '6':
                if cartela_de_pontos['regra_simples'][int(combinacao)] == -1:
                    dados = dados_rolados + dados_guardados
                    cartela_de_pontos = faz_jogada(dados, combinacao, cartela_de_pontos)
                    jogada_feita = True
                else:
                    print('Essa combinação já foi utilizada.')

            elif combinacao == 'sem_combinacao' or combinacao == 'quadra' or combinacao == 'full_house' or combinacao == 'sequencia_baixa' or combinacao == 'sequencia_alta' or combinacao == 'cinco_iguais':
                if cartela_de_pontos['regra_avancada'][combinacao] == -1:
                    dados = dados_rolados + dados_guardados
                    cartela_de_pontos = faz_jogada(dados, combinacao, cartela_de_pontos)
                    jogada_feita = True
                else:
                    print('Essa combinação já foi utilizada.')

            else:
                print('Combinação inválida. Tente novamente.')

        else:
            print('Opção inválida. Tente novamente.')

imprime_cartela(cartela_de_pontos)

pontuacao = 0
soma_simples = 0

for i in cartela_de_pontos['regra_simples']:
    pontuacao += cartela_de_pontos['regra_simples'][i]
    soma_simples += cartela_de_pontos['regra_simples'][i]

for i in cartela_de_pontos['regra_avancada']:
    pontuacao += cartela_de_pontos['regra_avancada'][i]

if soma_simples >= 63:
    pontuacao += 35

print(f'Pontuação total: {pontuacao}')
