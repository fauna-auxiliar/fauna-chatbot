from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir tu blog
origins = [
    "https://faunaauxiliar.blogspot.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # <--- tu blog
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(message: dict):
    user_message = message.get("message")
    # Aquí iría la lógica de tu chatbot
    return {"response": f"Echo: {user_message}"}
