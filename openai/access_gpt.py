from openai import OpenAI
import keys 
import os

os.environ["OPENAI_API_KEY"] = keys.OPEN_AI_KEY

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="What is the capital of Spain?"
)

print(response.output_text)