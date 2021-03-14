import requests
from time import sleep
# ---- #
import tweepy
# ---- #
import btsping.pingvlive as vl
from btsping.credentials import bot_token
# -- #
token = bot_token
# -- #

def sendMessage(token, id, status):
	livemessage = f'''
	BTS ESTA EM LIVE! ‧₊˚✩彡.
	Bts esta em live no vlive! Assista pelo app ou pelo link abaixo:
	↳ https://www.vlive.tv/post/{vl.getLatestPost("FE619", "3498")}୭̥⋆*｡
	'''
	notlivemessage = '''
	BTS NAO ESTA EM LIVE! ‧₊˚✩彡.
	Mas quando estiver, assista pelo app ou pelo site:
	↳ https://www.vlive.tv/channel/FE619 ୭̥⋆*｡
	'''

	if status == "live":
		response = requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data ={'chat_id': id, 'text': livemessage}).json()
	else:
		response = requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data ={'chat_id': id, 'text': notlivemessage}).json()


# ---- #

if __name__ == '__main__':
	while True:
		lpost = vl.getLatestPost("FE619", "3498")

		if vl.detectType(lpost) == "VIDEO":
			if vl.checkLive(lpost) == True:
				sendMessage(token, "-1001378910921", "live")
				sleep(14400)
				continue
			else:
				print("Last post is not a video!")
				sleep(180)
				continue
		else:
			print("Last post is not a video!")
			sleep(180)
			continue
