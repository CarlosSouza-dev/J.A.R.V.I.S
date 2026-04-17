import speech_recognition as sr
import torch
from TTS.api import TTS
import os
import pygame
import time

pygame.mixer.init()

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[*] Iniciando motor de voz usando: {device.upper()}")

print("[*] Carregando a IA do XTTSv2. Isso pode demorar alguns segundos...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print("[*] IA carregada com sucesso!\n")

def falar(texto):
    print(f"J.A.R.V.I.S: {texto}")
    saida = "resposta_jarvis.wav"
    amostra_voz = "def2.wav"

    txt_clean = texto.replace(".", "")
    txt_clean = txt_clean + " "

    try:
        tts.tts_to_file(
            text=txt_clean,
            speaker_wav=amostra_voz,
            language="pt",
            file_path=saida
        )
        pygame.mixer.music.load(saida)
        pygame.mixer.music.play()
        
        # Espera a música terminar
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        time.sleep(0.3)
        pygame.mixer.music.unload()

    except Exception as e:
        print(f"Erro na clonagem de voz: {e}")

def ouvir():
    reconhecedor = sr.Recognizer()

    reconhecedor.pause_threshold = 0.5
    reconhecedor.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=0.5)
        print("\nOuvindo...")

        try:
            audio = reconhecedor.listen(source, timeout= 5, phrase_time_limit = 5)
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