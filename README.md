# Análise dos Laureados do Prêmio Nobel

Este projeto realiza uma análise exploratória e estatística dos dados históricos do **Prêmio Nobel**, abrangendo desde a sua criação até os dias atuais. O objetivo é identificar padrões de premiação, a evolução da participação feminina e a correlação entre o sucesso científico de um país (medido em prêmios per capita) e seus indicadores socioeconômicos, como o **Índice de Desenvolvimento Humano (IDH)**, o **Nível de Democracia** e o **Investimento em Pesquisa e Desenvolvimento (P&D)**.

A aplicação conta com uma interface desenvolvida em **Streamlit**, que apresenta os dados de forma dinâmica, simulando uma conversa com o usuário.

---

## 🚀 Funcionalidades

O projeto oferece as seguintes análises e visualizações:

- **Histórico e Curiosidades**: Informações sobre os primeiros vencedores e marcos históricos.
- **Participação Feminina**:
    - Evolução da participação de mulheres no Nobel por década.
    - Comparativo da presença feminina entre as diferentes categorias (Física, Química, Medicina, Literatura, Paz e Economia).
- **Análise de Correlação**:
    - Nobel per capita vs. Pontuação de Democracia.
    - Nobel per capita vs. Índice de Desenvolvimento Humano (IDH).
    - Nobel per capita vs. Investimento em Pesquisa e Desenvolvimento (% do PIB).
- **Rankings e Estatísticas**:
    - Top 10 países com mais prêmios (total e per capita).
    - Lista de laureados que receberam o prêmio mais de uma vez.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes ferramentas e bibliotecas:

- **Linguagem**: [Python](https://www.python.org/) (v3.11+)
- **Análise de Dados**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualização**: [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- **Interface Web**: [Streamlit](https://streamlit.io/)
- **Fontes de Dados**:
    - [Kaggle](https://www.kaggle.com/) (Dados do Nobel via `kagglehub`)
    - [World Bank API](https://data.worldbank.org/) (Dados populacionais via `wbdata`)
    - Arquivos locais (IDH, Democracia e P&D)

---

## 📂 Estrutura do Repositório

| Arquivo/Pasta | Descrição |
| :--- | :--- |
| `app.py` | Ponto de entrada da aplicação Streamlit. |
| `main.py` | Script principal para execução rápida de funções básicas. |
| `funcoes.py` | Contém a lógica de extração, limpeza e cálculos estatísticos. |
| `organizar.py` | Funções para estruturação e tratamento inicial dos DataFrames. |
| `funcoesGraficos.py` | Lógica de geração de gráficos com Matplotlib e Seaborn. |
| `dados/` | Pasta contendo os arquivos `.csv` e `.xlsx` utilizados na análise. |
| `notebooks/` | Jupyter Notebooks utilizados para exploração inicial e testes. |
| `requirements.txt` | Lista de dependências do projeto. |

---

## 🔧 Como Executar

### Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Recomenda-se o uso de um ambiente virtual.

### Passo a Passo

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/FelipeSoares-code/analise-laureados-premio-nobel.git
   cd analise-laureados-premio-nobel
   ```

2. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar a aplicação Streamlit**:
   ```bash
   streamlit run app.py
   ```

---

## 📊 Fontes de Dados

Os dados utilizados neste projeto provêm de fontes confiáveis:
- **Nobel Prize Dataset**: Extraído via Kaggle.
- **Índice de Democracia**: Dados históricos de regimes políticos.
- **IDH (Human Development Index)**: Relatórios de desenvolvimento humano.
- **P&D (Research and Development)**: Dados do Banco Mundial sobre gastos em ciência e tecnologia.

---

## 👤 Autor

Desenvolvido por **Felipe Soares**.
Sinta-se à vontade para contribuir com este projeto ou entrar em contato!

---
> *Nota: Este projeto foi desenvolvido para fins de estudo e análise de dados.*
