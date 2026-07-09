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

def correlIdhNobel(df):
    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["idh"],
        df["premios_per_capita"],
        alpha=0.7
    )

    plt.xlabel("IDH (2023)")
    plt.ylabel("Prêmios Nobel per capita")
    plt.title("IDH x Prêmios Nobel per capita por país")

    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

def correlPD_Nobel(df):
    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["pd"],
        df["premios_per_capita"],
        alpha=0.7
    )

    plt.xlabel("Investimento em P&D (% do PIB)")
    plt.ylabel("Prêmios Nobel per capita")
    plt.title("Investimento em P&D x Prêmios Nobel per capita por país")

    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

def evolucaoMulheresCateg(df):
    heatmap = df.pivot(
        index="categoria",
        columns="decada",
        values="percentual"
    )

    plt.figure(figsize=(12,4))

    sns.heatmap(
        heatmap,
        annot=True,
        cmap="Blues",
        fmt=".1f"
    )

    plt.xlabel("Década")
    plt.ylabel("Categoria")
    plt.title("Participação feminina (%) por categoria")

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