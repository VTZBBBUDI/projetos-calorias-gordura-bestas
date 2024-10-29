# Calculando as calorias queimadas durante o exercício ativo

# Variáveis e constantes
pausas = 5
duracao_malhacao_ativa = 60 - (pausas * 1.5)  # tempo de exercício em minutos sem as pausas
peso = 78.7  # peso em kg
MET = 3.5 # MET estimado para musculacao ate a falha

# Cálculo
calorias_queimadas_ativa = duracao_malhacao_ativa * (MET * 3.5 * peso / 200)
calorias = round(calorias_queimadas_ativa, 1)

METcaminhada = 5 #caminhada a 5.6 km/h
duracao_caminhada = 30
calorias_queimadas_caminhada = duracao_caminhada * (METcaminhada * 3.5 * peso/200)
calorias_caminhada = round(calorias_queimadas_caminhada, 1)

calorias_totais_perdidas_ativa = calorias_caminhada + calorias_queimadas_ativa
calorias_totais = round(calorias_totais_perdidas_ativa, 1)
print(f'MUSCULACAO: {calorias}\nESTEIRA/CAMINHADA: {calorias_caminhada}\nCALORIAS TOTAIS PERDIDAS NA ACADEMIA: {calorias_totais}')