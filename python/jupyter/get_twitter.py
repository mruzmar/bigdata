#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API



consumer_key = '4sOMQjw0h6lQ8LQArqkRkzVVD'
consumer_secret = 'y9kiBdSKzxYzwRK65CgsvqZ36EUKQyA951ejNL3ymIjIatfffn'
access_token = '3297510194-9YBYBKi6gqtQXMWkXb6lXGVLEL5P13QdlbGz5sC'
access_token_secret = 'x9l8Umru6kPLuiYlK28rZ1Nj46AtI5nBTBQ5aNOCi95yW'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Si se quiere filtrar por determinados keywords
    #stream.filter(track=['python', 'javascript', 'ruby'])
    stream.filter(track=['a', 'b', 'c'])