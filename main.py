from habilidades import falar, ouvir, navegador, spotify, pensar, instagram

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

            if "descansar" in comando_def or "standby" in comando_def:
                falar("Sistemas em Standby, chame se precisar, senhor.")
                break
            
            if "sair" in comando_def or "desligar" in comando_def:
                falar("Desligando Sistemas, Até logo, senhor.")
                exit()

            elif "navegador" in comando_def:
                navegador()
            
            elif "spotify" in comando_def:
                spotify()
            
            elif "instagram" in comando_def:
                instagram()
            
            resp_jarvis = pensar(comando_def)
            falar(resp_jarvis)
            