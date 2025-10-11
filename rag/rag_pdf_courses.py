from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import init_chat_model

# Supress warnings from GRPC 
import os
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_CPP_VERBOSITY"] = "NONE"

# 1. Load 
loader = PyPDFLoader(
    r"./rag/courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

# 2. Split into chunks 
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400, 
    chunk_overlap=100)

chunks = splitter.split_documents(docs)
print("No. of chunks :", len(chunks))

# 3. Access embeddings model
embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001")


# 4. Create Vector DB - Facebook AI Similarity Search
db = FAISS.from_documents(chunks,embeddings_model)   
print('Created FAISS index')

# 5. Access LLM
question = "What is the duration of SAP course?"

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# 6. Search for matching document
retriever = db.as_retriever(search_kwargs={"k": 2})
search_results = retriever.invoke(question)

# 7. Create context with matching docs 
context = "\n".join([doc.page_content for doc in search_results])

# 8. Create prompt
prompt = f"""
Please answer the question using the context only. 
If you don't know the answer, say you do not know.

{context}

Question: {question}
Answer: 
"""

# 9. Invoke LLM with prompt 
result = llm.invoke(prompt)

# 10. Show results 
print(result.content)
