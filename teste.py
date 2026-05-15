# Dentro do loop de conversa ativa no main.py:

            if "anote" in comando_continuo or "salve no obsidian" in comando_continuo:
                falar("Qual deve ser o título da nota, senhor?")
                titulo_nota = ouvir()
                
                if titulo_nota:
                    # Pedimos para a IA formatar o que foi conversado antes de salvar
                    prompt_resumo = f"Resuma os pontos principais da nossa última explicação sobre {titulo_nota} em formato de lista (markdown)."
                    conteudo_para_salvar = pensar(prompt_resumo)
                    
                    import memoria
                    status = memoria.salvar_nota(titulo_nota, conteudo_para_salvar)
                    falar(status)