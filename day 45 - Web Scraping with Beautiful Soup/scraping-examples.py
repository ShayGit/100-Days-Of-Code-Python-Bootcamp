from bs4 import BeautifulSoup
#import lxml


with open("website.html",encoding="utf8") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
#print(soup.prettify())
#print(soup.title)
#(soup.title.string)

#print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
#
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)