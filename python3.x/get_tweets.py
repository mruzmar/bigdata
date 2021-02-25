#Si no se encuentra instalado tweepy
# pip install tweepy
# o si se necesitan permisos: sudo pip install tweepy
import tweepy

#Variables that contains the user credentials to access Twitter API 
access_token = "15002884-QxpvkW1jNTQ3YpO9Vn4yW9Cx8n7UyvwdVzVkrmMbw"
access_token_secret = "eaFWhbH2Mn1trxlYoKlLZsk3nzkk4wsiaFTyIkDbLEYob"
consumer_key = "C1voYrjnzAcwjRU1k8SmL72vK"
consumer_secret = "Uvk3ljIL8duuLM7XxLXrlXBBEkHDl040dxgJox8p9pdJVcxRjh"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = "madrid"
# Language code (follows ISO 639-1 standards)
language = "es"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.user.screen_name,"Tweeted:",tweet.text)