import matplotlib.pyplot as plt
import seaborn as sns
import funcoes as fn
import numpy as np
import pandas as pd

def correlDemocrNobel(df):
    df_filtrado = df[df["premios_per_capita"] > 0].copy()

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.scatterplot(
        data=df_filtrado,
        x="pontos",
        y="premios_per_capita",
        size="premios",
        sizes=(50, 300),
        legend=True,
        ax=ax
    )

    ax.set_title("Democracia vs. Prêmios Nobel per capita (2013–2021)")
    ax.set_xlabel("Índice de Democracia")
    ax.set_ylabel("Prêmios Nobel per capita")

    fig.tight_layout()
    return fig


def correlIdhNobel(df):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df["idh"],
        df["premios_per_capita"],
        alpha=0.7
    )

    ax.set_xlabel("IDH (2023)")
    ax.set_ylabel("Prêmios Nobel per capita")
    ax.set_title("IDH x Prêmios Nobel per capita por país")

    ax.grid(alpha=0.3)

    fig.tight_layout()
    return fig


def correlPD_Nobel(df):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df["pd"],
        df["premios_per_capita"],
        alpha=0.7
    )

    ax.set_xlabel("Investimento em P&D (% do PIB)")
    ax.set_ylabel("Prêmios Nobel per capita")
    ax.set_title("Investimento em P&D x Prêmios Nobel per capita por país")

    ax.grid(alpha=0.3)

    fig.tight_layout()
    return fig


def evolucaoMulheresCateg(df):
    heatmap = df.pivot(
        index="categoria",
        columns="decada",
        values="percentual"
    )

    fig, ax = plt.subplots(figsize=(12, 4))

    sns.heatmap(
        heatmap,
        annot=True,
        cmap="Blues",
        fmt=".1f",
        ax=ax
    )

    ax.set_xlabel("Década")
    ax.set_ylabel("Categoria")
    ax.set_title("Participação feminina (%) por categoria")

    fig.tight_layout()
    return fig


def evolucaoTotalMulheres(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        df["decada"],
        df["percentual"],
        marker="o",
        linewidth=2
    )

    ax.set_title("Participação feminina entre os laureados do Nobel por década")
    ax.set_xlabel("Década")
    ax.set_ylabel("Participação (%)")
    ax.grid(alpha=0.3)

    fig.tight_layout()
    return fig