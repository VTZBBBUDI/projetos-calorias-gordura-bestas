# Script para calcular o tempo necessário para atingir um percentual de gordura corporal alvo

def calcular_tempo_reducao_gordura(peso, bf_atual, bf_alvo, consumo_calorico, tmt):
    # Cálculo do déficit diário
    deficit_diario = tmt - consumo_calorico
    
    # Quantidade atual e alvo de gordura corporal
    gordura_atual = peso * (bf_atual / 100)
    gordura_alvo = peso * (bf_alvo / 100)
    
    # Quantidade de gordura a perder
    gordura_a_perder = gordura_atual - gordura_alvo
    
    # Calorias totais para perder a gordura desejada (1 kg de gordura = 7700 calorias)
    calorias_necessarias = gordura_a_perder * 7700
    
    # Tempo necessário em dias
    dias_necessarios = calorias_necessarias / deficit_diario
    
    return dias_necessarios

# Exemplo de uso
peso = 78.7  # em kg
bf_atual = 23  # percentual de gordura atual
bf_alvo = 18  # percentual de gordura desejado
consumo_calorico = 2000  # consumo diário em calorias
tmt = 2460  # Taxa Metabólica Total (calorias para manter o peso)

# Calculando o tempo
dias_para_alvo = calcular_tempo_reducao_gordura(peso, bf_atual, bf_alvo, consumo_calorico, tmt)

print(f"Tempo necessário para reduzir o percentual de gordura corporal de {bf_atual}% para {bf_alvo}%: {dias_para_alvo:.0f} dias")
