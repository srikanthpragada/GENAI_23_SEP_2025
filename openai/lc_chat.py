from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4o-mini", model_provider="openai")

response = model.invoke("What is the capital of France?")
print(response.content)
print(response.usage_metadata['total_tokens'])

