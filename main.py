from habilidades import falar, ouvir, navegador, spotify, pensar, instagram, vscode, whatsapp, controlar_luz

CHAVE_ATIVACAO = ["jarvis", "jarafus", "garvest", "járvis", "jar", "chaves"]
falar(f"Sistemas em Standby, diga 'Jarvis' para a ativação.")

while True:
    trigger = ouvir()
    if any(palavra in trigger for palavra in CHAVE_ATIVACAO):
        falar("Como posso ajudar, senhor?")

        while True:
            comando_def = ouvir()
                
            if not comando_def:
                falar("Sistemas em Standby, chame se precisar, senhor.")
                break

            elif "descansar" in comando_def or "standby" in comando_def:
                falar("Sistemas em Standby, chame se precisar, senhor.")
                break
            
            elif "sair" in comando_def or "desligar" in comando_def:
                falar("Desligando Sistemas, Até logo, senhor.")
                exit()

            elif "navegador" in comando_def:
                navegador()
            
            elif "spotify" in comando_def:
                spotify()
            
            elif "instagram" in comando_def:
                instagram()
            
            elif "vscode" in comando_def:
                vscode()
            
            elif "whatsapp" in comando_def:
                whatsapp()
            
            elif "delta" in comando_def:
                falar("executando protocolo Delta, bons estudos, senhor.")
                navegador()
                spotify()
                whatsapp()
            
            elif "delta dois" in comando_def or "delta 2" in comando_def:
                falar("executando protocolo Delta 2, bons estudos, senhor.")
                navegador()
                spotify()
                whatsapp()
                vscode()
            
            elif "luz" in comando_def or "luzes" in comando_def:
                resposta = controlar_luz(comando_def)
                falar(resposta)
            
            else:
                resp_jarvis = pensar(comando_def)
                falar(resp_jarvis)
            