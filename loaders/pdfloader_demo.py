# Load PDF document
# pip install pypdf 

from langchain_community.document_loaders.pdf import PyPDFLoader    

# Load the PDF file
loader = PyPDFLoader("./loaders/courses_offered.pdf", mode = 'page')

# Load the documents
docs = loader.load()
print("Loaded Documents :", len(docs))


# Print the loaded documents
for doc in docs:
    #print(doc.metadata)
    print(doc.page_content[:50])  # Print the first 50 characters of each document
    print(len(doc.page_content))
    print("-" * 50)

