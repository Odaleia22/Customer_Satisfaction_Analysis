# Importando as bibliotecas

import streamlit as st
import nltk
nltk.data.path.append('/home/odaleia/Customer_Satisfaction_Analysis/minha_venv/nltk_data')
nltk.download('vader_lexicon')

#Título do sistema
st.write("Customer Satisfaction Analysis")

#Entada de Dados - A manifestação do cliente
user_input=st.text_input("Please rate our service:")

#Crição de máquina preditiva de análise de satisfação do cliente
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon") #O comando nltk.download("vader_lexicon") baixa o léxico VADER da biblioteca NLTK, utilizado para análise de sentimentos em textos.
s = SentimentIntensityAnalyzer()
score= s.polarity_scores(user_input)

if score == 0:
    st.write("#Neutral review😐")
elif score["neg"] !=0:
    st.write("#Bad review!😟")

elif score["pos"] !=0:
    st.write("#Good review!😃")