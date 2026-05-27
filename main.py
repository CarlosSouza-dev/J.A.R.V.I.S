import customtkinter as ctk
import threading
from habilidades import falar, ouvir, navegador, spotify, pensar, instagram, vscode, whatsapp, desligar, whiteboard, netflix
import memoria 

# Configuração visual do aplicativo
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class JarvisApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("J.A.R.V.I.S. - Painel Neural")
        self.geometry("400x450")
        self.resizable(False, False)

        # Variável de controle (Interruptor principal)
        self.jarvis_ativo = False 

        # --- DESIGN DA INTERFACE ---
        self.label_titulo = ctk.CTkLabel(self, text="J.A.R.V.I.S. CORE", font=("Segoe UI", 24, "bold"))
        self.label_titulo.pack(pady=30)

        # O "Botão Neural"
        self.botao_neural = ctk.CTkButton(
            self,
            text="STANDBY",
            font=("Segoe UI", 20, "bold"),
            width=200,
            height=200,
            corner_radius=100,
            fg_color="#1f538d", # Azul
            hover_color="#14375e",
            command=self.alternar_jarvis
        )
        self.botao_neural.pack(pady=20)

        self.label_status = ctk.CTkLabel(self, text="Sistemas em repouso.", font=("Segoe UI", 14))
        self.label_status.pack(pady=10)
        
        # Boas-vindas silenciosas do sistema (apenas visual)
        print("[*] J.A.R.V.I.S. Iniciado em modo Standby visual.")

    # --- LÓGICA DE CONTROLE DE TELA ---
    def atualizar_tela(self, texto_botao, cor_botao, texto_status):
        self.botao_neural.configure(text=texto_botao, fg_color=cor_botao)
        self.label_status.configure(text=texto_status)

    def alternar_jarvis(self):
        """ É acionado quando você clica no círculo central """
        if not self.jarvis_ativo:
            self.jarvis_ativo = True
            self.atualizar_tela("OUVINDO...", "#c93434", "Microfone aberto. Pode falar.") # Vermelho
            
            # Roda o seu loop personalizado em segundo plano
            threading.Thread(target=self.loop_cerebro, daemon=True).start()
        else:
            self.jarvis_ativo = False
            self.atualizar_tela("STANDBY", "#1f538d", "Sistemas em repouso.") # Azul

    # --- O SEU CÉREBRO PERSONALIZADO ---
    def loop_cerebro(self):
        # Substitui o trigger antigo. Ao clicar, ele já se apresenta.
        falar("Como posso ajudar, senhor?")

        while self.jarvis_ativo:
            comando_def = ouvir()

            # Verificação de segurança caso o botão tenha sido desligado no meio do processo
            if not self.jarvis_ativo:
                break

            # 1. Silêncio detectado (Timeout)
            if not comando_def:
                self.after(0, self.atualizar_tela, "STANDBY", "#1f538d", "Sistemas em repouso.")
                falar("Sistemas em Standby, chame se precisar, senhor.")
                self.jarvis_ativo = False
                break
            
            # 2. Integração com Obsidian
            elif "anote" in comando_def or "salve no bloco" in comando_def:
                self.after(0, self.atualizar_tela, "PENSANDO...", "#e3a822", "Preparando anotação...")
                falar("Qual deve ser o título da nota, senhor?")
                
                self.after(0, self.atualizar_tela, "OUVINDO...", "#c93434", "Aguardando título...")
                titulo_nota = ouvir()

                if titulo_nota:
                    self.after(0, self.atualizar_tela, "PENSANDO...", "#e3a822", "Llama gerando resumo...")
                    prompt_resumo = f"Resuma os pontos principais da nossa última explicação sobre {titulo_nota} em formato de lista (markdown)."
                    conteudo_para_salvar = pensar(prompt_resumo)
                    
                    status = memoria.salvar_nota(titulo_nota, conteudo_para_salvar)
                    
                    self.after(0, self.atualizar_tela, "FALANDO...", "#28a745", "Acessando o cofre...")
                    falar(status)

            # 3. Comandos de Repouso
            elif "descansar" in comando_def or "standby" in comando_def:
                self.after(0, self.atualizar_tela, "STANDBY", "#1f538d", "Sistemas em repouso.")
                falar("Sistemas em Standby, chame se precisar, senhor.")
                self.jarvis_ativo = False
                break
            
            # 4. Desligar o programa todo
            elif "sair" in comando_def or "desligar" in comando_def:
                falar("Desligando Sistemas. Até logo, senhor.")
                self.after(0, self.destroy) # Fecha a janela do CustomTkinter de forma limpa
                break

            # 5. Aplicativos Soltos
            elif "navegador" in comando_def:
                self.after(0, self.atualizar_tela, "EXECUTANDO", "#8a2be2", "Abrindo Navegador...")
                navegador()
            
            elif "spotify" in comando_def:
                self.after(0, self.atualizar_tela, "EXECUTANDO", "#1db954", "Abrindo Spotify...")
                spotify()
            
            elif "instagram" in comando_def:
                self.after(0, self.atualizar_tela, "EXECUTANDO", "#e1306c", "Abrindo Instagram...")
                instagram()
            
            elif "netflix" in comando_def:
                self.after(0, self.atualizar_tela, "EXECUTANDO", "#e1306c", "Abrindo NETFLIX...")
                netflix()
            
            elif "editor" in comando_def:
                self.after(0, self.atualizar_tela, "EXECUTANDO", "#007acc", "Abrindo VS Code...")
                vscode()
            
            elif "whatsapp" in comando_def:
                self.after(0, self.atualizar_tela, "EXECUTANDO", "#25d366", "Abrindo WhatsApp...")
                whatsapp()
            
            # 6. Protocolos Multi-Tarefas
            elif "delta" in comando_def:
                self.after(0, self.atualizar_tela, "EXECUTANDO", "#8a2be2", "Protocolo Delta Ativo")
                falar("Executando protocolo Delta. Bons estudos, senhor.")
                whiteboard()
                spotify()
                navegador()
                whatsapp()
            
            elif "ômega" in comando_def:
                self.after(0, self.atualizar_tela, "EXECUTANDO", "#8a2be2", "Protocolo Ômega Ativo")
                falar("Executando protocolo ômega. Bons estudos, senhor.")
                navegador()
                spotify()
                whatsapp()
                vscode()
            
            elif "boa noite" in comando_def:
                desligar()
            
            # 7. Resposta inteligente (IA Local)
            else:
                self.after(0, self.atualizar_tela, "PENSANDO...", "#e3a822", "Llama 3.2 processando...")
                resp_jarvis = pensar(comando_def)
                
                if self.jarvis_ativo:
                    self.after(0, self.atualizar_tela, "FALANDO...", "#28a745", "Simulação de voz ativa.")
                    falar(resp_jarvis)

            # 8. Retorno do loop para ouvir o próximo comando
            if self.jarvis_ativo:
                self.after(0, self.atualizar_tela, "OUVINDO...", "#c93434", "Microfone aberto. Aguardando comando.")

if __name__ == "__main__":
    app = JarvisApp()
    app.mainloop()