# Load document from website 
import re 
import os
os.environ["USER_AGENT"] = "webbaseloader-script/0.1"
from langchain_community.document_loaders import WebBaseLoader    

# Load webpage from website 
loader = WebBaseLoader(
    web_paths=("https://www.srikanthtechnologies.com/testimonials.aspx",
               "https://www.srikanthtechnologies.com/coursesoffered.aspx")
)

# Load the documents
docs = loader.load()
print("Loaded Documents :", len(docs))

my_docs = []

# Print the loaded documents
for doc in docs:
    print("Document Size :", len(doc.page_content))
    content = doc.page_content
    new_content = re.sub(' +', ' ', content) 
    new_content = re.sub('\n+', '\n', new_content) 

    my_docs.append( Document(page_content = new_content))
    
    print(new_content[:50])  # Print the first 50 characters of each document
    print("-" * 50)
