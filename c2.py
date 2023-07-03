import random

# Definir os parâmetros do problema
capacidade_maxima = 10  # Capacidade máxima da mochila
numero_de_itens = 5  # Número de itens disponíveis
pesos = [2, 3, 4, 5, 6]  # Peso de cada item
valores = [4, 5, 6, 7, 8]  # Valor de cada item

tamanho_da_populacao = 50
taxa_de_mutacao = 0.1
numero_de_geracoes = 100

def criar_individuo():
    return [random.randint(0, 1) for _ in range(numero_de_itens)]

def criar_populacao():
    return [criar_individuo() for _ in range(tamanho_da_populacao)]

def calcular_aptidao(individuo):
    valor_total = sum(valores[i] for i in range(numero_de_itens) if individuo[i] == 1)
    peso_total = sum(pesos[i] for i in range(numero_de_itens) if individuo[i] == 1)
    
    if peso_total > capacidade_maxima:
        penalidade = 0.5  # Penalidade para indivíduos que excedem a capacidade
    else:
        penalidade = 0
    
    return valor_total - penalidade * (peso_total - capacidade_maxima)

def selecionar_pais(populacao):
    pais = random.choices(populacao, k=2, weights=[calcular_aptidao(individuo) for individuo in populacao])
    return pais[0], pais[1]

def cruzar(individuo1, individuo2):
    ponto_de_corte = random.randint(1, numero_de_itens - 1)
    descendente = individuo1[:ponto_de_corte] + individuo2[ponto_de_corte:]
    return descendente

def mutar(individuo):
    for i in range(numero_de_itens):
        if random.random() < taxa_de_mutacao:
            individuo[i] = 1 - individuo[i]  # Mutação de bit
    return individuo

def atualizar_populacao(populacao):
    nova_populacao = []
    while len(nova_populacao) < tamanho_da_populacao:
        pai1, pai2 = selecionar_pais(populacao)
        descendente = cruzar(pai1, pai2)
        descendente = mutar(descendente)
        nova_populacao.append(descendente)
    return nova_populacao

def executar_algoritmo_genetico():
    populacao = criar_populacao()
    melhor_aptidao = 0
    melhor_individuo = None
    
    for geracao in range(numero_de_geracoes):
        populacao = atualizar_populacao(populacao)
        aptidoes = [calcular_aptidao(individuo) for individuo in populacao]
        indice_melhor = aptidoes.index(max(aptidoes))
        
        if aptidoes[indice_melhor] > melhor_aptidao:
            melhor_aptidao = aptidoes[indice_melhor]
            melhor_individuo = populacao[indice_melhor]
        
        print(f"Geração: {geracao+1}, Melhor Aptidão: {melhor_aptidao}")
    
    print("Melhor Solução:")
    print(f"Indivíduo: {melhor_individuo}")
    print(f"Aptidão: {melhor_aptidao}")

executar_algoritmo_genetico()
