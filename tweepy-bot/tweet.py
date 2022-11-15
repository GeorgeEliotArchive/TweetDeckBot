import tweepy
import pandas as pd
from datetime import datetime, timedelta
import schedule_tweet

# Authenticate to Twitter
auth = tweepy.OAuthHandler("0hhzcWG7aZdEyQYbaRaFSd9Ay", "bUrEuve61hWsy0jIpXvIErrVOWcFZ8h8IEsnKIk8F6lbEJUFFf")
auth.set_access_token("1510689012964642818-cqaf3Y8UtDXFA4dQVdnyhBZLkXF0In", "Ae2pWeU5i1upO39K8dHTw99KxsastwYnGzwyLXZ2UErc8")

api = tweepy.API(auth)

# # get content
# df = pd.read_excel('GE Fiction Quotes.xlsx')
#
# for i, row in df.iterrows():
#     print(row['Formated'])

# schedule on tweet deck


username = 'EliotArchive'
password = 'GeorgeEliotArchive1'
now_dt = datetime.now()
with schedule_tweet.session(username, password) as session:
    dt = now_dt + timedelta(minutes=2)
    session.tweet(dt, f'First Tweet 🚀 {dt.isoformat()}')

    dt = now_dt + timedelta(minutes=3)
    session.tweet(dt, f'Second Tweet 💥 {dt.isoformat()}')


# tweet
# api.update_status("Hi, here's a tweet")
