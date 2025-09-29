from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

# Inicializa FastAPI
app = FastAPI()

# Configura CORS para que tu blog pueda llamar a la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar "*" por la URL de tu blog
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Modelo de datos para recibir los mensajes
class ChatRequest(BaseModel):
    message: str

# Endpoint /chat
@
