#!/usr/bin/env python

import json
from urllib.request import urlopen
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.reddit
stories = db.stories

# drop existing collection
stories.drop()

# get the reddit home page
reddit_page = urlopen("http://www.reddit.com/r/technology/.json")

# parse the json into python objects
parsed = json.loads(reddit_page.read().decode('utf-8'))

# iterate through every news item on the page
for item in parsed['data']['children']:
    # put it in mongo
    stories.insert_one(item['data'])
