from dotenv import load_dotenv
import json
import os
import requests

load_dotenv()

TOKEN = os.getenv("TOKEN_TINY")

BASE_URL = "https://api.tiny.com.br/api2"


def buscar_produto_por_sku(sku):

    url = f"{BASE_URL}/produtos.pesquisa.php"

    params = {
        "token": TOKEN,
        "formato": "json",
        "pesquisa": sku
    }

    response = requests.get(url, params=params)

    dados = response.json()

    produtos = dados["retorno"].get("produtos", [])

    for item in produtos:

        produto = item["produto"]

        if produto["codigo"] == sku:
            return produto

    return None

def obter_produto_completo(produto_id):
    url = f"{BASE_URL}/produto.obter.php"

    params = {
        "token": TOKEN,
        "id": produto_id,
        "formato": "json"
    }

    response = requests.get(url, params=params)

    dados = response.json()

    return dados["retorno"]["produto"]


def obter_estoque_por_sku(sku):

    produto = buscar_produto_por_sku(sku)

    if not produto:
        raise Exception(f"Produto não encontrado: {sku}")

    produto_id = produto["id"]
    url = f"{BASE_URL}/produto.obter.estoque.php"

    params = {
        "token": TOKEN,
        "id": produto_id,
        "formato": "json"
    }

    response = requests.get(url, params=params)

    dados = response.json()

    produto_estoque = dados["retorno"]["produto"]
    estoque = produto_estoque.get("saldo", 0) - produto_estoque.get("saldoReservado", 0)

    try:
        return int(float(estoque))
    except:
        return 0
    

def atualizar_estoque_por_sku(sku, estoque):

    produto = buscar_produto_por_sku(sku)

    if not produto:
        raise Exception(
            f"Produto não encontrado ao atualizar o estoque: {sku}"
        )

    produto_id = produto["id"]

    url = f"{BASE_URL}/produto.atualizar.estoque.php"

    payload = {
        "token": TOKEN,
        "formato": "json",
        "estoque": json.dumps({
            "estoque": {
                "idProduto": int(produto_id),
                "tipo": "B",
                "quantidade": float(estoque),
                "observacoes": "Sincronização automática"
            }
        })
    }

    response = requests.post(
        url,
        data=payload
    )
    
    return response.json()