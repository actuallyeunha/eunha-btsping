import requests
from time import sleep
# ---- #
import btsping.pingvlive as vl
from btsping.credentials import bot_token, api_key, api_secret, access_token, access_token_secret
# -- #
token = bot_token
# -- #

def sendMessage(token, id, status, twiapi):
	api = twiapi
	livemessage = f'''
	BTS ESTA EM LIVE! ‧₊˚✩彡.
	Bts esta em live no vlive! Assista pelo app ou pelo link abaixo:
	↳ https://www.vlive.tv/post/{vl.getLatestPost("FE619", "3498")} ୭̥⋆*｡
	'''
	notlivemessage = '''
	BTS NAO ESTA EM LIVE! ‧₊˚✩彡.
	Mas quando estiver, assista pelo app ou pelo site:
	↳ https://www.vlive.tv/channel/FE619 ୭̥⋆*｡
	'''

	if status == "live":
		response = requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data ={'chat_id': id, 'text': livemessage}).json()
		api.update_status(livemessage)
	else:
		return "opa, algo deu errado"

# ---- #

if __name__ == '__main__':
	auth = tweepy.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	while True:
		lpost = vl.getLatestPost("FE619", "3498")

		if vl.detectType(lpost) == "VIDEO":
			if vl.checkLive(lpost) == True:
				print("ALERTA DE LIVE!")
				sendMessage(token, "-1001378910921", "live", api)
				sleep(14400)
				continue
			else:
				print("NAO ESTAO EM LIVE!")
				sendMessage(token, "-1001378910921", "live", api)
				sleep(180)
				continue
		else:
			print("ULTIMO POST NAO E LIVE")
			sleep(180)
			continue
