 
from langchain.chat_models import init_chat_model
# import keys 
# import os
# os.environ["GEMINI_API_KEY"] =  keys.GOOGLEKEY

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")


while True:
    query = input("Enter query [end to stop]:")
    if query.lower() == 'end':
        break 

    response = model.invoke(query)
    print(response.content)
    print('='  * 50)


