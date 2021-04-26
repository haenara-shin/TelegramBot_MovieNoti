import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190530'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
forDX = soup.select_one('span.forDX')
if (forDX):
    forDX = forDX.find_parent('div', class_='col-times')
    title = forDX.select_one('div.info-movie > a > strong').get_text().strip()
    print(title + ' 4DX 예매가 열렸습니다.')
else:
    print('4DX 예매가 아직 열리지 않았습니다.')



# title_list = soup.select('div.info-movie')
# for title_lists in title_list:
#     print(title_lists.select_one('a > strong').get_text().strip())
