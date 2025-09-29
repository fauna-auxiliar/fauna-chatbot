from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura tu API key de OpenAI
openai.api_key = "TU_API_KEY_AQUI"

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}

@app.post("/chat")
async def chat(request: ChatRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="No se proporcionó un prompt")

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=request.prompt,
            max_tokens=150,
            temperature=0.7
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
