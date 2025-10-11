
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chat_models import init_chat_model
import os 
os.environ["USER_AGENT"] = "my-rag-app/1.0"
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts.prompt import PromptTemplate

# embedding_model = HuggingFaceEndpointEmbeddings(
#     model="sentence-transformers/all-MiniLM-L6-v2",
#     huggingfacehub_api_token= keys.HUGGINGFACEKEY
# )

embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001")

folder_path = "./rag/andrew_vectors"

if os.path.exists(folder_path):
    db = FAISS.load_local(folder_path, embeddings_model, allow_dangerous_deserialization=True)
    print("Loaded FAISS index")
else:
    loader = WebBaseLoader("https://www.andrewng.org/about")    
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=256,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(docs)
    print("Number of chunks created: ", len(chunks))

    db = FAISS.from_documents(chunks, embeddings_model)
    print('Created FAISS index')
    db.save_local(folder_path)  # Save embeddings and docs 


question = "How many research papers Andrew Ng authored?"
retriever = db.as_retriever()

results = retriever.invoke(question)
print("Number of documents retrieved: ", len(results))

matching_docs_str = "\n".join([doc.page_content for doc in results])

prompt_template = """
Give me answer to my question based on the context.

{context}

Question: {question}
"""

prompt  = PromptTemplate.from_template(prompt_template)
final_prompt = prompt.format(context=matching_docs_str, question=question)

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
 
result =  llm.invoke(final_prompt)
print(result.content)
