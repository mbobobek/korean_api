import importlib

def load_words(book: str, gwa: int):
    book = book.upper()

    # Hozircha faqat 1A
    if book != "1A":
        return []

    try:
        module = importlib.import_module(f"book_1A.gwa{gwa}")
        return module.WORDS
    except Exception as e:
        print("Import error:", e)
        return []
