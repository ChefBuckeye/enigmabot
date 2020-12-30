#Reddit Bot API Test environment
#Create main bot logic here
#Setup not to read/reply to controversial (suicide, depression, etc) subreddits.
#Developed by Caleb Duress (ChefBuckeyeRBLX)
#Core Version 0.1 12/25/20 Development Edition
import random
import praw
import rater
import api
from rater import checkMyComments
from time import sleep
from app import encrypt
#Config for reddit things
bots = ["theenigmabot","UtdStatBot"] #Bot Ignore list, best to prevent spamming any bots and read actual posts
cache = []
wordLib =["enigma","code","key","password","secretive","quiet","secret","confidential","classified","undisclosed", "untold","unknown","top secret","veiled","cryptic","obscure","covert","on the q.t.","private","dark secret","shrouded","decrypted","encrypted","encryption","decryption"]
reddit = api.reddit
subreddit = reddit.subreddit("testingground4bots")
hot = subreddit.hot(limit=5)

def Sweep(): #Comments and submissions
    print("Grabbing latest posts...")
    #for submission in subreddit.stream.submissions(pause_after=4):
    #    print(submission.title)
    print("Checking comments...")
    for comment in subreddit.stream.comments():
        #print(comment.body)
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in wordLib)
        if comment.id not in cache and isMatch:
            print("Match found! Comment ID: " + comment.id)
            secretMessage = encrypt(comment.body) #Encrypts comment before reply
            if str(comment.author) != "theenigmabot": #Prevents replying to self
                if str(comment.author) != "UtdStatBot":
                    try: #Prevent crashing the script
                        comment.reply("I see this is a " + wordLib[random.randrange(0, len(wordLib) - 1)] + " topic, may I suggest a better comment?\nHere I encrypted your message for you so you can edit and replace:\n" + secretMessage + "\nIf you need to decrypt this you can click here. This is an automated message.")
                        print("Replied to " + str(comment.author) + " at " + comment.id)
                        cache.append(comment.id)
                        sleep(200) #Just to prevent overly fast spam
                    except Exception:
                        print("Error! Failed to post to " + comment.id + ": " + comment.body)
                        sleep(60)
                #sleep(900)
            else:
                print("Accidentally read my own comment")
                cache.append(comment.id)
    print("Finished sweep. This is a development branch, so there is no autonomous loop")
    checkMyComments()
#for submission in hot_python:
#    if not submission.stickied:
#        print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(submission.title,
#                                                                        submission.ups,
#                                                                        submission.downs,
#                                                                        submission.visited))
        #ups = submission.ups
        #submission.reply("Hello, I'm a bot in a development app. This page has " + str(ups) + " upvotes.")
#Enigma machine bot
#Scrape comments and submissions for keywords/phrases
#Send body to app.py to encrypt and return.
def onLaunch():
    print("**************************************************************\n***********Loading ChefBuckeye's reddit Bot " + api.version + "*************\n**************************************************************\n**************************************************************")
    print("Initializing bot...")
    Sweep()


onLaunch()
#DEVELOPMENT EDITION --- DO NOT TEST LIVE UNLESS SUPERVISED