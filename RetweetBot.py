# Twitter : @DiscriminantBot
# Bot which retweets the tweets having Arificial Intelligence in their contents.


import tweepy
import time

def tconfig():
    global api, finp
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    print('| Pranit Twitter Retweet Bot | ')
    print('\nRateLimit Cooldown (If Any)...\n')

def Retweet():
    count = 0
    criteria = 'Artificial Intelligence'
    # criteria = input('Enter Tweet/Hashtag/Username/Screen-name (As Criteria) : ')
    print('\nRetweet List:-')
    while True:
        try:
            time.sleep(10)
            target_tweets = api.search(q=criteria)
        except:
            time.sleep(15*60)
        for tweet in reversed(target_tweets):
            try:
                api.retweet(tweet.id)
            except:
                #print('Error: Moving to Retweet Next Tweet.')
                time.sleep(15)
            else:
                count+=1
                text = tweet.text.replace('\n', '|')
                if len(text)<150: text = text[:100]
                print(str(count) + '.  Retweeted:  ' + text)
                time.sleep(10)

tconfig()
Retweet()
