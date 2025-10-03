from huggingface_hub import InferenceClient
import keys 
model_id = "openai/gpt-oss-120b"
client = InferenceClient(model=model_id, 
                         token=keys.HUGGINGFACE_KEY, provider="novita")

messages = [
    {"role": "user", "content": "What are important 3 cities in France? Just give city names only."}
]

response = client.chat_completion(messages)
#print(response)
print(response.choices[0].message.content)
