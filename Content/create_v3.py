import json
import os
from pathlib import Path

import openai

PROMPT = "license plates with car"
data_dir = Path.cwd() / "responses"

data_dir.mkdir(exist_ok=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

file_name = data_dir / f"{PROMPT[:5]}-{response['created']}.json"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)