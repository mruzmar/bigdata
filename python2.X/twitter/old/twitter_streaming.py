#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 


access_token = "15002884-QxpvkW1jNTQ3YpO9Vn4yW9Cx8n7UyvwdVzVkrmMbw"
access_token_secret = "eaFWhbH2Mn1trxlYoKlLZsk3nzkk4wsiaFTyIkDbLEYob"
consumer_key = "C1voYrjnzAcwjRU1k8SmL72vK"
consumer_secret = "Uvk3ljIL8duuLM7XxLXrlXBBEkHDl040dxgJox8p9pdJVcxRjh"



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

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])