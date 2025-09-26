@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error al generar respuesta: {str(e)}"

    return {"reply": reply}
