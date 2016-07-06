# Haven't edited this yet, so not generic/working right now.

import time, datetime, json, os, logging

from pymongo import MongoClient, cursor
from bson import ObjectId

from config import MONGO_URL, COLLECTION

print MONGO_URL

# MongoDB
client = MongoClient(MONGO_URL)
db = client[COLLECTION]

# Methods
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def to_json(val):
	if isinstance(val, cursor.Cursor):
		results = []
		for document in val:
			results.append(document)
		val = results
	return JSONEncoder().encode(val)

def insert(collection, hash_message):
	insert_result = db[collection].insert_one( hash_message )
	insert_id = str(insert_result.inserted_id)
	return insert_id

def get(collection, query=False):
	if not query:
		query = {}
	return to_json(db[collection].find(query))
