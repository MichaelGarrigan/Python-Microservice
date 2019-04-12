
import requests
import json
from models.streamersModel import insertTopStreams
from models.streamersStaticModel import selectStreamIfAvailable, insertStreamIntoStaticTable
from helperFunctions.config import twitch

def callTwitchApi():
    url = 'https://api.twitch.tv/kraken/streams'
    headers = {'Client-ID': twitch['Client-ID']}

    res = requests.get(url, headers=headers)
    # parse from json
    topStreams = json.loads(res.text)
    topStreamsList = topStreams['streams']

    return topStreamsList

def retrieveTopStreamers(dbConnection, cursor, time):
  streams = callTwitchApi()
  
  # iterate over streams
  for stream in streams:
    # staticStreams will be either None or a tuple
    staticStreams = selectStreamIfAvailable(dbConnection, cursor, int(stream['channel']['_id']))
    if staticStreams is None: 
      insertStreamIntoStaticTable(dbConnection, cursor, stream)
      

  # then add data to db with models/topStreamsModel.py
  insertTopStreams(dbConnection, cursor, time, streams) 