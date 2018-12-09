#coding=utf-8
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

def main():
    bot = Bot()
    bot.run()

@respond_to('今何時？')
def now(message):
    strftime = datetime.now(JST).strftime("%Y/%m/%d %H時%M分%S秒だよ～")
    message.reply(strftime)

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()