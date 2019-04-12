
def roundTimeDown(time_now):
  # round minuite down to nearest 5 min increment
  remainder = time_now.minute % 5
  minute = time_now.minute - remainder
  
  return [time_now.year, time_now.month, time_now.day, time_now.hour, minute]
