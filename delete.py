from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    # 1. File bata data read garne
    with open("data.json", "r") as file:
        data = json.load(file)

    # 2. User khojne ra delete garne
    user_found = False
    for user in data:
        if user["id"] == user_id:
            data.remove(user) # List bata tyo user hataune
            user_found = True
            break

    # 3. Yadi user vetiyena bhane error dine
    if not user_found:
        raise HTTPException(status_code=404, detail="User vetiyena, delete garna sakiyena!")

    # 4. Baki vayeko data lai pheri file ma save garne
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

    return {
        "message": f"User ID {user_id} user delete successfully "
        }