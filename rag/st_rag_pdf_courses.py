from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts.prompt import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings
import streamlit as st 
import os 

# Embeddings model and LLM 
embeddings_model = OllamaEmbeddings(model="nomic-embed-text")
llm = OllamaLLM(model="llama3.2:1b")

folder_path = "./course_vectors"

if os.path.exists(folder_path):
    db = FAISS.load_local(folder_path, embeddings_model,
                          allow_dangerous_deserialization=True)
    print("Loaded FAISS index")
else:
    loader = PyPDFLoader(r"./courses_offered.pdf", mode="page")

    docs = loader.load()

    # Split docs into chunks
    splitter = RecursiveCharacterTextSplitter( chunk_size=400,
            chunk_overlap=100)

    chunks = splitter.split_documents(docs)
    db = FAISS.from_documents(chunks, embeddings_model)
    print('Created FAISS index')
    db.save_local(folder_path)


prompt_template = """:
Consider the following context and give a short answer for the given question.

Context : {context}

Question:{question}
"""

prompt  = PromptTemplate.from_template(prompt_template)

retriever = db.as_retriever()


st.title("RAG Demo")
query = st.text_input("Enter your query :")

if len(query) > 0:
    results = retriever.invoke(query)
    matching_docs_str = "\n".join([doc.page_content for doc in results])
    final_prompt = prompt.format(context=matching_docs_str, question=query)
    result =  llm.invoke(final_prompt)
    st.write(result)
    