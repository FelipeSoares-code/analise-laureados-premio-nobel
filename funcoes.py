import requests, pandas as pd, kagglehub, organizar as orgn, wbdata
from bs4 import BeautifulSoup
from kagglehub import KaggleDatasetAdapter
from pathlib import Path
from datetime import datetime

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

def extrairDfNobel():
    path = Path(
        kagglehub.dataset_download("joebeachcapital/nobel-prize")
    )

    arquivo = path / "nobel-prize-laureates.csv"

    df = pd.read_csv(
        arquivo,
        sep=";"
    )

    return df

def extrairDemocracias():
    df = pd.read_excel("dados_democracia.xlsx", sheet_name="FIW13-21")

    return df

def correlDemocrNobel(laureados, dadosDemocracia, populacao):
    laureados  = pd.DataFrame(laureados)
    dadosDemocracia = pd.DataFrame(dadosDemocracia)
    populacao = pd.DataFrame(populacao)

    laureados_2013_2021 = laureados.query("ano >= 2013 and ano <= 2021").copy()

    laureados_2013_2021.rename(columns={"pais_nasc" : "pais"}, inplace=True)

    laureados_2013_2021["pais"] = laureados_2013_2021["pais"].replace({
        "USA": "United States",
        "the Netherlands": "Netherlands",
        "USSR (now Russia)": "Russia",
        "British Mandate of Palestine (now Israel)": "Israel",
        "Belgian Congo (now Democratic Republic of the Congo)": "Congo (Kinshasa)",
        "Scotland": "United Kingdom"
    })

    nobelPorAno = (
        laureados_2013_2021
        .groupby(["pais", "ano"])
        .size()
        .reset_index(name="premios")
    )

    df = dadosDemocracia.merge(
        nobelPorAno,
        on=["pais", "ano"],
        how="left"
    )

    df = df.merge(
        populacao,
        on=["pais", "ano"],
        how="left"
    )

    df["premios"] = df["premios"].fillna(0)

    df["premios_per_capita"] = df["premios"] / df["populacao"]

    return df

def extrairPopulacao():
    indicadores = {
        "SP.POP.TOTL": "populacao"
    }

    dfPop = wbdata.get_dataframe(
        indicadores,
        date=(datetime(2013,1,1), datetime(2021,12,31))
    )

    dfPop = dfPop.reset_index()

    # Extrai apenas o nome do país (string) caso venha como objeto/lista
    dfPop["country"] = dfPop["country"].apply(
        lambda x: x["value"] if isinstance(x, dict)
        else (x[0] if isinstance(x, list) else str(x))
    )

    dfPop.rename(columns={
        "country": "pais",
        "date": "ano"
    }, inplace=True)

    dfPop["ano"] = dfPop["ano"].astype(int)

    # Remove agregados regionais do Banco Mundial (ex: "World", "Europe & Central Asia")
    dfPop = dfPop.dropna(subset=["populacao"])

    return dfPop
