
from dbConnection import connectToDB
from controllers.generateNewCustomTime import newCustomTime
import psycopg2
import datetime

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
    print('select: ', newCustomTime(dbConnection, cursor))
    # --TODO-- capture this in a variable and sent to a new function to process it

    # Get top games from twitch api and insert into db
    # => /controllers/apiTopGames.py

    # Get top streamers from twitch api and insert into db
    # => /controllers/apiTopStreamers.py

    # disconnect from postgres db
    cursor.close()
    dbConnection.close()
    print("PostgreSQL connection is closed")

# Uncomment to run this project locally
handle_main('event', 'context')