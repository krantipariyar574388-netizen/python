from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel

# Input data valid garna BaseModel use garne
class UpdateUserRequest(BaseModel):
    name : str
    age : int
    faculty : str 

app = FastAPI()

@app.put("/users/{user_id}")
def update_user(user_id: int, update_user_payload: UpdateUserRequest):

    # 1. Purano data read garne
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Not found data.json file ")

    # 2. user_id ko aadhar ma user khojne ra update garne
    user_found = False
    updated_user = None

    for user in data:
        if user["id"] == user_id:
            # Data update garne logic
            user["name"] = update_user_payload.name
            user["age"] = update_user_payload.age
            user["faculty"] = update_user_payload.faculty
            
            user_found = True
            updated_user = user
            break

    # 3. Yadi user vetiyena bhane 404 error dine
    if not user_found:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")

    # 4. Update bhayeko list lai pheri file ma save garne
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

    return {
        "message": "User updated successfully",
        "user": updated_user,
    }