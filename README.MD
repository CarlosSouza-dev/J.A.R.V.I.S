# J.A.R.V.I.S. Core 🧠⚡

Um assistente virtual local de altíssimo desempenho, construído em Python. Projetado para rodar 100% offline garantindo privacidade absoluta e baixa latência. Integrado com hardware IoT (EM DESENVOLVIMENTO: 'servidor_jarvis.py'), memória de longo prazo (Obsidian) e automação de sistema operacional.

## 🚀 Recursos Principais

* **Cérebro LLM Local:** Processamento de linguagem natural utilizando **Llama 3.2** via Ollama, otimizado para placas de vídeo RTX (com controle rigoroso de contexto de memória).
* **Motor de Voz Assíncrono (Barge-in):** Sintetização de voz realista via XTTSv2 com arquitetura *multithreading*, permitindo interromper o assistente a qualquer momento pela palavra de ativação.
* **Interface (GUI):** Painel de controle moderno em Modo Escuro construído com CustomTkinter, operando em threads isoladas para evitar travamento visual do aplicativo.
* **Integração IoT (Ekaza/Tuya):** Controle direto de lâmpadas e interruptores inteligentes pela rede local (sem dependência de nuvem) usando `tinytuya`.
* **Hipocampo Digital:** Módulo nativo de memória de longo prazo que resume conversas e salva anotações formatadas diretamente em cofres do **Obsidian** via Markdown.
* **Protocolos de Produtividade:** Gatilhos de automação (PyAutoGUI) que preparam o ambiente de trabalho e estudos, inicializando e gerenciando instâncias do VS Code, Spotify e WhatsApp (Protocolos Alfa e Delta).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **IA & LLM:** Ollama (Llama 3.2 3B), PyTorch
* **Áudio & TTS:** SpeechRecognition, TTS (Coqui), Pygame
* **Interface:** CustomTkinter
* **Automação e Rede:** Tinytuya, PyAutoGUI, Dotenv

## ⚙️ Pré-requisitos

Antes de clonar o projeto, certifique-se de ter instalado em sua máquina:

1. **Python 3.10** ou superior.
2. **Ollama:** Faça o download do motor em [ollama.com](https://ollama.com/).
3. **Modelo Llama 3.2:** Abra o terminal do seu sistema operacional e execute:
   ```bash
   ollama pull llama3.2
   ```

## 📥 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/jarvis-core.git
   cd jarvis-core
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## 🔐 Configuração de Ambiente

Este projeto requer credenciais locais para gerenciar sua casa inteligente e salvar anotações. 

1. Na raiz do projeto, duplique o arquivo `.env.example` e renomeie a cópia para `.env`.
2. Preencha as variáveis de ambiente com os dados da sua rede e sistema:

   ```env
   DEVICE_ID=seu_device_id_ekaza
   DEVICE_IP=ip_local_do_interruptor
   LOCAL_KEY=sua_local_key
   CAMINHO_VAULT=C:\Caminho\Para\Seu\Obsidian
   ```

> **Aviso de Segurança:** Nunca faça o commit do seu arquivo `.env`. O projeto possui um `.gitignore` configurado para impedir o upload acidental de credenciais e dados pessoais.

## 🕹️ Como Usar

Para iniciar o J.A.R.V.I.S., você pode executar o script principal no terminal ou utilizar o arquivo em lote:

**Via Terminal:**
```bash
python main.py
```

**Via Atalho (Windows):**
Basta dar um duplo clique no arquivo `iniciar_jarvis.bat`.

Ao abrir o painel neural, clique no botão central **"STANDBY"** para iniciar a escuta ativa. O anel visual informará os status de processamento local, escuta do microfone e simulação de voz em tempo real.
