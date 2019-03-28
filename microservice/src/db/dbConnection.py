
import psycopg2
from helperFunctions.config import db

'''
Attempt to establish a postgresql connection
@return -- failure will return error
@return -- success will return connection object
'''

def connectToDB():
  try:
    connection = psycopg2.connect(
      user =     db['user'],
      password = db['password'],
      host =     db['host'],
      port =     db['port'],
      database = db['database']
    )
  except Exception as error :
    return error
  else:
    return connection