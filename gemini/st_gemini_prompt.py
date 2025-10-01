import keys 
import streamlit as st
import os 
from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = keys.GOOGLEKEY
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

st.title("Gemini Demo ")
prompt = st.text_input("Enter your prompt")
if len(prompt.strip()) > 0:
     response = model.invoke(prompt)
     st.write(f"<h4>{response.content}</h4>", unsafe_allow_html = True)

