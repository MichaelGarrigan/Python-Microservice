
'''
@name -> insertTopStreams
@param (dbConnection) -> db connection object
@param (cursor) -> db cursor object
@param (time) -> a list of 5 integers that means [year, month, day, hour, minute]
@param (topStreams) -> list of 20 dictionary objects
'''

def insertTopStreams(dbConnection, cursor, time, topStreams):
  # multidimensional list
  # list order: [channel_id, display_name, language, game, created_at, followers, views, viewers, preview_template]
  items = []
  for stream in topStreams:
    item = []
    item.append(str(stream['channel']['_id']))
    item.append(str(stream['channel']['display_name']))
    item.append(str(stream['channel']['language']))
    item.append(str(stream['game']))
    item.append(str(stream['created_at']))
    item.append(str(stream['channel']['followers']))
    item.append(str(stream['channel']['views']))
    item.append(str(stream['viewers']))
    item.append(str(stream['preview']['template']))
    items.append(item)

  query = 'INSERT INTO top_streams (custom_timestamp, stream_01, stream_02, stream_03, stream_04, stream_05, stream_06, stream_07, stream_08, stream_09, stream_10, stream_11, stream_12, stream_13, stream_14, stream_15, stream_16, stream_17, stream_18, stream_19, stream_20) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
  cursor.execute(
    query, 
    [
      time, 
      items[0], items[1], items[2], items[3], items[4], 
      items[5], items[6], items[7], items[8], items[9],
      items[10], items[11], items[12], items[13], items[14], 
      items[15], items[16], items[17], items[18], items[19]
    ]
  )
  dbConnection.commit()