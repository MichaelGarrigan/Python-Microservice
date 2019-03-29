
from db.dbConnection import connectToDB
from controllers.generateNewCustomTime import newCustomTime
from controllers.apiTopGames import retrieveTopGames
import psycopg2

# Entry Point for AWS Lambda Service
def handle_main(event, context):
  
  # connect to postgres db
  dbConnection = connectToDB()

  if type(dbConnection) == psycopg2.OperationalError:
    # --TODO-- log out error message and timestamp
    print('DB error: ', dbConnection)
  else:
    cursor = dbConnection.cursor()
    
    # Generate Custom Time with /controllers/generateNewCustomTime.py
    time = newCustomTime(dbConnection, cursor)
    
    if(time):
      # insert time into db

      # Get top games from twitch api and insert into db
      retrieveTopGames(dbConnection, cursor, time)

      # Get top streamers from twitch api and insert into db
      # => /controllers/apiTopStreamers.py

    # disconnect from postgres db
    cursor.close()
    dbConnection.close()
    print("PostgreSQL connection is closed")

# Uncomment to run this project locally
handle_main('event', 'context')