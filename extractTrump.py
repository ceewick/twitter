import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import pandas as pd
import json
import os
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
tree = '/home/ceewick/cs/py4e/twitter/'
acct = 'realdonaldtrump'
url = twurl.augment(TWITTER_URL,
                    {'screen_name': acct})
c = urllib.request.urlopen(url, context=ctx)
data = c.read().decode()

## Create/Export JSON file of tweets
with open(os.path.join(tree, 'tTweets.json'),'w') as file:
    js = json.loads(data)
    json.dump(js,file,indent=4,sort_keys=True)
print('{}'.format('JSON output file created'))

## JSON to Pandas
df = pd.DataFrame.from_dict(js)
df2 = pd.Series()
print('{}'.format('Pandas DataFrame created'))

# ## Pandas to CSV
df.to_csv('{}.csv'.format('tTweets'), sep=',')
print('{}'.format('CSV output file created'))

## Pandas DataFrame to SQLite3 Database
''' issues here. Need to give dataTypes'''
# with sqlite3.connect('tTweets.db') as conn:
#     df.to_sql(name='tTweets', con=conn, if_exists=append)


