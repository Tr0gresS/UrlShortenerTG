import requests
import telegram.error
from telegram.ext import Updater, CommandHandler


Bitl_Token = "<<<<<BİTLY-TOKEN>>>>>>>"
Tg_BotToken = "<<<<<<BOT-TOKEN>>>>>>>"


def url_shortener(update, context):
    try:
        url_ = (str(update.message.text).split(" ")[1])
        header = {
            "Authorization": F"Bearer {Bitl_Token} ",
            "Content-Type": "application/json"
        }
        params = {
            "long_url": str(url_)
        }

        response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=params, headers=header)
        kisa_url = response.json()["link"]
        orjinal_url = response.json()["long_url"]
        message_ = f"""

🔸 Adı : {update.message.from_user.first_name}

⚫️Orjinal Url  : {orjinal_url}

🟢 Kısaltılmış Url : {kisa_url}\n\n

        
        """

        update.message.reply_text(message_)

    except telegram.error.NetworkError and KeyError:
        pass






if __name__ == '__main__':
    updater = Updater(Tg_BotToken, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("url", url_shortener))

    updater.start_polling()
    updater.idle()