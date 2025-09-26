from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Permitir solicitudes desde tu blog
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://faunaauxiliar.blogspot.com"],  # o ["*"] para todos
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de mensaje
class Message(BaseModel):
    message: str

@app.post("/")
async def chat(msg: Message):
    # Aquí puedes integrar OpenAI o lógica de tu chatbot
    user_msg = msg.message
    bot_msg = f"Recibido: {user_msg}"  # ejemplo simple
    return {"message": bot_msg}
