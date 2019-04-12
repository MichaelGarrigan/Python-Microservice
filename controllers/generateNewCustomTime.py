
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

  if (time_now_rounded == oldTime): 
    return False
  else: 
    return time_now_rounded