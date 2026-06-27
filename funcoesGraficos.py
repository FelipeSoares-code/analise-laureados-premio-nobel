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
        hue="pais",              
        size="premios",          
        sizes=(50, 300),
        legend=False             
    )

    plt.title("Democracia vs. Prêmios Nobel per capita (2013–2021)")
    plt.xlabel("Índice de Democracia")
    plt.ylabel("Prêmios Nobel per capita")
    plt.tight_layout()
    plt.show()