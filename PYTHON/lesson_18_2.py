# uv add openai
from openai import OpenAI 
import json

CONFIG_FILE = "./config.json"

with open(CONFIG_FILE, "r", encoding="utf8") as file:
    config = json.load(file)

BASE_URL = config["baseURL"]
API_KEY = config["api_key"]
MODEL = config["model"]
IS_MULTIMODAL = config["image"]

MESSAGE = "Расскажи смешной анекдот про Git и обебзьянку!"


client = OpenAI(
  base_url=BASE_URL,
  api_key=API_KEY,
)

completion = client.chat.completions.create(
  model=MODEL,
  messages=[{
    "role": "user",
    "content": MESSAGE
  }]
)

print(completion.choices[0].message.content)