import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)




url = "https://timesofindia.indiatimes.com/"

fetchAndSaveToFile(url, "E:\\Data Engineering\\Web-Scraping\\times.html")