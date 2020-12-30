#Reddit Bot API Config File
#Setup all API work with reddit here, and import in core.
#Developed by Caleb Duress (ChefBuckeyeRBLX)
#API Version 1 12/25/20 Development Edition
import praw
#Login Details

version = "0.1.0a.1"
http_limit = 30
#id = ["client id","client secret","username","password","user agent"]
id = [] #Use above ID for actual production (so karma is alone)
reddit = praw.Reddit(client_id = id[0],
                    client_secret = id[1],
                    username = id[2],
                    password = id[3],
                    user_agent = id[4]) #Seems doesn't like just the name
print("API has been loaded and is ready.")
