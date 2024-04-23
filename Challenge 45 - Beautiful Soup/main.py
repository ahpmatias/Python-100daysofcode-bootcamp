import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_website_html = response.text
soup = BeautifulSoup(movies_website_html, 'html.parser')
titles_list = [title.getText() for title in soup.find_all(name='h3', class_='title')]
titles_list.reverse()

with open('movie_ranking.txt', mode='w', encoding='utf-8') as file:
    for movie in titles_list:
        file.write(f'{movie}\n')



