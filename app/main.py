from fastapi import FastAPI
from app.routes import items, clock_in


app = FastAPI()

# include routers
app.include_router(items.router, tags=['items'])
app.include_router(clock_in.router, tags=['clock_in'])

# root route
@app.get('/')
def read_root():
    return {'message': 'FastAPI CRUD with MongoDB'}