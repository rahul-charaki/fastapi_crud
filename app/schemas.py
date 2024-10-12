from datetime import datetime
from bson import ObjectId

# Item entity
def item_entity(item: dict) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'email': item['email'],
        'item_name': item['item_name'],
        'quantity': item['quantity'],
        'expiry_date': item['expiry_date'],
        'inserted_data': item['inserted_data']
    }

# ClockIn entity
def clock_in_entity(clock_in: dict) -> dict:
    return {
        'id': str(clock_in['_id']),
        'email': clock_in['email'],
        'location': clock_in['location'],
        'inserted_data': clock_in['inserted_data']
    }