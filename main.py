from telegram import Bot

TOKEN="6665234104:AAF_jMyABpGRuWBmHqQ5TmnFykcqyCFc_NA"
bot=Bot(TOKEN)
url="https://jasmina07.pythonanywhere.com/"

#print(bot.set_webhook(url))
# print(bot.delete_webhook())
print(bot.get_webhook_info())