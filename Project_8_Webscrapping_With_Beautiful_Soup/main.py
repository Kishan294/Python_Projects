from bs4 import BeautifulSoup
import lxml

with open("website.html", "r", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))  # Provide only link

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url.getText())
