import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3",class_="title")

titles = [title.getText() for title in titles]
movies = titles[::-1]

with open("movies.txt", "w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")