from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

# Inicializa FastAPI
app = FastAPI()

# Configura CORS para tu blog
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por la URL de tu blog si quieres restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Modelo de datos
class ChatRequest(BaseModel):
    message: str

# Endpoint /chat
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Modelo más barato y rápido
            messages=[{"role": "user", "content": user_message}]
        )
        
        # Aseguramos que extraemos el mensaje correctamente según la versión
        if hasattr(response.choices[0], "message") and hasattr(response.choices[0].message, "content"):
            reply = response.choices[0].message.content
        elif hasattr(response.choices[0], "text"):
            reply = response.choices[0].text
        else:
            reply = "Error: No se pudo obtener la respuesta del chatbot."
            
    except Exception as e:
        # Esto imprimirá el error en los logs de Render
        print("Error al llamar a OpenAI:", e)
        raise HTTPException(status_code=500, detail=f"Error con OpenAI: {str(e)}")

    return {"reply": reply}

# Endpoint raíz para probar
@app.get("/")
async def root():
    return {"message": "API funcionando correctamente!"}
