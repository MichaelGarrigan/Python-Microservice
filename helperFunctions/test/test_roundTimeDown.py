
from datetime import datetime
from helperFunctions.roundTimeDown import roundTimeDown

time_1 = datetime(2020, 6, 1, 10, 0)
time_2 = datetime(2020, 6, 1, 10, 12)
time_3 = datetime(2020, 6, 1, 10, 19)
time_4 = datetime(2020, 6, 1, 10, 55)

def test_roundTimeDown_works_with_0_minute():
  assert roundTimeDown(time_1) == [2020, 6, 1, 10, 0]

def test_roundTimeDown_works_with_12_minute():
  assert roundTimeDown(time_2) == [2020, 6, 1, 10, 10]

def test_roundTimeDown_works_with_19_minute():
  assert roundTimeDown(time_3) == [2020, 6, 1, 10, 15]

def test_roundTimeDown_works_with_55_minute():
  assert roundTimeDown(time_4) == [2020, 6, 1, 10,55]

def test_returns_a_list():
  assert isinstance(roundTimeDown(time_1), list)