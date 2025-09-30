from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import keys 
import os 

llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key= keys.OPENAIKEY)

# Run a query
#response = llm.invoke([HumanMessage(content="What is the capital of France?")])

response = llm.invoke("What is the capital of France?")

print(response.content)

