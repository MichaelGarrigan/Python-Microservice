
'''
@name -> insertTopGames
@param (dbConnection) -> db connection object
@param (cursor) -> db cursor object
@param (time) -> a list of 5 integers that means [year, month, day, hour, minute]
@param (topGames) -> list of 20 dictionary objects
'''

def insertTopGames(dbConnection, cursor, time, topGames):
  # multidimensional list
  # list order: [_id, name, channels, viewers, popularity]
  items = []
  for game in topGames:
    item = []
    item.append(str(game['game']['_id']))
    item.append(game['game']['name'])
    item.append(str(game['channels']))
    item.append(str(game['viewers']))
    item.append(str(game['game']['popularity']))
    items.append(item)

  query = 'INSERT INTO top_games (custom_timestamp, game_01, game_02, game_03, game_04, game_05, game_06, game_07, game_08, game_09, game_10, game_11, game_12, game_13, game_14, game_15, game_16, game_17, game_18, game_19, game_20) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
  cursor.execute(
    query, 
    [
      time, 
      items[0], items[1], items[2], items[3], items[4], 
      items[5], items[6], items[7], items[8], items[9],
      items[10], items[11], items[12], items[13], items[14], 
      items[15], items[16], items[17], items[18], items[19]
    ]
  )
  dbConnection.commit()