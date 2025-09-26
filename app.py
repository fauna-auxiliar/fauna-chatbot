from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pregunta(BaseModel):
    pregunta: str

@app.get("/")
def home():
    return {"mensaje": "✅ Chatbot backend funcionando en Render"}

@app.post("/chat")
def chat(data: Pregunta):
    # Respuesta de prueba, aquí puedes integrar OpenAI o tu lógica
    return {"respuesta": f"Recibí tu pregunta: {data.pregunta}"}
