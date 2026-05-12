import time
from datetime import datetime

from sincronizar import sincronizar_estoques

print(datetime.now() + ' - Sincronização iniciada')

while True:

    log = False

    try:

        agora = datetime.now()
        hora = agora.hour

        sincronizar_estoques(log)

        # Madrugada
        if 0 <= hora <= 6:
            intervalo = 1800  # 30 minutos

        else:

            intervalo = 600  # 10 minutos
       

        time.sleep(intervalo)

    except Exception as e:

        print(f"Erro: {e}")

        time.sleep(600)
    
    except KeyboardInterrupt:

        print(f"Programa finalizado")
        break
        