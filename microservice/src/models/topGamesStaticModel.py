
from psycopg2 import sql

# 1) query db for specific game title
def selectGameIfAvailable(dbConnection, cursor, id):
  query = sql.SQL('SELECT * FROM top_games_static WHERE game_id={}').format(sql.Literal(id))
  cursor.execute(query)
  gameTuple = cursor.fetchone()
  print('static return: ', gameTuple)
  print('static return type: ', type(gameTuple))
  return gameTuple


# 2) insert new game into top_games_static table
def insertGameIntoStaticTable(dbConnection, cursor, game):
  query = 'INSERT INTO top_games_static (game_id, name, box_art_url, logo_template) VALUES (%s, %s, %s, %s)'
  cursor.execute(query, [game['id'], game['name'], game['box_art_url'], 'none'])
  dbConnection.commit()