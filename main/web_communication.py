import requests

url = "localhost:3000"
r = requests.get(url)
text = r.text
print(text)