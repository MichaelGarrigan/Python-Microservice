
import requests
import json
from models.topGamesModel import insertTopGames
from models.topGamesStaticModel import selectGameIfAvailable, insertGameIntoStaticTable
from helperFunctions.config import twitch

def callTwitchApi():
    url = 'https://api.twitch.tv/kraken/games/top'
    payload = {'limit': '21'}
    headers = {'Client-ID': twitch['Client-ID']}

    res = requests.get(url, params=payload, headers=headers)

    # parse from json
    topGames = json.loads(res.text)
    topGamesList = topGames['top']

    return topGamesList

def retrieveTopGames(dbConnection, cursor, time):
  games = callTwitchApi()
  
  # iterate over games
  for game in games:
    # staticGame will be either None or a tuple
    staticGame = selectGameIfAvailable(dbConnection, cursor, int(game['game']['_id']))
    if staticGame is None: 
      insertGameIntoStaticTable(dbConnection, cursor, game)
      

  # then add data to db with models/topGamesModel.py
  insertTopGames(dbConnection, cursor, time, games) 