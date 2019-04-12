
from db.dbConnection import connectToDB
from models.customTimeModel import retrieveOldCustomTime

# db Setup Connection and retrieve value
dbConnection = connectToDB()
cursor = dbConnection.cursor()
result = retrieveOldCustomTime(dbConnection, cursor)

def test_result_is_a_list():
  assert isinstance(result, list)

def test_is_a_list_of_5_items():
  assert len(result) == 5