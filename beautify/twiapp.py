import rich 	#Use o rich. De preferencia sempre.
import json

import tweepy

#~		~#
with open("btsping/credentials.json") as read_file:	#Importando as chaves necessarias
	credentials = json.load(read_file)
read_file.close()

auth = tweepy.OAuthHandler(credentials['twiapi_k'], credentials['twiapi_s'])
auth.set_access_token(credentials['twiac_t'], credentials['twiac_t_s'])
twiapi = tweepy.API(auth)
#~		~#

def twi_post(post_id):
	msg = f"""BTS ESTA EM LIVE! ‧₊˚✩彡.
 Bts esta em live no vlive! Assista pelo app ou pelo link abaixo:
 ↳ https://www.vlive.tv/post/{post_id} ୭̥⋆*｡"""
	twiapi.update_status(msg)