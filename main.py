from habilidades import falar, ouvir, navegador, spotify, pensar, instagram, vscode, whatsapp ,desligar, whiteboard

import memoria 

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
            
            elif "anote" in comando_def or "salve no bloco" in comando_def:
                falar("Qual deve ser o título da nota, senhor?")
                titulo_nota = ouvir()

                if titulo_nota:
                    prompt_resumo = f"Resuma os pontos principais da nossa última explicação sobre {titulo_nota} em formato de lista (markdown)."
                    conteudo_para_salvar = pensar(prompt_resumo)
                    
                    status = memoria.salvar_nota(titulo_nota, conteudo_para_salvar)
                    falar(status)

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
            
            elif "editor" in comando_def:
                vscode()
            
            elif "whatsapp" in comando_def:
                whatsapp()
            
            elif "delta" in comando_def:
                falar("executando protocolo Delta, bons estudos, senhor.")
                whiteboard()
                spotify()
                navegador()
                whatsapp()
            
            elif "ômega" in comando_def:
                falar("executando protocolo ômega, bons estudos, senhor.")
                navegador()
                spotify()
                whatsapp()
                vscode()
            
            elif "boa noite" in comando_def:
                desligar()
            
            else:
                resp_jarvis = pensar(comando_def)
                falar(resp_jarvis)
            