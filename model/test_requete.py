import requests

requete = {"word":"table"}

url = 'http://127.0.0.1:5000/'
res = requests.post(url, data=requete)
output = res.text

print(output)