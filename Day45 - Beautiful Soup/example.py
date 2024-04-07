from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.select('.titleline a')
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

print(article_texts)
print(article_links)
print(article_upvotes)

index = article_upvotes.index(max(article_upvotes))
print(index)

print(article_texts[index*2 + 2])






















# with open('website.html', encoding='UTF-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get('href'))
