import os
from TwitterAPI import TwitterAPI
from dotenv import load_dotenv
import datetime

load_dotenv()
now = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

SEARCH_TERM = 'rosamariabartra'

KEY = os.getenv("KEY")
SECRET = os.getenv("SECRET")
TOKEN_KEY = os.getenv("TOKEN_KEY")
TOKEN_SECRET = os.getenv("TOKEN_SECRET")


api = TwitterAPI(KEY,
                 SECRET,
                 TOKEN_KEY,
                 TOKEN_SECRET)

result = api.request('search/tweets', {'q': SEARCH_TERM})
saneazed_result = {"request_date": now, "data": []}
for item in result:
    saneazed_result['data'].append(item)

print('\nQUOTA: %s' % result.get_quota())

dirname = os.path.dirname(__file__)
print(dirname)


def saveJson():
    import io
    import json
    with io.open('./data/data-{}.json'.format(now), 'w', encoding='utf-8') as f:
        f.write(json.dumps(saneazed_result, ensure_ascii=False, indent=2))


saveJson()
