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
    allow_origins=["*"],  # Puedes restringir a tu blog más adelante
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura tu API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Modelo de datos
class ChatRequest(BaseModel):
    message: str

# Endpoint /chat
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Cambia si quieres otro modelo
            messages=[{"role": "user", "content": user_message}],
            temperature=0.7
        )
        reply = response.choices[0].message.content
        return {"reply": reply}

    except Exception as e:
        # Devuelve el error completo para depuración
        return {"error": str(e)}

# Endpoint raíz
@app.get("/")
async def root():
    return {"message": "API funcionando correctamente!"}
