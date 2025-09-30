#pip install openai
#Create key using https://platform.openai.com/api-keys

from openai import OpenAI
import keys

client = OpenAI(api_key=keys.OPEN_AI_KEY)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=False,
  messages=[
    {"role": "user",
     "content": "Who won IPL 2025"}
  ]
)

print(completion.choices[0].message.content);
