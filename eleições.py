import requests
import json
import pandas as pd

dados = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
)

json_dados = json.loads(dados.content)

candidato = []
partido = []
porcetagem = []
votos = []

for inf in json_dados['cand']:

    if inf['seq'] == '1' or inf['seq'] == '2' or inf['seq'] == '3' or inf['seq'] == '4' or inf['seq'] == '5' :
        candidato.append(inf['nm']), partido.append(inf['n']), porcetagem.append(inf['pvap']), votos.append(inf['vap'])

pres_eleicao = pd.DataFrame(list(zip(candidato, partido, porcetagem, votos, )), columns = [
    'Candidato', 'Partido', 'Porcetagem', 'Num de Votos'
])

print(pres_eleicao)
