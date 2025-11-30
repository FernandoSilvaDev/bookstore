import requests

url = "http://127.0.0.1:8000/bookstore/v1/product/"
headers = {"Authorization": "Token e110154a212211f6e59bab2dad61d66cd3810a69"}

response = requests.get(url, headers=headers)
print(response.json())