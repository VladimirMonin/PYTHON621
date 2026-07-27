# Продолжение развития программы из 18_2.py


# uv add openai
from openai import OpenAI
import json

CONFIG_FILE = "./data/config.json"

with open(CONFIG_FILE, "r", encoding="utf8") as file:
    config = json.load(file)


def read_file(file_path: str, file_type: str = "text") -> dict | str:
    if file_type not in ["text", "json"]:
        raise ValueError("file_type может быть только или text или json")

    if file_type == "text":
        with open(file_path, "r", encoding="utf8") as file:
            return file.read()
    elif file_type == "json":
        with open(file_path, "r", encoding="utf8") as file:
            return json.load(file)
    
    return ""


config = read_file(CONFIG_FILE, "json")

if isinstance(config, dict):
    BASE_URL = config["baseURL"]
    API_KEY = config["api_key"]
    MODEL = config["model"]
    IS_MULTIMODAL = config["image"]

else:
    raise Exception("С конфигом что-то не так!!! ААААА!!!!")

MESSAGE = "Расскажи смешной анекдот про Git и обебзьянку!"


client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

completion = client.chat.completions.create(
    model=MODEL, messages=[{"role": "user", "content": MESSAGE}]
)

print(completion.choices[0].message.content)
