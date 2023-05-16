import os

import openai

PROMPT = "license plate from an image with many cars"

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

print(response["data"][0]["b64_json"][:50])