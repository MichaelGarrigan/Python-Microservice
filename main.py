
from dbConnection import connectToDB
import psycopg2

# connect to postgres db
dbConnection = connectToDB()

if type(dbConnection) == psycopg2.OperationalError:
  # log out error message and timestamp
  print('DB error: ', dbConnection)
else:
  cursor = dbConnection.cursor()

  # Generate Custom Time with /controllers/generateNewCustomTime.py

  # Get top games from twitch api and insert into db
  # => /controllers/apiTopGames.py

  # Get top streamers from twitch api and insert into db
  # => /controllers/apiTopStreamers.py

  # disconnect from postgres db
  cursor.close()
  dbConnection.close()
  print("PostgreSQL connection is closed")