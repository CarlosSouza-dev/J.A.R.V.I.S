import speech_recognition as sr
import torch
from TTS.api import TTS
import pygame
import os
import time # <-- Nova biblioteca para consertar o engasgo

# Inicializa o motor de áudio
pygame.mixer.init()

# Carrega a IA (Seu "Reator Arc")
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[*] Iniciando Motor de Voz usando: {device.upper()}")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print("[*] IA carregada com sucesso!\n")

def falar(texto):
    """ Clona a voz, limpa o texto e toca sem engasgos """
    print(f"J.A.R.V.I.S.: {texto}")
    
    saida = "resposta_jarvis.wav"
    amostra_voz = "2.wav" 
    
    # [Filtro Sanitário]: Remove o ponto final para a IA não ler em voz alta
    texto_limpo = texto.replace(".", "")
    # Opcional: Adiciona um espaço extra no final para ajudar a IA a terminar suavemente
    texto_limpo = texto_limpo + " "
    
    try:
        # Gera o áudio usando o texto limpo
        tts.tts_to_file(
            text=texto_limpo, 
            speaker_wav=amostra_voz, 
            language="pt",
            file_path=saida
        )
        
        # Toca o áudio
        pygame.mixer.music.load(saida)
        pygame.mixer.music.play()
        
        # Espera a música terminar
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        # O ANTÍDOTO DO ENGASGO: Espera um pouquinho a mais antes de desligar
        time.sleep(0.3) 
        pygame.mixer.music.unload()
        
    except Exception as e:
        print(f"Erro na voz: {e}")

def ouvir():
    """ Escuta o microfone de forma rápida e adaptável """
    reconhecedor = sr.Recognizer()
    
    # Ajustes finos de ouvido
    reconhecedor.pause_threshold = 0.5 # Para de ouvir mais rápido quando você pausa
    reconhecedor.dynamic_energy_threshold = True # Adapta ao barulho do seu quarto
    
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=0.5) # Calibragem mais rápida (meio segundo)
        print("\nOuvindo...")
        
        try:
            audio = reconhecedor.listen(source, timeout=5, phrase_time_limit=5)
            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            return texto.lower()
            
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            return ""