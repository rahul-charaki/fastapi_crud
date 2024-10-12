from fastapi import APIRouter, HTTPException, status
from app.models import Item
from app.database import db, object_id_to_str
from app.schemas import item_entity
from bson import ObjectId
from datetime import datetime, timezone

router = APIRouter()

# get all items
@router.post('/items', response_model=dict)
async def create_item(item: Item):
    item_dict = item.model_dump()  # Use model_dump() instead of dict()
    item_dict['inserted_data'] = datetime.now(timezone.utc)  # Use timezone-aware datetime
    result = await db['items'].insert_one(item_dict)
    item_dict['_id'] = str(result.inserted_id)
    return item_dict

# filter items
@router.get('/items/filter')
async def filter_items(email: str = None, expiry_date: datetime = None, inserted_date: datetime = None, quantity: int= None):
    query = {}
    if email:
        query['email'] = email
    if expiry_date:
        query['expiry_date'] = {'$gte': expiry_date}
    if inserted_date:
        query['inserted_data'] = {'$gte': inserted_date}
    if quantity:
        query['quantity'] = {'$gte': quantity}

    items = await db['items'].find(query).to_list(100)
    return [object_id_to_str(item) for item in items]

# aggregation
@router.get('/items/aggregation')
async def get_item_count_by_email():
    pipeline = [
        {'$group': {'_id': '$email', 'count': {'$sum': 1}}}
    ]
    result = await db['items'].aggregate(pipeline).to_list(100)
    return [{'email': item['_id'], 'count': item['count']} for item in result]

# get item by id
@router.get('/items/{id}')
async def read_item(id: str):
    item = await db['items'].find_one({'_id': ObjectId(id)})
    if item:
        return object_id_to_str(item)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')

# delete item
@router.delete('/items/{id}')
async def delete_item(id: str):
    result = await db['items'].delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return {'message': 'Item deleted successfully'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')

# update item
@router.put('/items/{id}')
async def update_item(id: str, item: Item):
    item_dict = item.dict()
    item_dict['inserted_data'] = datetime.utcnow()
    result = await db['items'].update_one({'_id': ObjectId(id)}, {'$set': item_dict})
    if result.modified_count:
        return {'message': 'Item updated successfully'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')

