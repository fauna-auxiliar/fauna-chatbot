from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Origen exacto de tu blog
origins = [
    "https://faunaauxiliar.blogspot.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(data: dict):
    user_message = data.get("message", "")
    return {"message": f"Recibido: {user_message}"}
