import requests, pandas as pd, kagglehub, organizar as orgn
from kagglehub import KaggleDatasetAdapter
from pathlib import Path
from datetime import datetime

def extrairDfNobel():
    path = Path("./datasets")
    arquivo = path / "nobel-prize-laureates.csv"

    # Só baixa se o CSV ainda não existir
    if not arquivo.exists():
        kagglehub.dataset_download(
            "joebeachcapital/nobel-prize",
            output_dir=path
        )

    df = pd.read_csv(
        arquivo,
        sep=";"
    )

    return df

def extrairDemocracias():
    df = pd.read_excel("dados/dados_democracia.xlsx", sheet_name="FIW13-21")

    return df

def correlDemocrNobel(laureados : pd.DataFrame, dadosDemocracia : pd.DataFrame, populacao : pd.DataFrame):

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

def correlIdhNobel(laureados : pd.DataFrame, idh : pd.DataFrame, populacao : pd.DataFrame):

    laureados = laureados.rename(columns={"pais_nasc": "pais"})

    laureados["pais"] = laureados["pais"].replace({
        "USA": "United States",
        "the Netherlands": "Netherlands",
        "USSR (now Russia)": "Russia",
        "British Mandate of Palestine (now Israel)": "Israel",
        "Belgian Congo (now Democratic Republic of the Congo)": "Congo (Kinshasa)",
        "Scotland": "United Kingdom"
    })

    idh = (
        idh[["pais", 2023]]
        .rename(columns={2023: "idh"})
        .copy()
    )

    idh["idh"] = pd.to_numeric(idh["idh"], errors="coerce")
    idh = idh.dropna(subset=["idh"])

    nobelPorPais = (
        laureados
        .groupby("pais")
        .size()
        .reset_index(name="premios")
    )

    df = idh.merge(
        nobelPorPais,
        on="pais",
        how="left"
    )

    df["premios"] = df["premios"].fillna(0).astype(int)

    df = df.merge(
        populacao,
        on="pais",
        how="left"
    )

    df["premios_per_capita"] = df["premios"] / df["populacao"]

    return df

def correlPD_Nobel(laureados : pd.DataFrame, pd_df : pd.DataFrame, populacao : pd.DataFrame):

    laureados = laureados.rename(columns={"pais_nasc": "pais"})

    laureados["pais"] = laureados["pais"].replace({
        "USA": "United States",
        "the Netherlands": "Netherlands",
        "USSR (now Russia)": "Russia",
        "British Mandate of Palestine (now Israel)": "Israel",
        "Belgian Congo (now Democratic Republic of the Congo)": "Congo (Kinshasa)",
        "Scotland": "United Kingdom"
    })

    nobelPorPais = (
        laureados
        .groupby("pais")
        .size()
        .reset_index(name="premios")
    )

    anos = [str(ano) for ano in range(1996, 2025)]
    pd_df = pd_df[["pais"] + anos]

    pd_df["pd"] = pd_df[anos].ffill(axis=1).iloc[:, -1]

    pd_df = pd_df[["pais", "pd"]]

    pd_df = pd_df.dropna()

    df = pd_df.merge(
        nobelPorPais,
        on="pais",
        how="left"
    )

    df = df.merge(
        populacao,
        on="pais",
        how="left"
    )

    df["premios_per_capita"] = df["premios"] / df["populacao"]
    
    return df

def extrairPopulacao():
    url = (
        "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL"
        "?format=json"
        "&date=2013:2021"
        "&per_page=20000"
    )

    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()[1]

    dfPop = pd.DataFrame(dados)

    dfPop = dfPop[
        ["country", "date", "value"]
    ]

    dfPop.rename(columns={
        "country": "pais",
        "date": "ano",
        "value": "populacao"
    }, inplace=True)

    dfPop["pais"] = dfPop["pais"].apply(
        lambda x: x["value"] if isinstance(x, dict) else str(x)
    )

    dfPop["ano"] = dfPop["ano"].astype(int)

    # Remove registros sem população
    dfPop = dfPop.dropna(subset=["populacao"])

    return dfPop

def topQuantNobel(laureados : pd.DataFrame, quant : int):
    laureados["pais_nasc"] = laureados["pais_nasc"].replace({
        "USA": "United States",
        "the Netherlands": "Netherlands",
        "USSR (now Russia)": "Russia",
        "British Mandate of Palestine (now Israel)": "Israel",
        "Belgian Congo (now Democratic Republic of the Congo)": "Congo (Kinshasa)",
        "Scotland": "United Kingdom"
    })
    df = (
        laureados
        .groupby("pais_nasc")
        .size()
        .reset_index(name="Total Laureados")
        .sort_values("Total Laureados", ascending=False)
        .head(quant)
    )

    df = df.rename(columns={"pais_nasc": "País"}).set_index("País")
    
    return df

def topNobelPerCapita(laureados : pd.DataFrame, populacao : pd.DataFrame, quant : int):
    laureados["pais_nasc"] = laureados["pais_nasc"].replace({
        "USA": "United States",
        "the Netherlands": "Netherlands",
        "USSR (now Russia)": "Russia",
        "British Mandate of Palestine (now Israel)": "Israel",
        "Belgian Congo (now Democratic Republic of the Congo)": "Congo (Kinshasa)",
        "Scotland": "United Kingdom"
    })
    laureados_renamed = laureados.rename(columns={"pais_nasc": "pais"})
    
    nobelPorPais = (
        laureados_renamed
        .groupby("pais")
        .size()
        .reset_index(name="premios")
    )
    
    populacao_media = populacao.groupby("pais")["populacao"].mean().reset_index()
    
    df = nobelPorPais.merge(
        populacao_media,
        on="pais",
        how="left"
    )
    
    # garante tipos numéricos e calcula prêmios por 1 milhão de habitantes
    df["populacao"] = pd.to_numeric(df["populacao"], errors="coerce")
    df["premios"] = pd.to_numeric(df["premios"], errors="coerce").fillna(0)
    df.loc[df["populacao"] == 0, "populacao"] = pd.NA
    df["per_capita"] = (df["premios"] / df["populacao"]) * 1_000_000
    
    df = (
        df
        .dropna(subset=["per_capita"])
        .sort_values("per_capita", ascending=False)
        .head(quant)
    )
    
    df = df.rename(columns={"pais": "País"})[["País", "premios", "per_capita"]].set_index("País")
    
    return df

def topVencedores(laureados : pd.DataFrame):
    df = (
        laureados
        .groupby("nome_completo")
        .size()
        .reset_index(name="Quantidade de Prêmios")
        .query("`Quantidade de Prêmios` > 1")
        .sort_values("Quantidade de Prêmios", ascending=False)
    )
    
    df = df.rename(columns={"nome_completo": "Nome"}).set_index("Nome")
    
    return df
