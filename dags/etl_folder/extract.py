import pandas as pd
import json
import tweepy
import s3fs
from datetime import datetime
import os
from dotenv import load_dotenv

# Extract information from .env file
load_dotenv()
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
def extract(consumer_key, consumer_secret, access_token, access_token_secret):
    #Conection to Twitter
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    api = tweepy.API(auth)

    tweets = api.user_timeline(
        screen_name = '@JMilei',
        count = 200,
        include_rts = False,
        tweet_mode = 'extended'
    )

    tweets_list =[]
    for tweet in tweets:
        text = tweet._json['full_text']
        
        data_extract = {
            'user': tweet.user.screen_name,
            'text': text,
            'favorite_count': tweet.favorite_count,
            'retweet_count': tweet.retweet_count,
            'created_at': tweet.created_at
        }
        tweets_list.append(data_extract)
        
    df = pd.DataFrame(tweets_list)

    df.to_csv('milei_tweets.csv')