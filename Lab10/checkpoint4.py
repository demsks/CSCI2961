from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient()

if __name__ == '__main__':

  client = MongoClient()
  db = client.csci2963

  #Fetch all records
  for record in db.definitions.find():
      print(record)

  #Fetch one record
  print
  print(db.definitions.find_one())

  #Fetch a specific record
  print
  print(db.definitions.find_one({"word": "Objective"}))

  #Fetch a record by object id
  print
  print(db.definitions.find_one({ '_id': ObjectId('56fe9e22bad6b23cde07b8d8')}))

  #Insert a new record
  print
  record_id = db.definitions.insert_one({"word": "Testing", "definition":" a test!"}).inserted_id
  print(db.definitions.find_one({"word": "Testing"}))