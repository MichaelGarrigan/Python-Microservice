
import datetime

'''
@name -> incrementOldTime 

@param (oldTime) -> a list of 5 integers
@return -> an updated list of 5 integers

@about -> The format for the list:
       -> [17, 3, 2019, 00, 13] 
       -> [day, month, year, min, hour]
'''

print('datetime: ', datetime.datetime.now())

def incrementOldTime(oldTime):
  day    = oldTime[0]
  month  = oldTime[1]
  year   = oldTime[2]
  minute = oldTime[3]
  hour   = oldTime[4]

  

  # parse oldTime and increment it by five minutes
  return newTime