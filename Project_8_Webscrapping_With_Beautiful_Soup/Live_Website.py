from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_we_page = response.text

soup = BeautifulSoup(yc_we_page, "html.parser")

articles = soup.find_all(name='a', class_="titlelink")
article_text = []
article_link = []

for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.get("href")
    article_link.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_='score')]
# print(article_text)
# print(article_link)
# print(article_upvote)

max_upvote = article_upvote[0]

for max in article_upvote:
    if max_upvote < max:
        max_upvote = max
index = article_upvote.index(max)

print(f"Max upvote is: {max_upvote}\nTitle is {article_text[index]}\nLink is: {article_link[index]}")