from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_loader import load_words

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/flashcards")
def flashcards(book: str, gwa: int):
    words = load_words(book, gwa)

    return {
        "book": book,
        "gwa": gwa,
        "total": len(words),
        "words": words,   # TAYANCH — bu sening WORDS massiving aynan shu ko‘rinishda ketadi
    }
