import random

def rolar_dados(quantidade):
    lista = []
    
    for i in range(quantidade):
        lista.append(random.randint(1, 6))
    
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    dados_rolados = dados_rolados[:dado_para_guardar] + dados_rolados[dado_para_guardar + 1:]
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    dados_no_estoque = dados_no_estoque[:dado_para_remover] + dados_no_estoque[dado_para_remover + 1:]
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados):
    pontos = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }
    for dado in dados:
        pontos[dado] += dado
    return pontos

def calcula_pontos_soma(dados):
    soma = 0
    for dado in dados:
        soma += dado
    return soma

def calcula_pontos_sequencia_baixa(dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados:
        return 15
    elif 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 15
    elif 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 15
    else:
        return 0

def calcula_pontos_sequencia_alta(dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 30
    elif 2 in dados and 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 30
    else:
        return 0
    
def calcula_pontos_full_house(dados):
    contagem = {}
    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1
    for valor in contagem:
        if contagem[valor] == 3:
            tem_3 = True
        elif contagem[valor] == 2:
            tem_2 = True
        else:
            tem_3 = False
            tem_2 = False
    if tem_3 and tem_2 == True:
        soma = 0
        for dado in dados:
            soma += dado
        return soma
    else:
        return 0

def calcula_pontos_quadra(dados):
    contagem = {}
    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1
    for valor in contagem:
        if contagem[valor] >= 4:
            soma = 0
            for dado in dados:
                soma += dado
            return soma
    else:
        return 0
    
def calcula_pontos_quina(dados):
    contagem = {}
    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1
    for valor in contagem:
        if contagem[valor] >= 5:
            return 50
    return 0


def calcula_pontos_regra_avancada(dados):
    pontos = {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }
    
    return pontos



def faz_jogada(dados, categoria, cartela_de_pontos):
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancados = calcula_pontos_regra_avancada(dados)
    
    if categoria == "1" or categoria == "2" or categoria == "3" or categoria == "4" or categoria == "5" or categoria == "6":
        cartela_de_pontos['regra_simples'][int(categoria)] = pontos_simples[int(categoria)]
    else:
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]
    
    return cartela_de_pontos




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
