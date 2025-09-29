from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Inicialización de la app
app = Flask(__name__)
CORS(app)  # Permitir CORS desde cualquier origen

# Configura tu API Key de OpenAI
openai.api_key = "TU_API_KEY_AQUI"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "No se proporcionó un prompt"}), 400

        # Llamada a la API de OpenAI
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )

        return jsonify({"response": response.choices[0].text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return jsonify({"message": "API funcionando correctamente"})

if __name__ == "__main__":
    # Para desarrollo local
    app.run(host="0.0.0.0", port=5000, debug=True)
