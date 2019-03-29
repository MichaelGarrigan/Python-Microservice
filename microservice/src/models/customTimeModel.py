
from psycopg2 import sql

'''
@name -> retrieveOldCustomTime 

@param (dbConnection) -> db connection object
@param (cursor) -> db cursor object
@return -> a python list of 5 integers that means [year, month, day, hour, minute]

@about -> This model will retrieve the last row from the same table with every call.
       -> The column 'time_custom' will have a value that constantly changes every five minutes.
'''

def retrieveOldCustomTime(dbConnection, cursor):
  query = 'SELECT time_custom FROM last_custom_time_stamp ORDER BY id DESC LIMIT 1'
  cursor.execute(query)
  oldTimeTuple = cursor.fetchone()

  return oldTimeTuple[0]


'''
@name -> insertNewCustomTime 
@param (dbConnection) -> db connection object
@param (cursor) -> db cursor object
@return -> None
'''

def insertNewCustomTime(dbConnection, cursor, time):
  query = sql.SQL('INSERT INTO last_custom_time_stamp (time_custom) VALUES ({})').format(sql.Literal(time))
  cursor.execute(query)
  dbConnection.commit()