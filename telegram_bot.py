import telegram

bot = telegram.Bot(token = 'INPUTYOURTOEKN')

for i in bot.getUpdates():
    print(i.message)

bot.sendMessage(chat_id=947502140, text='This is a test!!!')
