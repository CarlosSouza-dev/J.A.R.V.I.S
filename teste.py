import google.generativeai as genai

# Cole a sua chave aqui dentro
CHAVE_API = "AIzaSyBz6y5v89c2mohs--183ps1GxgAAcwzDhw"
genai.configure(api_key=CHAVE_API)

print("Procurando cérebros disponíveis nos servidores do Google...\n")

try:
    for m in genai.list_models():
        # Filtra apenas os modelos que conseguem gerar texto (pensar)
        if 'generateContent' in m.supported_generation_methods:
            print(f"Modelo compatível encontrado: {m.name}")
except Exception as e:
    print(f"Erro ao conectar com o Google: {e}")