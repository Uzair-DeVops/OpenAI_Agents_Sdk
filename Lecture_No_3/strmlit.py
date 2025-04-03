import streamlit as st
from Agent import AIagent
import asyncio

st.title('Chatbot')

userquery = st.text_input("write you message here")


if st.button("enter"):
    response = asyncio.run(AIagent(userquery))

    st.write(response)