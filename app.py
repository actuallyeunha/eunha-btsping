from flask import Flask, request
import telegram
from btsping.credentials import bot_token, bot_user_name,URL
# -- #
import btsping.pingvlive as pvl
# -- #
global bot
global TOKEN

# ---- #
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)
# ---- #
@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
	update = telegram.Update.de_json(request.get_json(force=True), bot)

	chat_id = update.message.chat.id
	msg_id = update.message.message_id

	text = update.message.text.encode('utf-8').decode()

	print("[BTSPing] New message:", text)

	if text == "/start":
		bot_welcome = """
		Eu detecto sempre que os meninos entrarem em live no vlive.
		Mando as notificacoes para o canal BTS Ping, la voce pode receber avisos de um jeito mais consistente e confiavel pq convenhamos q confiar no vlive nao da certo!
		"""
		bot.sendChatAction(chat_id=chat_id, action="typing")
		sleep(1.5)
		bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
	else:
		bot_error = """
		Oh oh... Alguma coisa deu errado! Verifique o comando e tente novamente!
		"""

	return 'ok'
@app.route('/enablewatching', methods=['GET', 'POST'])
def enable_watching():
	while True:
			lpost = getLatestPost("FE619", "3498")
		
		if detectType(lpost) == "VIDEO":
			if checkLive(lpost) == True:
				print("")
				bot_live = """
				Detectei uma live no canal do BTS do vlive! Vai conferir!
				"""
				bot.sendMessage(chat_id=1682719158, text=bot_live)
				sleep(7200)
		else:
			print("Probably not live...")


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
	s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
	if s:
		return "[BTSPing] Webhook setup OK"
	else:
		return "[BTSPing] webhook setup failed"


@app.route('/')
def index():
	return '.'
# ---- #

if __name__ == '__main__':
	app.run(threaded=True)