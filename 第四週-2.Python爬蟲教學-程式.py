import requests
from bs4 import BeautifulSoup
import csv

url = "https://tw.news.yahoo.com/"

headers = {
    "User-Agent": "Mozilla/5.0" }
response = requests.get(url, headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("h3")

news_list = []

for title in titles:
    text = title.get_text()
    news_list.append(text)
    print(text)
    
with open("news.csv", "w", newline="", encoding="utf-8-sig") as file:

    writer = csv.writer(file)

    writer.writerow(["News Title"]) 

    for news in news_list:
        writer.writerow([news])