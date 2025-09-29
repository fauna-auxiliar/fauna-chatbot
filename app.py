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
    allow_origins=["*"],  # Cambia "*" por la URL de tu blog si quieres restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura la API key de OpenAI (debe estar en las variables de entorno de Render)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Modelo de datos
class ChatRequest(BaseModel):
    message: str

# Endpoint /chat
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": request.message}]
        )
        reply = response.choices[0].message.content
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error con OpenAI: {str(e)}")

# Endpoint raíz de prueba
@app.get("/")
async def root():
    return {"message": "API funcionando correctamente!"}
