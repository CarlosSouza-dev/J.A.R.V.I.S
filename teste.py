import tinytuya

# ---------------------------------------------------------
# CONFIGURAÇÃO DO INTERRUPTOR EKAZA (TUYA)
# Você precisará preencher estes 3 dados depois!
# ---------------------------------------------------------
ID_DISPOSITIVO = "SEU_DEVICE_ID_AQUI"
IP_DISPOSITIVO = "192.168.X.X"
LOCAL_KEY = "SUA_LOCAL_KEY_AQUI"

def controlar_luz(comando):
    """ Conecta no interruptor Ekaza pela rede Wi-Fi local e muda o estado """
    try:
        # Cria a conexão com o interruptor
        luz = tinytuya.OutletDevice(ID_DISPOSITIVO, IP_DISPOSITIVO, LOCAL_KEY)
        luz.set_version(3.3) # Versão padrão da maioria dos dispositivos Ekaza
        
        if "ligar" in comando or "acender" in comando:
            luz.turn_on()
            return "Luzes ligadas, senhor."
            
        elif "desligar" in comando or "apagar" in comando:
            luz.turn_off()
            return "Luzes desligadas. Entrando em modo noturno."
            
        else:
            return "Desculpe, devo ligar ou desligar as luzes?"
            
    except Exception as e:
        print(f"[ERRO EKAZA]: {e}")
        return "Senhor, perdi a conexão com a rede elétrica do quarto."