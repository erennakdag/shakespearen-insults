import time
import tweepy
from pprint import pprint
from insult import status_text

# 0Auth
auth = tweepy.OAuthHandler("API Key", "API Key Secret")
auth.set_access_token("Access Token Key", "Access Token Key Secret")

# creating the API Handler
api = tweepy.API(auth)

last_mentions_id = []

# getting ther mentions
while True:
    print("Listening to mentions...")
    mentions = api.mentions_timeline()
    if mentions:
        print("Found some...")
        for mention in mentions:
            reply_id = mention._json["id"]
            if reply_id in last_mentions_id:
                print("I already replied to that!")
            else:
                print(f"Replying to {reply_id}")
                pprint(api.update_status(status_text(), in_reply_to_status_id=reply_id , auto_populate_reply_metadata=True)._json)
                last_mentions_id.append(reply_id)
                if len(last_mentions_id) > 20:
                    last_mentions_id.pop(0)
                print(last_mentions_id)
    time.sleep(60)
