import streamlit as st
import time
from datetime import datetime
import organizar as orgn
import funcoesGraficos as fg
import matplotlib.pyplot as plt
import pandas as pd
import funcoes as fn

def msg(txt):
    return st.chat_message("assistant").write(txt)

def pause():
    return time.sleep(0)


hora = datetime.now().hour

laureados = orgn.laureados().copy()

if hora >= 5 and hora < 12:
    saudacao = "Bom dia"
elif hora >= 12 and hora <= 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

st.title("Análise dos Laureados do Prêmio Nobel")

pause()
msg(f"Olá, {saudacao}!")
pause()
msg("Gostaria de compartilhar com você algumas curiosidades sobre os laureados do Prêmio do Nobel")

pause()
primeiro_ano = laureados['ano'].min()
msg(f"O primeiro Prêmio Nobel foi entregue em {primeiro_ano}")

pause()
primeiros_vencedores = laureados.query(f"ano == {primeiro_ano}")['nome_completo'].astype(str).tolist()
msg(f"Os primeiros vencedores foram: {', '.join(primeiros_vencedores)}")

pause()
primeira_mulher = laureados.query("genero == 'female'").sort_values("ano").iloc[0]
msg(f"A primeira mulher vencedora do Prêmio Nobel foi {primeira_mulher['nome_completo']} em {primeira_mulher['ano']}")

pause()
msg("Vou lhe mostrar um gráfico mostrando a evolução da participação feminina no Prêmio Nobel")
totalMulheres = orgn.mulheresTotal(laureados)
fig = fg.evolucaoTotalMulheres(totalMulheres)
st.pyplot(fig)

pause()
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

pause()
msg("Vou lhe mostrar um gráfico com a evolução da participação feminina em cada categoria")
fig = fg.evolucaoMulheresCateg(mulheresCateg)
st.pyplot(fig)

pause()
democr = orgn.democracias()
popul = fn.extrairPopulacao()
correlDemocr = fn.correlDemocrNobel(laureados, democr, popul)
msg("Analisando os países que já venceram o nobel, eu quis verificar se há alguma correlação entre o número de Nobel per capita de um país com os pontos de democracia que ele possue")

correlDemocrNum = correlDemocr['pontos'].corr(correlDemocr['premios_per_capita'])
correlPosit = True if correlDemocrNum > 0 else False
msg(f"Fazendo o calculo de correlação entre o número de Nobel per capita e os pontos de democracia do país, cheguei a conclusão que a correlação é {"positiva" if correlPosit else "negativa"} em {(correlDemocrNum * 100):.2f}%")

pause()
msg("Segue o gráfico mostrando a correlação entre nível de democracia de um país e o número de nobel")
fig = fg.correlDemocrNobel(correlDemocr)
st.pyplot(fig)

pause()
msg("Ainda sobre correlações, analisei a correlação entre o IDH do país com a quantidade de Nobel per capita")
idh = orgn.idh()
correlIdh = fn.correlIdhNobel(laureados, idh, popul)
correlIdhNum = correlIdh['idh'].corr(correlDemocr['premios_per_capita'])
correlPosit = True if correlIdhNum > 0 else False
msg(f"A correlação é {'positiva' if correlPosit else 'negativa'} em {(correlIdhNum * 100):.2f}%")
msg("Segue gráfico mostrando a correlação")
fig = fg.correlIdhNobel(correlIdh)
st.pyplot(fig)

pause()
msg("Como ultima análise de correlação, quis verificar a correlação entre o número de laureados de um país com o seu investimento em pesquisa e desenvolvimento(P&D)")
pesq_desenv = orgn.pesquisaEDesenvolvimento()
correlPd = fn.correlPD_Nobel(laureados, pesq_desenv, popul)
correlPdNum = correlPd['pd'].corr(correlPd['premios_per_capita'])
correlPosit = True if correlPdNum > 0 else False
msg(f"Pela a análise feita, a correlação é {'positiva' if correlPosit else 'negativa'} em {(correlPdNum * 100):.2f}%")
msg("Segue gráfico com a correlação")
fig = fg.correlPD_Nobel(correlPd)
st.pyplot(fig)

pause()
msg("Veja a tabela completa com os dados apresentados")
tab = pd.DataFrame()
corrNums = [correlDemocrNum, correlIdhNum, correlPdNum]
tab['Correlação com o número de prêmios per capita'] = ['Nível de Democracia', 'IDH', 'Investimento em Pesquisa e Desenvolvimento']
tab['tipo correlação'] = ['positiva' if c > 0 else 'negativa' for c in corrNums]
tab['% correlação'] = [f'{c * 100:.2f}%' for c in corrNums]
st.table(tab)

pause()
msg("Agora para finalizar a análise, irei apresentar algumas tabelas com informações uteis")
pause()

msg("Países com mais Prêmios Nobel no total")
tab = fn.topQuantNobel(laureados, 10)
st.table(tab)

msg("Países com mais Prêmios Nobel per capita")
tab = fn.topNobelPerCapita(laureados, popul, 10)
st.table(tab)

msg("Laureados que receberam mais de um Nobel")
tab = fn.topVencedores(laureados)
st.table(tab)

pause()
msg("Essa foram algumas curiosidades sobre os vencedores do Prêmio Nobel")
pause()
msg("Espero que tenha gostado")
pause()
msg("Até a próxima!")