#pip install google-genai
#Create key using https://aistudio.google.com/apikey

from google import genai

# create GEMINI_API_KEY environment variable 
# or 
# client = genai.Client(api_key="YOUR_API_KEY")

client =  genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="List names of 5 important cities in India. Just give names."
)
print(response.text)
 
