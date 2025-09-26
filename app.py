# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

# Configura tu API Key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Permitir solicitudes desde tu blog
origins = [
    "https://faunaauxiliar.blogspot.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos para recibir mensajes
class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "Chatbot activo"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message

    try:
        # Llamada a OpenAI GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error al generar respuesta: {str(e)}"

    return {"reply": reply}
