from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama
# import sistema  # Descomente caso suas funções da Ekaza estejam no arquivo sistema.py

app = Flask(__name__)
CORS(app) # Libera o acesso do tablet

def processar_ia(mensagem_usuario):
    """ Envia o comando para o Llama 3.2 processar localmente na RTX 4070 """
    prompt_sistema = (
        "Você é o Jarvis. Responda de forma educada e curta. "
        "Se o usuário pedir para ligar ou apagar as luzes, responda EXATAMENTE "
        "com as palavras: COMANDO_LUZ_LIGAR ou COMANDO_LUZ_DESLIGAR."
    )
    
    try:
        resposta = ollama.chat(
            model='llama3.2', 
            messages=[
                {'role': 'system', 'content': prompt_sistema},
                {'role': 'user', 'content': mensagem_usuario}
            ],
            options={
                'num_ctx': 2048  # Mantém a memória de curto prazo otimizada
            }
        )
        return resposta['message']['content']
    except Exception as e:
        return f"Erro nos circuitos locais: {e}"

def acionar_ekaza(acao):
    """ Lógica para interagir com o interruptor inteligente """
    if acao == "LIGAR":
        # sistema.controlar_luz("ligar")
        return "Luzes ligadas, senhor."
    elif acao == "DESLIGAR":
        # sistema.controlar_luz("desligar")
        return "Luzes apagadas. Entrando em modo noturno."
    return "Comando não reconhecido."

@app.route('/comando', methods=['POST'])
def processar_comando():
    dados = request.get_json()
    mensagem = dados.get("mensagem", "")
    
    # 1. Aciona o Cérebro Local
    resposta_ia = processar_ia(mensagem)
    
    # 2. Verifica gatilhos de hardware (Ekaza)
    if "COMANDO_LUZ_LIGAR" in resposta_ia:
        resposta_texto = acionar_ekaza("LIGAR")
    elif "COMANDO_LUZ_DESLIGAR" in resposta_ia:
        resposta_texto = acionar_ekaza("DESLIGAR")
    else:
        # Se não for comando de luz, devolve a resposta falada da IA
        resposta_texto = resposta_ia

    return jsonify({"resposta": resposta_texto})

if __name__ == '__main__':
    # Expõe a porta 5000 para a rede Wi-Fi local
    app.run(host='0.0.0.0', port=5000, debug=True)