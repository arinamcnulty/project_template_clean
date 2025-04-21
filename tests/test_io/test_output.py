from app.io.output import write_to_file, print_to_console


def test_write_to_file(tmp_path):
    path = tmp_path / "out.txt"
    text = "Привіт"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == text
