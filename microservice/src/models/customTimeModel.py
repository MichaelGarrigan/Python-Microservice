
'''
@name -> retrieveOldCustomTime 

@param (dbConnection) -> db connection object
@param (cursor) -> db cursor object
@return -> a python list of 5 integers that means [year, month, day, hour, minute]

@about -> This model will retrieve the last row from the same table with every call.
       -> The column 'time_custom' will have a value that constantly changes every five minutes.
'''

def retrieveOldCustomTime(dbConnection, cursor):
  sql = 'SELECT time_custom FROM last_custom_time_stamp ORDER BY id DESC LIMIT 1'
  cursor.execute(sql)
  oldTimeTuple = cursor.fetchone()

  return oldTimeTuple[0]

# 2) insert new time into last_custom_time_stamp table

# query = """ 
#       INSERT INTO top_games (GAME_ID, NAME, BOX_ART_URL) VALUES (%s,%s,%s)"""
#     values = (item['id'], item['name'], item['box_art_url'])
#     cursor.execute(query, values)
#     connection.commit()