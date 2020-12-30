#Reddit bot comment garbage collector
#If comment < 0, the comment will be deleted for karma protection
#TODO: Fix imports in core/or whatever is the problem
import praw
import api
def checkMyComments():
    for comment in api.reddit.redditor(api.username).comments.new():
        if comment.score < -1:
            comment.delete()