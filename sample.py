import requests
import telegram
import time
from bs4 import BeautifulSoup

bot = telegram.Bot(token='1071428517:AAGNs7k2uOFyCorK2TnmMJpevsa6F21qMf0')
# me = bot.getMe()
chat_id = bot.getUpdates()[-1].message.chat.id

url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'
# url = 'http://www.bawoosarang.com'

if __name__ == "__main__":
    latest_num = 0

    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        posts = soup.find("tr", {"class" : "list1"})
        post_num = posts.find("td", {"class" : "eng list_vspace"}).text

        if latest_num != post_num :
            latest_num = post_num
            link = 'http://www.ppomppu.co.kr/zboard/'+posts.find("td", { "valign" : "middle"}).find("a").attrs['href']
            title = posts.find("font", {"class" : "list_title"}).text

            # Send a message to bot
            msg = '[새글]\n' + title + link
            print(msg)
            bot.sendMessage(chat_id, msg)

            print(title)
            print(link)

        time.sleep(30)
        print('Latest Number: ' + latest_num)
