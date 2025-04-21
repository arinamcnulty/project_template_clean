def get_input_text():
    """Отримує текст від користувача через консоль."""
    return input("Введіть текст: ")

def read_file_builtin():
    """Зчитує вміст текстового файлу 'data/input.txt' за допомогою open()."""
    with open("data/input.txt", "r", encoding="utf-8") as file:
        return file.read()

def read_file_pandas():
    """Зчитує CSV-файл 'data/input.csv' як DataFrame за допомогою pandas."""
    import pandas as pd
    return pd.read_csv("data/input.csv")
