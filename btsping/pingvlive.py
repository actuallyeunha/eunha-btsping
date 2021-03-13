import vlivepy as vl
# -- #
from vlivepy.board import getBoardPosts
from vlivepy.connections import postIdToVideoSeq, getPostInfo
import re
from .credentials import bot_token
# ---- #

token = bot_token

def getLatestPost(aid, bid):
	posts = getBoardPosts(bid, aid, session=None, latest=True)

	lpost = re.search("\w\W\w\w\w\w\w\w\w\w", str(posts['data'][0])).group()

	return lpost

def detectType(pid):
	post_type = vl.postTypeDetector(pid)
	return post_type

def checkLive(pid):
	pstatus = vl.OfficialVideoPost(pid).official_video_type

	if pstatus == "LIVE":
		return True
	else:
		return False

if __name__ == '__main__':
	print("Why you using this bare? use app.py!")