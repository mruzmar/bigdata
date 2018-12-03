#
import json
import pandas as pd
#import matplotlib.pyplot as plt
import re


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


def main():


	#Reading Tweets
	#print 'Reading Tweets\n'
	tweets_data_path = './data.txt'

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
            print str(tweet['text'])
	        tweets_data.append(tweet)
	    except:
	        continue


	#Structuring Tweets
	#print 'Structuring Tweets\n'
	#tweets = pd.DataFrame()
	#tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
	#tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
	#tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
	#print str(tweets)

if __name__=='__main__':
	main()