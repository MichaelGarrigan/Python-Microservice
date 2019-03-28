
from dbConnection import connectToDB
from models.customTimeModel import retrieveOldCustomTime

# db Setup Connection and retrieve value
dbConnection = connectToDB()
cursor = dbConnection.cursor()
result = retrieveOldCustomTime(dbConnection, cursor)

def test_result_is_a_tuple():
  assert isinstance(result, tuple)

def test_result_is_a_tuple_and_has_length_of_1():
  assert len(result) == 1

def test_tuples_single_item_is_a_list():
  firstItem = result[0]
  assert isinstance(firstItem, list)

def test_tuples_single_item_is_a_list_of_5_items():
  firstItem = result[0]
  assert len(firstItem) == 5