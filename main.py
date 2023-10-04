from telegram import*
from flask import request, Flask

TOKEN="6442939025:AAFj8oC6_RTuzIarwoWbbGpL8-GrVJ2-s-g"
bot=Bot(TOKEN)
url="https://jasmina.pythonanywhere.com/webhook/"

print(bot.set_webhook(url))