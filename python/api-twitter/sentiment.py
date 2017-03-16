from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey = '4sOMQjw0h6lQ8LQArqkRkzVVD'
csecret = 'y9kiBdSKzxYzwRK65CgsvqZ36EUKQyA951ejNL3ymIjIatfffn'
atoken = '3297510194-9YBYBKi6gqtQXMWkXb6lXGVLEL5P13QdlbGz5sC'
asecret = 'x9l8Umru6kPLuiYlK28rZ1Nj46AtI5nBTBQ5aNOCi95yW'



from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):

		all_data = json.loads(data)

		tweet = all_data["text"]
		sentiment_value, confidence = s.sentiment(tweet)
		print(tweet, sentiment_value, confidence)

		if confidence*100 >= 80:
			output = open("twitter-out.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])
