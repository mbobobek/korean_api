import importlib

def load_words(book: str, gwa: int):
    module_name = f"book_{book}.gwa{gwa}"

    try:
        module = importlib.import_module(module_name)
        return module.WORDS
    except Exception as e:
        print("ERROR:", e)
        return []
