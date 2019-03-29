
import requests
import json
from models.topGamesModel import insertTopGames
from helperFunctions.config import twitch

def callTwitchApi():
    url = 'https://api.twitch.tv/helix/games/top'
    payload = {'first': '15'}
    headers = {'Client-ID': twitch['Client-ID']}

    res = requests.get(url, params=payload, headers=headers)

    # parse from json
    topGames = json.loads(res.text)
    topGamesList = topGames['data']

    print('top games: ', topGamesList)
    print('top games: ', type(topGamesList))
    print('top games: ', len(topGamesList))

    return topGamesList

def retrieveTopGames(dbConnection, cursor, time):

  games = callTwitchApi()

  # iterate over games
  # for game in games:
    # see if this game in top_games_static table
    # use models/topGamesStaticModel.py
    # if no, then add it

  # then add data to db with models/topGamesModel.py
  # insertTopGames(dbConnection, cursor, time, topGames) 