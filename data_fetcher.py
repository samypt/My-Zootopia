import requests
import os
from dotenv import load_dotenv

load_dotenv("keys.env")
API_KEY = os.getenv("API_KEY")
HEADERS = {'X-Api-Key': API_KEY}
URL = 'https://api.api-ninjas.com/v1/animals?name='


def fetch_data(animal):
    full_url = URL + animal
    try:
        response = requests.get(full_url, headers=HEADERS)
        response.raise_for_status()  # Raises an error if the request failed
        if response.status_code == requests.codes.ok:
            print('response was successful')
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Error fetching animal data: {e}")