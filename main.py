from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_loader import load_words

app = FastAPI()

# CORS — web uchun ruxsat berish
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # keyin xohlasang faqat vercel domenini qoldiramiz
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "ok", "message": "Korean API is running"}

# ASOSIY ROUTE — web frontend aynan SHU yo‘ldan foydalanadi
@app.get("/api/flashcards")
def flashcards(book: str, gwa: int):
    words = load_words(book, gwa)

    return {
        "book": book,
        "gwa": gwa,
        "total": len(words),
        "words": words
    }
