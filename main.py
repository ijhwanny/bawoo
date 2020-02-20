# -*- coding: utf-8 -*-

import requests
import telegram
from bs4 import BeautifulSoup
import time, os
from datetime import datetime
import logging, logging.handlers


##############################################################################
### Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
##############################################################################
# logging.basicConfig(filename='./server.log', level=logging.INFO)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
# fileMaxByte = 1024 * 1024 * 100

streamHandler = logging.StreamHandler()
fileHandler = logging.FileHandler('./server.log')
# fileHandler = logging.handlers.RotatingFileHandler(filename, maxBytes=fileMaxByte, backupCount=10)

streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

logger.setLevel(level=logging.INFO)


##############################################################################
### Function to return the latest post
##############################################################################
def get_latest_post() :
    req = requests.get(url)
    time.sleep(5)
    soup = BeautifulSoup(req.text, 'html.parser')
    posts = soup.find("tr", {"class" : "list"})
    return posts


##############################################################################
### Function to return the latest post id and title
##############################################################################
def get_latest_post_detail(posts) :
    post = dict();
    post['id'] = posts.find("nobr").text
    post['title'] = posts.find("a").text
    return post


##############################################################################
### Function to make an alarm message
##############################################################################
def set_message(post) :
    link = 'http://bawoosarang.com/bbs/zboard.php?id=climging'
    message = '[바우사랑: 신규산행일정] \n' + post['title'] + link
    return message


##############################################################################
### Get alarm bot and set channel_id
##############################################################################
mytoken = '...'
bot = telegram.Bot(token=mytoken)
me = bot.getMe()

# Notify a new posting to channel
mychannel = '@bawoo'


##############################################################################
### Set target url and Base directory
##############################################################################
url = 'http://bawoosarang.com/bbs/zboard.php?id=climging'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(BASE_DIR)


##############################################################################
### Main Function
##############################################################################
if __name__ == "__main__":
    latest_num = 0

    while True:
        # Get current timestamp for logging
        timestamp = datetime.now().strftime('%y-%m-%d %H:%M:%S')
        posts = get_latest_post()
        latest_post = get_latest_post_detail(posts)

        try :
            with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read :
                before = f_read.readline()

                if before != latest_post['id'] :
                    # Send a message to bot
                    msg = set_message(latest_post)
                    bot.sendMessage(mychannel, msg)
                    print("{} ===> NEW POST ID: {}\t TITLE: {}" \
                                    .format(timestamp, \
                                            latest_post['id'], \
                                            latest_post['title']))
                else :
                    print("{} ===> POST ID: {}\t TITLE: {}" \
                                    .format(timestamp, \
                                            latest_post['id'], \
                                            latest_post['title']))
                    pass
        except FileNotFoundError as ex:
                print("ERROR: {}" .format(ex))
                msg = set_message(latest_post)
                bot.sendMessage(mychannel, msg)
                print("{} ===> NEW POST ID: {}\t TITLE: {}" \
                                .format(timestamp, \
                                        latest_post['id'], \
                                        latest_post['title']))
        finally :
                f_read.close()

        with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write :
            f_write.write(latest_post['id'])
            f_write.close()

        time.sleep(30)


##############################################################################
### Reference
### https://beomi.github.io/gb-crawling/posts/2017-04-20-HowToMakeWebCrawler-Notice-with-Telegram.html
### https://colab.research.google.com/drive/1mAMKZE8xZw_zCgUwp6BWDGxO8pUccGm4#scrollTo=Ihdn-ar_DFnu
##############################################################################
