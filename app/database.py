from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from datetime import datetime

# connect to mongodb
client = AsyncIOMotorClient('mongodb+srv://charakirahul:X0vMCtZFOcGHVrnY@cluster0.5vurg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['crud_db']

# convert object id to string
def object_id_to_str(item):
    item['_id'] = str(item['_id'])
    return item