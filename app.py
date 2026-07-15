import streamlit as st
import time
from datetime import datetime
import organizar as orgn

def msg(txt):
    return st.chat_message("assistant").write(txt)

hora = datetime.now().hour

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
msg("Gostaria de compailhar com você algumas curiosidades sobre os laureados do Prêmio do Nobel")

time.sleep(2)
msg(f"O Prêmio Nobel existe desde {orgn.laureados().count()}")



