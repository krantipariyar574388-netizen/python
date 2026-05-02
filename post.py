from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    name : str
    age : int
    faculty : str 

app = FastAPI()
@app.post("/users")
def create_user(create_user_payload: CreateUserRequest):

    # return "OK"

    # read existing users
    with open("data.json", "r") as file:
        data = json.load(file)

    #create new user object
    new_user = {
        "id": len(data) + 1,
        "name": create_user_payload.name,
        "age": create_user_payload.age,
        "faculty": create_user_payload.faculty,

        # in short using model_dump
        # **create_user_payload.model_dump()
    }

    #append new user
    data.append(new_user)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

        return {
            "message": "User created successfully",
            "user": new_user,
        }
