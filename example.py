import tweepy

#Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

#Create API object
api = tweepy.API(auth)

#Create tweet
api.update_status("Hi Twitter")
