
from models.customTimeModel import retrieveOldCustomTime
from helperFunctions.incrementOldTime import incrementOldTime

# connect to db
def newCustomTime(dbConnection, cursor):

  # query db for last time recorded
  oldTime = retrieveOldCustomTime(dbConnection, cursor)
  oldTimeAsAList = oldTime[0]

  # Increment the old time by five minutes
  updatedTime = incrementOldTime(oldTimeAsAList)
  
  
  # increment time and save to a variable

  # write new time to db