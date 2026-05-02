from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    name : str
    age : int
    faculty : str 

app = FastAPI()

users_list = [
    {
    "id": 1,
     "name": "Kranti",
     "age": 22,
     "faculty": "BCA"
     },
    {
        "id": 2,
        "name": "Surakshya",
        "age": 21,
        "faculty": "BCA"
        },
    {
        "id": 3,
        "name": "Priyasha",
        "age": 23,
        "faculty": "BBS"
        },
]

@app.get("/")
def get_all_users():
    return users_list

@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    for user in users_list:
        if user["id"] == user_id:
            return user
        
    # raise HTTPException(status_code=404, detail="User not found")
    if user_id > 3 : 
        return JSONResponse(
            status_code=404,
            content = {'message': 'user with id doesnot exist'.format(user_id)},
        )

# # @app.get("/")
# # def create_user(create_user_payload : CreateUserRequest):

# #     return "OK"

