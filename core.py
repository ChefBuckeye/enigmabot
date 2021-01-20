#Reddit Bot API Test environment
#Create main bot logic here
#Setup not to read/reply to controversial (suicide, depression, etc) subreddits.
#Developed by Caleb Duress (ChefBuckeyeRBLX)
#Core Version 0.1.2a 12/25/20 Development Edition
import random
import praw
import rater
import api
from rater import checkMyComments
from time import sleep
from app import encrypt
from praw.models import Message
#Config for reddit things
bots = ["theenigmabot","UtdStatBot"] #Bot Ignore list, best to prevent spamming any bots and read actual posts
cache = []
unread_messages = []
wordLib =["enigma","key","password","secretive","quiet","secret","confidential","classified","undisclosed", "untold","unknown","top secret","veiled","cryptic","obscure","covert","on the q.t.","private","dark secret","shrouded","decrypted","encrypted","encryption","decryption"]
reddit = api.reddit
subreddit = reddit.subreddit("testingground4bots")
#hot = subreddit.hot(limit=5) Not being used, remove if needed.
#############################
print("**************************************************************\n***********Loading ChefBuckeye's reddit Bot " + api.version + "*************\n**************************************************************\n**************************************************************")
print("Initializing bot...")
while True:
    #Submissions, comments, messages, mentions
    
    for comment in subreddit.comments(limit=25): #Reply to unread comments
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in wordLib)
        #There's a better way than caching, mark_read() and comment.read() might work better
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
                    except RATELIMIT: #Will catch rate limit exceptions instead of all exceptions, will help decoding other issues
                        print("Error! Failed to post to " + comment.id + ": " + comment.body)
                        sleep(60)
                #sleep(900)
                else:
                    print("Bots detected")
                    cache.append(comment.id)
            else:
                print("Accidentally read my own comment")
                cache.append(comment.id)
    #Reply without any notes, straight encrypted with credits
    #TODO: Double posts/replies when you mention or message the bot
    for message in reddit.inbox.unread(limit=25): #Messages
        secretMessage = encrypt(message.body) #Encrypts comment before reply
        try: #Prevent crashing the script
            message.reply(secretMessage + "\n\nEncrypted by theenigmabot by u/ChefBuckeyeRBLX. For daily keys see my user.")
            print("Replied to a mention by " + str(message.author))
            message.mark_read()
            sleep(30) #Just to prevent overly fast spam
        except RATELIMIT:
            print("Error! Failed to reply to " + str(message.author) + message.body)
            sleep(60)
    #Reply without any notes, though do note that they were called with credits and encryption.
    for mention in reddit.inbox.mentions(limit=25): #Mentions
        secretMessage = encrypt(mention.body) #Encrypts comment before reply
        if mention.id not in cache:
            try: #Prevent crashing the script
                mention.reply(secretMessage + "\n\nEncrypted by theenigmabot by u/ChefBuckeyeRBLX. For daily keys see my user.")
                print("Replied to a mention by " + str(mention.author))
                mention.mark_read()
                cache.append(mention.id)
                sleep(30) #Just to prevent overly fast spam
            except RATELIMIT:
                print("Error! Failed to reply to " + str(mention.author) + mention.body)
                sleep(60)
    #checkMyComments()
#Daily new keys
#Post keys on user board
################################
#DEVELOPMENT EDITION --- DO NOT TEST LIVE UNLESS SUPERVISED
