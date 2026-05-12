TAMANHOS_PADRAO = [
    "P",
    "M",
    "G",
    "GG",
    "XG",
    "G2",
]

TAMANHOS_COMPLETOS = [
    "P",
    "M",
    "G",
    "GG",
    "XG",
    "G2",
    "G3",
    "G4",
    "G5",
    "G6",
]

TAMANHOS_PP = [
    "PP",
    "P",
    "M",
    "G",
    "GG",
    "XG",
    "G2",
    "G3"
]

TAMANHOS_FEMININO = [
    "PP",
    "P",
    "M",
    "G",
    "GG",      
]

PRODUTOS = [
    {   #casual preta
        "pai": "16030040001",
        "tamanhos": TAMANHOS_COMPLETOS,
        "derivados": [
            "1075",
            "1406",
            "1476",
            "1073",
            "1327",
            "2016",
            "1386",
            "1365",
            "1328",
            "1149",
            "1323",
            "1329",
            "1146",
            "1164",
            "1311",
            "1309",
            "1059",
            "1150",
            "1186",
            "1384",
            "1088",
            "1326",
            "1288",
            "1250",
            "2001-PTO"
        ]
    },

    {   #casual Off
        "pai": "16030040003",
        "tamanhos": TAMANHOS_COMPLETOS,
        "derivados": [
            "1482",
            "1474",
            "1478", 
            "2001-OFF"          

        ]
    },

    {   #casual branca
        "pai": "16030040002",
        "tamanhos": TAMANHOS_COMPLETOS,
        "derivados": [
            "1480",
            "1175",
            "1231",
            "1475",
            "1086",
            "1123",
            "1042",
            "1092",
            "1461",
            "1090"
        ]
    },

    {   #moletom off
        "pai": "16090010003",
        "tamanhos": TAMANHOS_PP,
        "derivados": [
            "2005"
        ]
    },

    {   #moletom preto
        "pai": "16090010001",
        "tamanhos": TAMANHOS_PP,
        "derivados": [
            "2002",
            "2013",
            "2012",
            "1378",
            "2006",
            "1376"
        ]
    },

    {   #baby look preto
        "pai": "BRV26230001",
        "tamanhos": TAMANHOS_FEMININO,
        "derivados": [
            "2015",
            "2014",
            "1447"
        ]
    },

    {   #baby look off
        "pai": "BRV26230003",
        "tamanhos": TAMANHOS_FEMININO,
        "derivados": [
            "2007",
            "1446"
        ]
    },

    {   #baby look rosa
        "pai": "BRV26230007",
        "tamanhos": TAMANHOS_FEMININO,
        "derivados": [
            
        ]
    },

    {   #Street amarela
        "pai": "875652124",
        "tamanhos": TAMANHOS_PP,
        "derivados": [
            "1485",
            "2003"
        ]
    },

    {   #Street preta
        "pai": "16030850001",
        "tamanhos": TAMANHOS_PP,
        "derivados": [
            
        ]
    },

    {   #Street Off
        "pai": "16030850003",
        "tamanhos": TAMANHOS_PP,
        "derivados": [
            
        ]
    },

    {   #Street Branca
        "pai": "16030850002",
        "tamanhos": TAMANHOS_PP,
        "derivados": [
            
        ]
    },

    {   #Street Verde
        "pai": "16030850071",
        "tamanhos": TAMANHOS_PP,
        "derivados": [
            "2000",
            "2253"
        ]
    },

    {   #Cropped Off
        "pai": "BRV26200003",
        "tamanhos": TAMANHOS_FEMININO,
        "derivados": [
           "2010"
           "2009"
           "1484"
        ]
    },

    {   #Cropped Preto
        "pai": "BRV26200001",
        "tamanhos": TAMANHOS_FEMININO,
        "derivados": [
            "1325"
            "1273"
            "1285"
        ]
    },
   
    {   #Cropped Marrom
        "pai": "BRV26200348",
        "tamanhos": TAMANHOS_FEMININO,
        "derivados": [
           
        ]
    },

    {   #Regata Machão fio 20 CInza antibes
        "pai": "BRV265500102",
        "tamanhos": TAMANHOS_PADRAO,
        "derivados": [
           
        ]
    },

    {   #Regata Machão fio 20 Preto marmorizado
        "pai": "BRV26550345",
        "tamanhos": TAMANHOS_PADRAO,
        "derivados": [
           "2004"
        ]
    },

    {   #Regata Machão fio 20 Marinho marmorizado
        "pai": "BRV26550345",
        "tamanhos": TAMANHOS_PADRAO,
        "derivados": [
           "1415"
        ]
    },

    {   #Regata Machão fio 30 OFF
        "pai": "1602009003",
        "tamanhos": TAMANHOS_PADRAO,
        "derivados": [
           "4512"
        ]
    },

     {   #Regata Machão fio 30 Branco
        "pai": "1602009002",
        "tamanhos": TAMANHOS_PADRAO,
        "derivados": [
           "1282"
        ]
    },


]

def gerar_sku_derivado(
    derivado,
    tamanho
):
    return f"{derivado}-{tamanho}"

RELACOES = {}

for produto in PRODUTOS:

    sku_pai = produto["pai"]

    derivados = produto["derivados"]

    tamanhos = produto["tamanhos"]

    if not derivados:
        continue

    for tamanho in tamanhos:

        chave = f"{sku_pai}{tamanho}"

        lista_derivados = []

        for derivado in derivados:

            lista_derivados.append(
                gerar_sku_derivado(
                    derivado,
                    tamanho
                )
            )

        RELACOES[chave] = {
            "estoque_seguranca": 0,
            "derivados": lista_derivados
        }