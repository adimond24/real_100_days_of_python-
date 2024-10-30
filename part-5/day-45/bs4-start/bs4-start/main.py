from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links= []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

# print(article_text)
# print(article_link)
# print(int(article_upvote[0].split()[0]))




# with open("website.html") as files:
#     contents = files.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.getText())