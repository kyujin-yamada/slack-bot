from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run()

@respond_to('今何時？')
def now(message):
    strftime = datetime.now().strftime("%Y/%m/%d %H時%M分%S秒だよ～")
    message.reply(strftime)

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()