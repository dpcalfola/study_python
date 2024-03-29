import requests
from bs4 import BeautifulSoup

titles = []
search_word = '한국축구'
url = f'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query={search_word}&oquery={search_word}&tqi=h2vymdp0Jy0ss5iZ6dhssssstvh-255036&acq={search_word}&acr=1&qdt=0'
# print(url)

req = requests.get(url)
html = req.text
# print(html)

soup = BeautifulSoup(html, 'html.parser')
search_result = soup.select_one('.list_news')
news_links = search_result.select('.bx > .news_wrap > .news_area > .news_contents > .news_tit')

# print(news_links)

for i in news_links:
    titles.append(i.get_text())

print(titles)
