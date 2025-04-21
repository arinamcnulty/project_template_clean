def print_to_console(text):
    """Виводить текст у консоль."""
    print(text)

def write_to_file(text):
    """Записує текст до файлу 'data/output.txt' за допомогою open()."""
    with open("data/output.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")
