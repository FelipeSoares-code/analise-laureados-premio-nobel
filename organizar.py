import funcoes as fn, numpy as np, pandas as pd

def nacionalidades():
    nacionalidades = fn.extrairNacionalidades()

    # Index(['Id', 'Firstname', 'Surname', 'Born', 'Died', 'Born country',
    #    'Born country code', 'Born city', 'Died country', 'Died country code',
    #    'Died city', 'Gender', 'Year', 'Category', 'Overall motivation',
    #    'Motivation', 'Organization name', 'Organization city',
    #    'Organization country', 'Geo Shape', 'Geo Point 2D'],
    #   dtype='str')

    nacionalidades.drop(
        [
            'Born city','Died city',
            'Overall motivation', 'Motivation',
            'Organization city', 'Geo Shape', 'Geo Point 2D'
        ],
        axis='columns', inplace=True
    )

    nacionalidades.rename(columns={
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
        "Year" : "ano_venc",
        "Category" : "categoria",
        "Organization name" : "nome_org",
        "Organization country" : "pais_org"
    }, inplace=True)

    return nacionalidades

def laureados():
    # Index(['Ano', 'Física [ 21 ]', 'Química [ 22 ]',
    #    'Fisiologia ou Medicina [ 23 ]', 'Literatura [ 24 ]', 'Paz [ 25 ]',
    #    'Economia (Prêmio Sveriges Riksbank) [ 26 ]'],
    #   dtype='str')

    df = fn.extrairTabWiki("https://pt.wikipedia.org/wiki/Laureados_com_o_Nobel")

    df = df.replace(["Não foi atribuído", "Não foi atribuído[nota 4]", "—"], np.nan)

    df.rename(columns={
        "Ano" : "ano",
        "Física [ 21 ]" : "fisica",
        "Química [ 22 ]" : "quimica",
        "Fisiologia ou Medicina [ 23 ]" : "medicina",
        "Literatura [ 24 ]" : "literatura",
        "Paz [ 25 ]" : "paz",
        "Economia (Prêmio Sveriges Riksbank) [ 26 ]" : "economia"
    }, inplace=True)

    df = df.iloc[:-1] #todas linhas permanecem menos a ultima

    df["ano"] = pd.to_numeric(df["ano"], errors="coerce").astype(int)

    return df

    


