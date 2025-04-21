from app.io.input import get_input

def test_get_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Іван")
    result = get_input()
    assert result == "Іван"
