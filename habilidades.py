import speech_recognition as sr  
import torch
from TTS.api import TTS
import pygame
import time
import pyautogui
import ollama
import tinytuya
import os

from dotenv import load_dotenv
load_dotenv()

pygame.mixer.init()
pyautogui.PAUSE = 1.0
#--------------------------------------------------------------------------
# CÉREBRO JARVIS

def pensar(comando_usuario):
    print("Jarvis está pensando (Llama 3.2)...")
    try:
        # O prompt precisa ser muito claro sobre o idioma, senão ele responde em inglês!
        prompt = """Você é o J.A.R.V.I.S., o sistema de inteligência artificial do Tony Stark.
        Regras:
        1. Seja educado, um pouco formal e bem sarcástico (estilo britânico). Mas sem deixar de ser divertido
        2. Chame o usuário de "Senhor".
        3. Suas respostas DEVEM ser curtas e diretas, feitas para serem lidas em voz alta.
        4. Responda toda e qualquer pergunta que seu usuário fizer.
        """
        
        resposta = ollama.chat(model='llama3.2', messages=[
            {'role': 'system', 'content': prompt},
            {'role': 'user', 'content': comando_usuario}
        ])
        
        texto_limpo = resposta['message']['content'].replace("*", "").replace("\"", "")
        return texto_limpo
        
    except Exception as e:
        print(f"Erro no cérebro local: {e}")
        return "Desculpe senhor, meus circuitos lógicos locais estão sobrecarregados."
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# CARREGANDO IA DE FALA

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[*] Iniciando motor de voz usando: {device.upper()}")

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print("[*] IA carregada com sucesso!\n")

# Voz do Jarvis
def falar(texto):
    print(f"J.A.R.V.I.S: {texto}")
    saida = "resposta_jarvis.wav"
    amostra_voz = "def1def.wav"

    txt_clean = texto.replace(".", "") + " "

    try:
        tts.tts_to_file(
            text=txt_clean,
            speaker_wav=amostra_voz,
            language="pt",
            file_path=saida
        )

        r_int = sr.Recognizer()
        mic_int = sr.Microphone()

        def detectar_int(rec, audio):
            try:
                comando_corte = rec.recognize_google(audio, language='pt-BR').lower()
                if "jarvis" in comando_corte or "parar" in comando_corte or "pare" in comando_corte:
                    print("\nINTERRUPÇÃO DETECTADA! Cortando o áudio e esperando novos comandos.")
                    pygame.mixer.music.stop()
            except:
                pass
        
        with mic_int as source:
            r_int.adjust_for_ambient_noise(source, duration=0.2)
        
        parar_escuta_background = r_int.listen_in_background(mic_int, detectar_int)

        pygame.mixer.music.load(saida)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)        
        time.sleep(0.3)
        pygame.mixer.music.unload()

        parar_escuta_background(wait_for_stop=False)

    except Exception as e:
        print(f"Erro na clonagem de voz: {e}")
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# OUVIDOS DO JARVIS

def ouvir():
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=0.5)
        print("\nOuvindo...")

        try:
            audio = reconhecedor.listen(source, timeout= 5, phrase_time_limit = 10)
            print("Processando áudio...")

            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            print(f"Entendido: '{texto}'")
            return texto.lower()

        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            print(f"Erro no microfone: {e}")
            return ""
#--------------------------------------------------------------------------

def navegador():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    pyautogui.hotkey("win", "up")


def spotify():
    pyautogui.press("win")
    pyautogui.write("spotify")
    pyautogui.press("enter")

def instagram():
    pyautogui.press("win")
    pyautogui.write("instagram")
    pyautogui.press("enter")

def vscode():
    pyautogui.press("win")
    pyautogui.write("vscode")
    pyautogui.press("enter")
    pyautogui.hotkey("win", "up")

def whatsapp():
    pyautogui.press("win")
    pyautogui.write("whatsapp")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.hotkey("win", "up")

def netflix():
    pyautogui.press("win")
    pyautogui.write("netflix")
    pyautogui.press("enter")

def whiteboard():
    pyautogui.press("win")
    pyautogui.write("whiteboard")
    pyautogui.press("enter")
    pyautogui.hotkey("win", "up")
    
def desligar():
    falar("desligando tudo, chefia.")
    os.system("shutdown /s /t 0")

DEVICE_ID = os.getenv("EKAZA_ID")
DEVICE_IP = os.getenv("EKAZA_IP")
LOCAL_KEY = os.getenv("EKAZA_KEY")

def controlar_luz(comando):
    try:
        luz = tinytuya.OutletDevice(DEVICE_ID, DEVICE_IP, LOCAL_KEY)
        luz.set_version(3.3)

        if "ligar" in comando or "acender" in comando:
            luz.turn_on()
            return "Luzes ligadas, senhor."
        
        elif "apagar" in comando or "desligar" in comando:
            luz.turn_off()
            return "Luzes apagadas, senhor."
        
        else:
            return "Desculpe ,devo apagar ou ligar as luzes?"
    
    except Exception as e:
        print(f"[ERRO EKAZA]: {e}")
        return "Senhor, perdi a conexão com a rede elétrica do quarto."