import tweepy
from os import environ

#keys and values on heroku dashboard    
'''CONSUMER_KEY = environ['CONSUMER_KEY']  
CONSUMER_SECRET = environ['CONSUMER_SECRET'] 
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']'''

auth = tweepy.OAuthHandler("7XQIiej0rjCgtF2cyh7rHLM18", "Y5D5YbXMZbBbhnFb5GMNXG17TL3vvB0ZicyWCiCm3Wvk9J6C0e")
auth.set_access_token("1158777417735036934-yWh83v9i2r1XhRmJzlbbqH1OsZiIjD", "2JJh0OlCjrxuajcbYgoyvTZJTQO3vyOVt0PNhAfSNz3py")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication")
    timeline = api.home_timeline()

    api.update_status("hoes mad")
    #time.sleep(60*2) #tweets every 2 minutes
except:
    print("Error during authenication")
