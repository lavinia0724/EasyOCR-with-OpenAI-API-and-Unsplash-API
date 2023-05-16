import requests
import json
import os

access_key = os.getenv('ACCESS_KEY')
base_url = 'https://api.unsplash.com/'

def download_image(url, file_path, output):
    response = requests.get(url)
    with open(output + '/' + file_path, 'wb') as file:
        file.write(response.content)

def search_and_download(query, count, output):
    search_url = base_url + 'search/photos'
    headers = {'Authorization': 'Client-ID ' + access_key}
    params = {'query': query, 'per_page': count}
    response = requests.get(search_url, headers=headers, params=params)
    data = json.loads(response.text)
    # print(data)

    for i, photo in enumerate(data['results']):
        image_url = photo['urls']['regular']
        file_path = f'image_{i}.jpg'
        download_image(image_url, file_path, output)

def main():
    query = input("Enter your search query: ")
    count = int(input("Enter the number of images to download: "))

    cur_dir = os.getcwd()
    output = cur_dir + f'/{query}'
    if not os.path.exists(output):
        os.mkdir(output)

    search_and_download(query, count, output)

if __name__ == '__main__':
    main()
