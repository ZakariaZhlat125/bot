import re 
from flask import Flassk ,request
import telegram 
from telebot.credetials import bot_token ,bot_user_name,URL

global bot
global TOKEN 
TOKEN=bot_token
bot =telegram.Bot(token=TOKEN)

app=Flask(__name__)
@app.route('/{}'.format(TOKEN),methods=['POST'])
def respond():
    update=telegram.Update.de_json(request.get_json(force=True),bot)
    chat_id=update.message.chat.id
    msg_id =update.message.message_id
    text=update.message.text.encode('utf-8').decode()
    print("got text message:",text)
    if text=="/start":
        bot_welcome="""
        Welcome to coolAvatar bot , the bot is using the service from
        http://avatars.adorable.io/ to generate cool looking avatar based on the name
        you enter so please enter a name and the bot will reply with an avatar for your name.
        """
        bot.sendMessage(chat_id=chat_id,text=bot_welcome,reply_to_message_id=msg_id)
    else:
        try:
            text=re.sub(r"\W","_",text)
            url="https://api.adorable.io/avatars/285/{}.png".format(text.strip())
            bot.sendPhoto(chat_id=chat_id,photo=url, reply_to_message_id=msg_id)
        Exception:
        bot.sendMessage(chat_id=chat_id,text="There was a problem in the name you used ,please enter different name",reply_to_message_id=msg_id)
    return 'ok'
@app.route('/set_webhook',method=['GET','POST'])
def set_webhook():
    s=bot.setWebhook('{URL}{HOOK}'.format(URL=URL,HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
@app.route('/')
def index():
    return '.'

if __name__=='__main__':
    app.run(threaded=True)
        