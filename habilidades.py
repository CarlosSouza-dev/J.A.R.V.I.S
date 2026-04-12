import speech_recognition as sr
import torch
from TTS.api import TTS
import winsound
import os

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[*] Iniciando motor de voz usando: {device.upper()}")

print("[*] Carregando a IA do XTTSv2. Isso pode demorar alguns segundos...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print("[*] IA carregada com sucesso!\n")

def falar(texto):
    print(f"J.A.R.V.I.S: {texto}")
    saida = "resposta_jarvis.wav"
    amostra_voz = "2.wav"

    try:
        tts.tts_to_file(
            text=texto,
            speaker_wav=amostra_voz,
            language="pt",
            file_path=saida
        )
    except Exception as e:
        print(f"Erro na clonagem de voz: {e}")

def ouvir():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=0.5)
        print("\nOuvindo...")

        try:
            audio = reconhecedor.listen(source, timeout=5)
            print("Processando áudio...")
            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            return texto.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            print(f"Erro no microfone: {e}")
            return ""