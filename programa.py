from funcoes import *

def jogo():
    cartela = {
        'regra_simples': {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1},
        'regra_avancada': {
            'sem_combinacao':-1,
            'quadra':-1,
            'full_house':-1,
            'sequencia_baixa':-1,
            'sequencia_alta':-1,
            'cinco_iguais':-1
        }
    }

    imprime_cartela(cartela)

    for _ in range(12):

        dados_guardados = []
        dados_rolados = rolar(dados_guardados)
        contador_rerrolagens = 0
        mostrar_menu = True

        while True:
            if mostrar_menu:
                print("Dados rolados:", dados_rolados)
                print("Dados guardados:", dados_guardados)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

            mostrar_menu = True
            escolha = input()

            if escolha == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                indice = int(input())
                if 0 <= indice < len(dados_rolados):
                    dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)

            elif escolha == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                indice = int(input())
                if 0 <= indice < len(dados_guardados):
                    dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)

            elif escolha == "3":
                if contador_rerrolagens >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    dados_rolados = rolar(dados_guardados)
                    contador_rerrolagens += 1

            elif escolha == "4":
                imprime_cartela(cartela)

            elif escolha == "0":
                print("Digite a combinação desejada:")
                while True:
                    categoria = input()

                    if categoria in ["1","2","3","4","5","6"]:
                        if cartela['regra_simples'][int(categoria)] != -1:
                            print("Essa combinação já foi utilizada.")
                        else:
                            break
                    elif categoria in cartela['regra_avancada']:
                        if cartela['regra_avancada'][categoria] != -1:
                            print("Essa combinação já foi utilizada.")
                        else:
                            break
                    else:
                        print("Combinação inválida. Tente novamente.")

                cartela = faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                break

            else:
                print("Opção inválida. Tente novamente.")
                mostrar_menu = False

    imprime_cartela(cartela)

    total = sum(pontos for pontos in cartela['regra_simples'].values() if pontos != -1) + \
            sum(pontos for pontos in cartela['regra_avancada'].values() if pontos != -1)

    if sum(pontos for pontos in cartela['regra_simples'].values() if pontos != -1) >= 63:
        total += 35

    print("Pontuação total:", total)

jogo()