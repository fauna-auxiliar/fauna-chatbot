from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
origins = [
    "https://faunaauxiliar.blogspot.com",  # tu blog
    "http://localhost",                     # opcional para pruebas locales
    "http://127.0.0.1:5500"                 # opcional para pruebas locales
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # permite estos orígenes
    allow_credentials=True,
    allow_methods=["*"],    # permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],    # permite todos los headers
)

@app.get("/")
def read_root():
    return {"message": "Hola, mundo!"}

@app.post("/chat")
def chat_endpoint(message: str):
    # Aquí va tu lógica de chatbot
    response = f"Echo: {message}"  # ejemplo de respuesta
    return {"response": response}
