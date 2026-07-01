import funcoes as fn, numpy as np, pandas as pd

def laureados():
    df = fn.extrairDfNobel()

    # Index(['Id', 'Firstname', 'Surname', 'Born', 'Died', 'Born country',
    #    'Born country code', 'Born city', 'Died country', 'Died country code',
    #    'Died city', 'Gender', 'Year', 'Category', 'Overall motivation',
    #    'Motivation', 'Organization name', 'Organization city',
    #    'Organization country', 'Geo Shape', 'Geo Point 2D'],
    #   dtype='str')

    df.drop(
        [
            'Born city','Died city',
            'Overall motivation', 'Motivation',
            'Organization city', 'Geo Shape', 'Geo Point 2D'
        ],
        axis='columns', inplace=True
    )

    df.rename(columns={
        "Id" : "id",
        "Firstname" : "nome",
        "Surname" : "sobrenome",
        "Born" : "nascimento",
        "Died" : "morte",
        "Born country" : "pais_nasc",
        "Born country code" : "cod_pais_nasc",
        "Died country" : "pais_morte",
        "Died country code" : "cod_pais_morte",
        "Gender" : "genero",
        "Year" : "ano",
        "Category" : "categoria",
        "Organization name" : "nome_org",
        "Organization country" : "pais_org"
    }, inplace=True)

    df = df.set_index("id").reset_index()

    df.dropna(how="all", inplace=True)

    df["nascimento"] = pd.to_datetime(df["nascimento"])

    df["idade_premio"] = df["ano"] - df["nascimento"].dt.year

    df["decada"] = (df["ano"] // 10) * 10

    return df

def nobelPorNac(db):
    db = pd.DataFrame(db)
    df = (
        db
        .groupby("pais_nasc")
        .size()
        .reset_index(name="qtd_nobel")
    )

    df.rename(columns={
        "pais_nasc" : "pais"
    }, inplace=True)

    return df

def democracias():
    df = fn.extrairDemocracias()

    df = df[["Country/Territory", "Edition", "Total"]]

    df.rename(columns={
        "Country/Territory" : "pais",
        "Edition" : "ano",
        "Total" : "pontos"
    }, inplace=True)

    df = df.sort_values(["ano", "pais"]).reset_index()

    return df

def mulheresPorCategoria(df):
    dfMulheres = df.query("genero == 'female'")

    total = (
        df.groupby(["decada", "categoria"])
            .size()
            .rename("total")
    )

    mulheres = (
        dfMulheres.groupby(["decada", "categoria"])
            .size()
            .rename("mulheres")
    )

    participacao = pd.concat([total, mulheres], axis=1)

    participacao["mulheres"] = participacao["mulheres"].fillna(0)

    participacao["percentual"] = (
        participacao["mulheres"] /
        participacao["total"] * 100
    )

    return participacao

def mulheresTotal(df):
    dfMulheres = df.query("genero == 'female'")

    total = (
        df.groupby("decada")
            .size()
            .rename("total")
    )

    mulheres = (
        dfMulheres.groupby("decada")
            .size()
            .rename("mulheres")
    )

    participacao = pd.concat([total, mulheres], axis=1)

    participacao = participacao.reset_index()

    participacao["mulheres"] = participacao["mulheres"].fillna(0)

    participacao["percentual"] = (
        participacao["mulheres"] /
        participacao["total"] * 100
    )

    return participacao
    

    


