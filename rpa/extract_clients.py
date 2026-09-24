"""Extrai clientes de uma pagina HTML e envia o lote ao webhook do n8n."""

from __future__ import annotations

import argparse
import os
from decimal import Decimal, InvalidOperation

import requests
from bs4 import BeautifulSoup


def extract_clients(html: str) -> list[dict[str, object]]:
    soup = BeautifulSoup(html, "html.parser")
    clients: list[dict[str, object]] = []
    for row in soup.select("#clientes tbody tr"):
        cells = [cell.get_text(" ", strip=True) for cell in row.select("td")]
        if len(cells) != 4:
            continue
        name, email, balance_raw, profile = cells
        try:
            balance = float(Decimal(balance_raw.replace("R$", "").replace(".", "").replace(",", ".").strip()))
        except InvalidOperation:
            continue
        clients.append({"nome": name, "email": email.strip().lower(), "saldo": balance, "perfil": profile.strip().lower()})
    return clients


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-url", default=os.getenv("CLIENTS_URL"))
    parser.add_argument("--source-file", default="data/clientes.html")
    parser.add_argument("--webhook-url", default=os.getenv("N8N_WEBHOOK_URL"))
    args = parser.parse_args()

    if args.source_url:
        source = requests.get(args.source_url, timeout=20)
        source.raise_for_status()
        html = source.text
    else:
        with open(args.source_file, encoding="utf-8") as file:
            html = file.read()

    clients = extract_clients(html)
    if not clients:
        raise RuntimeError("Nenhum cliente valido foi extraido do HTML.")
    if not args.webhook_url:
        raise RuntimeError("Informe --webhook-url ou N8N_WEBHOOK_URL.")

    response = requests.post(args.webhook_url, json={"clientes": clients, "origem": args.source_url or args.source_file}, timeout=30)
    response.raise_for_status()
    print(response.json())


if __name__ == "__main__":
    main()
