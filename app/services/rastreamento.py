import httpx
from bs4 import BeautifulSoup
from datetime import datetime


def consultar_status_encomenda(codigo: str) -> dict:
    """
    Consulta real ao site LinkCorreios para extrair status da encomenda.

    """
    url = f"https://www.linkcorreios.com.br/{codigo}"

    with httpx.Client() as client:
        response = client.get(url)
        if response.status_code != 200:
            return {"status": "Erro ao consultar", "atualizado_em": datetime.utcnow()}

        soup = BeautifulSoup(response.text, "html.parser")

        status_div = soup.find("div", {"class": "card-body"})

        if not status_div:
            return {"status": "Status não encontrado", "atualizado_em": datetime.utcnow()}

        status_text = status_div.get_text(strip=True).split("\n")[0]

        return {"status": status_text, "atualizado_em": datetime.utcnow()}
