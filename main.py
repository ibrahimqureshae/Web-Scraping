import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)

url = "https://timesofindia.indiatimes.com/"

r = requests.get(url)
print (r.text) 