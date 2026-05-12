from time import sleep
from datetime import datetime
from relacoes import RELACOES
from tiny_api import (
    obter_estoque_por_sku,
    atualizar_estoque_por_sku
)

ULTIMOS_ESTOQUES = {}

def sincronizar_estoques(log):
   
    global ULTIMOS_ESTOQUES

    for sku_base, config in RELACOES.items():
        
        try:
            sleep(5)
            estoque = obter_estoque_por_sku(sku_base)

            estoque_seguranca = config[
                "estoque_seguranca"
            ]

            estoque_final = max(
                estoque - estoque_seguranca,
                0
            )

            derivados = config["derivados"]

            for sku_derivado in derivados:
                #sleep(5)
                estoque_anterior = (
                    ULTIMOS_ESTOQUES.get(
                        sku_derivado
                    )
                )

                if estoque_anterior == estoque_final:

                    if log:
                        print(
                            f"{datetime.now()} {sku_derivado} sem alteração"
                        )
                    continue

                atualizar_estoque_por_sku(
                    sku_derivado,
                    estoque_final
                )

                ULTIMOS_ESTOQUES[
                    sku_derivado
                ] = estoque_final

                if log:
                    print(
                        f"{datetime.now()} - {sku_derivado} atualizado para {estoque_final}"
                    ) 

        except Exception as e:

            print(f"{datetime.now()} Erro: {e}")

    