from pathlib import Path

from rpa.extract_clients import extract_clients


def test_extracts_expected_clients() -> None:
    html = Path("data/clientes.html").read_text(encoding="utf-8")
    clients = extract_clients(html)
    assert len(clients) == 4
    assert clients[0] == {
        "nome": "Ana Silva",
        "email": "ana.silva@example.com",
        "saldo": 12500.0,
        "perfil": "conservador",
    }
