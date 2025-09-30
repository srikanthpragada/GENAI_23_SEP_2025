import keys 
import os 
from langchain.chat_models import init_chat_model

os.environ["OPENAI_API_KEY"] = keys.OPEN_AI_KEY

model = init_chat_model("gpt-4o-mini", model_provider="openai")

response = model.invoke("What is the capital of France?")
print(response.content)
print(response.response_metadata['token_usage']['total_tokens'])

