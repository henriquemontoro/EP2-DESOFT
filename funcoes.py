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
