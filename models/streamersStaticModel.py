
from psycopg2 import sql

# 1) query db for specific streamer title
def selectStreamIfAvailable(dbConnection, cursor, id):
  query = sql.SQL('SELECT * FROM top_streams_static WHERE user_id={}').format(sql.Literal(id))
  cursor.execute(query)
  streamTuple = cursor.fetchone()
  
  return streamTuple

# 2) insert new stream into top_streams_static table
def insertStreamIntoStaticTable(dbConnection, cursor, stream):
  query = 'INSERT INTO top_streams_static (user_id, user_name, name, language, created_at, logo, url) VALUES (%s, %s, %s, %s, %s, %s, %s)'
  cursor.execute(
    query, 
    [stream['channel']['_id'], stream['channel']['display_name'], stream['channel']['name'], stream['channel']['language'], stream['channel']['created_at'], stream['channel']['logo'], stream['channel']['url']]
  )
  dbConnection.commit()