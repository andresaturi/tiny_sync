import time
from datetime import datetime

from sincronizar import sincronizar_estoques


while True:

    print('Sincronização iniciada')
    
    try:

        agora = datetime.now()
        hora = agora.hour

        sincronizar_estoques()

        # Madrugada
        if 0 <= hora <= 6:
            intervalo = 1800  # 30 minutos

        else:

            intervalo = 600  # 10 minutos
       

        time.sleep(intervalo)

    except Exception as e:

        print(f"Erro: {e}")

        time.sleep(600)