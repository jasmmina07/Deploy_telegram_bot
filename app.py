import os 
from flask import Flask, request
import telegram

TOKEN='6442939025:AAFj8oC6_RTuzIarwoWbbGpL8-GrVJ2-s-g'

app = Flask(__name__)

@app.route('/webhook/',methods=["POST", "GET"])
def main():
    if request.method == "POST":
        update = request.get_json()

        text = update['message']['text']
        chat_id = update['message']['chat']['id']

        bot = telegram.Bot(TOKEN)

        bot.sendMessage(chat_id, text)

        return 'Ok'
    else:
        return {"result": "Only post request"}


if __name__ == "__main__":
    app.run(debug=True)