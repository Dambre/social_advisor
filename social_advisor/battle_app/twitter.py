# -*- coding: utf-8 -*-

import pytz
from datetime import datetime

from django.conf import settings

import tweepy

from .models import WordUsage, Word
from .dictionary import exclude_by_type

def auth():
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    return auth

api = tweepy.API(auth())

 
def get_word_statistics(search_word):
    '''
    get tweets with this word
    '''
    try:
        word = search_word
        last_tweet_id = int(word.last_tweet_id)
        tweets = api.search(
            q=word.word,
            count=100,
            result_type='recent',
            since_id=last_tweet_id)
    
    except Exception:
        tweets = []

    for tweet in tweets:
        print(tweet.text)
        if last_tweet_id < tweet.id:
            last_tweet_id = tweet.id
        words = exclude_by_type(tweet.text)
        for tweet_word in words:
            try:
                word = Word.objects.get(word=tweet_word.lower())
            except Word.DoesNotExist:
                word = Word.objects.create(word=tweet_word, last_tweet_id=tweet.id)
            
            WordUsage.objects.create(
                word=word,
                retweets=tweet.retweet_count,
                likes=tweet.favorite_count,
                timestamp=pytz.utc.localize(tweet.created_at))

    word = Word.objects.get(word=search_word)
    word.update_latest_id(last_tweet_id)
