import vlivepy as vl
# -- #
from vlivepy.board import getBoardPosts
from vlivepy.connections import postIdToVideoSeq, getPostInfo
import re
# ---- #

def getLatestPost(aid, bid):
	posts = getBoardPosts(bid, aid, session=None, latest=True)

	lpost = re.search("\w\W\w\w\w\w\w\w\w\w", str(posts['data'][0])).group()

	print(lpost)

	return lpost

def detectType(pid):
	post_type = vl.postTypeDetector(pid)

	print(post_type)

	return post_type

def checkLive(pid):
	pstatus = vl.OfficialVideoPost(pid).official_video_type

	if pstatus == "LIVE":
		print("Live!")
		print("")
		return True
	else:
		print("Not live!")
		print("")
		return False

if __name__ == '__main__':
	print("Why are you running this? You should be using it as a base...")
	print("Anyways... I'll check for BTS by default.")

	lpost = getLatestPost("FE619", "3498")
	
	if detectType(lpost) == "VIDEO":
		checkLive(lpost)
		print("")

	else:
		print("Probably not live...")




