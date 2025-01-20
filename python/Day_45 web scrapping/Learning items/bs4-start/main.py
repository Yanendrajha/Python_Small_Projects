from bs4 import BeautifulSoup


import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

# Creating the soup object & using the find_all methid to get hold of the name,link & upvote of te daily popular news.

soup = BeautifulSoup(yc_webpage, "html.parser")
article_tag = soup.find_all(name="span", class_="titleline")
texts = []
links = []
i = 0
for article in article_tag:
    article_tag_inside = article.find(name="a")
    texts.append(article_tag_inside.getText())
    links.append(article_tag_inside.get("href"))
    i += 1

upvote = [score.getText() for score in soup.find_all(name="span", class_="score")]

i = len(upvote)

for j in range(0, i):
    print(texts[j])
    print(links[j])
    print(upvote[j].split(" ")[0])























# with open("website.html") as file:
#   contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# with soup, we can use the entire html code within python, use it, change it, or even rewrite it.

# print all the html code
# print(soup)

# print all html code with correct indentation
# print(soup.prettify())

# Collect all anchor tags
# all_anchor_tags = soup.find_all(name="a")

# print all anchor tags
# print(all_anchor_tags)

# print all the text or string part from the anchor tags

# for tag in all_anchor_tags:

# print all the text or string part from the anchor tags
# print(tag.getText())

# print any tag we wish to use
# print(tag.get("href"))


# find item by tags or queries
# here targeting the h1 tag and id of the particular sentence I wanted. (we can find it by using the id,class, or any targeting attribute

# heading = soup.find(name="h1", id="name")
# print(heading)

# printing the text inside the h1 tag
# print(heading.getText())

# selecting  item with the help of css selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)
# print(company_url.get("href"))
# print(company_url.getText())



