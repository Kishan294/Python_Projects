import requests
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century"

response = requests.get(URL)
website_html = response.text
# print(website_html)
soup = BeautifulSoup(website_html, "html.parser")

all_movies_list = soup.select(selector="#maincontent h2 strong")

movies_list = []
for i in range(0, len(all_movies_list)):
    movie_name = f"{i+1}) {all_movies_list[len(all_movies_list)-i-1].getText()}"
    movies_list.append(movie_name)

with open("Movies_list.txt", 'w') as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
# print(movies_list)
