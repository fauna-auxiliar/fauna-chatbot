from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Permitir que el frontend (tu HTML) haga requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por tu dominio si quieres más seguridad
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat_endpoint(message: Message):
    user_text = message.text
    # Aquí va la lógica de tu chatbot, ahora simplemente devuelve el texto
    response_text = f"Respuesta del bot: {user_text}"
    return {"reply": response_text}
