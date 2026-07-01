import matplotlib.pyplot as plt
import seaborn as sns
import funcoes as fn
import numpy as np
import pandas as pd

def correlDemocrNobel(df):
    df_filtrado = df[df["premios_per_capita"] > 0].copy()

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df_filtrado,
        x="pontos",   
        y="premios_per_capita",       
        size="premios",          
        sizes=(50, 300),
        legend=True             
    )

    plt.title("Democracia vs. Prêmios Nobel per capita (2013–2021)")
    plt.xlabel("Índice de Democracia")
    plt.ylabel("Prêmios Nobel per capita")
    plt.tight_layout()
    plt.show()

def evolucaoMulheresCateg(df):
    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="decada",   
        y="percentual",       
        size="mulheres",          
        sizes=(50, 300),
        hue="categoria",
        legend=False             
    )

    plt.title("Evolução porcentagem de mulheres vencedoras do nobel")
    plt.xlabel("Década")
    plt.ylabel("Quantidade de mulheres vencedoras (%)")
    plt.tight_layout()
    plt.show()

def evolucaoTotalMulheres(df):
    plt.figure(figsize=(12,6))

    plt.plot(
        df["decada"],
        df["percentual"],
        marker="o",
        linewidth=2
    )

    plt.title("Participação feminina entre os laureados do Nobel por década")
    plt.xlabel("Década")
    plt.ylabel("Participação (%)")
    plt.grid(alpha=0.3)

    plt.show()