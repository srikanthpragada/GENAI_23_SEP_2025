from langchain.chat_models import init_chat_model

model = init_chat_model("gemma3:1b", model_provider="ollama")
response = model.invoke("What is the capital of France?")

#print(response)
print(response.content)
