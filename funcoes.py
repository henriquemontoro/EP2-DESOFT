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
