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
    print("Authentication OK")
    timeline = api.home_timeline()
    #prints user's most recent 20 tweets
    '''for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")'''

    #tweets to feed
    #for i in range(0, 7):
    api.update_status("sUwU?")

    #prints a user's bio details & followers
    '''user = api.get_user("KidCudi")
    print("User detail:")
    print(user.name)
    print(user.description)
    print(user.location)
    print("Last 20 followers:")
    for follower in user.followers():
        print(follower.name)'''

    #following an account
    '''api.destroy_friendship("kanyewest")'''
except:
    print("Error during authentication")
