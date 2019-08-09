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

    while True:
        api.update_status("Fuckers in school telling me, always in the barber shop
\"Chief Keef ain't 'bout this, Chief Keef ain't 'bout that. My boy a BD...\"")
        time.sleep(60*3) #tweets every 3 minutes
except:
    print("Error during authenication")
