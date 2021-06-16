from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
db = []

class Data(BaseModel):
    Name: str
    Contact_no: int
    Department: str

@app.get('/')
def index():
    return{'key':'value'}

@app.get('/profile')
def get_profile():
    return db

@app.post('/profile')
def create_data_of_employee(employee: Data):
    db.append(employee.dict())
    return db[-1]

@app.delete('/profile{employee_id}')
def delete_profile(employee_id: int):
    db.pop(employee_id-1)
    return {}

@app.get('/profile{employee_id}')
def get_employee_by_id(employee_id: int):
    return db[employee_id-1]