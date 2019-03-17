
from models.customTimeModel import retrieveOldCustomTime

# connect to db
def newCustomTime(dbConnection, cursor):

  # query db for last time recorded
  oldTime = retrieveOldCustomTime(dbConnection, cursor)
  oldTimeAsAList = oldTime[0]

  print('oldTimeList', oldTimeAsAList)
  
  
  # increment time and save to a variable

  # write new time to db