import keys 

import os
os.environ["GOOGLE_API_KEY"] =  keys.GOOGLEKEY

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
 
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", 
                             temperature=0.9, 
                             max_output_tokens=500,
                             model_kwargs= { "frequency_penalty": 1.5} )
                             

response = llm.invoke([HumanMessage(content="write a story about Sun. It should be no more than 5 sentences")])
print(response.content)
 
