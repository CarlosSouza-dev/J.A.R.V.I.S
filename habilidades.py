import speech_recognition as sr
import pyttsx3

def falar(texto):
    print(f"J.A.R.V.I.S: {texto}")
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    engine.stop()

def ouvir():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration = 1)
        print("Ouvindo...")
        audio = reconhecedor.listen(source, timeout=5, phrase_time_limit=5)

    try:
        texto = reconhecedor.recognize_google(audio, language = 'pt-BR')
        return texto.lower()
    except:
        return ""