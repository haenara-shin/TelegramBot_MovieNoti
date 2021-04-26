import requests
#import telegram
from bs4 import BeautifulSoup
#from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = 'INPUTYOURTOKEN') # input your token
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190530'
def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    forDX = soup.select_one('span.forDX')
    if (forDX):
        forDX = forDX.find_parent('div', class_='col-times')
        title = forDX.select_one('div.info-movie > a > strong').get_text().strip()
        bot.sendMessage(chat_id=947502140, text=title + ' 4DX 예매가 열렸습니다.')
        sched.pause()
        #print(title + ' 4DX 예매가 열렸습니다.')
    else:
        bot.sendMeassge(chat_id=947502140, text='4DX 예매가 아직 열리지 않았습니다.')

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()
#
#
# import telegram
#
# bot = telegram.Bot(token = 'YOURTOKEN')
#
# for i in bot.getUpdates():
#     print(i.message)
#
# bot.sendMessage(chat_id=947502140, text='This is a test!!!')


