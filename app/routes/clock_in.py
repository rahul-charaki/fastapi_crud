from fastapi import APIRouter, HTTPException, status
from app.models import ClockIn
from app.database import db, object_id_to_str
from app.schemas import clock_in_entity
from bson import ObjectId
from datetime import datetime

router = APIRouter()

#get all clock ins
@router.post('/clock_in', response_model=dict)
async def create_clock_in(clock_in: ClockIn):
    clock_in_dict = clock_in.dict()
    clock_in_dict['inserted_data'] = datetime.utcnow()
    result = await db['clock_in'].insert_one(clock_in_dict)
    return {'id': str(result.inserted_id)}

#filter clock ins
@router.get('/clock_in/filter')
async def filter_clock_ins(email: str = None, location: str = None, inserted_date: datetime = None):
    query = {}
    if email:
        query['email'] = email
    if location:
        query['location'] = location
    if inserted_date:
        query['inserted_data'] = {'$gte': inserted_date}

    clock_ins = await db['clock_in'].find(query).to_list(100)
    return [object_id_to_str(clock_in) for clock_in in clock_ins]

#aggregation
@router.get('/clock_in/{id}')
async def read_clock_in(id: str):
    record = await db['clock_in'].find_one({'_id': ObjectId(id)})
    if record:
        return object_id_to_str(record)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Clock in not found')

#delete clock in
@router.delete('/clock_in/{id}')
async def delete_clock_in(id: str):
    result = await db['clock_in'].delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return {'message': 'Clock in deleted successfully'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Clock in not found')

#update clock in
@router.put('/clock_in/{id}')
async def update_clock_in(id: str, clock_in: ClockIn):
    clock_in_dict = {key: value for key, value in clock_in.dict().items() if key != "inserted_data"}
    result = await db['clock_in'].update_one({'_id': ObjectId(id)}, {'$set': clock_in_dict})
    if result.modified_count:
        return {'message': 'Clock in updated successfully'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Clock in not found')