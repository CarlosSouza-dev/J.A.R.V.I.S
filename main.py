from habilidades import falar, ouvir
from datetime import datetime

falar("Sistemas Iniciados. Como posso ajudar, senhor?")
while True:
    comando = ouvir()
    if comando:
        print(f"Você disse: {comando}")

        if "sair" in comando or "desligar" in comando:
            falar("Desligando Sistemas, Até logo, senhor.")
            break
        elif "quem é você" in comando:
            falar("Eu sou Jarvis, a Inteligência Suprema.")

        elif "que horas são" in comando:
            agora = datetime.now().strftime('%H:%M')
            falar(f"Agora são {agora}")
        else:
            falar("Comando Desconhecido")