from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Permitir tu blog como origen
origins = [
    "https://faunaauxiliar.blogspot.com",
    "https://www.faunaauxiliar.blogspot.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # Aquí debes conectar con tu modelo/chatbot
    user_message = request.message

    # Respuesta de prueba
    reply = f"Recibí tu mensaje: {user_message}"
    return {"reply": reply}
