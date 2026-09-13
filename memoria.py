import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

CAMINHO_VAULT = os.getenv("CAMINHO_VAULT")

def salvar_nota(titulo, content, pasta="Jarvis"):
    caminho_pasta = os.path.join(CAMINHO_VAULT, pasta)

    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    caminho_arq = os.path.join(caminho_pasta, f"{titulo}.md")
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    try:
        with open(caminho_arq, "a", encoding="utf-8") as f:
            f.write(f"\n\n## Entrada em {agora}\n")
            f.write(content)
        return f"nota '{titulo}' atualizada no seu obsidian com sucesso, senhor."
    except Exception as e:
        print(f"Erro de memória: {e}")
        return "Não consegui acessar o banco de dados do Obsidian."