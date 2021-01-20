#Reddit Bot API Config File
#Setup all API work with reddit here, and import in core.
#Developed by Caleb Duress (ChefBuckeyeRBLX)
#API Version 1 12/25/20 Development Edition
import praw
#Login Details

version = "0.1.0.2a"
http_limit = 30
#id = ["client id","client secret","username","password","user agent"]
id = ["1w1C7IaxLisUYQ","N8lYc84RstIwsZ1TIGVGs4hyMr8Hrw","theenigmabot","x8bwA7d2-qIoDEXC_aFoIdYnTxtugwsgQYXh2AHS8os=","Enigma Encryption Bot 0.1.2 by /u/ChefBuckeyeRBLX"]
#Use above ID for actual production (so karma is alone)
reddit = praw.Reddit(client_id = id[0],
                    client_secret = id[1],
                    username = id[2],
                    password = id[3],
                    user_agent = id[4]) #Seems doesn't like just the name
print("API has been loaded and is ready.")
