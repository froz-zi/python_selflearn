import requests

url = "https://api.github.com"

response = requests.get(url)

print("Status code:", response.status_code)
print("Data dari API:")
print(response.json())