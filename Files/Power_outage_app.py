# ***WORK IN PROGRESS***

# Install Twitter Scraper
# !pip install twitterscraper

import pickle
import pandas as pd
import time, datetime
import re

from flask import Flask, request, Response, render_template, jsonify
from datetime import timedelta
from twitterscraper import query_tweets
from nltk.tokenize import RegexpTokenizer


app = Flask('powerOutage')

# route 1: Form
@app.route('/')
def home():
    # return a preset form template
    return render_template('form.html')

# route 4: show a form to the user
@app.route('/form')
def form():
    # use flask's render_template function to display an html page
    return render_template('form.html')


# route 5: accept the form submission and scrape twitter in that state then run our model and output results
@app.route('/submit')
def make_predictions():
    # load in the form data from the incoming request
    user_input = request.args

    # manipulate data into a format that we pass to our model
    state = user_input['state']

    # set empty lists that we will fill with tweet data
    text = []
    locs = []
    times = []

    # scrape twitter for tweets containing certain keywords
    query_string = f'"power outage" OR "power is out" OR "power\'s out" OR "blackouts" OR "blackout" -"video game" OR "power failure" OR "power failures" OR "no electricity" OR "power shortage" OR "electrical failure" OR "power loss" OR "power cuts" OR "power cut" OR "power went out" OR "power interuption" OR "brownout" OR "power goes out" OR "brownouts" OR "without power" near:"{state}" within:15mi -filter:retweets'
    list_of_tweets = query_tweets(query_string,
                            begindate = datetime.datetime.today().date(),
                            enddate = datetime.datetime.today().date() + timedelta(days=1),
                            poolsize = 2,
                            lang="en"
                           )

    # loop through each tweet to grab data and append the data to their respective lists
    for tweet in list_of_tweets:
        locs.append(state)
        text.append(tweet.text)
        times.append(tweet.timestamp)

    # build the dataframe
    df = pd.DataFrame({
        'tweet': text,
        'location': locs,
        'time_stamp': times,
    })

    # remove any twitter pic urls
    df['tweet'] = [re.sub(r'pic.twitter.com\S+', '', post).strip() for post in df['tweet']]

    # remove any http urls
    df['tweet'] = [re.sub(r'http\S+', '', post).strip() for post in df['tweet']]

    # instatiate the tokenizer
    tknr = RegexpTokenizer(r'[a-zA-Z&0-9]+')

    # start with empty lists
    tokens = []

    # fill the list with tokenized versions of each post title
    for post in df['tweet']:
        tokens.append(" ".join(tknr.tokenize(post.lower())))

    df['tweet'] = tokens

    # next we should use our pickled model to predict probability of power outage based on our master_tweets

    model = pickle.load(open('./final_model.p', 'rb'))

    preds_proba = []
    for tweet in df.drop_duplicates()['tweet']:
        preds_proba.append(model.predict_proba([tweet])[0][1])

    pred = round(sum(preds_proba)/len(preds_proba), 2)

    # return the view
    return render_template('results.html', pred=(pred * 100), state=state)


if __name__ == '__main__':
    app.run(debug=True)
