import speech_recognition as sr
import pyttsx3

# Inicializa o motor de voz
engine = pyttsx3.init()

def falar(texto):
    """ Faz o computador falar o texto passado """
    print(f"J.A.R.V.I.S.: {texto}")
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    """ Escuta o microfone e retorna a string do que foi dito """
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        print("Ouvindo...")
        audio = reconhecedor.listen(source)

    try:
        texto = reconhecedor.recognize_google(audio, language='pt-BR')
        return texto.lower()
    except:
        return ""

# --- LOOP PRINCIPAL ---
falar("Sistemas iniciados. Como posso ajudar, senhor?")

while True:
    comando = ouvir()
    
    if comando:
        print(f"Você disse: {comando}")
        
        if "sair" in comando or "desligar" in comando:
            falar("Desligando sistemas. Até logo, senhor.")
            break
            
        elif "quem é você" in comando:
            falar("Eu sou o Jarvis, seu assistente virtual em Python.")
            
        elif "horas" in comando:
            # Exemplo de lógica simples
            from datetime import datetime
            agora = datetime.now().strftime('%H:%M')
            falar(f"Agora são {agora}")
        
        else:
            falar("Comando não reconhecido, mas estou processando.")