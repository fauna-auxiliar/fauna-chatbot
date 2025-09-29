from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

# Inicializa FastAPI
app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes poner tu blog: ["https://faunaauxiliar.blogspot.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura el cliente de OpenAI con tu API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Modelo de datos para la request
class ChatRequest(BaseModel):
    message: str

# Endpoint /chat
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # más rápido y barato
            messages=[{"role": "user", "content": request.message}]
        )
        reply = response.choices[0].message.content
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error con OpenAI: {str(e)}")

# Endpoint de prueba raíz
@app.get("/")
async def root():
    return {"message": "API funcionando correctamente!"}
