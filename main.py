
"""
https://improveandrepeat.com/2022/04/python-friday-117-streaming-search-results-with-tweepy/
"""
import tweepy
from tweepy import StreamingClient, StreamRule
import os
from dotenv import load_dotenv
load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')

class TweetPrinterV2(tweepy.StreamingClient):
    
    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print("-"*50)

printer = TweetPrinterV2(bearer_token)

# add new rules    
rule = StreamRule(value="Sterling")
printer.add_rules(rule)

printer.filter()

"""
1621632802184728576 None (None): Oferta laboral: Python Backend Developer - Buscamos un Python Backend Developer para una reconocida Institución... https://t.co/qdfd0vvZTi
"""