from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_loader import load_words

app = FastAPI()

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Vercel, Telegram, lokal — hammasi ishlaydi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "ok"}

# --- ASOSIY API: /api/flashcards ---
@app.get("/api/flashcards")
def flashcards(book: str, gwa: int):
    words = load_words(book, gwa)

    return {
        "book": book,
        "gwa": gwa,
        "total": len(words),
        "words": words,
    }
