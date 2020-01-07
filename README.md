# api twitter get data
insall and run
 ```sh
# tener python 3.5 para arriba
sudo apt install python3-pip 
pip3 install virtualenv
pipenv shell         ----start env 
pipenv install		--- install dependencias
cp .env.example .env   --  poner las variables de twiter en .env
python src/main.py .  ejecutar
python src/stream.py .  ejecutar modo stream
usa las palabras de trendingWords
 ``` 

# search words

["rosamariabartra"]

### example item form request

```json
{
  "created_at": "Sun Nov 24 15:03:50 +0000 2019",
  "id": 1198618232149696512,
  "id_str": "1198618232149696512",
  "text": "@rosamariabartra Ja, ja, ja! Buen chiste! Me hace reír está chiflada inflada. Es alucinante lo que cacarea esta car… https://t.co/QsuEWBhSV4",
  "truncated": true,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "rosamariabartra",
        "name": "Rosa María Bartra",
        "id": 67978697,
        "id_str": "67978697",
        "indices": [
          0,
          16
        ]
      }
    ],
    "urls": [
      {
        "url": "https://t.co/QsuEWBhSV4",
        "expanded_url": "https://twitter.com/i/web/status/1198618232149696512",
        "display_url": "twitter.com/i/web/status/1…",
        "indices": [
          117,
          140
        ]
      }
    ]
  },
  "metadata": {
    "iso_language_code": "es",
    "result_type": "recent"
  },
  "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
  "in_reply_to_status_id": 1198608553818222592,
  "in_reply_to_status_id_str": "1198608553818222592",
  "in_reply_to_user_id": 67978697,
  "in_reply_to_user_id_str": "67978697",
  "in_reply_to_screen_name": "rosamariabartra",
  "user": {
    "id": 1120900139722465281,
    "id_str": "1120900139722465281",
    "name": "Marcelino Ccolqque",
    "screen_name": "marcelloqolqe",
    "location": "",
    "description": "Polyglot. Professor of grammar, literature and languages. Writer. Journalist. Liberal right.  (La discrepanza è tollerata ma non l'insulto)",
    "url": null,
    "entities": {
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 11,
    "friends_count": 383,
    "listed_count": 1,
    "created_at": "Wed Apr 24 03:59:53 +0000 2019",
    "favourites_count": 23,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": false,
    "verified": false,
    "statuses_count": 536,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "F5F8FA",
    "profile_background_image_url": null,
    "profile_background_image_url_https": null,
    "profile_background_tile": false,
    "profile_image_url": "http://pbs.twimg.com/profile_images/1121539163604566024/lWcQDce5_normal.png",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1121539163604566024/lWcQDce5_normal.png",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1120900139722465281/1556234836",
    "profile_link_color": "1DA1F2",
    "profile_sidebar_border_color": "C0DEED",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "has_extended_profile": false,
    "default_profile": true,
    "default_profile_image": false,
    "following": false,
    "follow_request_sent": false,
    "notifications": false,
    "translator_type": "none"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 0,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "lang": "es"
}
```