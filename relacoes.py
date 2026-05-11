TAMANHOS = [
    "PP",
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

CASUAIS = [
    "16030040001",
    "16030040002",
    "16030040003"
]

TAMANHOS_GRANDES = [
    "G3",
    "G4",
    "G5",
    "G6"
]

PRODUTOS = [
    {   #casual preta
        "pai": "16030040001",
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
        "derivados": [
            "1482",
            "1474",
            "1478", 
            "2001-OFF"          

        ]
    },

    {   #casual branca
        "pai": "16030040002",
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
        "derivados": [
            "2005"
        ]
    },

    {   #moletom preto
        "pai": "16090010001",
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
        "derivados": [
            "2015",
            "2014",
            "1447"
        ]
    },

    {   #baby look off
        "pai": "BRV26230003",
        "derivados": [
            "2007",
            "1446"
        ]
    },

    {   #baby look rosa
        "pai": "BRV26230007",
        "derivados": [
            
        ]
    },

]

RELACOES = {}

for produto in PRODUTOS:

    sku_pai = produto["pai"]

    derivados = produto["derivados"]

    for tamanho in TAMANHOS:

        if (
            sku_pai not in CASUAIS
            and tamanho in TAMANHOS_GRANDES
        ):
            continue

        chave = f"{sku_pai}{tamanho}"

        lista_derivados = []

        for derivado in derivados:

            lista_derivados.append(
                f"{derivado}-{tamanho}"
            )

        RELACOES[chave] = {
            "estoque_seguranca": 0,
            "derivados": lista_derivados
        }