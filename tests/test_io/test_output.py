from app.io.output import show_output

def test_show_output(capsys):
    show_output("Анна")
    captured = capsys.readouterr()
    assert "Привіт, Анна!" in captured.out
