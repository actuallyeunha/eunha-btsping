import json
from re import search

import vlivepy as vl
from vlivepy.board import getBoardPosts
from vlivepy.connections import postIdToVideoSeq, getPostInfo

#~		~#
def getLatestPost(cid, bid):
	b_posts = getBoardPosts(cid, bid, session=None, latest=True)
	l_post = search("\w\W\w\w\w\w\w\w\w\w", str(b_posts['data'][0])).group()

	return l_post


def isItVideo(pid):
	post_type = vl.postTypeDetector(pid)

	if post_type == "VIDEO":
		return True
	else:
		return False


def isItLive(pid):
	post_status = vl.OfficialVideoPost(pid).official_video_type

	if post_status == "LIVE":
		return True
	else:
		return False
