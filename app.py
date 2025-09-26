from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir tu blog como origen
origins = [
    "https://faunaauxiliar.blogspot.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def chat_endpoint(message: dict):
    user_message = message.get("message", "")
    # Aquí tu lógica del chatbot
    return {"message": f"Recibido: {user_message}"}
