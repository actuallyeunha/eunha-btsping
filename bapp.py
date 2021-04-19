from console import console
import json
#~
from time import sleep
from datetime import datetime
#~
import teleapp
import twiapp
#~
import btsping.vliveping as vl

#~		~#
with open("settings.json") as read_file:	#Importa as configuracoes.
	settings = json.load(read_file)
read_file.close()

#~	~	~#
def load_settings(old_settings):
	old_settings = old_settings
	with open("settings.json") as read_file:
		settings = json.load(read_file)
	read_file.close()

	if old_settings != settings:
		console.print("[info]INFO[text]: Novas configuracões detectadas! Recarregando...")
		return settings
	else:
		return old_settings
		pass

def load_posts():	#Importa informacoes de lives passadas.
	with open("posts.json") as read_file:	
		posts = json.load(read_file)
	read_file.close()
	return posts

def get_time():
	now = datetime.now()
	current_time = now.strftime("%H:%M%p")
	return current_time

#~	~	~#
if __name__ == '__main__':
	while True:
		posts = load_posts()
		settings = load_settings(settings)
		l_post = vl.getLatestPost(settings['c_id'], settings['b_id'])
		if l_post != posts['latest']:
			if vl.isItVideo(l_post) == True:

				if vl.isItLive(l_post) == True:

					if l_post != posts['latest_live']:
						print("\r\033[K", end="\r")
						console.print(f"[info]{get_time()} ୭̥⋆*｡ [Check][text]: Live detectada!\n")

						if settings['Telegram'] == "True":
							console.print(f"[info]{get_time()} ୭̥⋆*｡ [Teleapp][text]: Mandando mensagem!")
							teleapp.send_msg(l_post)
						else:
							pass

						if settings['Twitter'] == "True":
							console.print(f"[info]{get_time()} ୭̥⋆*｡ [Twiapp][text]: Fazendo post!")
							twiapp.twi_post(l_post)
							pass
						else:
							pass

						posts['latest_live'] = l_post #Reescreve o id da ultima live feita.
						with open("posts.json", 'w') as write_file:
							json.dump(posts, write_file, indent=1)
						write_file.close()

						posts['latest'] = l_post #Reescreve o id da ultima live feita.
						with open("posts.json", 'w') as write_file:
							json.dump(posts, write_file, indent=1)
						write_file.close()
						sleep(10)
						continue
					else:
						print("\r\033[K", end="\r")
						console.print(f"[info]{get_time()} ୭̥⋆*｡ [Check][text]: Mesma live de antes!", end="")
						posts['latest'] = l_post #Reescreve o id do ultimo post feito.
						with open("posts.json", 'w') as write_file:
							json.dump(posts, write_file, indent=1)
						write_file.close()
						sleep(60)
						continue

				else:
					print("\r\033[K", end="\r")
					console.print(f"[info]{get_time()} ୭̥⋆*｡ [Check][text]: Não é uma live!", end="")
					posts['latest'] = l_post #Reescreve o id do ultimo post feito.
					with open("posts.json", 'w') as write_file:
						json.dump(posts, write_file, indent=1)
					write_file.close()
					sleep(60)
					continue
			else:
				print("\r\033[K", end="\r")
				console.print(f"[info]{get_time()} ୭̥⋆*｡ [Check][text]: Post não é um video!", end="")
				posts['latest'] = l_post #Reescreve o id do ultimo post feito.
				with open("posts.json", 'w') as write_file:
					json.dump(posts, write_file, indent=1)
				write_file.close()
				sleep(60)
				continue
		else:
			print("\r\033[K", end="\r")
			console.print(f"[info]{get_time()} ୭̥⋆*｡ [Check][text]: Mesmo post de antes!", end="")
			posts['latest'] = l_post #Reescreve o id do ultimo post feito.
			with open("posts.json", 'w') as write_file:
				json.dump(posts, write_file, indent=1)
			write_file.close()
			sleep(60)
			continue
