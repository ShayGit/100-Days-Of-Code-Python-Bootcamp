import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text,"html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_upvotes = soup.find_all(name="span", class_="score")
article_texts=[]
article_links=[]

for article in articles:
    article_text = article.getText()
    article_link = article.get("href")
    article_texts.append(article_text)
    article_links.append(article_link)


article_upvotes =[int(upvote.getText().split()[0]) for upvote in article_upvotes]
print(article_texts)
print(article_links)
print(article_upvotes)
max_upvote = max(article_upvotes)
index = article_upvotes.index(max_upvote)
print(article_texts[index])
print(article_links[index])