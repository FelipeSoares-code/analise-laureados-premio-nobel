import streamlit as st
import time
from datetime import datetime
import organizar as orgn
import funcoesGraficos as fg
import matplotlib.pyplot as plt
import pandas as pd

def msg(txt):
    return st.chat_message("assistant").write(txt)

hora = datetime.now().hour

laureados = orgn.laureados().copy()

if hora >= 5 and hora < 12:
    saudacao = "Bom dia"
elif hora >= 12 and hora <= 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

st.title("Análise dos Laureados do Prêmio Nobel")

time.sleep(1)
msg(f"Olá, {saudacao}!")
time.sleep(1)
msg("Gostaria de compartilhar com você algumas curiosidades sobre os laureados do Prêmio do Nobel")

time.sleep(2)
primeiro_ano = laureados['ano'].min()
msg(f"O primeiro Prêmio Nobel foi entregue em {primeiro_ano}")

time.sleep(2)
primeiros_vencedores = laureados.query(f"ano == {primeiro_ano}")['nome_completo'].astype(str).tolist()
msg(f"Os primeiros vencedores foram: {', '.join(primeiros_vencedores)}")

time.sleep(2)
primeira_mulher = laureados.query("genero == 'female'").sort_values("ano").iloc[0]
msg(f"A primeira mulher vencedora do Prêmio Nobel foi {primeira_mulher['nome_completo']} em {primeira_mulher['ano']}")

time.sleep(2)
msg("Vou lhe mostrar um gráfico mostrando a evolução da participação feminina no Prêmio Nobel")
totalMulheres = orgn.mulheresTotal(laureados)
fig = fg.evolucaoTotalMulheres(totalMulheres)
st.pyplot(fig)

time.sleep(2)
mulheresCateg = orgn.mulheresPorCategoria(laureados)
listCateg = mulheresCateg['categoria'].unique().tolist()
categs = {}
for c in listCateg:
    categs.update({c : mulheresCateg.query(f"categoria == '{c}'")['mulheres'].sum()})
max_categoria = max(categs, key=categs.get)
percent_total = (
    mulheresCateg.query(f"categoria == '{max_categoria}'")["mulheres"].sum() /
    mulheresCateg.query(f"categoria == '{max_categoria}'")["total"].sum() * 100
)
msg(f"A categoria com o maior número de laureadas mulheres é: {max_categoria}, com {int(categs[max_categoria])} mulheres no total")
msg(f"Na categoria {max_categoria} as mulheres representam {percent_total:.2f}% do total de vencedores")

time.sleep(2)
msg("Vou lhe mostrar um gráfico com a evolução da participação feminina em cada categoria")
fig = fg.evolucaoMulheresCateg(mulheresCateg)
st.pyplot(fig)
