# Ler quanto dinheiro uma pessoa tem na carteira e mostrar quantos dólares ela pode comprar.

import requests
import json

try:
    real = float(input("Quanto dinheiro você tem na carteira? R$"))

    # Pegar as informações das cotações através da API
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes.raise_for_status()  # Levanta um erro se a requisição não foi bem sucedida
    cotacoes = cotacoes.json()
    cotacao_dolar = float(cotacoes['USDBRL']["bid"])

    print(f"A cotação do dólar está: {cotacao_dolar:.2f}")
    conversao = real / cotacao_dolar
    print(f"Você consegue comprar: ${conversao:.2f}")

except requests.exceptions.RequestException as e:
    print(f"Erro ao obter a cotação: {e}")
except ValueError as e:
    print(f"Erro ao converter valor: {e}")