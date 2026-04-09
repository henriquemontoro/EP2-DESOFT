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
    
    if categoria in cartela_de_pontos['regra_simples']:
        cartela_de_pontos['regra_simples'][int(categoria)] = pontos_simples[int(categoria)]
    else:
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]
    
    return cartela_de_pontos
