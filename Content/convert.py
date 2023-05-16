import json
from base64 import b64decode
from pathlib import Path

data_dir = Path.cwd() / "responses"
json_file = data_dir / "licen-1684206176.json"
image_dir = Path.cwd() / "images" / json_file.stem

image_dir.mkdir(parents=True, exist_ok=True)

with open(json_file, mode="r", encoding="utf-8") as file:
    response = json.load(file)

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = image_dir / f"{json_file.stem}-{index}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)