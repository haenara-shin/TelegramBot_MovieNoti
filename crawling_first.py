import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190810'
html = requests.get(url)
# print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('div.info-movie')
for title_lists in title_list:
    print(title_lists.select_one('a > strong').get_text().strip())
