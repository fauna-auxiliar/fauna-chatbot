from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

# Configuración de CORS para tu blog
origins = [
    "https://faunaauxiliar.blogspot.com",  # tu blog
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint del chatbot
@app.post("/")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    # Lógica del chatbot con OpenAI
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response.choices[0].message.content
    return {"message": reply}

# Endpoint de prueba opcional
@app.get("/")
async def root():
    return {"message": "El chatbot está activo"}
