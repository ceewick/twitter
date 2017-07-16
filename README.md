While re-looking at Charles Severence's book and the chapters on JSON and web services, I thought this might be an interesting project to practice data science. 

Planning to record, download, and analyze his tweets. 

Note: 'oauth.py','twitter1.py','twurl.py' are from his course and not related to the tTweets project.

Also note: in the .gitignore, you'll see I didn't push my 'hidden.py' file. If you are doing this project, you will need that file in your directory. That file contains something similar to what's below....

# hidden.py
# Keep this file separate

# https://apps.twitter.com/
# Create new App and get the four strings

def oauth():
    return {"consumer_key": "",
            "consumer_secret": "",
            "token_key": "",
            "token_secret": ""}
