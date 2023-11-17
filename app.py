import streamlit as st
import requests


st.title('Sentiment Analysis Using GPT')
sent = st.text_input('Enter Your sentance:')
clf_btn = st.button(label='Classify')
if sent and clf_btn:
    fastapi_url = 'http://127.0.0.1:8000/emotion?'
    response = requests.post(
        r'http://127.0.0.1:8000/emotion', params={'user_pormpt': sent})
    if response.status_code == 200:
        st.write(f'_{sent} is:_ __{response.json()}__')

