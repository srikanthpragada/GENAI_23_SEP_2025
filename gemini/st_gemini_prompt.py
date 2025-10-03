import streamlit as st
from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

st.title("Gemini Demo ")
prompt = st.text_input("Enter your prompt")
if len(prompt.strip()) > 0:
     response = model.invoke(prompt)
     st.write(f"<h5>{response.content}</h5>", unsafe_allow_html = True)

