import rich 	#Use o rich. De preferencia sempre.
import requests
import json

#~		~#
with open("btsping/credentials.json") as read_file:	#Importando as chaves necessarias
	credentials = json.load(read_file)
read_file.close()
#~		~#
with open("settings.json") as read_file:	#Importa as configuracoes
	settings = json.load(read_file)
read_file.close()

def send_msg(post_id):
	msg = f"""BTS ESTA EM LIVE! ‧₊˚✩彡.
 Bts esta em live no vlive! Assista pelo app ou pelo link abaixo:
 ↳ https://www.vlive.tv/post/{post_id} ୭̥⋆*｡"""
	sendmessage = requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(credentials['tel_t']), data ={'chat_id': settings['tel_chatid'], 'text': msg}).json()
	return "sucess!"