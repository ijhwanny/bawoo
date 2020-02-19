import telegram

bot = telegram.Bot(token='1071428517:AAGNs7k2uOFyCorK2TnmMJpevsa6F21qMf0')

#생성한 텔레그램 봇 정보
me = bot.getMe()
print(me)

#생성한 텔레그램 봇 /start 시작 후 사용자 id 받아 오기

chat_id = bot.getUpdates()[-1].message.chat.id
print('user id :', chat_id)



#사용자 id로 메시지 보내기
bot.sendMessage(chat_id, u'bot이 보낸 메시지')
