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
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_message}]
        )
        print("Respuesta OpenAI:", response)  # <--- imprime en logs de Render
        reply = response.choices[0].message.content
    except Exception as e:
        print("Error OpenAI:", e)  # <--- imprime error real
        raise HTTPException(status_code=500, detail=f"Error con OpenAI: {str(e)}")
    return {"reply": reply}


    except Exception as e:
        # Devuelve el error completo para depuración
        return {"error": str(e)}

# Endpoint raíz
@app.get("/")
async def root():
    return {"message": "API funcionando correctamente!"}
