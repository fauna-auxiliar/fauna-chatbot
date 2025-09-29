from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

# Inicializa FastAPI
app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por la URL de tu frontend si quieres restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura tu API key (debe estar en las variables de entorno de Render)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Modelo de datos para la request
class ChatRequest(BaseModel):
    message: str

# Endpoint /chat
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message

    try:
        # Llamada a la API de OpenAI (nueva sintaxis >=1.0.0)
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # usa este mejor que "gpt-4", es más barato y rápido
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error con OpenAI: {str(e)}")

    return {"reply": reply}

# Endpoint de prueba raíz
@app.get("/")
async def root():
    return {"message": "API funcionando correctamente!"}
