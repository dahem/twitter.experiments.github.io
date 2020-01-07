from tweepy import OAuthHandler, Stream, StreamListener
from dotenv import load_dotenv
import csv
import os
import datetime
import json
import io

load_dotenv()
KEY = os.getenv("KEY")
SECRET = os.getenv("SECRET")
TOKEN_KEY = os.getenv("TOKEN_KEY")
TOKEN_SECRET = os.getenv("TOKEN_SECRET")

consumer_key=KEY
consumer_secret=SECRET

access_token=TOKEN_KEY
access_token_secret=TOKEN_SECRET

def get_key_list():
    ans = []
    with open('./trendingWords.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ans.append(row['keylist'])
    return ans
    
def save_json(data, now):
    with io.open('./data-stream/data-{}.json'.format(now), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self):
        self.pack = []
 
    def on_data(self, data):
        self.pack.append(json.loads(data))
        if len(self.pack) == 10:
            now = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            saneazed_result = { "request_date": now, "data": self.pack }
            save_json(saneazed_result, now)
            self.pack = []
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=get_key_list())