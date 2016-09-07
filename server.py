import time
from slackclient import SlackClient

from bot import Bot

bot = Bot()

with open('history.txt', 'r') as fh:
    for line in fh:
        bot.add_sentence(line.strip())

token = "GET YOUR OWN TOKEN"  # found at https://api.slack.com/web#authentication
sc = SlackClient(token)

fh = open('history.txt', 'a')

if sc.rtm_connect():

    while True:
        evts = sc.rtm_read()

        for evt in evts:
            if evt["type"] == "message" and "text" in evt:
                if evt["text"].lower().startswith("hey bot"):
                    sc.api_call("chat.postMessage",
                                channel="#general",
                                text=bot.get_sentence(),
                                username="august_bot",
                                icon_emoji=":robot_face:")
                else:
                    if "subtype" not in evt or ("subtype" in evt and evt["subtype"] != "bot_message"):
                        fh.write(evt['text']+'\n')
                        bot.add_sentence(evt["text"])

        time.sleep(1)
else:
    print("Connection Failed, invalid token?")

fh.close()
