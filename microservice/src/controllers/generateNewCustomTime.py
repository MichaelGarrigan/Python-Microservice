
from datetime import datetime
from models.customTimeModel import retrieveOldCustomTime
from helperFunctions.roundTimeDown import roundTimeDown

# connect to db
def newCustomTime(dbConnection, cursor):

  time_now = datetime.now()

  # round down current time
  time_now_rounded = roundTimeDown(time_now)

  # query db for last time recorded
  oldTime = retrieveOldCustomTime(dbConnection, cursor)
  
  print('old Time: ', oldTime)
  oldTimeAsAList = oldTime[0]

  # Increment the old time by five minutes
  # updatedTime = incrementOldTime(oldTimeAsAList)
  
  
  # increment time and save to a variable

  # write new time to db