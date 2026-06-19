import requests, pandas as pd, kagglehub
from bs4 import BeautifulSoup
from kagglehub import KaggleDatasetAdapter
from pathlib import Path

def extrairTabWiki(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, "html.parser")

    tabela = soup.find("table", class_="wikitable")

    linhas = tabela.find_all("tr")

    dados = []

    for linha in linhas:
        colunas = linha.find_all(["th", "td"])
        dados.append([c.get_text(" ", strip=True) for c in colunas])

    df = pd.DataFrame(dados[1:], columns=dados[0])

    return df

def dfNacionalidades():
    path = Path(
        kagglehub.dataset_download("joebeachcapital/nobel-prize")
    )

    arquivo = path / "nobel-prize-laureates.csv"

    df = pd.read_csv(
        arquivo,
        sep=";"
    )

    return df