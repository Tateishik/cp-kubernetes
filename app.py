import requests
import json
from datetime import datetime
import time

def guardar_dados():
    url = 'https://api.polygon.io/v2/aggs/ticker/X:BTCUSD/prev'

    api_key = '2sb4tv2vEPF87Em73FForBMuxaFyJgLe'

    try:
        response = requests.get(url, params={'apiKey': api_key})

        if response.status_code == 200:

            dados_cripto = response.json()

            preco_alto = dados_cripto["results"][0]["h"]
            preco_baixo = dados_cripto["results"][0]["l"]

            data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            dados_registro = f"Data/Hora: {data_hora_atual}, Preço mais alto: {preco_alto}, Preço mais baixo: {preco_baixo}\n"

            with open('dados_cripto.txt', 'a') as arquivo:
                arquivo.write(dados_registro)

            print("Dados de criptomoeda registrados com sucesso.")

        else:
            print("Erro ao fazer a solicitação à API:", response.status_code)

    except Exception as e:
        print("Erro na solicitação:", e)


while True:
    agora = datetime.now().time()

    if agora.hour == 22 and agora.minute == 0:

        guardar_dados()

        espera = 60
        print(f"Aguardando até a próxima verificação de hora... ({espera} segundos)")
        time.sleep(espera)
