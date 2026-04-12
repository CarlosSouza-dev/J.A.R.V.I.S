import speech_recognition as sr
import torch
from TTS.api import TTS
import winsound  # Biblioteca nativa do Windows para tocar arquivos .wav
import os

# -------------------------------------------------------------------
# CONFIGURAÇÃO DA IA DE VOZ (O "Cérebro" de áudio)
# -------------------------------------------------------------------

# Verifica se a RTX 4070 está ativa e pronta para uso
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[*] Iniciando Motor de Voz usando: {device.upper()}")

print("[*] Carregando a IA do XTTSv2. Isso pode demorar uns segundos...")
# Carrega o modelo de voz da Coqui TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print("[*] IA de Voz carregada com sucesso!\n")

# -------------------------------------------------------------------
# FUNÇÕES DE AÇÃO
# -------------------------------------------------------------------

def falar(texto):
    """ Clona a voz e fala o texto passado """
    print(f"J.A.R.V.I.S.: {texto}")
    
    arquivo_saida = "resposta_jarvis.wav"
    amostra_voz = "jarvis_sample.mp3" # <-- O nome do seu arquivo de 9 seg
    
    try:
        # A IA gera o áudio clonado com base no texto e na amostra
        tts.tts_to_file(
            text=texto, 
            speaker_wav=amostra_voz, 
            language="pt", # "pt" para Português, "en" para Inglês
            file_path=arquivo_saida
        )
        
        # Toca o áudio gerado
        winsound.PlaySound(arquivo_saida, winsound.SND_FILENAME)
        
    except Exception as e:
        print(f"Erro na clonagem de voz: {e}")

def ouvir():
    """ Escuta o microfone e retorna a string do que foi dito """
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        print("\nOuvindo...")
        
        try:
            # Espera até 5 seg para você falar, e grava até 5 seg de fala
            audio = reconhecedor.listen(source, timeout=5, phrase_time_limit=5)
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