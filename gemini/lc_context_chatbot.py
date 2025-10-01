 
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

messages = [SystemMessage(content = "Give short answers")]

while True:
    query = input("Enter query [end to stop, new to start new chat]:")
    if query.lower() == 'end':
        break 
 
    messages.append(HumanMessage(content = query))
    response = model.invoke(messages)

    print(response.content)
    print('='  * 50)

    messages.append(response)

    print("="  * 50)
    for message in messages:
        message.pretty_print();


