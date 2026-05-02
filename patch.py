from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
from typing import Optional

# PATCH ko lagi Optional fields bhayeko model
class PatchUserRequest(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    faculty : Optional[str] = None

app = FastAPI()

@app.patch("/users/{user_id}")
def patch_user(user_id: int, patch_user_payload: PatchUserRequest):

    # 1. File bata data read garne
    with open("data.json", "r") as file:
        data = json.load(file)

    # 2. User khojne ra partial update garne
    user_found = False
    updated_user = None

    for user in data:
        if user["id"] == user_id:
            # Yadi payload ma data pathayeko chha bhane matra update garne
            if patch_user_payload.name is not None:
                user["name"] = patch_user_payload.name
            
            if patch_user_payload.age is not None:
                user["age"] = patch_user_payload.age
                
            if patch_user_payload.faculty is not None:
                user["faculty"] = patch_user_payload.faculty
            
            user_found = True
            updated_user = user
            break

    # 3. User na-vetauda error dine
    if not user_found:
        raise HTTPException(status_code=404, detail="User vetiyena!")

    # 4. File ma save garne
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

    return {
        "message": "User data update partially",
        "user": updated_user
    }